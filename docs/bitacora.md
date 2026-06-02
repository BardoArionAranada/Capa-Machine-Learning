# Bitacora del Proyecto

## 2026-06-01

### Entrada 001 - Creacion del repositorio de trabajo

Cree la carpeta de trabajo para la fase de **Machine Learning** y la prepare como repositorio independiente para subirla a GitHub.

Acciones realizadas:

- Defini la estructura base del proyecto.
- Agregue un `README.md` con el contexto de la capa.
- Agregue un `.gitignore` inicial.
- Cree esta bitacora para documentar todo el proceso paso a paso.

Observaciones:

- La fase de machine learning depende de las capas previas `OLTP`, `ETL` y `OLAP`.
- La fuente principal de datos identificada hasta este momento es `restaurante_dw`.
- El objetivo sera entrenar modelos sobre el esquema analitico y generar salidas consumibles para Qlik.
- El alcance general de esta capa contempla trabajar con `4 modelos de machine learning`, aunque todavia no se definan sus nombres concretos.

Siguiente paso:

- Validar el contenido real de `restaurante_dw` y comenzar la definicion del primer caso de uso de machine learning.

### Entrada 002 - Preparacion del entorno local y carga de bases

Deje listo el entorno local en PostgreSQL para poder comenzar a trabajar la capa de machine learning sin depender de que otra persona me comparta capturas o resultados parciales.

Bases cargadas localmente:

- `restaurante` como base `OLTP`
- `restaurante_dw` como base analitica / `Data Warehouse`

Validaciones realizadas en `restaurante`:

- `pedido = 1200`
- `pago = 1204`
- `detallepedido = 5348`
- `cliente = 800`
- `platillo = 60`

Validaciones realizadas en `restaurante_dw`:

- `fact_ventas = 1131`
- `dim_tiempo = 365`
- `dim_cliente = 800`
- `dim_empleado = 50`
- `dim_platillo = 60`
- `dim_pago = 1149`
- `dim_sucursal = 5`

Conclusion de esta etapa:

- Ya tengo cargadas las dos bases mas importantes para la fase de machine learning.
- Ya existe una fuente analitica real sobre la cual se puede comenzar a trabajar.
- La base principal para modelado sera `restaurante_dw`.

Decision para la salida del proyecto:

- El formato principal que voy a preparar para el equipo de Qlik sera `Parquet`.
- Ademas de eso, el resultado final tambien puede quedar persistido dentro de la base para dejar evidencia tecnica del proceso.

Alcance adicional definido:

- La capa de machine learning se desarrollara considerando `4 modelos`.
- La seleccion exacta de esos modelos se hara despues de revisar mejor la estructura y el comportamiento de los datos del `Data Warehouse`.

Siguiente paso:

- Conectarme desde el gestor de base de datos y revisar `fact_ventas` y las dimensiones del `Data Warehouse`.

### Entrada 003 - Definicion de la conexion de trabajo sobre el modelo analitico

Defini la conexion principal de trabajo para esta fase directamente sobre la base `restaurante_dw` en PostgreSQL local.

Datos de la conexion:

- `Host = localhost`
- `Port = 5432`
- `Database = restaurante_dw`
- `Username = postgres`

Interpretacion de esta conexion dentro del proyecto:

- `restaurante` se conserva como capa `OLTP`
- `restaurante_dw` se toma como modelo analitico / `Data Warehouse`
- esta es la base desde la cual comenzare la exploracion y preparacion de datos para machine learning

Acciones realizadas:

- Deje documentada la conexion de trabajo.
- Cree el primer archivo SQL del proyecto para exploracion inicial del modelo.
- Organice las primeras consultas para revisar la tabla de hechos y su union con dimensiones.

Archivos relacionados:

- `docs/conexion_y_modelo_dw.md`
- `sql/01_exploracion_inicial_dw.sql`

Siguiente paso:

- Ejecutar la exploracion inicial desde DBeaver y revisar el comportamiento de `fact_ventas`.

### Entrada 004 - Cambio de enfoque para trabajar especificamente con el modelo OLAP de Victor

Despues de revisar mejor la situacion del proyecto, confirme que para esta fase debo trabajar especificamente con el modelo `OLAP` del equipo de Victor y no solo con el `Data Warehouse` generado por `ETL`.

Ajuste realizado:

- Mantengo `restaurante_dw` como referencia tecnica util.
- Pero la fuente principal de trabajo para esta fase pasa a ser el esquema `olap` montado dentro de la base `restaurante`.

Acciones realizadas:

- Prepare un script para montar localmente el modelo OLAP de Victor.
- Deje un script de validacion para confirmar que se cree `olap.fact_ventas`.
- Documente la conexion correcta para revisarlo desde DBeaver.

Archivos relacionados:

- `sql/02_montaje_olap_victor.sql`
- `sql/03_validacion_olap_victor.sql`
- `docs/modelo_olap_victor.md`

Siguiente paso:

- Ejecutar el montaje del esquema `olap` y validar cuantos registros reales genera su tabla de hechos.

### Entrada 005 - Montaje y validacion local del modelo OLAP de Victor

Ejecute localmente el modelo `OLAP` de Victor sobre la base `restaurante`, usando un esquema separado llamado `olap`.

Resultado del montaje:

- El esquema `olap` se creo correctamente.
- Las dimensiones se cargaron correctamente.
- La tabla `olap.fact_ventas` tambien se genero correctamente.

Conteos validados:

- `olap.dim_tiempo = 365`
- `olap.dim_cliente = 800`
- `olap.dim_platillo = 60`
- `olap.dim_sucursal = 5`
- `olap.dim_empleado = 50`
- `olap.dim_mesa = 80`
- `olap.dim_metodo_pago = 4`
- `olap.fact_ventas = 5380`

Total de registros del esquema `olap`:

- `6744`

Conclusion de esta etapa:

- Ya quedo validado que el modelo de Victor si puede montarse localmente.
- La fuente principal de trabajo para machine learning pasa a ser `olap.fact_ventas`.
- El modelo `OLAP` actual no llega por si solo a `10000` filas en la tabla de hechos.

Siguiente paso:

- Entrar desde DBeaver a la base `restaurante`, revisar el esquema `olap` y comenzar la exploracion del cubo desde esa estructura.
