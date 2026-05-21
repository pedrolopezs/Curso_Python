# Tema 9 · Notebooks de laboratorio

Estos notebooks están pensados para abrirse desde `Tema09/notebooks`.

Estructura esperada:

```text
Tema09/
├── src/
└── notebooks/
```

Cada notebook localiza automáticamente el directorio `src` y lo guarda en la variable de entorno `TEMA09_SRC`.

En este tema se ejecutan los scripts desde `src` usando celdas `%%bash` y comandos como `python fichero.py`. Este enfoque reproduce mejor el comportamiento de una terminal real y evita problemas de caché de imports dentro del kernel de Jupyter.

Orden recomendado:

1. `01_Modulo_Validaciones.ipynb`
2. `02_Import_Completo.ipynb`
3. `03_Import_Recurso.ipynb`
4. `04_Import_Alias.ipynb`
5. `05_Import_Todo_No_Recomendado.ipynb`
6. `06_Modulo_Importable_Main.ipynb`
7. `07_Errores_Importacion_Pycache.ipynb`
8. `08_Paquete_Propio_Soporte_TI.ipynb`
