# 08 Paso 03 - Clasificación de Ticket Alto

## Objetivo

Entrenar el primer modelo formal del proyecto usando **Regresión Logística** para clasificar si un ticket es alto o no.

## Entrada

- `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`

## Notebook principal

- `notebooks/03_Modelo_Clasificacion_Ticket_Alto/03_Modelo_Clasificacion_Ticket_Alto.ipynb`

## Salidas esperadas

- `parquets/03_Modelo_Clasificacion_Ticket_Alto/03_tickets_clasificados.parquet`

## Variables utilizadas

Se usaron variables de contexto y comportamiento del ticket, evitando columnas que dieran fuga directa del target.

## Métricas validadas

- `accuracy = 0.6282`
- `precision = 0.3710`
- `recall = 0.8364`
- `f1 = 0.5140`
- `roc_auc = 0.7311`

## Conclusiones iniciales

- el modelo s logra identificar buena parte de los tickets altos
- la capacidad de recuperacion de la clase positiva es mejor que la precision
- como primera capa predictiva del proyecto, el resultado ya es útil para continuar
