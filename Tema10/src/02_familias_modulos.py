"""
Tema 10 - Biblioteca estándar
Laboratorio 2: familias de módulos útiles en administración TI.

Objetivo:
    Clasificar módulos estándar por área de uso para facilitar su selección.
"""

modulos = {
    "sistema_y_entorno": ["sys", "os", "platform"],
    "ficheros_y_rutas": ["pathlib", "shutil", "glob", "tempfile"],
    "procesos": ["subprocess"],
    "datos": ["csv", "json", "configparser", "tomllib"],
    "operacion": ["logging", "datetime", "zoneinfo"],
    "seguridad": ["hashlib", "hmac", "secrets", "random"],
    "persistencia": ["sqlite3"],
    "http_basico": ["urllib"],
    "linea_comandos": ["argparse"],
    "colecciones": ["collections"],
}

print("=== Familias de módulos estándar ===")
for area, nombres in modulos.items():
    print(f"{area:20} -> {', '.join(nombres)}")
