# Guía de Parquets del Proyecto

Esta carpeta concentra los archivos `Parquet` del proyecto y su documentación asociada.

Organización por etapa:

1. `01_Carga_y_Validacion_Parquet`
2. `02_EDA_Base_Tickets`
3. `03_Modelo_Clasificacion_Ticket_Alto`
4. `04_Modelo_Regresion_Total_Pedido`
5. `05_Modelo_Segmentacion_Clientes`

Cada subcarpeta puede contener:

- el archivo `Parquet` principal de la etapa
- un archivo `.md` que explica qué contiene, para qué sirve y cómo se puede visualizar en Qlik

Para evitar confusión, las métricas de los modelos quedaron integradas en los archivos `.md` de cada etapa, no como parquets separados.

Cada uno de estos archivos también puede regenerarse desde el notebook correspondiente de su etapa.

El parquet `01` nace directamente desde la base `restaurante.olap`, mientras que los demás se generan a partir de los parquets previos dentro del mismo flujo del proyecto.

## Por qué existen 5 parquets

Los `5` parquets no representan `5` modelos distintos.

- `01` y `02` son parquets de soporte del proceso
- `03`, `04` y `05` corresponden a los `3` modelos de Machine Learning

La idea del flujo es:

1. construir la base principal
2. preparar la base para `EDA`
3. entrenar y exportar el modelo de clasificación
4. entrenar y exportar el modelo de regresión
5. entrenar y exportar el modelo de segmentación

## Qué parquets le interesan a Qlik

Para el equipo de Qlik, los archivos más importantes son:

- `03_tickets_clasificados.parquet`
- `04_tickets_regresion.parquet`
- `05_clientes_segmentados.parquet`

Los archivos `01` y `02` sirven principalmente para explicar y validar el proceso interno de construcción de la base.
