# Conexion y Modelo de Trabajo

## Conexion actual

La conexion actual de trabajo para la capa de machine learning es:

- `Host`: `localhost`
- `Port`: `5432`
- `Database`: `restaurante_dw`
- `Username`: `postgres`

## Esta base es OLAP o es otra cosa

Para efectos del proyecto, esta base corresponde al modelo analitico que voy a consumir en la capa de machine learning.

Interpretacion por capas:

- `restaurante` = `OLTP`
- `ETL` = proceso de extraccion, transformacion y carga
- `restaurante_dw` = modelo analitico / `Data Warehouse`

Aunque tecnicamente tambien se puede hablar de `Data Warehouse`, en la practica esta es la base analitica sobre la que voy a trabajar y es la que funciona como punto de partida para la capa de machine learning.

## Por que se trabajara aqui

- Ya contiene una tabla de hechos: `fact_ventas`
- Ya contiene dimensiones: `dim_tiempo`, `dim_cliente`, `dim_empleado`, `dim_platillo`, `dim_pago`, `dim_sucursal`
- Ya esta modelada para analisis y no para transacciones operativas

## Primer archivo SQL del proyecto

La exploracion inicial se documenta en:

- `sql/01_exploracion_inicial_dw.sql`

## Siguiente paso

Ejecutar las consultas iniciales para:

1. ver registros reales de `fact_ventas`
2. entender el modelo desde negocio
3. confirmar que esta sera la base de partida para la tabla base de machine learning
