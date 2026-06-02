from pathlib import Path
import os

import pandas as pd
from sqlalchemy import create_engine, text


BASE_DIR = Path(__file__).resolve().parents[1]
SQL_PATH = BASE_DIR / "sql" / "04_base_tickets_modelado.sql"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_PATH = OUTPUT_DIR / "base_tickets_modelado.parquet"


def build_connection_url() -> str:
    host = os.getenv("PGHOST", "localhost")
    port = os.getenv("PGPORT", "5432")
    database = os.getenv("PGDATABASE", "restaurante")
    user = os.getenv("PGUSER", "postgres")
    password = os.getenv("PGPASSWORD", "postgres")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"


def load_query() -> str:
    return SQL_PATH.read_text(encoding="utf-8")


def export_parquet() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    engine = create_engine(build_connection_url())
    query = load_query()

    with engine.connect() as connection:
        dataframe = pd.read_sql(text(query), connection)

    dataframe.to_parquet(OUTPUT_PATH, index=False)

    print("Base exportada correctamente")
    print(f"Filas exportadas: {len(dataframe)}")
    print(f"Archivo generado: {OUTPUT_PATH}")


if __name__ == "__main__":
    export_parquet()
