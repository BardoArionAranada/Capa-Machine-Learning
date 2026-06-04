# 01 Base Tickets Modelado

## Qué contiene este archivo

Este `Parquet` contiene la base principal del proyecto para Machine Learning.

La información ya no está en granularidad de línea individual de venta, sino en una **fila por ticket reconstruido** a partir del `OLAP` de Víctor.

En este proyecto, un ticket representa una compra resumida del restaurante.

## Fuente

- base: `restaurante`
- esquema: `olap`
- tabla origen principal: `olap.fact_ventas`

## Nombre del archivo esperado

- `01_base_tickets_modelado.parquet`

## Validación actual

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
- `líneas_ticket`
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

## Para qué sirve

Este archivo será la base de entrada para:

1. `Regresión Logística`
2. `Regresión Lineal`
3. `K-Means`

## Por qué estos datos le sirven al restaurante

Esta base le sirve al restaurante porque resume el comportamiento de venta a nivel ticket. Eso permite revisar cuánto gasta cada cliente, en qué ciudad se vende más, qué turnos generan tickets más altos y qué combinaciones de productos aparecen con más frecuencia.

## Como se debería ver en Qlik

En Qlik este `Parquet` se debería poder usar como una tabla analítica de tickets con visualizaciones como:

- distribución de `total_pedido`
- tickets altos vs tickets normales
- ventas por ciudad
- ventas por turno
- ventas por metodo de pago
- comparativos entre tickets con bebida, postre o entrada

## Observacion

Este es el `Parquet` principal de trabajo del proyecto y debe ser la referencia base para los notebooks y los modelos.

La reconstrucción por ticket es funcional para arrancar el proyecto, pero debe validarse en el notebook `01` porque el `OLAP` no trae `id_pedido` y la agrupación es una aproximación analítica.

Guía relaciónada:

- `docs/12_entender_base_tickets.md`
