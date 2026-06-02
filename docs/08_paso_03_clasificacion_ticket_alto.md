# 08 Paso 03 - Clasificacion de Ticket Alto

## Objetivo

Entrenar el primer modelo formal del proyecto usando **Regresion Logistica** para clasificar si un ticket es alto o no.

## Entrada

- `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`

## Script principal

- `scripts/03_entrenar_regresion_logistica.py`

## Salidas esperadas

- `parquets/03_Modelo_Clasificacion_Ticket_Alto/03_tickets_clasificados.parquet`
- `parquets/03_Modelo_Clasificacion_Ticket_Alto/03_metricas_clasificacion.parquet`

## Variables utilizadas

Se usaron variables de contexto y comportamiento del ticket, evitando columnas que dieran fuga directa del target.

## Metricas validadas

- `accuracy = 0.6282`
- `precision = 0.3710`
- `recall = 0.8364`
- `f1 = 0.5140`
- `roc_auc = 0.7278`

## Conclusiones iniciales

- el modelo si logra identificar buena parte de los tickets altos
- la capacidad de recuperacion de la clase positiva es mejor que la precision
- como primera capa predictiva del proyecto, el resultado ya es util para continuar
