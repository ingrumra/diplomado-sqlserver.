# Taller Módulo 2 · SQL Server y T-SQL

**Estudiante:** Ingrid Umbacía  
**Tema:** Caso práctico de biblioteca  
**Herramientas:** Python, pandas, pymssql y SQL Server

Este repositorio contiene el desarrollo del taller evaluable del Módulo 2. El ejercicio consiste en crear una base de datos de biblioteca, cargar datos sintéticos y resolver diez consultas usando T-SQL desde un notebook de Python.

## Archivos

- `M2_taller_notebook_estudiante_RESUELTO_CON_SALIDAS.ipynb`: notebook final desarrollado y con salidas visibles.
- `M2_taller_notebook_estudiante_ORIGINAL.ipynb`: notebook base entregado en clase.
- `requirements.txt`: dependencias de Python.
- `probar_conexion.py`: prueba rápida de conexión a SQL Server.
- `GUIA_ENTREGA_RAPIDA_M2.md`: guía breve para ejecutar y revisar la entrega.

## Consultas desarrolladas

1. `SELECT`, `TOP` y ordenamiento.
2. Filtros usando variables de Python.
3. Paginación con `OFFSET` y `FETCH`.
4. Funciones de fecha.
5. Funciones de texto.
6. Conversión de tipos.
7. Manejo de valores nulos.
8. Lógica condicional con `CASE` e `IIF`.
9. CTE para agregación por categoría.
10. Funciones de ventana con `ROW_NUMBER` y `PARTITION BY`.

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

## Prueba de conexión

```bash
python probar_conexion.py
```

## Ejecución

Abrir el notebook `M2_taller_notebook_estudiante_RESUELTO_CON_SALIDAS.ipynb` y ejecutar las celdas en orden. El notebook ya conserva salidas visibles para revisión en GitHub.
