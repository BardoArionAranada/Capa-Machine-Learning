from pathlib import Path
import json

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# Rutas oficiales de entrada y salida de la etapa 04.
BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "parquets" / "02_EDA_Base_Tickets" / "02_base_eda_tickets.parquet"
OUTPUT_DIR = BASE_DIR / "parquets" / "04_Modelo_Regresion_Total_Pedido"
PREDICTIONS_PATH = OUTPUT_DIR / "04_tickets_regresion.parquet"
MODEL_DIR = BASE_DIR / "models" / "04_Modelo_Regresion_Total_Pedido"
MODEL_PATH = MODEL_DIR / "04_modelo_regresion_lineal.joblib"
FEATURES_PATH = MODEL_DIR / "04_features_regresion_lineal.json"


# Variables seleccionadas para estimar el total del pedido.
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

TARGET = "total_pedido"


def build_pipeline(X: pd.DataFrame) -> Pipeline:
    # Separa variables numericas y categoricas para su transformacion.
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
            ("regressor", LinearRegression()),
        ]
    )


def train_and_export() -> None:
    # Crea las carpetas de salida para los artefactos de la etapa 04.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    # Lee la base EDA y separa features y target de regresion.
    df = pd.read_parquet(INPUT_PATH)
    X = df[FEATURES].copy()
    y = df[TARGET].copy()

    # Divide los datos para medir el desempeno del modelo en prueba.
    X_train, X_test, y_train, y_test, idx_train, idx_test = train_test_split(
        X,
        y,
        df.index,
        test_size=0.2,
        random_state=42,
    )

    # Entrena un pipeline temporal para validar metricas.
    pipeline = build_pipeline(X)
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    # Resume las metricas principales del modelo de regresion.
    metrics_df = pd.DataFrame(
        [
            {"metrica": "mae", "valor": round(float(mean_absolute_error(y_test, y_pred)), 4)},
            {"metrica": "rmse", "valor": round(float(np.sqrt(mean_squared_error(y_test, y_pred))), 4)},
            {"metrica": "r2", "valor": round(float(r2_score(y_test, y_pred)), 4)},
            {"metrica": "train_rows", "valor": int(len(X_train))},
            {"metrica": "test_rows", "valor": int(len(X_test))},
        ]
    )

    # Entrena el modelo final con toda la informacion disponible.
    final_pipeline = build_pipeline(X)
    final_pipeline.fit(X, y)

    # Genera la salida final con predicciones y errores por ticket.
    df_predictions = df.copy()
    df_predictions["pred_total_pedido"] = final_pipeline.predict(X)
    df_predictions["residuo_total_pedido"] = df_predictions["total_pedido"] - df_predictions["pred_total_pedido"]
    df_predictions["error_abs_total_pedido"] = df_predictions["residuo_total_pedido"].abs()
    df_predictions["modelo"] = "Regresion Lineal"
    df_predictions["fuente_parquet"] = "02_base_eda_tickets.parquet"
    df_predictions["conjunto_evaluacion"] = "train"
    df_predictions.loc[idx_test, "conjunto_evaluacion"] = "test"

    test_lookup = pd.DataFrame(
        {
            "idx": idx_test,
            "pred_total_pedido_test": y_pred,
            "residuo_total_pedido_test": y_test.to_numpy() - y_pred,
        }
    ).set_index("idx")

    df_predictions = df_predictions.join(test_lookup, how="left")

    # Exporta el parquet principal y los artefactos del modelo entrenado.
    df_predictions.to_parquet(PREDICTIONS_PATH, index=False)
    joblib.dump(final_pipeline, MODEL_PATH)
    FEATURES_PATH.write_text(json.dumps(FEATURES, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Modelo de regresion entrenado correctamente")
    print(f"Predicciones guardadas en: {PREDICTIONS_PATH}")
    print(metrics_df.to_string(index=False))
    print(f"Modelo guardado en: {MODEL_PATH}")


if __name__ == "__main__":
    train_and_export()
