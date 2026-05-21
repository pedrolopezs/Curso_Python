"""
Tema 9 - Módulos
Laboratorio 3: pathlib, shutil y subprocess.

Objetivo:
    Usar módulos estándar para trabajar con rutas, copiar ficheros completos
    y ejecutar un comando externo de forma controlada.
"""

from pathlib import Path
import shutil
import subprocess

print("=== 1. Crear fichero de configuración con pathlib ===")
carpeta = Path("data")
carpeta.mkdir(exist_ok=True)

origen = carpeta / "config.json"
origen.write_text('{"servicio": "ssh", "puerto": 22}\n', encoding="utf-8")

print("Fichero creado:", origen)
print("Contenido:", origen.read_text(encoding="utf-8").strip())

print("\n=== 2. Copiar fichero con shutil.copy2() ===")
destino = carpeta / "config_copia.json"
shutil.copy2(origen, destino)
print("Copia creada:", destino)
print("Existe destino:", destino.exists())

print("\n=== 3. Ejecutar comando externo con subprocess.run() ===")
resultado = subprocess.run(
    ["ls", "-l", str(carpeta)],
    capture_output=True,
    text=True,
    check=False,
)
print("Código de retorno:", resultado.returncode)
print("Salida estándar:")
print(resultado.stdout.strip())
if resultado.stderr:
    print("Salida de error:")
    print(resultado.stderr.strip())
