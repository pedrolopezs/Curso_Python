"""
Tema 9 - Módulos
Laboratorio 4: datetime, calendar, random y secrets.

Objetivo:
    Usar módulos estándar para fechas, calendarios, selección pseudoaleatoria
    y generación de tokens seguros.
"""

from datetime import date, datetime, timedelta
import calendar
import random
import secrets

print("=== 1. Fechas con datetime ===")
hoy = date.today()
ventana = hoy + timedelta(days=7)
print("Hoy:", hoy.isoformat())
print("Ventana de mantenimiento:", ventana.isoformat())
print("Fecha y hora actual:", datetime.now().isoformat(timespec="seconds"))

print("\n=== 2. Consultas con calendar ===")
print("Año actual:", hoy.year)
print("¿Es bisiesto?", calendar.isleap(hoy.year))
print("Calendario del mes actual:")
print(calendar.month(hoy.year, hoy.month))

print("\n=== 3. random para pruebas no críticas ===")
servicios = ["ssh", "nginx", "postgresql", "backup"]
print("Servicio seleccionado para prueba:", random.choice(servicios))
print("Muestra de dos servicios:", random.sample(servicios, 2))

print("\n=== 4. secrets para tokens de seguridad ===")
token = secrets.token_hex(16)
print("Token seguro:", token)
