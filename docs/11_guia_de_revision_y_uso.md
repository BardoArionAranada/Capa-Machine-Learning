# 11 Guia de Revision y Uso

## Objetivo de esta guia

Este archivo resume como revisar rapidamente el proyecto y como aprovechar sus salidas para el equipo de Qlik o para una revision tÃ©cnica general.

## Fuente del proyecto

La capa de Machine Learning trabaja sobre:

- base: `restaurante`
- esquema: `olap`
- tabla principal: `olap.fact_ventas`

## Flujo seguido

1. validar el `OLAP` de VÃ­ctor
2. reconstruir tickets
3. generar la base principal en `Parquet`
4. preparar la base `EDA`
5. entrenar `3` modelos
6. exportar resultados en `Parquet`

## Como generar los parquets paso a paso

La ruta principal del proyecto es ejecutar los notebooks por etapa.

Cada notebook toma su entrada desde la carpeta `parquets/` del proyecto y guarda su salida tambiÃ©n dentro de esa misma carpeta local. Asi el proceso queda concentrado dentro del repositorio y puede revisarse por etapas.

En la etapa `01`, la entrada no es otro parquet. Esa etapa se conecta a la base `restaurante`, consulta el esquema `olap` y ejecuta la lÃ³gica definida en:

- `sql/04_base_tickets_modelado.sql`

Con eso genera el primer parquet del flujo.

Orden recomendado:

1. `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb`
2. `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`
3. `notebooks/03_Modelo_Clasificacion_Ticket_Alto/03_Modelo_Clasificacion_Ticket_Alto.ipynb`
4. `notebooks/04_Modelo_Regresion_Total_Pedido/04_Modelo_Regresion_Total_Pedido.ipynb`
5. `notebooks/05_Modelo_Segmentacion_Clientes/05_Modelo_Segmentacion_Clientes.ipynb`

Con ese orden se generan las salidas `01` a `05` dentro de `parquets/`.

## Como usar los notebooks

Su funcion principal es:

- ejecutar cada etapa
- mostrar el proceso paso a paso
- revisar visualmente la informaciÃ³n
- explicar la lÃ³gica de cada etapa
- ensenar tablas, mÃ©tricas y grÃ¡ficas de apoyo
- exportar el parquet correspondiente de la etapa

## Como se conectan SQL, notebooks y parquets

La relaciÃ³n entre archivos es esta:

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

## Como se puede revisar este proyecto

- abrir el `README.md` principal
- revisar esta guia
- consultar los documentos del `docs/05` al `docs/10`
- consultar `docs/12_entender_base_tickets.md` para entender la base inicial
- abrir los notebooks `01` a `05`
- revisar los parquets y su documentacion por etapa

## Como puede usar esto el equipo de Qlik

### Etapa 01

Sirve como base general de tickets para entender el negocio.

### Etapa 02

Sirve para hojas exploratorias y validaciÃ³n de consistencia.

### Etapa 03

Sirve para visualizar probabilidades y clasificaciÃ³n de tickets altos.

### Etapa 04

Sirve para comparar total real vs total estimado y analizar error del modelo.

### Etapa 05

Sirve para segmentar clientes y construir tableros de valor, frecuencia y gasto.

Para el equipo de Qlik, los archivos mÃ¡s importantes son:

1. `03_tickets_clasificados.parquet`
2. `04_tickets_regresion.parquet`
3. `05_clientes_segmentados.parquet`

## Sentido de negocio

Los modelos elegidos tienen sentido para la empresa restaurante porque permiten responder tres preguntas utiles:

1. **ClasificaciÃ³n:** que condiciones se relacionan con tickets altos
2. **RegresiÃ³n:** cuanto podrÃ­a valer un pedido segun su contexto
3. **SegmentaciÃ³n:** que tipos de clientes tiene el restaurante segun su comportamiento histÃ³rico

## Validación general

Los resultados son coherentes con el volumen del `OLAP` y con la granularidad del proyecto:

- etapas `01` a `04`: `1167` tickets
- etapa `05`: `800` clientes

Esto es consistente porque la etapa `05` ya no trabaja por ticket, sino por cliente agregado.
