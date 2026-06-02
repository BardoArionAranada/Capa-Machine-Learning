from pathlib import Path
import os
import warnings

import pandas as pd
import psycopg2


# Rutas base del proyecto y salida oficial de la etapa 01.
BASE_DIR = Path(__file__).resolve().parents[1]
SQL_PATH = BASE_DIR / "sql" / "04_base_tickets_modelado.sql"
OUTPUT_DIR = BASE_DIR / "parquets" / "01_Carga_y_Validacion_Parquet"
OUTPUT_PATH = OUTPUT_DIR / "01_base_tickets_modelado.parquet"


def build_connection_params() -> dict:
    # Construye los parametros de conexion para leer el OLAP local.
    return {
        "host": os.getenv("PGHOST", "localhost"),
        "port": os.getenv("PGPORT", "5432"),
        "dbname": os.getenv("PGDATABASE", "restaurante"),
        "user": os.getenv("PGUSER", "postgres"),
        "password": os.getenv("PGPASSWORD", "postgres"),
    }


def load_query() -> str:
    # Carga la consulta SQL que reconstruye la base por ticket.
    return SQL_PATH.read_text(encoding="utf-8")


def export_parquet() -> None:
    # Asegura la carpeta de salida antes de ejecutar la exportacion.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    query = load_query()

    # Lee el resultado del OLAP directamente desde PostgreSQL.
    connection = psycopg2.connect(**build_connection_params())
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message="pandas only supports SQLAlchemy connectable"
            )
            dataframe = pd.read_sql_query(query, connection)
    finally:
        connection.close()

    # Guarda la base oficial de la etapa 01 en formato Parquet.
    dataframe.to_parquet(OUTPUT_PATH, index=False)

    print("Base exportada correctamente")
    print(f"Filas exportadas: {len(dataframe)}")
    print(f"Archivo generado: {OUTPUT_PATH}")


if __name__ == "__main__":
    export_parquet()
