# 04 Metricas de Regresion

## Que contiene este archivo

Este parquet guarda las metricas principales del modelo de **Regresion Lineal** para estimar el `total_pedido`.

## Archivo asociado

- `04_metricas_regresion.parquet`

## Metricas incluidas

- `mae`
- `rmse`
- `r2`
- `train_rows`
- `test_rows`

## Resultado validado

- `mae = 92.3532`
- `rmse = 111.6319`
- `r2 = 0.2364`
- `train_rows = 933`
- `test_rows = 234`

## Como interpretar este parquet

- sirve para medir el error del modelo de regresion
- permite comparar esta version con mejoras futuras
- deja trazabilidad para el reporte final del proyecto

## Como se deberia ver en Qlik

En Qlik este parquet se puede usar para:

- mostrar tarjetas KPI con las metricas del modelo
- comparar el desempeno entre distintas versiones de regresion
- documentar la evolucion del proyecto de Machine Learning
