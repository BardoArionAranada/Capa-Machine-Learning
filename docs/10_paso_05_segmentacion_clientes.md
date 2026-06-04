# 10 Paso 05 - Segmentación de Clientes

## Objetivo

Entrenar el tercer modelo formal del proyecto usando **K-Means** para segmentar clientes según su comportamiento histórico de compra.

## Entrada

- `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`

## Notebook principal

- `notebooks/05_Modelo_Segmentacion_Clientes/05_Modelo_Segmentacion_Clientes.ipynb`

## Salidas esperadas

- `parquets/05_Modelo_Segmentacion_Clientes/05_clientes_segmentados.parquet`

## Variables utilizadas

Se usaron agregados por cliente relaciónados con frecuencia, gasto, variedad de consumo y recencia.

## Métricas validadas

- `n_clientes = 800`
- `n_clusters = 3`
- `inercia = 3206.5986`
- `silhouette = 0.3836`

## Conclusiones iniciales

- la segmentación ya separa clientes en tres grupos interpretables
- el resultado es útil para construir tableros de valor y comportamiento
- esta salida complementa bien las predicciones por ticket de las etapas anteriores
