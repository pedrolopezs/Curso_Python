"""
Tema 10 - Biblioteca estándar
Laboratorio 1: documentación y módulos incluidos con Python.

Objetivo:
    Comprobar que los módulos estándar se importan sin instalar paquetes externos
    y consultar documentación básica desde el propio módulo.
"""

import json
import shutil
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
BACKUP_DIR = BASE_DIR / "backup"
DATA_DIR.mkdir(parents=True, exist_ok=True)
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

print("=== 1. Consultar documentación breve de un módulo ===")
print(json.__doc__.splitlines()[0])

print("\n=== 2. Convertir un diccionario Python a JSON ===")
servicio = {"servicio": "ssh", "puerto": 22, "estado": "OK"}
texto_json = json.dumps(servicio, indent=4, ensure_ascii=False)
print(texto_json)

print("\n=== 3. Crear un fichero y copiarlo con shutil.copy2() ===")
origen = DATA_DIR / "config.json"
destino = BACKUP_DIR / "config.json"

origen.write_text(texto_json, encoding="utf-8")
shutil.copy2(origen, destino)

print("Origen :", origen)
print("Destino:", destino)
print("Copia creada:", destino.exists())

print("\n=== 4. Comando útil en terminal ===")
print("python -m pydoc json")
