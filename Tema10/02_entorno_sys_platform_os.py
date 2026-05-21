"""
Tema 9 - Módulos
Laboratorio 2: sys, platform y os.

Objetivo:
    Usar módulos estándar para obtener información básica del intérprete, del
    sistema operativo y del proceso actual.
"""

import os
import platform
import sys

print("=== 1. Información del intérprete Python ===")
print("Versión completa:", sys.version)
print("Versión corta:", sys.version.split()[0])
print("Ejecutable:", sys.executable)

print("\n=== 2. Primeras rutas de búsqueda de módulos ===")
for ruta in sys.path[:5]:
    print(ruta)

print("\n=== 3. Información del sistema operativo ===")
print("Sistema:", platform.system())
print("Release:", platform.release())
print("Versión:", platform.version())
print("Arquitectura:", platform.machine())

print("\n=== 4. Variables de entorno y proceso ===")
usuario = os.environ.get("USER") or os.environ.get("USERNAME")
print("Usuario:", usuario)
print("PID actual:", os.getpid())
print("Directorio actual:", os.getcwd())
