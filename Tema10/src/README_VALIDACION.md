# Tema 10 - Biblioteca estándar - src

Scripts generados para los laboratorios del Tema 10.

## Ejecución recomendada

Desde la carpeta del tema:

```bash
cd ~/Curso_Python/Tema10
source .venv/bin/activate
cd src
python --version
```

Ejecutar los scripts por orden:

```bash
python 01_documentacion_y_paquetes.py
python 02_familias_modulos.py
python 03_sistema_entorno.py
python 04_rutas_ficheros.py
python 05_temporales.py
python 06_procesos_subprocess.py
python 07_formatos_datos.py
python 08_logging.py
python 09_fechas_zonas.py
python 10_seguridad_basica.py
python 11_sqlite3_persistencia.py
python 12_http_urllib.py
python 13_argparse_servicio.py --servicio ssh --puerto 22
python 14_collections_counter.py
python 15_ejemplo_integrado_soporte.py
```

## Notas

- Todos los scripts usan únicamente módulos de la biblioteca estándar.
- Cada script crea los ficheros o directorios que necesita bajo `Tema10/data`, `Tema10/logs`, `Tema10/output` o `Tema10/backup`.
- El script `12_http_urllib.py` requiere conexión a Internet; si no hay salida, debe fallar de forma controlada.
