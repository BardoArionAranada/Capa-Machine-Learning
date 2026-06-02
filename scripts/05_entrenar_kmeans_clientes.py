from pathlib import Path
import json

import joblib
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.metrics import silhouette_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# Rutas oficiales de entrada y salida de la etapa 05.
BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "parquets" / "02_EDA_Base_Tickets" / "02_base_eda_tickets.parquet"
OUTPUT_DIR = BASE_DIR / "parquets" / "05_Modelo_Segmentacion_Clientes"
CLIENTS_PATH = OUTPUT_DIR / "05_clientes_segmentados.parquet"
METRICS_PATH = OUTPUT_DIR / "05_metricas_segmentacion.parquet"
MODEL_DIR = BASE_DIR / "models" / "05_Modelo_Segmentacion_Clientes"
MODEL_PATH = MODEL_DIR / "05_modelo_kmeans.joblib"
FEATURES_PATH = MODEL_DIR / "05_features_kmeans.json"


# Variables numericas para construir los segmentos de clientes.
FEATURES = [
    "numero_tickets",
    "gasto_total",
    "ticket_promedio",
    "ticket_maximo",
    "cantidad_total_productos",
    "promedio_productos_ticket",
    "categorias_distintas_totales",
    "dias_activos",
    "dias_desde_ultimo_ticket",
]


def construir_base_clientes(df: pd.DataFrame) -> pd.DataFrame:
    # Convierte la fecha para calcular recencia y permanencia.
    df = df.copy()
    df["fecha"] = pd.to_datetime(df["fecha"])
    fecha_max = df["fecha"].max()

    # Agrega la base a nivel cliente para la segmentacion.
    clientes = (
        df.groupby("id_cliente", dropna=False)
        .agg(
            numero_tickets=("id_ticket_modelado", "nunique"),
            gasto_total=("total_pedido", "sum"),
            ticket_promedio=("total_pedido", "mean"),
            ticket_maximo=("total_pedido", "max"),
            cantidad_total_productos=("cantidad_total", "sum"),
            promedio_productos_ticket=("cantidad_total", "mean"),
            platillos_distintos_totales=("platillos_distintos", "sum"),
            categorias_distintas_totales=("categorias_distintas", "sum"),
            ultimo_ticket=("fecha", "max"),
            primer_ticket=("fecha", "min"),
            ciudades_visitadas=("ciudad", "nunique"),
            sucursales_visitadas=("id_sucursal", "nunique"),
            usa_bebida=("incluye_bebida", "max"),
            usa_postre=("incluye_postre", "max"),
            usa_entrada=("incluye_entrada", "max"),
            usa_platillo_fuerte=("incluye_platillo_fuerte", "max"),
            metodo_pago_frecuente=("metodo_pago", lambda s: s.mode().iloc[0] if not s.mode().empty else "Sin dato"),
        )
        .reset_index()
    )

    # Deriva columnas de recencia y tiempo activo.
    clientes["dias_activos"] = (clientes["ultimo_ticket"] - clientes["primer_ticket"]).dt.days + 1
    clientes["dias_desde_ultimo_ticket"] = (fecha_max - clientes["ultimo_ticket"]).dt.days

    return clientes


def nombrar_segmentos(clientes: pd.DataFrame) -> pd.DataFrame:
    # Ordena los clusters por gasto y volumen para asignar etiquetas amigables.
    ranking = (
        clientes.groupby("cluster")
        .agg(gasto_total_promedio=("gasto_total", "mean"), numero_tickets_promedio=("numero_tickets", "mean"))
        .sort_values(["gasto_total_promedio", "numero_tickets_promedio"])
        .reset_index()
    )

    etiquetas_base = [
        "Clientes de bajo valor",
        "Clientes de valor medio",
        "Clientes de alto valor",
    ]

    mapping = {
        row["cluster"]: etiquetas_base[idx]
        for idx, (_, row) in enumerate(ranking.iterrows())
    }

    clientes["segmento_cliente"] = clientes["cluster"].map(mapping)
    return clientes


def train_and_export() -> None:
    # Crea las carpetas de salida para la etapa 05.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    # Lee la base EDA y la transforma a nivel cliente.
    df = pd.read_parquet(INPUT_PATH)
    clientes = construir_base_clientes(df)

    # Prepara el pipeline de escalado y clustering.
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", Pipeline(steps=[("scaler", StandardScaler())]), FEATURES),
        ],
        remainder="drop",
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("clusterer", KMeans(n_clusters=3, random_state=42, n_init=20)),
        ]
    )

    # Entrena el modelo de segmentacion.
    pipeline.fit(clientes[FEATURES])
    clientes["cluster"] = pipeline.predict(clientes[FEATURES])
    clientes = nombrar_segmentos(clientes)

    # Calcula metricas basicas del clustering.
    X_transformed = pipeline.named_steps["preprocessor"].transform(clientes[FEATURES])
    silhouette = silhouette_score(X_transformed, clientes["cluster"])

    metrics_df = pd.DataFrame(
        [
            {"metrica": "n_clientes", "valor": int(len(clientes))},
            {"metrica": "n_clusters", "valor": 3},
            {"metrica": "inercia", "valor": round(float(pipeline.named_steps["clusterer"].inertia_), 4)},
            {"metrica": "silhouette", "valor": round(float(silhouette), 4)},
        ]
    )

    # Exporta la base segmentada y los artefactos del modelo.
    clientes.to_parquet(CLIENTS_PATH, index=False)
    metrics_df.to_parquet(METRICS_PATH, index=False)
    joblib.dump(pipeline, MODEL_PATH)
    FEATURES_PATH.write_text(json.dumps(FEATURES, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Modelo de segmentacion entrenado correctamente")
    print(f"Clientes segmentados guardados en: {CLIENTS_PATH}")
    print(f"Metricas guardadas en: {METRICS_PATH}")
    print(f"Modelo guardado en: {MODEL_PATH}")


if __name__ == "__main__":
    train_and_export()
