# Bitácora del Proyecto

## 2026-06-01

### Entrada 001 - Creación del repositorio de trabajo

Creé la carpeta de trabajo para la fase de **Machine Learning** y la prepare como repositorio independiente para subirla a GitHub.

Acciones realizadas:

- Definí la estructura base del proyecto.
- Agregue un `README.md` con el contexto de la capa.
- Agregue un `.gitignore` inicial.
- Creé esta bitácora para documentar el proceso paso a paso.

### Entrada 002 - Preparación del entorno local y carga de bases

Preparé el entorno local de PostgreSQL para revisar las capas previas del proyecto y poder trabajar sin depender de resultados parciales.

Bases cargadas localmente:

- `restaurante` como base `OLTP`
- `restaurante_dw` como referencia del `ETL`

Validaciones principales:

- `restaurante.detallepedido = 5348`
- `restaurante.pedido = 1200`
- `restaurante.pago = 1204`
- `restaurante_dw.fact_ventas = 1131`

### Entrada 003 - Montaje local del modelo OLAP de Víctor

Monté localmente el modelo `OLAP` de Víctor dentro de:

- base `restaurante`
- esquema `olap`

Conteos validados:

- `olap.fact_ventas = 4770`
- `olap.dim_tiempo = 365`
- `olap.dim_cliente = 800`
- `olap.dim_platillo = 60`
- `olap.dim_sucursal = 5`
- `olap.dim_empleado = 50`
- `olap.dim_mesa = 80`
- `olap.dim_metodo_pago = 4`

Conclusión:

- La fuente principal de trabajo para Machine Learning pasa a ser `olap.fact_ventas`.

### Entrada 004 - Confirmación del alcance del proyecto

Después de revisar las capas del proyecto, quedaron definidos estos puntos:

- el requisito de `10000` datos aplica al `OLTP`
- el `OLAP` puede tener menos registros porque quedó enfocado a ventas
- si se puede avanzar formalmente con Machine Learning usando el `OLAP` de Víctor
- el alcance final de esta capa será de **3 modelos de machine learning**
- la salida principal para Qlik será en formato `Parquet`

### Entrada 005 - Limpieza del repositorio y definicion del primer paso real

La documentación del repositorio quedó alineada con la situación final del proyecto.

Hallazgos técnicos importantes:

- `olap.fact_ventas` tiene `4770` líneas de venta
- el cubo permite reconstruir aproximadamente `1167` tickets
- el percentil 75 de `total_pedido` es `525`
- eso permite proponer una variable objetivo inicial para clasificación de `ticket_alto`

Siguiente paso:

- ejecutar la exploración inicial del `OLAP`
- generar la base de tickets para modelado
- exportar la base a `Parquet`
