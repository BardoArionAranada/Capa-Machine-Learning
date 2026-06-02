# Plan de Trabajo de Machine Learning

## Objetivo general

Construir la capa de **Machine Learning** del proyecto restaurante a partir del `OLAP` de Victor y entregar resultados en `Parquet` para el equipo de Qlik.

## Flujo aprobado

1. leer datos desde `restaurante.olap`
2. construir la base analitica
3. exportar la base a `Parquet`
4. trabajar en Python sobre el `Parquet`
5. entrenar y evaluar `3 modelos`
6. exportar resultados finales en `Parquet`

## Primer entregable tecnico

El primer entregable de esta carpeta sera una base por ticket lista para modelado.

Archivos asociados:

- `sql/01_exploracion_inicial_olap_victor.sql`
- `sql/04_base_tickets_modelado.sql`
- `scripts/01_exportar_base_tickets_olap.py`

Salida esperada:

- `parquets/01_Carga_y_Validacion_Parquet/01_base_tickets_modelado.parquet`

## Tres modelos definidos

### Modelo 1 - Clasificacion

Objetivo:

- predecir si un ticket sera `ticket_alto`

Target propuesto:

- `ticket_alto = 1` si `total_pedido >= 525`
- `ticket_alto = 0` en otro caso

Modelo definido:

- `Regresion Logistica`

### Modelo 2 - Regresion

Objetivo:

- predecir el `total_pedido`

Modelo definido:

- `Regresion Lineal`

### Modelo 3 - Segmentacion

Objetivo:

- agrupar clientes por comportamiento historico de compra

Base requerida:

- agregados por cliente construidos desde la base por ticket

Modelo definido:

- `K-Means`

## Variables utiles para la base por ticket

- fecha
- mes
- trimestre
- dia_semana
- fin_semana
- id_cliente
- id_sucursal
- ciudad
- id_empleado
- tipo_empleado
- turno
- id_mesa
- capacidad_mesa
- id_metodo_pago
- metodo_pago
- lineas_ticket
- cantidad_total
- platillos_distintos
- categorias_distintas
- subtotal_ticket
- total_pedido
- monto_pago
- diferencia_pago
- incluye_bebida
- incluye_postre
- incluye_entrada
- incluye_platillo_fuerte

## Entregables para Qlik

Se planea entregar por lo menos estos archivos:

1. `tickets_predichos.parquet`
2. `clientes_segmentados.parquet`
3. `metricas_modelos.parquet` o una tabla equivalente

## Orden de trabajo en notebooks

Siguiendo el estilo de Mineria de Datos, el flujo de notebooks sera:

1. `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb`
2. `notebooks/02_EDA_Base_Tickets/02_EDA_Base_Tickets.ipynb`
3. `notebooks/03_Modelo_Clasificacion_Ticket_Alto/03_Modelo_Clasificacion_Ticket_Alto.ipynb`
4. `notebooks/04_Modelo_Regresion_Total_Pedido/04_Modelo_Regresion_Total_Pedido.ipynb`
5. `notebooks/05_Modelo_Segmentacion_Clientes/05_Modelo_Segmentacion_Clientes.ipynb`

## Base de datos por etapa

### Etapa 01

- `parquets/01_Carga_y_Validacion_Parquet/01_base_tickets_modelado.parquet`

### Etapa 02

- `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`

### Etapa 03

- `parquets/03_Modelo_Clasificacion_Ticket_Alto/03_tickets_clasificados.parquet`
- `parquets/03_Modelo_Clasificacion_Ticket_Alto/03_metricas_clasificacion.parquet`

### Etapa 04

- `parquets/04_Modelo_Regresion_Total_Pedido/04_tickets_regresion.parquet`
- `parquets/04_Modelo_Regresion_Total_Pedido/04_metricas_regresion.parquet`

### Etapa 05

- `parquets/05_Modelo_Segmentacion_Clientes/05_clientes_segmentados.parquet`
- `parquets/05_Modelo_Segmentacion_Clientes/05_metricas_segmentacion.parquet`
