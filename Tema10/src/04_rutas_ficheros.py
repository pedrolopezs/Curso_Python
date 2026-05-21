"""
Tema 10 - Biblioteca estándar
Laboratorio 4: rutas y ficheros con pathlib, shutil y glob.

Objetivo:
    Crear ficheros de configuración, copiarlos a una carpeta de backup
    y localizar ficheros por patrón.
"""

from pathlib import Path
import shutil
import glob


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
BACKUP_DIR = BASE_DIR / "backup"

print("=== 1. Preparar directorios ===")
DATA_DIR.mkdir(parents=True, exist_ok=True)
BACKUP_DIR.mkdir(parents=True, exist_ok=True)
print("Data  :", DATA_DIR)
print("Backup:", BACKUP_DIR)

print("\n=== 2. Crear ficheros JSON de ejemplo ===")
(DATA_DIR / "config1.json").write_text('{"servicio": "ssh", "estado": "activo"}\n', encoding="utf-8")
(DATA_DIR / "config2.json").write_text('{"servicio": "nginx", "estado": "activo"}\n', encoding="utf-8")
(DATA_DIR / "notas.txt").write_text("Fichero auxiliar\n", encoding="utf-8")
print("Ficheros creados en:", DATA_DIR)

print("\n=== 3. Copiar el directorio data a backup/data_copia ===")
destino_copia = BACKUP_DIR / "data_copia"
shutil.copytree(DATA_DIR, destino_copia, dirs_exist_ok=True)
print("Copia creada en:", destino_copia)

print("\n=== 4. Buscar ficheros JSON con glob ===")
patron = str(destino_copia / "*.json")
archivos = glob.glob(patron)

for archivo in archivos:
    print("JSON respaldado:", archivo)
