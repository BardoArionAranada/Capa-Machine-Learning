# 01 Base Tickets Modelado

## Que contiene este archivo

Este `Parquet` contiene la base principal del proyecto para Machine Learning.

La informacion ya no esta en granularidad de linea individual de venta, sino en una **fila por ticket reconstruido** a partir del `OLAP` de Victor.

## Fuente

- base: `restaurante`
- esquema: `olap`
- tabla origen principal: `olap.fact_ventas`

## Nombre del archivo esperado

- `01_base_tickets_modelado.parquet`

## Validacion actual

El archivo ya fue generado y validado con:

- `1167` filas
- una fila por ticket reconstruido

## Variables principales

- `id_ticket_modelado`
- `fecha`
- `mes`
- `trimestre`
- `dia_semana`
- `fin_semana`
- `id_cliente`
- `id_sucursal`
- `ciudad`
- `id_empleado`
- `tipo_empleado`
- `turno`
- `id_mesa`
- `capacidad_mesa`
- `id_metodo_pago`
- `metodo_pago`
- `lineas_ticket`
- `cantidad_total`
- `platillos_distintos`
- `categorias_distintas`
- `subtotal_ticket`
- `total_pedido`
- `monto_pago`
- `diferencia_pago`
- `incluye_bebida`
- `incluye_postre`
- `incluye_entrada`
- `incluye_platillo_fuerte`
- `ticket_alto`

## Para que sirve

Este archivo sera la base de entrada para:

1. `Regresion Logistica`
2. `Regresion Lineal`
3. `K-Means`

## Como se deberia ver en Qlik

En Qlik este `Parquet` se deberia poder usar como una tabla analitica de tickets con visualizaciones como:

- distribucion de `total_pedido`
- tickets altos vs tickets normales
- ventas por ciudad
- ventas por turno
- ventas por metodo de pago
- comparativos entre tickets con bebida, postre o entrada

## Observacion

Este es el `Parquet` principal de trabajo del proyecto y debe ser la referencia base para los notebooks y los modelos.

La reconstruccion por ticket es funcional para arrancar el proyecto, pero debe validarse en el notebook `01` porque el `OLAP` no trae `id_pedido` y la agrupacion es una aproximacion analitica.
