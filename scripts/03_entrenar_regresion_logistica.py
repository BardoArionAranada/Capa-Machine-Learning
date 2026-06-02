from pathlib import Path
import json

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# Rutas oficiales de entrada y salida de la etapa 03.
BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "parquets" / "02_EDA_Base_Tickets" / "02_base_eda_tickets.parquet"
OUTPUT_DIR = BASE_DIR / "parquets" / "03_Modelo_Clasificacion_Ticket_Alto"
PREDICTIONS_PATH = OUTPUT_DIR / "03_tickets_clasificados.parquet"
METRICS_PATH = OUTPUT_DIR / "03_metricas_clasificacion.parquet"
MODEL_DIR = BASE_DIR / "models" / "03_Modelo_Clasificacion_Ticket_Alto"
MODEL_PATH = MODEL_DIR / "03_modelo_regresion_logistica.joblib"
FEATURES_PATH = MODEL_DIR / "03_features_regresion_logistica.json"


FEATURES = [
    "dia",
    "mes",
    "trimestre",
    "dia_semana",
    "dia_tipo",
    "fin_semana",
    "ciudad",
    "capacidad_sucursal",
    "tipo_empleado",
    "salario",
    "turno",
    "numero_mesa",
    "capacidad_mesa",
    "metodo_pago",
    "lineas_ticket",
    "cantidad_total",
    "platillos_distintos",
    "categorias_distintas",
    "incluye_bebida",
    "incluye_postre",
    "incluye_entrada",
    "incluye_platillo_fuerte",
]

TARGET = "ticket_alto"


def build_pipeline(X: pd.DataFrame) -> Pipeline:
    # Separa variables numericas y categoricas para el preprocesamiento.
    numericas = X.select_dtypes(include=["number", "bool"]).columns.tolist()
    categoricas = X.select_dtypes(include=["object"]).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                numericas,
            ),
            (
                "cat",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("encoder", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categoricas,
            ),
        ]
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=2000, class_weight="balanced")),
        ]
    )


def train_and_export() -> None:
    # Asegura carpetas de salida para parquets y modelo entrenado.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    # Lee la base EDA y separa features y target.
    df = pd.read_parquet(INPUT_PATH)
    X = df[FEATURES].copy()
    y = df[TARGET].copy()

    # Divide la muestra para evaluar el modelo antes de entrenarlo completo.
    X_train, X_test, y_train, y_test, idx_train, idx_test = train_test_split(
        X,
        y,
        df.index,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    # Entrena un pipeline temporal para calcular metricas sobre test.
    pipeline = build_pipeline(X)
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    y_prob = pipeline.predict_proba(X_test)[:, 1]

    # Resume las metricas principales del modelo de clasificacion.
    metrics_df = pd.DataFrame(
        [
            {"metrica": "accuracy", "valor": round(float(accuracy_score(y_test, y_pred)), 4)},
            {"metrica": "precision", "valor": round(float(precision_score(y_test, y_pred)), 4)},
            {"metrica": "recall", "valor": round(float(recall_score(y_test, y_pred)), 4)},
            {"metrica": "f1", "valor": round(float(f1_score(y_test, y_pred)), 4)},
            {"metrica": "roc_auc", "valor": round(float(roc_auc_score(y_test, y_prob)), 4)},
            {"metrica": "train_rows", "valor": int(len(X_train))},
            {"metrica": "test_rows", "valor": int(len(X_test))},
        ]
    )

    # Entrena el modelo final con toda la base disponible.
    final_pipeline = build_pipeline(X)
    final_pipeline.fit(X, y)

    # Genera la salida final con predicciones y probabilidades por ticket.
    df_predictions = df.copy()
    df_predictions["pred_ticket_alto"] = final_pipeline.predict(X)
    df_predictions["prob_ticket_alto"] = final_pipeline.predict_proba(X)[:, 1]
    df_predictions["modelo"] = "Regresion Logistica"
    df_predictions["fuente_parquet"] = "02_base_eda_tickets.parquet"
    df_predictions["conjunto_evaluacion"] = "train"
    df_predictions.loc[idx_test, "conjunto_evaluacion"] = "test"

    test_lookup = pd.DataFrame(
        {
            "idx": idx_test,
            "pred_ticket_alto_test": y_pred,
            "prob_ticket_alto_test": y_prob,
        }
    ).set_index("idx")

    df_predictions = df_predictions.join(test_lookup, how="left")

    # Exporta parquets y artefactos para trazabilidad del proyecto.
    df_predictions.to_parquet(PREDICTIONS_PATH, index=False)
    metrics_df.to_parquet(METRICS_PATH, index=False)
    joblib.dump(final_pipeline, MODEL_PATH)
    FEATURES_PATH.write_text(json.dumps(FEATURES, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Modelo de clasificacion entrenado correctamente")
    print(f"Predicciones guardadas en: {PREDICTIONS_PATH}")
    print(f"Métricas guardadas en: {METRICS_PATH}")
    print(f"Modelo guardado en: {MODEL_PATH}")


if __name__ == "__main__":
    train_and_export()
