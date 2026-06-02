from pathlib import Path
import runpy


# Este archivo sirve como punto de entrada claro para la etapa 05.
SCRIPT_PATH = Path(__file__).resolve().parents[1] / "05_entrenar_kmeans_clientes.py"


if __name__ == "__main__":
    # Ejecuta el script principal del modelo de segmentacion de clientes.
    runpy.run_path(str(SCRIPT_PATH), run_name="__main__")
