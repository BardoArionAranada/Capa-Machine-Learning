# 05 Clientes Segmentados

## Que contiene esta etapa

Esta carpeta concentra los resultados del modelo de **K-Means** para segmentacion de clientes.

## Archivos esperados

- `05_clientes_segmentados.parquet`

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

## Por que se eligio este modelo

Se eligio **K-Means** porque en esta etapa no existe una etiqueta previa de cliente y lo que se busca es descubrir grupos de comportamiento.

Este modelo conviene porque:

- permite segmentar clientes sin necesidad de una clase ya definida
- resume patrones de compra en grupos faciles de interpretar
- ayuda a encontrar clientes de bajo, medio y alto valor
- sirve bien como primera aproximacion para analisis comercial

## Resultado validado

Metricas obtenidas en la prueba:

- `n_clientes = 800`
- `n_clusters = 3`
- `inercia = 3206.5986`
- `silhouette = 0.3836`

## Archivo que interesa a Qlik

El archivo principal para Qlik en esta etapa es:

- `05_clientes_segmentados.parquet`

## Por que le sirve al restaurante

Este modelo le sirve al restaurante porque permite separar a los clientes segun su comportamiento historico. Eso ayuda a:

- detectar clientes de mayor valor
- revisar frecuencia de compra y recencia
- pensar en promociones o estrategias por segmento
- distinguir clientes que conviene retener, activar o fidelizar

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
