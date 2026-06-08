# 09 Paso 04 - Regresión Total Pedido

## Objetivo

Entrenar el segundo modelo formal del proyecto usando **Regresión Lineal** para estimar el `total_pedido`.

## Entrada

- `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`

## Notebook principal

- `notebooks/04_Modelo_Regresion_Total_Pedido/04_Modelo_Regresion_Total_Pedido.ipynb`

## Salidas esperadas

- `parquets/04_Modelo_Regresion_Total_Pedido/04_tickets_regresion.parquet`

## Variables utilizadas

Se usaron variables operativas y de contexto del ticket, evitando columnas que dieran fuga directa del valor real del pedido.

## Métricas validadas

- `mae = 92.3808`
- `rmse = 111.6614`
- `r2 = 0.2360`

## Conclusiones iniciales

- el modelo ya produce una estimacin útil del total del pedido
- el error todavía deja espacio de mejora en futuras versiones
- como segunda capa de resultados, esta salida ya puede alimentar visualizaciones en Qlik
