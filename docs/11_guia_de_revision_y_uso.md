# 11 Guía de Revisión y Uso

## Objetivo de esta guía

Este archivo resume cómo revisar rápidamente el proyecto y cómo aprovechar sus salidas para el equipo de Qlik o para una revisión técnica general.

## Fuente del proyecto

La capa de Machine Learning trabaja sobre:

- base: `restaurante`
- esquema: `olap`
- tabla principal: `olap.fact_ventas`

## Flujo seguido

1. validar el `OLAP` de Víctor
2. reconstruir tickets
3. generar la base principal en `Parquet`
4. preparar la base `EDA`
5. entrenar `3` modelos
6. exportar resultados en `Parquet`

## Cómo generar los parquets paso a paso

La ruta principal del proyecto es ejecutar los notebooks por etapa.

Cada notebook toma su entrada desde la carpeta `parquets/` del proyecto y guarda su salida también dentro de esa misma carpeta local. Así el proceso queda concentrado dentro del repositorio y puede revisarse por etapas.

En la etapa `01`, la entrada no es otro parquet. Esa etapa se conecta a la base `restaurante`, consulta el esquema `olap` y ejecuta la lógica definida en:

- `sql/04_base_tickets_modelado.sql`

Con eso genera el primer parquet del flujo.

Orden recomendado:

1. `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb`
2. `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`
3. `notebooks/03_Modelo_Clasificacion_Ticket_Alto/03_Modelo_Clasificacion_Ticket_Alto.ipynb`
4. `notebooks/04_Modelo_Regresion_Total_Pedido/04_Modelo_Regresion_Total_Pedido.ipynb`
5. `notebooks/05_Modelo_Segmentacion_Clientes/05_Modelo_Segmentacion_Clientes.ipynb`

Con ese orden se generan las salidas `01` a `05` dentro de `parquets/`.

## Cómo usar los notebooks

Su función principal es:

- ejecutar cada etapa
- mostrar el proceso paso a paso
- revisar visualmente la información
- explicar la lógica de cada etapa
- enseñar tablas, métricas y gráficas de apoyo
- exportar el parquet correspondiente de la etapa

## Cómo se conectan SQL, notebooks y parquets

La relación entre archivos es esta:

1. `sql/04_base_tickets_modelado.sql` define la consulta de la base inicial
2. `01_Carga_y_Validacion_Parquet.ipynb` ejecuta esa consulta y genera el parquet `01`
3. `02_EDA_Base_Tickets.ipynb` lee el parquet `01` y genera el parquet `02`
4. `03`, `04` y `05` leen el parquet `02` y generan sus salidas finales

## Parquets finales a revisar

1. `parquets/01_Carga_y_Validacion_Parquet/01_base_tickets_modelado.parquet`
2. `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`
3. `parquets/03_Modelo_Clasificacion_Ticket_Alto/03_tickets_clasificados.parquet`
4. `parquets/04_Modelo_Regresion_Total_Pedido/04_tickets_regresion.parquet`
5. `parquets/05_Modelo_Segmentacion_Clientes/05_clientes_segmentados.parquet`

## Cómo se puede revisar este proyecto

- abrir el `README.md` principal
- revisar esta guía
- consultar los documentos del `docs/05` al `docs/10`
- consultar `docs/12_entender_base_tickets.md` para entender la base inicial
- abrir los notebooks `01` a `05`
- revisar los parquets y su documentación por etapa

## Cómo puede usar esto el equipo de Qlik

### Etapa 01

Sirve como base general de tickets para entender el negocio.

### Etapa 02

Sirve para hojas exploratorias y validación de consistencia.

### Etapa 03

Sirve para visualizar probabilidades y clasificación de tickets altos.

### Etapa 04

Sirve para comparar total real vs total estimado y analizar error del modelo.

### Etapa 05

Sirve para segmentar clientes y construir tableros de valor, frecuencia y gasto.

Para el equipo de Qlik, los archivos más importantes son:

1. `03_tickets_clasificados.parquet`
2. `04_tickets_regresion.parquet`
3. `05_clientes_segmentados.parquet`

## Sentido de negocio

Los modelos elegidos tienen sentido para la empresa restaurante porque permiten responder tres preguntas útiles:

1. **Clasificación:** qué condiciones se relaciónan con tickets altos
2. **Regresión:** cuánto podría valer un pedido según su contexto
3. **Segmentación:** qué tipos de clientes tiene el restaurante según su comportamiento histórico

## Validación general

Los resultados son coherentes con el volumen del `OLAP` y con la granularidad del proyecto:

- etapas `01` a `04`: `1167` tickets
- etapa `05`: `800` clientes

Esto es consistente porque la etapa `05` ya no trabaja por ticket, sino por cliente agregado.
