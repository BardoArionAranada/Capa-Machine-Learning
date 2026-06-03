# Estado Tecnico Inicial

## Objetivo de este documento

Concentrar el estado tecnico de arranque de la capa de **Machine Learning** usando como fuente principal el **OLAP de VÃ­ctor**.

## Bases revisadas localmente

Se revisaron estas bases para entender las capas previas del proyecto:

- `restaurante` -> `OLTP`
- `restaurante_dw` -> referencia del `ETL`

Sin embargo, la base principal para esta fase queda definida como:

- `restaurante`
- esquema `olap`

## Validación resumida por capa

### OLTP

- `detallepedido = 5348`
- `pedido = 1200`
- `pago = 1204`
- total general del `OLTP = 10010`

### ETL / DW

- `fact_ventas = 1131`
- total general del `DW = 3560`

### OLAP de VÃ­ctor

- `olap.fact_ventas = 5380`
- `olap.dim_tiempo = 365`
- `olap.dim_cliente = 800`
- `olap.dim_platillo = 60`
- `olap.dim_sucursal = 5`
- `olap.dim_empleado = 50`
- `olap.dim_mesa = 80`
- `olap.dim_metodo_pago = 4`
- total del esquema `olap = 6744`

## Interpretacion

- El requisito de `10000` datos aplica al `OLTP`.
- El `OLAP` de VÃ­ctor se enfoco en ventas, por eso su volumen es menor.
- Esta capa puede avanzar con los `5380` registros de `olap.fact_ventas`.

## Decision de trabajo

La capa de Machine Learning se desarrollara con este flujo:

1. leer el `OLAP` de VÃ­ctor
2. reconstruir tickets analÃ­ticos
3. exportar la base a `Parquet`
4. trabajar los modelos en Python a partir del `Parquet`
5. generar nuevos `Parquet` con resultados para Qlik

## Alcance actual

- `3 modelos de machine learning`
- salida principal en `Parquet`
- foco analÃ­tico en ventas del restaurante

## Siguiente accion recomendada

Ejecutar la exploraciÃ³n inicial del `OLAP` y construir la primera base de tickets para modelado.
