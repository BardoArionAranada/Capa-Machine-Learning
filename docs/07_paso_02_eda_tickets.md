# 07 Paso 02 - EDA de Tickets

## Objetivo

Preparar una base propia para el analisis exploratorio de tickets y revisar su comportamiento antes de comenzar el entrenamiento de modelos.

## Flujo de esta etapa

1. leer el `Parquet` base de la etapa `01`
2. generar una base derivada para EDA
3. agregar columnas de apoyo para exploracion
4. guardar el resultado en la carpeta de `parquets/02`
5. analizar esa base desde el notebook `02`

## Script de esta etapa

- `scripts/02_preparar_base_eda_tickets.py`

## Salida esperada

- `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`

## Variables agregadas para esta etapa

- `anio_mes`
- `dia_tipo`
- `residuo_subtotal_total`
- `residuo_abs_subtotal_total`
- `residuo_pago_total`
- `ticket_consistente_subtotal`
- `ticket_consistente_pago`
- `rango_total_pedido`

## Hallazgo principal que debe revisarse

La consistencia entre `subtotal_ticket` y `total_pedido` es baja, mientras que la consistencia entre `monto_pago` y `total_pedido` es mucho mejor.

Ese hallazgo es importante porque afecta la confianza en algunas variables derivadas para los modelos posteriores.
