from pathlib import Path
import runpy


# Este archivo sirve como punto de entrada claro para la etapa 04.
SCRIPT_PATH = Path(__file__).resolve().parents[1] / "04_entrenar_regresion_total_pedido.py"


if __name__ == "__main__":
    # Ejecuta el script principal del modelo de regresion del total del pedido.
    runpy.run_path(str(SCRIPT_PATH), run_name="__main__")
