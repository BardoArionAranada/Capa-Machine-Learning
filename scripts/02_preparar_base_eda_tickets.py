from pathlib import Path

import pandas as pd


# Rutas base para transformar la salida 01 en la base EDA oficial.
BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "parquets" / "01_Carga_y_Validacion_Parquet" / "01_base_tickets_modelado.parquet"
OUTPUT_DIR = BASE_DIR / "parquets" / "02_EDA_Base_Tickets"
OUTPUT_PATH = OUTPUT_DIR / "02_base_eda_tickets.parquet"


def preparar_base_eda() -> None:
    # Crea la carpeta de salida de la etapa 02.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Lee la base validada de la etapa 01.
    df = pd.read_parquet(INPUT_PATH)

    # Genera columnas de calendario y consistencia para el analisis exploratorio.
    df["anio_mes"] = pd.to_datetime(df["fecha"]).dt.strftime("%Y-%m")
    df["dia_tipo"] = df["fin_semana"].map({True: "Fin de semana", False: "Entre semana"})
    df["residuo_subtotal_total"] = df["subtotal_ticket"] - df["total_pedido"]
    df["residuo_abs_subtotal_total"] = df["residuo_subtotal_total"].abs()
    df["residuo_pago_total"] = df["monto_pago"] - df["total_pedido"]
    df["ticket_consistente_subtotal"] = (df["residuo_abs_subtotal_total"] <= 0.01).astype(int)
    df["ticket_consistente_pago"] = (df["residuo_pago_total"].abs() <= 0.01).astype(int)

    # Crea un rango simple para clasificar montos de pedido.
    df["rango_total_pedido"] = pd.cut(
        df["total_pedido"],
        bins=[0, 300, 520, float("inf")],
        labels=["Bajo", "Medio", "Alto"],
        include_lowest=True
    )

    columnas_ordenadas = [
        "id_ticket_modelado",
        "fecha",
        "anio_mes",
        "dia",
        "mes",
        "nombre_mes",
        "trimestre",
        "anio",
        "dia_semana",
        "dia_tipo",
        "fin_semana",
        "id_cliente",
        "id_sucursal",
        "ciudad",
        "capacidad_sucursal",
        "id_empleado",
        "tipo_empleado",
        "salario",
        "turno",
        "id_mesa",
        "numero_mesa",
        "capacidad_mesa",
        "id_metodo_pago",
        "metodo_pago",
        "lineas_ticket",
        "cantidad_total",
        "platillos_distintos",
        "categorias_distintas",
        "subtotal_ticket",
        "total_pedido",
        "monto_pago",
        "diferencia_pago",
        "residuo_subtotal_total",
        "residuo_abs_subtotal_total",
        "residuo_pago_total",
        "ticket_consistente_subtotal",
        "ticket_consistente_pago",
        "incluye_bebida",
        "incluye_postre",
        "incluye_entrada",
        "incluye_platillo_fuerte",
        "ticket_alto",
        "rango_total_pedido"
    ]

    # Reordena columnas y exporta la base oficial del EDA.
    df = df[columnas_ordenadas]
    df.to_parquet(OUTPUT_PATH, index=False)

    print("Base EDA exportada correctamente")
    print(f"Filas exportadas: {len(df)}")
    print(f"Archivo generado: {OUTPUT_PATH}")


if __name__ == "__main__":
    preparar_base_eda()
