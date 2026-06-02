# 05 Clientes Segmentados

## Que contiene esta etapa

Esta carpeta concentra los resultados del modelo de **K-Means** para segmentacion de clientes.

## Archivos esperados

- `05_clientes_segmentados.parquet`
- `05_metricas_segmentacion.parquet`

## Fuente de datos

El modelo usa como entrada:

- `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`

## Variables usadas por el modelo

- `numero_tickets`
- `gasto_total`
- `ticket_promedio`
- `ticket_maximo`
- `cantidad_total_productos`
- `promedio_productos_ticket`
- `categorias_distintas_totales`
- `dias_activos`
- `dias_desde_ultimo_ticket`

## Resultado validado

Metricas obtenidas en la prueba:

- `n_clientes = 800`
- `n_clusters = 3`
- `inercia = 3206.5986`
- `silhouette = 0.3836`

## Interpretacion rapida

- el modelo ya separa a los clientes en tres grupos utiles
- la segmentacion puede apoyar a Qlik para comparar valor y frecuencia por cliente
- esta salida sirve bien para tableros de comportamiento historico

## Como se deberia ver en Qlik

En Qlik esta salida deberia servir para:

- ver segmentos de clientes
- comparar gasto por cluster
- analizar comportamiento por frecuencia y ticket promedio
- filtrar clientes por segmento, metodo de pago frecuente o ciudades visitadas
