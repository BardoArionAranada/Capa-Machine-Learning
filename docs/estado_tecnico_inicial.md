# Estado Tecnico Inicial

## Objetivo de este documento

Este documento concentra el estado tecnico de arranque de la capa de **Machine Learning**, tomando como base el proyecto restaurante y las capas previas ya desarrolladas.

## Bases disponibles localmente

Actualmente tengo disponibles dos bases de datos en PostgreSQL local:

- `restaurante`
- `restaurante_dw`

## Significado de cada base

- `restaurante`: corresponde a la capa `OLTP`
- `restaurante_dw`: corresponde a la capa analitica / `Data Warehouse`

## Validacion de tablas principales

### Base `restaurante`

- `pedido = 1200`
- `pago = 1204`
- `detallepedido = 5348`
- `cliente = 800`
- `platillo = 60`

### Base `restaurante_dw`

- `fact_ventas = 1131`
- `dim_tiempo = 365`
- `dim_cliente = 800`
- `dim_empleado = 50`
- `dim_platillo = 60`
- `dim_pago = 1149`
- `dim_sucursal = 5`

## Implicaciones para la capa de machine learning

- Ya existe una base analitica lista para exploracion y modelado.
- La tabla central para comenzar el trabajo es `fact_ventas`.
- El modelado se hara tomando como fuente principal `restaurante_dw`.
- Si se requiere enriquecer alguna variable, se puede consultar tambien la base `restaurante`.
- El alcance general del proyecto contempla utilizar `4 modelos de machine learning`, aunque todavia no se haya cerrado la seleccion final.

## Forma prevista de entrega para Qlik

La salida final para el equipo de Qlik se preparara principalmente en:

- `Parquet`

Adicionalmente, si es necesario, tambien se puede dejar una tabla final dentro de la base con predicciones, scores o segmentos ya calculados.

## Siguiente accion recomendada

Entrar al gestor de base de datos y validar:

1. `SELECT * FROM fact_ventas LIMIT 10;`
2. una consulta unida entre `fact_ventas` y dimensiones para entender el modelo como negocio
