# Modelo OLAP de Víctor

## Fuente oficial para esta fase

La capa de **Machine Learning** trabajar específicamente con el modelo `OLAP` construido por Víctor.

Conexión:

- `Host = localhost`
- `Port = 5432`
- `Database = restaurante`
- `Schema = olap`
- `Username = postgres`

## Tablas disponibles

- `olap.fact_ventas`
- `olap.dim_tiempo`
- `olap.dim_cliente`
- `olap.dim_platillo`
- `olap.dim_sucursal`
- `olap.dim_empleado`
- `olap.dim_mesa`
- `olap.dim_metodo_pago`

## Granularidad observada

La tabla `olap.fact_ventas` no representa un pedido completo en una sola fila.

Cada fila representa una **línea de venta** asociada a:

- tiempo
- cliente
- platillo
- sucursal
- empleado
- mesa
- metodo de pago

Medidas disponibles:

- `cantidad`
- `precio_unitario`
- `subtotal`
- `total_pedido`
- `monto_pago`

## Conteos validados

- `olap.fact_ventas = 4770`
- `olap.dim_tiempo = 365`
- `olap.dim_cliente = 800`
- `olap.dim_platillo = 60`
- `olap.dim_sucursal = 5`
- `olap.dim_empleado = 50`
- `olap.dim_mesa = 80`
- `olap.dim_metodo_pago = 4`

## Hallazgos útiles para modelado

- `olap.fact_ventas` contiene `4770` líneas de venta
- se pueden reconstruir aproximadamente `1167` tickets analíticos
- el percentil 75 de `total_pedido` es `525`
- alrededor del `23.48%` de los tickets reconstruidos quedan clasificados como `ticket_alto` usando ese corte

## Observacion técnica importante

La reconstrucción de tickets es **aproximada** porque el `OLAP` no incluye un identificador directo de pedido.

Eso significa que:

- el archivo `Parquet` de la etapa `01` ya se pudo generar correctamente
- pero antes de entrenar modelos se debe revisar la coherencia entre `subtotal_ticket` y `total_pedido`
- el notebook `01_Carga_y_Validacion_Parquet.ipynb` ser la primera validación formal de esa consistencia

## Implicacion para la capa de Machine Learning

El trabajo no se hará directo sobre la línea individual final.

Primero conviene construir una **base por ticket** usando agrupaciones sobre:

- `id_tiempo`
- `id_cliente`
- `id_sucursal`
- `id_empleado`
- `id_mesa`
- `id_metodo_pago`
- `total_pedido`
- `monto_pago`

Sobre esa base se podrían levantar:

1. clasificación de `ticket_alto`
2. regresión de `total_pedido`
3. segmentación de clientes
