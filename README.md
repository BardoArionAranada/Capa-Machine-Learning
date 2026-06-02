# Capa Machine Learning

Repositorio de trabajo para la fase de **Machine Learning** del proyecto final de la materia **Desarrollo de Inteligencia de Negocios**.

## Contexto del proyecto

El proyecto completo se construyo por capas entre varios equipos:

1. `OLTP`
2. `ETL`
3. `OLAP`
4. `Machine Learning`
5. `Visualizacion en Qlik`

En esta etapa ya no se trabajara sobre el `DW` del ETL como fuente principal, sino sobre el **modelo OLAP de Victor**, tal como quedo confirmado para la fase de Machine Learning.

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
- El profesor ya confirmo que si se puede avanzar con Machine Learning usando este `OLAP`.

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

## Documentacion

La evidencia del trabajo se mantendra en:

- `docs/01_bitacora.md`
- `docs/02_estado_tecnico_inicial.md`
- `docs/03_modelo_olap_victor.md`
- `docs/04_plan_de_trabajo_ml.md`
- `docs/05_paso_01_generar_parquet.md`
- `docs/06_seleccion_de_modelos.md`
- `docs/07_paso_02_eda_tickets.md`

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
- [x] Profesor confirmo que se puede trabajar sobre el OLAP de Victor
- [x] Alcance ajustado a `3 modelos de machine learning`
- [x] Formato principal de salida definido en `Parquet`
- [x] Explorar el OLAP con consultas de negocio
- [x] Generar la base de tickets para modelado
- [x] Exportar la base inicial a `Parquet`
- [x] Preparar la base derivada para `EDA` en `Parquet`
- [ ] Entrenar el primer modelo
