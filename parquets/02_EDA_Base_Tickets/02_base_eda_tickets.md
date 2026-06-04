# 02 Base EDA Tickets

## Qué contiene este archivo

Este `Parquet` contiene la base preparada específicamente para el **análisis exploratorio de datos**.

Parte de la base por ticket del paso `01`, pero agrega columnas pensadas para revisar calidad, consistencia y comportamiento general del dataset.

La finalidad de esta etapa no es predecir todavía, sino entender mejor los tickets antes de pasar a los modelos.

## Nombre del archivo esperado

- `02_base_eda_tickets.parquet`

## Fuente

Se genera a partir de:

- `parquets/01_Carga_y_Validacion_Parquet/01_base_tickets_modelado.parquet`

## Variables nuevas para EDA

- `anio_mes`
- `dia_tipo`
- `residuo_subtotal_total`
- `residuo_abs_subtotal_total`
- `residuo_pago_total`
- `ticket_consistente_subtotal`
- `ticket_consistente_pago`
- `rango_total_pedido`

## Validación actual

La base fue generada y preparada para analizar:

- `1167` tickets
- consistencia entre `subtotal_ticket` y `total_pedido`
- consistencia entre `monto_pago` y `total_pedido`

Hallazgos iniciales:

- solo `9` tickets quedaron consistentes entre `subtotal_ticket` y `total_pedido`
- `930` tickets quedaron consistentes entre `monto_pago` y `total_pedido`

## Para qué sirve

Este archivo será la entrada del notebook:

- `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`

También sirve como base de entrada para que las etapas `03`, `04` y `05` tomen una versión más entendida del dataset.

## Por qué estos datos le sirven al restaurante

Esta base sirve porque ayuda a entender la calidad y el comportamiento de los datos antes de tomar decisiones con modelos predictivos. En una empresa de restaurante eso es importante para saber si los montos, pagos y subtotales son coherentes y si el patron de ventas es estable.

## Como se debería ver en Qlik

En Qlik esta base podría servir para visualizaciones como:

- distribución de `total_pedido`
- tickets altos vs normales
- residuo entre `subtotal_ticket` y `total_pedido`
- consistencia de pago por metodo de pago
- comparativos por turno, ciudad y dia de la semana

## Observación importante

Esta etapa no corrige todavía la base para modelado final; su función es **entender** y **evidenciar** el comportamiento real de los tickets antes de entrenar modelos.

En terminos simples:

- `01` construye la base
- `02` la explora y la valida
- `03`, `04` y `05` la usan para Machine Learning
