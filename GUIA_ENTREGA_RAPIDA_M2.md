# Guía rápida de entrega · Taller Módulo 2

## Contenido de la entrega

Este repositorio contiene el desarrollo del taller evaluable del Módulo 2 sobre SQL Server y T-SQL, usando Python como entorno de conexión y visualización de resultados.

Archivos principales:

- `M2_taller_notebook_estudiante_RESUELTO_CON_SALIDAS.ipynb`: notebook desarrollado, comentado y con salidas visibles.
- `M2_taller_notebook_estudiante_ORIGINAL.ipynb`: versión original del taller, incluida como respaldo.
- `requirements.txt`: librerías necesarias para ejecutar el notebook.
- `probar_conexion.py`: script auxiliar para comprobar conexión a SQL Server.
- `README.md`: descripción general del repositorio.

## Objetivo del taller

El taller desarrolla un caso práctico de biblioteca. Primero se crea una base de datos llamada `biblioteca`, luego se crean dos tablas relacionales: `lectores` y `prestamos`. Después se cargan datos sintéticos y se resuelven diez consultas usando instrucciones y funciones de T-SQL.

## Temas desarrollados

1. Creación de base de datos y conexión desde Python.
2. Creación de tablas con llave primaria y llave foránea.
3. Inserción de datos sintéticos.
4. Consultas con `SELECT`, `TOP`, `ORDER BY` y filtros.
5. Uso de variables de Python dentro de consultas SQL.
6. Paginación con `OFFSET` y `FETCH`.
7. Funciones de fecha: `GETDATE`, `DATEADD`, `DATEDIFF`, `YEAR` y `MONTH`.
8. Funciones de texto: `LOWER`, `LEN`, `CHARINDEX` y `SUBSTRING`.
9. Conversión de tipos con `CONVERT` y `TRY_CONVERT`.
10. Manejo de nulos con `COALESCE`.
11. Lógica condicional con `IIF` y `CASE`.
12. CTE con `WITH`.
13. Funciones de ventana con `ROW_NUMBER` y `PARTITION BY`.

## Cómo subir a GitHub

1. Crear un repositorio nuevo en GitHub.
2. Subir estos archivos al repositorio:
   - `M2_taller_notebook_estudiante_RESUELTO_CON_SALIDAS.ipynb`
   - `M2_taller_notebook_estudiante_ORIGINAL.ipynb`
   - `README.md`
   - `requirements.txt`
   - `probar_conexion.py`
   - `GUIA_ENTREGA_RAPIDA_M2.md`
3. Confirmar el cambio con un mensaje como:

```bash
git commit -m "Entrega taller modulo 2 SQL Server biblioteca"
```

## Cómo ejecutar el notebook

El notebook está diseñado para ejecutarse en un entorno donde SQL Server esté disponible con estos datos de conexión:

```python
server="db"
user="sa"
password="TuClave_Fuerte123"
database="biblioteca"
```

Antes de ejecutar, instalar dependencias:

```bash
pip install -r requirements.txt
```

Luego probar conexión:

```bash
python probar_conexion.py
```

Finalmente, abrir el notebook y ejecutar las celdas en orden.

## Nota de entrega

El notebook `M2_taller_notebook_estudiante_RESUELTO_CON_SALIDAS.ipynb` ya contiene las consultas desarrolladas, comentarios metodológicos y salidas visibles para revisión en GitHub.
