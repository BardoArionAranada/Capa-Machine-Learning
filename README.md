# Capa Machine Learning

Repositorio de trabajo para la fase de **Machine Learning** del proyecto final de la materia **Desarrollo de Inteligencia de Negocios**.

## Contexto del proyecto

El proyecto completo se construyó por capas entre varios equipos:

1. `OLTP`
2. `ETL`
3. `OLAP`
4. `Machine Learning`
5. `Visualización en Qlik`

En esta etapa ya no se trabajará sobre el `DW` del ETL como fuente principal, sino sobre el **modelo OLAP de Víctor**, que se tomó como fuente principal para la fase de Machine Learning.

## Tema del proyecto

La base representa la operación de un **restaurante**.

La capa de Machine Learning se enfocará específicamente en el comportamiento de **ventas** del restaurante a partir del esquema analítico `olap`.

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

## Estado validado del OLAP de Víctor

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

Observación importante:

- El requisito de `10000` datos se cumple en la capa `OLTP`.
- El `OLAP` de Víctor quedó enfocado a ventas, por eso su volumen es menor.

## Enfoque de trabajo

El flujo de esta capa será:

1. Explorar el `OLAP` de Víctor.
2. Reconstruir una base analítica por ticket a partir de `olap.fact_ventas`.
3. Exportar la base inicial a `Parquet`.
4. Trabajar los modelos en Python a partir del `Parquet`.
5. Exportar resultados en `Parquet` para el equipo de Qlik.

## Cómo se ejecuta el proyecto

La generación de resultados se puede seguir directamente desde los notebooks de cada etapa.

Todas las rutas de entrada y salida quedaron definidas dentro de la carpeta local del proyecto. Esto significa que cada notebook toma sus parquets desde `parquets/` y vuelve a guardar sus resultados dentro de esa misma carpeta del repositorio.

Orden recomendado:

1. ejecutar `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb`
2. ejecutar `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`
3. ejecutar `notebooks/03_Modelo_Clasificacion_Ticket_Alto/03_Modelo_Clasificacion_Ticket_Alto.ipynb`
4. ejecutar `notebooks/04_Modelo_Regresion_Total_Pedido/04_Modelo_Regresion_Total_Pedido.ipynb`
5. ejecutar `notebooks/05_Modelo_Segmentacion_Clientes/05_Modelo_Segmentacion_Clientes.ipynb`

Ese flujo genera los `5` parquets principales del proyecto.

Cada notebook:

- realiza su etapa correspondiente
- muestra tablas y métricas
- incluye gráficas de apoyo
- exporta su `Parquet` final

## Modelos definidos

Con la estructura actual del `OLAP`, los tres modelos definidos para el proyecto son:

1. **Regresión Logística**
   - objetivo: predecir si un ticket pertenece a ventas altas
   - base: tickets reconstruidos desde `olap.fact_ventas`

2. **Regresión Lineal**
   - objetivo: estimar el `total_pedido`
   - base: tickets reconstruidos y enriquecidos con dimensiones

3. **K-Means**
   - objetivo: agrupar clientes por comportamiento de compra
   - base: agregados históricos por cliente

## Primer paso real del proyecto

El primer paso no es entrenar modelos todavía.

Primero se debe:

1. validar el cubo `olap`
2. reconstruir los tickets
3. generar la **base de modelado**
4. exportarla a `Parquet`

Archivos iniciales para ese paso:

- `sql/01_exploracion_inicial_olap_victor.sql`
- `sql/04_base_tickets_modelado.sql`
- `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb`

Guía de apoyo para esta base:

- `docs/12_entender_base_tickets.md`

## Estructura del repositorio

- `docs/` documentación del proceso
- `sql/` consultas y construcción de bases analíticas
- `notebooks/` ejecución, exploración y validación por etapa
- `parquets/` archivos `Parquet` organizados por etapa
- `models/` artefactos de modelos entrenados

## Entrega para Qlik

La salida principal para el equipo de visualización será en:

- `Parquet`

Los archivos que interesan directamente para Qlik son:

- `parquets/03_Modelo_Clasificacion_Ticket_Alto/03_tickets_clasificados.parquet`
- `parquets/04_Modelo_Regresion_Total_Pedido/04_tickets_regresion.parquet`
- `parquets/05_Modelo_Segmentacion_Clientes/05_clientes_segmentados.parquet`

## Parquets finales por etapa

Dentro de la carpeta `parquets/` quedaron las salidas del proyecto organizadas por etapa:

1. `01_Carga_y_Validacion_Parquet/01_base_tickets_modelado.parquet`
2. `02_EDA_Base_Tickets/02_base_eda_tickets.parquet`
3. `03_Modelo_Clasificacion_Ticket_Alto/03_tickets_clasificados.parquet`
4. `04_Modelo_Regresion_Total_Pedido/04_tickets_regresion.parquet`
5. `05_Modelo_Segmentacion_Clientes/05_clientes_segmentados.parquet`

Cada etapa tiene su archivo `.md` explicando:

- qué contiene
- por qué sirve para el restaurante
- por qué se eligió ese enfoque
- como se podría usar en Qlik

## Documentación

La evidencia del trabajo se mantendrá en:

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
- `docs/12_entender_base_tickets.md`

## Notebooks disponibles

Los notebooks sirven para ejecutar, explicar y revisar el proyecto de forma visual:

1. `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb`
2. `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`
3. `notebooks/03_Modelo_Clasificacion_Ticket_Alto/03_Modelo_Clasificacion_Ticket_Alto.ipynb`
4. `notebooks/04_Modelo_Regresion_Total_Pedido/04_Modelo_Regresion_Total_Pedido.ipynb`
5. `notebooks/05_Modelo_Segmentacion_Clientes/05_Modelo_Segmentacion_Clientes.ipynb`

El flujo principal del proyecto ya puede ejecutarse por etapas directamente desde los notebooks.

## Estado actual

- [x] Repositorio base creado
- [x] Entorno local preparado en PostgreSQL
- [x] OLTP validado
- [x] ETL revisado como antecedente técnico
- [x] OLAP de Víctor montado y validado
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
- etapa `03`: clasificación de `ticket_alto` con `accuracy = 0.6282` y `roc_auc = 0.7278`
- etapa `04`: regresión de `total_pedido` con `mae = 92.3532` y `r2 = 0.2364`
- etapa `05`: segmentación de `800` clientes en `3` clusters con `silhouette = 0.3836`

## Coherencia general de los resultados

Los resultados son coherentes con la información disponible porque:

- el `OLAP` de Víctor se enfoca en ventas y permite reconstruir tickets
- la base final de tickets mantiene el mismo volumen entre las etapas `01` a `04`
- la etapa `05` reduce la granularidad a cliente, por eso baja de `1167` tickets a `800` clientes
- los tres modelos responden a necesidades distintas del restaurante:
  - clasificar tickets altos
  - estimar el total del pedido
  - segmentar clientes por comportamiento histórico
