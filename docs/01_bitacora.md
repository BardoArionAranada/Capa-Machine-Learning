# Bitacora del Proyecto

## 2026-06-01

### Entrada 001 - Creacion del repositorio de trabajo

Cree la carpeta de trabajo para la fase de **Machine Learning** y la prepare como repositorio independiente para subirla a GitHub.

Acciones realizadas:

- Defini la estructura base del proyecto.
- Agregue un `README.md` con el contexto de la capa.
- Agregue un `.gitignore` inicial.
- Cree esta bitacora para documentar el proceso paso a paso.

### Entrada 002 - Preparacion del entorno local y carga de bases

Prepare el entorno local de PostgreSQL para revisar las capas previas del proyecto y poder trabajar sin depender de resultados parciales.

Bases cargadas localmente:

- `restaurante` como base `OLTP`
- `restaurante_dw` como referencia del `ETL`

Validaciones principales:

- `restaurante.detallepedido = 5348`
- `restaurante.pedido = 1200`
- `restaurante.pago = 1204`
- `restaurante_dw.fact_ventas = 1131`

### Entrada 003 - Montaje local del modelo OLAP de Victor

Monte localmente el modelo `OLAP` de Victor dentro de:

- base `restaurante`
- esquema `olap`

Conteos validados:

- `olap.fact_ventas = 5380`
- `olap.dim_tiempo = 365`
- `olap.dim_cliente = 800`
- `olap.dim_platillo = 60`
- `olap.dim_sucursal = 5`
- `olap.dim_empleado = 50`
- `olap.dim_mesa = 80`
- `olap.dim_metodo_pago = 4`

Conclusion:

- La fuente principal de trabajo para Machine Learning pasa a ser `olap.fact_ventas`.

### Entrada 004 - Confirmacion del alcance con el profesor

Despues de revisar las capas y hablar con el profesor, quedaron confirmados estos puntos:

- el requisito de `10000` datos aplica al `OLTP`
- el `OLAP` puede tener menos registros porque quedo enfocado a ventas
- si se puede avanzar formalmente con Machine Learning usando el `OLAP` de Victor
- el alcance final de esta capa sera de **3 modelos de machine learning**
- la salida principal para Qlik sera en formato `Parquet`

### Entrada 005 - Limpieza del repositorio y definicion del primer paso real

Actualice la documentacion del repositorio para dejarla alineada con la situacion final del proyecto.

Ajustes realizados:

- quite la documentacion que dejaba a `restaurante_dw` como fuente principal
- deje el proyecto enfocado solo en el `OLAP` de Victor
- cambie el alcance de `4 modelos` a `3 modelos`
- documente que el primer paso real sera reconstruir una base por ticket

Hallazgos tecnicos importantes:

- `olap.fact_ventas` tiene `5380` lineas de venta
- el cubo permite reconstruir aproximadamente `1167` tickets
- el percentil 75 de `total_pedido` es `525`
- eso permite proponer una variable objetivo inicial para clasificacion de `ticket_alto`

Siguiente paso:

- ejecutar la exploracion inicial del `OLAP`
- generar la base de tickets para modelado
- exportar la base a `Parquet`
