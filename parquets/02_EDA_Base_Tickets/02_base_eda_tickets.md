# 02 Base EDA Tickets

## Que contiene este archivo

Este `Parquet` contiene la base preparada especificamente para el **analisis exploratorio de datos**.

Parte de la base por ticket del paso `01`, pero agrega columnas pensadas para revisar calidad, consistencia y comportamiento general del dataset.

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

## Validacion actual

La base fue generada y preparada para analizar:

- `1167` tickets
- consistencia entre `subtotal_ticket` y `total_pedido`
- consistencia entre `monto_pago` y `total_pedido`

Hallazgos iniciales:

- solo `9` tickets quedaron consistentes entre `subtotal_ticket` y `total_pedido`
- `930` tickets quedaron consistentes entre `monto_pago` y `total_pedido`

## Para que sirve

Este archivo sera la entrada del notebook:

- `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`

## Por que estos datos le sirven al restaurante

Esta base sirve porque ayuda a entender la calidad y el comportamiento de los datos antes de tomar decisiones con modelos predictivos. En una empresa de restaurante eso es importante para saber si los montos, pagos y subtotales son coherentes y si el patron de ventas es estable.

## Como se deberia ver en Qlik

En Qlik esta base podria servir para visualizaciones como:

- distribucion de `total_pedido`
- tickets altos vs normales
- residuo entre `subtotal_ticket` y `total_pedido`
- consistencia de pago por metodo de pago
- comparativos por turno, ciudad y dia de la semana

## Observacion importante

Esta etapa no corrige todavia la base para modelado final; su funcion es **entender** y **evidenciar** el comportamiento real de los tickets antes de entrenar modelos.
