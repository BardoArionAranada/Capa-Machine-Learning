# 11 Guia de Revision y Uso

## Objetivo de esta guia

Este archivo resume como revisar rapidamente el proyecto y como aprovechar sus salidas para el equipo de Qlik o para la revision del profesor.

## Fuente del proyecto

La capa de Machine Learning trabaja sobre:

- base: `restaurante`
- esquema: `olap`
- tabla principal: `olap.fact_ventas`

## Flujo seguido

1. validar el `OLAP` de Victor
2. reconstruir tickets
3. generar la base principal en `Parquet`
4. preparar la base `EDA`
5. entrenar `3` modelos
6. exportar resultados en `Parquet`

## Parquets finales a revisar

1. `parquets/01_Carga_y_Validacion_Parquet/01_base_tickets_modelado.parquet`
2. `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`
3. `parquets/03_Modelo_Clasificacion_Ticket_Alto/03_tickets_clasificados.parquet`
4. `parquets/04_Modelo_Regresion_Total_Pedido/04_tickets_regresion.parquet`
5. `parquets/05_Modelo_Segmentacion_Clientes/05_clientes_segmentados.parquet`

## Como puede revisar esto el profesor

- abrir el `README.md` principal
- revisar esta guia
- consultar los documentos del `docs/05` al `docs/10`
- abrir los notebooks `01` a `05`
- revisar los parquets y su documentacion por etapa

## Como puede usar esto el equipo de Qlik

### Etapa 01

Sirve como base general de tickets para entender el negocio.

### Etapa 02

Sirve para hojas exploratorias y validacion de consistencia.

### Etapa 03

Sirve para visualizar probabilidades y clasificacion de tickets altos.

### Etapa 04

Sirve para comparar total real vs total estimado y analizar error del modelo.

### Etapa 05

Sirve para segmentar clientes y construir tableros de valor, frecuencia y gasto.

## Sentido de negocio

Los modelos elegidos tienen sentido para la empresa restaurante porque permiten responder tres preguntas utiles:

1. **Clasificacion:** que condiciones se relacionan con tickets altos
2. **Regresion:** cuanto podria valer un pedido segun su contexto
3. **Segmentacion:** que tipos de clientes tiene el restaurante segun su comportamiento historico

## Validacion general

Los resultados son coherentes con el volumen del `OLAP` y con la granularidad del proyecto:

- etapas `01` a `04`: `1167` tickets
- etapa `05`: `800` clientes

Esto es consistente porque la etapa `05` ya no trabaja por ticket, sino por cliente agregado.
