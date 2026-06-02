# Modelo OLAP de Victor

## Aclaracion importante

La base `restaurante_dw` que se habia validado primero corresponde al `Data Warehouse` generado por la capa `ETL`.

Sin embargo, para esta fase de **Machine Learning**, si el profesor pide trabajar especificamente con el modelo del equipo `OLAP`, entonces la referencia correcta pasa a ser el modelo de Victor.

## Como esta planteado el modelo de Victor

El modelo compartido por Victor fue diseñado para ejecutarse:

- dentro de la base `restaurante`
- usando el esquema separado `olap`

Eso significa que:

- `public` conserva el `OLTP`
- `olap` contiene el modelo analitico

## Conexion correcta para revisar este modelo en DBeaver

La conexion se hace sobre:

- `Host`: `localhost`
- `Port`: `5432`
- `Database`: `restaurante`
- `Username`: `postgres`

Despues, dentro de la base, se debe revisar especificamente:

- `Schemas`
- `olap`

## Archivos del repositorio relacionados

- `sql/02_montaje_olap_victor.sql`
- `sql/03_validacion_olap_victor.sql`

## Proposito

Montar localmente el modelo de Victor, validar si realmente genera `olap.fact_ventas` y revisar si cumple con la granularidad esperada para la capa de machine learning.

## Estado validado

El esquema `olap` ya se monto localmente y produjo estos conteos:

- `olap.dim_tiempo = 365`
- `olap.dim_cliente = 800`
- `olap.dim_platillo = 60`
- `olap.dim_sucursal = 5`
- `olap.dim_empleado = 50`
- `olap.dim_mesa = 80`
- `olap.dim_metodo_pago = 4`
- `olap.fact_ventas = 5380`

Total del esquema `olap`:

- `6744`

## Interpretacion

- El modelo de Victor si existe y ya puede consumirse desde la capa de machine learning.
- La fact principal queda en `olap.fact_ventas`.
- Si alguien esperaba `10000` filas dentro de la fact del modelo `OLAP`, eso no se cumple con la version actual montada localmente.
