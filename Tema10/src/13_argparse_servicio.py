"""
Tema 10 - Biblioteca estándar
Laboratorio 13: argumentos de línea de comandos con argparse.

Objetivo:
    Convertir un script en una herramienta parametrizable desde terminal.

Ejemplos:
    python 13_argparse_servicio.py --servicio ssh --puerto 22
    python 13_argparse_servicio.py --servicio api --puerto 70000
"""

import argparse


def puerto_valido(puerto):
    """Devuelve True si el puerto está dentro del rango válido."""
    return 1 <= puerto <= 65535


parser = argparse.ArgumentParser(description="Comprobar un servicio y su puerto.")
parser.add_argument("--servicio", default="ssh", help="Nombre del servicio")
parser.add_argument("--puerto", type=int, default=22, help="Puerto TCP/UDP")

args = parser.parse_args()

print("Servicio:", args.servicio)
print("Puerto:", args.puerto)

if puerto_valido(args.puerto):
    print("Resultado: puerto válido")
else:
    print("Resultado: puerto fuera de rango")
