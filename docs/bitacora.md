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
