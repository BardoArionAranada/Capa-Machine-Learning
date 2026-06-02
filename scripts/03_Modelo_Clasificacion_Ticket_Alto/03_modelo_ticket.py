from pathlib import Path
import runpy


# Este archivo sirve como punto de entrada claro para la etapa 03.
SCRIPT_PATH = Path(__file__).resolve().parents[1] / "03_entrenar_regresion_logistica.py"


if __name__ == "__main__":
    # Ejecuta el script principal del modelo de clasificacion de tickets altos.
    runpy.run_path(str(SCRIPT_PATH), run_name="__main__")
