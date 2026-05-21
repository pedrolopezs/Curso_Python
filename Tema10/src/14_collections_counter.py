"""
Tema 10 - Biblioteca estándar
Laboratorio 14: colecciones especializadas con collections.

Objetivo:
    Usar Counter y defaultdict para resumir datos de forma clara.
"""

from collections import Counter, defaultdict


servicios = [
    {"nombre": "ssh", "estado": "OK", "equipo": "srv-web-01"},
    {"nombre": "nginx", "estado": "OK", "equipo": "srv-web-01"},
    {"nombre": "api", "estado": "ERROR", "equipo": "srv-app-01"},
    {"nombre": "backup", "estado": "ERROR", "equipo": "srv-bkp-01"},
    {"nombre": "dns", "estado": "OK", "equipo": "srv-dns-01"},
]

print("=== Conteo de estados con Counter ===")
conteo_estados = Counter(servicio["estado"] for servicio in servicios)
print(conteo_estados)
print("Servicios con ERROR:", conteo_estados["ERROR"])

print("\n=== Agrupar servicios por equipo con defaultdict ===")
servicios_por_equipo = defaultdict(list)

for servicio in servicios:
    servicios_por_equipo[servicio["equipo"]].append(servicio["nombre"])

for equipo, nombres in servicios_por_equipo.items():
    print(equipo, "->", ", ".join(nombres))
