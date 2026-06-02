# Capa Machine Learning

Repositorio de trabajo para la fase de **Machine Learning** del proyecto final de la materia **Desarrollo de Inteligencia de Negocios**.

## Contexto del proyecto

El proyecto completo se construyo por capas entre varios equipos:

1. `OLTP`
2. `ETL`
3. `OLAP`
4. `Machine Learning`
5. `Visualizacion en Qlik`

En esta etapa ya no se trabajara sobre el `DW` del ETL como fuente principal, sino sobre el **modelo OLAP de Victor**, que se tomo como fuente principal para la fase de Machine Learning.

## Tema del proyecto

La base representa la operacion de un **restaurante**.

La capa de Machine Learning se enfocara especificamente en el comportamiento de **ventas** del restaurante a partir del esquema analitico `olap`.

## Fuente principal de datos

Base local:

- `restaurante`

Esquema principal:

- `olap`

Tabla de hechos principal:

- `olap.fact_ventas`

Dimensiones disponibles:

- `olap.dim_tiempo`
- `olap.dim_cliente`
- `olap.dim_platillo`
- `olap.dim_sucursal`
- `olap.dim_empleado`
- `olap.dim_mesa`
- `olap.dim_metodo_pago`

## Estado validado del OLAP de Victor

Conteos validados en local:

- `olap.fact_ventas = 5380`
- `olap.dim_tiempo = 365`
- `olap.dim_cliente = 800`
- `olap.dim_platillo = 60`
- `olap.dim_sucursal = 5`
- `olap.dim_empleado = 50`
- `olap.dim_mesa = 80`
- `olap.dim_metodo_pago = 4`

Total de registros del esquema `olap`:

- `6744`

Observacion importante:

- El requisito de `10000` datos se cumple en la capa `OLTP`.
- El `OLAP` de Victor quedo enfocado a ventas, por eso su volumen es menor.

## Enfoque de trabajo

El flujo de esta capa sera:

1. Explorar el `OLAP` de Victor.
2. Reconstruir una base analitica por ticket a partir de `olap.fact_ventas`.
3. Exportar la base inicial a `Parquet`.
4. Trabajar los modelos en Python a partir del `Parquet`.
5. Exportar resultados en `Parquet` para el equipo de Qlik.

## Modelos definidos

Con la estructura actual del `OLAP`, los tres modelos definidos para el proyecto son:

1. **Regresion Logistica**
   - objetivo: predecir si un ticket pertenece a ventas altas
   - base: tickets reconstruidos desde `olap.fact_ventas`

2. **Regresion Lineal**
   - objetivo: estimar el `total_pedido`
   - base: tickets reconstruidos y enriquecidos con dimensiones

3. **K-Means**
   - objetivo: agrupar clientes por comportamiento de compra
   - base: agregados historicos por cliente

## Primer paso real del proyecto

El primer paso no es entrenar modelos todavia.

Primero se debe:

1. validar el cubo `olap`
2. reconstruir los tickets
3. generar la **base de modelado**
4. exportarla a `Parquet`

Archivos iniciales para ese paso:

- `sql/01_exploracion_inicial_olap_victor.sql`
- `sql/04_base_tickets_modelado.sql`
- `scripts/01_exportar_base_tickets_olap.py`

## Estructura del repositorio

- `docs/` documentacion del proceso
- `sql/` consultas y construccion de bases analiticas
- `scripts/` scripts en Python para extraccion, modelado y exportacion
- `notebooks/` exploracion y experimentacion
- `parquets/` archivos `Parquet` organizados por etapa
- `models/` artefactos de modelos entrenados
- `reports/` salidas para reporte final
- `data/` archivos temporales y auxiliares de trabajo

## Entrega para Qlik

La salida principal para el equipo de visualizacion sera en:

- `Parquet`

La idea es entregarles al menos:

- una base con predicciones por ticket
- una base con segmentos o scores por cliente

## Parquets finales por etapa

Dentro de la carpeta `parquets/` quedaron las salidas del proyecto organizadas por etapa:

1. `01_Carga_y_Validacion_Parquet/01_base_tickets_modelado.parquet`
2. `02_EDA_Base_Tickets/02_base_eda_tickets.parquet`
3. `03_Modelo_Clasificacion_Ticket_Alto/03_tickets_clasificados.parquet`
4. `04_Modelo_Regresion_Total_Pedido/04_tickets_regresion.parquet`
5. `05_Modelo_Segmentacion_Clientes/05_clientes_segmentados.parquet`

Cada etapa tiene su archivo `.md` explicando:

- que contiene
- por que sirve para el restaurante
- por que se eligio ese enfoque
- como se podria usar en Qlik

## Documentacion

La evidencia del trabajo se mantendra en:

- `docs/01_bitacora.md`
- `docs/02_estado_tecnico_inicial.md`
- `docs/03_modelo_olap_victor.md`
- `docs/04_plan_de_trabajo_ml.md`
- `docs/05_paso_01_generar_parquet.md`
- `docs/06_seleccion_de_modelos.md`
- `docs/07_paso_02_eda_tickets.md`
- `docs/08_paso_03_clasificacion_ticket_alto.md`
- `docs/09_paso_04_regresion_total_pedido.md`
- `docs/10_paso_05_segmentacion_clientes.md`
- `docs/11_guia_de_revision_y_uso.md`

## Estructura de notebooks

Siguiendo el formato trabajado en Mineria de Datos, esta capa se documentara tambien en notebooks `.ipynb` por etapa:

1. `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb`
2. `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`
3. `notebooks/03_Modelo_Clasificacion_Ticket_Alto/03_Modelo_Clasificacion_Ticket_Alto.ipynb`
4. `notebooks/04_Modelo_Regresion_Total_Pedido/04_Modelo_Regresion_Total_Pedido.ipynb`
5. `notebooks/05_Modelo_Segmentacion_Clientes/05_Modelo_Segmentacion_Clientes.ipynb`

## Estado actual

- [x] Repositorio base creado
- [x] Entorno local preparado en PostgreSQL
- [x] OLTP validado
- [x] ETL revisado como antecedente tecnico
- [x] OLAP de Victor montado y validado
- [x] Alcance ajustado a `3 modelos de machine learning`
- [x] Formato principal de salida definido en `Parquet`
- [x] Explorar el OLAP con consultas de negocio
- [x] Generar la base de tickets para modelado
- [x] Exportar la base inicial a `Parquet`
- [x] Preparar la base derivada para `EDA` en `Parquet`
- [x] Entrenar el primer modelo
- [x] Exportar resultados del primer modelo a `Parquet`
- [x] Entrenar el segundo modelo
- [x] Exportar resultados del segundo modelo a `Parquet`
- [x] Entrenar el tercer modelo
- [x] Exportar resultados del tercer modelo a `Parquet`

## Resultados validados

Resumen final de salidas:

- etapa `01`: `1167` tickets modelados
- etapa `02`: `1167` tickets para `EDA`
- etapa `03`: clasificacion de `ticket_alto` con `accuracy = 0.6282` y `roc_auc = 0.7278`
- etapa `04`: regresion de `total_pedido` con `mae = 92.3532` y `r2 = 0.2364`
- etapa `05`: segmentacion de `800` clientes en `3` clusters con `silhouette = 0.3836`

## Coherencia general de los resultados

Los resultados son coherentes con la informacion disponible porque:

- el `OLAP` de Victor se enfoca en ventas y permite reconstruir tickets
- la base final de tickets mantiene el mismo volumen entre las etapas `01` a `04`
- la etapa `05` reduce la granularidad a cliente, por eso baja de `1167` tickets a `800` clientes
- los tres modelos responden a necesidades distintas del restaurante:
  - clasificar tickets altos
  - estimar el total del pedido
  - segmentar clientes por comportamiento historico
