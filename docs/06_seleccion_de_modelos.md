# 06 Seleccion de Modelos de Machine Learning

## Decision general

Para este proyecto se trabajar con **3 modelos de machine learning** ya definidos.

La seleccion se hizo considerando:

- la estructura real del `OLAP` de Víctor
- la granularidad de `olap.fact_ventas`
- la posibilidad de reconstruir tickets
- la tilidad posterior para el equipo de Qlik

## Modelo 1 - Clasificación de ticket alto

### Objetivo

Predecir si un ticket pertenece a la categoria de venta alta.

### Por qué conviene

- el `OLAP` permite reconstruir tickets
- `total_pedido` tiene una distribución clara
- el percentil 75 da un corte razonable en `525`
- la salida es muy fácil de consumir en Qlik con colores, probabilidades y filtros

### Base principal

- `base_tickets_modelado.parquet`

### Variable objetivo propuest

- `ticket_alto = 1` si `total_pedido >= 525`
- `ticket_alto = 0` en otro caso

### Modelo elegido

- **Regresión Logística**

### Motivo de eleccion

- se alínea con una forma de trabajo clara y explicable para el proyecto
- es interpretable
- funciona bien como primer modelo de clasificación tabular
- permite comparar probabilidades y clases en Qlik

### Prioridad

- **Alta**

## Modelo 2 - Regresión de total de pedido

### Objetivo

Estimar el valor de `total_pedido` a partir de las caracteristicas del ticket.

### Por qué conviene

- el cubo ya contiene `total_pedido`
- hay suficientes tickets reconstruidos
- es un problema natural de negocio para ventas
- el resultado sirve para comparativos y pronósticos de valor

### Base principal

- `base_tickets_modelado.parquet`

### Variable objetivo

- `total_pedido`

### Modelo elegido

- **Regresión Lineal**

### Motivo de eleccion

- se alínea con una metodología simple y entendible para el proyecto
- es fácil de explicar y documentar
- sirve como línea base clara para estimar `total_pedido`

### Prioridad

- **Alta**

## Modelo 3 - Segmentación de clientes

### Objetivo

Agrupar clientes por comportamiento histórico de compra.

### Por qué conviene

- el `OLAP` tiene `800` clientes distintos
- desde la base por ticket se pueden agregar métricas por cliente
- el resultado se puede visualizar muy bien en Qlik como perfiles o segmentos

### Base principal

- agregado por cliente construido desde `base_tickets_modelado.parquet`

### Variables sugeridas

- número de tickets
- gasto total
- ticket promedio
- cantidad total consumida
- variedad de categorias
- porcentaje de tickets en fin de semana

### Modelo elegido

- **K-Means**

### Motivo de eleccion

- es uno de los modelos más claros para segmentación
- se adapta bien a agregados por cliente
- el resultado es fácil de explicar en el reporte final y en Qlik

### Prioridad

- **Media**

## Modelos definitivos del proyecto

1. `Regresión Logística` para clasificación de `ticket_alto`
2. `Regresión Lineal` para estimacin de `total_pedido`
3. `K-Means` para segmentación de clientes

## Orden recomendado de ejecución

1. Regresión Logística
2. Regresión Lineal
3. K-Means

## Motivo del orden

- los dos primeros modelos usan directamente la base por ticket
- la segmentación requiere antes construir un agregado por cliente
- así el trabajo avanza de lo más directo a lo más derivado
