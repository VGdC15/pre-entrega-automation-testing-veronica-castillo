import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def leer_json(nombre_archivo):
    """Lee un archivo JSON ubicado dentro de la carpeta data."""
    ruta_archivo = DATA_DIR / nombre_archivo

    with ruta_archivo.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def obtener_datos_prueba():
    """Devuelve todos los datos de prueba del proyecto."""
    return leer_json("test_data.json")