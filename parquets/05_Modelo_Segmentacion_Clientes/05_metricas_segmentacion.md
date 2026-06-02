# 05 Metricas de Segmentacion

## Que contiene este archivo

Este parquet guarda las metricas principales del modelo de **K-Means** para segmentacion de clientes.

## Archivo asociado

- `05_metricas_segmentacion.parquet`

## Metricas incluidas

- `n_clientes`
- `n_clusters`
- `inercia`
- `silhouette`

## Resultado validado

- `n_clientes = 800`
- `n_clusters = 3`
- `inercia = 3206.5986`
- `silhouette = 0.3836`

## Como interpretar este parquet

- permite validar el volumen real de clientes segmentados
- ayuda a justificar el numero de clusters elegidos
- deja evidencia del rendimiento general del modelo de segmentacion

## Como se deberia ver en Qlik

En Qlik este parquet se puede usar para:

- mostrar indicadores de la segmentacion
- apoyar una hoja de resumen del proceso de Machine Learning
- comparar resultados si despues se prueba otro valor de `k`
