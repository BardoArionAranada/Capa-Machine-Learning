# 06 Seleccion de Modelos de Machine Learning

## Decision general

Para este proyecto se trabajarÃ¡ con **3 modelos de machine learning** ya definidos.

La seleccion se hizo considerando:

- la estructura real del `OLAP` de VÃ­ctor
- la granularidad de `olap.fact_ventas`
- la posibilidad de reconstruir tickets
- la utilidad posterior para el equipo de Qlik

## Modelo 1 - ClasificaciÃ³n de ticket alto

### Objetivo

Predecir si un ticket pertenece a la categoria de venta alta.

### Por que conviene

- el `OLAP` permite reconstruir tickets
- `total_pedido` tiene una distribuciÃ³n clara
- el percentil 75 da un corte razonable en `525`
- la salida es muy facil de consumir en Qlik con colores, probabilidades y filtros

### Base principal

- `base_tickets_modelado.parquet`

### Variable objetivo propuesta

- `ticket_alto = 1` si `total_pedido >= 525`
- `ticket_alto = 0` en otro caso

### Modelo elegido

- **RegresiÃ³n LogÃ­stica**

### Motivo de eleccion

- se alinea con una forma de trabajo clara y explicable para el proyecto
- es interpretable
- funciona bien como primer modelo de clasificaciÃ³n tabular
- permite comparar probabilidades y clases en Qlik

### Prioridad

- **Alta**

## Modelo 2 - RegresiÃ³n de total de pedido

### Objetivo

Estimar el valor de `total_pedido` a partir de las caracteristicas del ticket.

### Por que conviene

- el cubo ya contiene `total_pedido`
- hay suficientes tickets reconstruidos
- es un problema natural de negocio para ventas
- el resultado sirve para comparativos y pronosticos de valor

### Base principal

- `base_tickets_modelado.parquet`

### Variable objetivo

- `total_pedido`

### Modelo elegido

- **RegresiÃ³n Lineal**

### Motivo de eleccion

- se alinea con una metodologia simple y entendible para el proyecto
- es facil de explicar y documentar
- sirve como lÃ­nea base clara para estimar `total_pedido`

### Prioridad

- **Alta**

## Modelo 3 - SegmentaciÃ³n de clientes

### Objetivo

Agrupar clientes por comportamiento histÃ³rico de compra.

### Por que conviene

- el `OLAP` tiene `800` clientes distintos
- desde la base por ticket se pueden agregar mÃ©tricas por cliente
- el resultado se puede visualizar muy bien en Qlik como perfiles o segmentos

### Base principal

- agregado por cliente construido desde `base_tickets_modelado.parquet`

### Variables sugeridas

- numero de tickets
- gasto total
- ticket promedio
- cantidad total consumida
- variedad de categorias
- porcentaje de tickets en fin de semana

### Modelo elegido

- **K-Means**

### Motivo de eleccion

- es uno de los modelos mÃ¡s claros para segmentaciÃ³n
- se adapta bien a agregados por cliente
- el resultado es facil de explicar en el reporte final y en Qlik

### Prioridad

- **Media**

## Modelos definitivos del proyecto

1. `Regresión LogÃ­stica` para clasificaciÃ³n de `ticket_alto`
2. `Regresión Lineal` para estimaciÃ³n de `total_pedido`
3. `K-Means` para segmentaciÃ³n de clientes

## Orden recomendado de ejecucion

1. RegresiÃ³n LogÃ­stica
2. RegresiÃ³n Lineal
3. K-Means

## Motivo del orden

- los dos primeros modelos usan directamente la base por ticket
- la segmentaciÃ³n requiere antes construir un agregado por cliente
- asi el trabajo avanza de lo mÃ¡s directo a lo mÃ¡s derivado
