# Paso 01 - Generar la base inicial en Parquet

## Objetivo

Tomar el `OLAP` de Victor, reconstruir una base por ticket y exportarla a `Parquet` para empezar a trabajar los modelos en Python.

## Flujo de ejecucion

### 1. Revisar el OLAP en DBeaver

Conexion:

- `Host = localhost`
- `Port = 5432`
- `Database = restaurante`
- `Schema = olap`
- `Username = postgres`

Archivo a ejecutar:

- `sql/01_exploracion_inicial_olap_victor.sql`

## 2. Instalar dependencias de Python

Desde la carpeta del proyecto:

```powershell
python -m pip install -r requirements.txt
```

## 3. Exportar la base de tickets a Parquet

Script a ejecutar:

- `scripts/01_exportar_base_tickets_olap.py`

Comando:

```powershell
python .\scripts\01_exportar_base_tickets_olap.py
```

## 4. Salida esperada

Archivo generado:

- `data/processed/base_tickets_modelado.parquet`

## 5. Resultado esperado del paso

Al terminar este paso ya debe existir:

- una base por ticket lista para Machine Learning
- un `Parquet` inicial para trabajar en Python
- el punto de partida para los tres modelos del proyecto

## 6. Siguiente paso inmediato

Despues de generar el `Parquet`, se debe abrir:

- `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb`

para validar que el archivo se lea correctamente y que la estructura de la base quede lista para el EDA.
