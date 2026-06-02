# 03 Metricas de Clasificacion

## Que contiene este archivo

Este parquet guarda las metricas principales del modelo de **Regresion Logistica** entrenado para clasificar si un ticket es alto o no.

## Archivo asociado

- `03_metricas_clasificacion.parquet`

## Metricas incluidas

- `accuracy`
- `precision`
- `recall`
- `f1`
- `roc_auc`
- `train_rows`
- `test_rows`

## Resultado validado

- `accuracy = 0.6282`
- `precision = 0.3710`
- `recall = 0.8364`
- `f1 = 0.5140`
- `roc_auc = 0.7278`
- `train_rows = 933`
- `test_rows = 234`

## Como interpretar este parquet

- sirve para documentar el rendimiento del modelo
- permite comparar esta version con modelos posteriores
- deja trazabilidad para el reporte final del proyecto

## Como se deberia ver en Qlik

En Qlik este parquet se puede usar para:

- mostrar tarjetas KPI con las metricas del modelo
- comparar el rendimiento entre distintos modelos
- construir una hoja de seguimiento del proceso de Machine Learning
