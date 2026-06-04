# 07 Paso 02 - EDA de Tickets

## Objetivo

Preparar una base propia para el análisis exploratorio de tickets y revisar su comportamiento antes de comenzar el entrenamiento de modelos.

En esta etapa todavía no se entrena ningún modelo. La idea del `EDA` es entender mejor la base, revisar su consistencia y detectar comportamientos importantes antes de pasar a las etapas `03`, `04` y `05`.

## Flujo de esta etapa

1. leer el `Parquet` base de la etapa `01`
2. generar una base derivada para EDA
3. agregar columnas de apoyo para exploración
4. guardar el resultado en la carpeta de `parquets/02`
5. analizar esa base desde el notebook `02`

## Notebook de esta etapa

- `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`

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

## Qué hace realmente esta etapa

La etapa `02` toma la base por ticket generada en el paso `01` y la enriquece con columnas pensadas para exploración.

Su función principal es:

- revisar la distribución de los tickets
- comparar comportamiento entre semana y fin de semana
- revisar si `subtotal_ticket` y `total_pedido` son coherentes
- revisar si `monto_pago` y `total_pedido` son coherentes
- dejar una base más clara para que los modelos posteriores trabajen sobre variables ya entendidas

En resumen:

- `01` = construir la base por ticket
- `02` = entender la base por ticket
- `03`, `04` y `05` = modelar sobre esa base

## Hallazgo principal que debe revisarse

La consistencia entre `subtotal_ticket` y `total_pedido` es baja, mientras que la consistencia entre `monto_pago` y `total_pedido` es mucho mejor.

Ese hallazgo es importante porque afecta la confianza en algunas variables derivadas para los modelos posteriores.

## Qué se debe ver al ejecutar el notebook 02

Al correr `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb` se deben ver:

- tablas de validación
- conteos de consistencia
- un histograma de `total_pedido`
- un boxplot de `total_pedido` por `dia_tipo`

Esas salidas ayudan a revisar si la base tiene sentido antes de entrenar modelos.

## Flujo que sigue

Una vez generado `02_base_eda_tickets.parquet`, las etapas `03`, `04` y `05` ya toman ese mismo archivo como entrada principal.
