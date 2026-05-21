"""
Tema 10 - Biblioteca estándar
Laboratorio 8: registros operativos con logging.

Objetivo:
    Registrar información técnica en un fichero log y mostrar al usuario
    mensajes controlados por pantalla.
"""

from pathlib import Path
import logging


BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "soporte.log"

# force=True permite reconfigurar logging si el script se relanza desde un entorno interactivo.
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)

print("=== Registrar operación ===")
logging.info("Inicio de comprobación de infraestructura.")
logging.warning("Latencia alta detectada en el servicio API.")

try:
    raise ConnectionRefusedError("Conexión rechazada por el puerto 5432")
except ConnectionRefusedError as error:
    logging.error("Fallo en nodo srv-db-01: %s", error)
    print("Error: La base de datos no está disponible en este momento.")

print("Log generado en:", LOG_FILE)
print("Últimas líneas del log:")
print(LOG_FILE.read_text(encoding="utf-8").strip().splitlines()[-3:])
