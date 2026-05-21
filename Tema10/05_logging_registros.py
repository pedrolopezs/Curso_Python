"""
Tema 9 - Módulos
Laboratorio 5: logging.

Objetivo:
    Usar logging como alternativa profesional a print() para registrar
    eventos, avisos y errores en scripts de soporte.
"""

from pathlib import Path
import logging

carpeta = Path("data")
carpeta.mkdir(exist_ok=True)
ruta_log = carpeta / "script_soporte.log"

logging.basicConfig(
    filename=ruta_log,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    force=True,
)

logger = logging.getLogger("soporte_ti")
logger.info("Inicio de comprobación")
logger.warning("Servicio detenido: api")
logger.error("Fallo de conexión con srv-db-01")

print("Log generado en:", ruta_log)
print("Contenido del log:")
print(ruta_log.read_text(encoding="utf-8").strip())
