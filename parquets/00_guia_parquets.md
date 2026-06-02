# Guia de Parquets del Proyecto

Esta carpeta concentra los archivos `Parquet` del proyecto y su documentacion asociada.

Organizacion por etapa:

1. `01_Carga_y_Validacion_Parquet`
2. `02_EDA_Base_Tickets`
3. `03_Modelo_Clasificacion_Ticket_Alto`
4. `04_Modelo_Regresion_Total_Pedido`
5. `05_Modelo_Segmentacion_Clientes`

Cada subcarpeta puede contener:

- el archivo `Parquet` principal de la etapa
- un archivo `.md` que explica que contiene, para que sirve y como se puede visualizar en Qlik

Para evitar confusion, las metricas de los modelos quedaron integradas en los archivos `.md` de cada etapa, no como parquets separados.

Cada uno de estos archivos tambien puede regenerarse desde el notebook correspondiente de su etapa.

## Por que existen 5 parquets

Los `5` parquets no representan `5` modelos distintos.

- `01` y `02` son parquets de soporte del proceso
- `03`, `04` y `05` corresponden a los `3` modelos de Machine Learning

La idea del flujo es:

1. construir la base principal
2. preparar la base para `EDA`
3. entrenar y exportar el modelo de clasificacion
4. entrenar y exportar el modelo de regresion
5. entrenar y exportar el modelo de segmentacion

## Que parquets le interesan a Qlik

Para el equipo de Qlik, los archivos mas importantes son:

- `03_tickets_clasificados.parquet`
- `04_tickets_regresion.parquet`
- `05_clientes_segmentados.parquet`

Los archivos `01` y `02` sirven principalmente para explicar y validar el proceso interno de construccion de la base.
