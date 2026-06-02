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

## 3. Generar la base de tickets desde el notebook 01

Notebook a ejecutar:

- `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb`

Ese notebook:

- consulta el `OLAP`
- reconstruye la base por ticket
- valida la estructura
- exporta el parquet de la etapa `01`

## 4. Salida esperada

Archivo generado:

- `parquets/01_Carga_y_Validacion_Parquet/01_base_tickets_modelado.parquet`

## 5. Resultado esperado del paso

Al terminar este paso ya debe existir:

- una base por ticket lista para Machine Learning
- un `Parquet` inicial para trabajar en Python
- el punto de partida para los tres modelos del proyecto

## 6. Siguiente paso inmediato

Despues de cerrar la etapa `01`, se debe ejecutar:

- `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`

para leer el parquet generado y construir la base de `EDA`.
