# Capa Machine Learning

Repositorio de trabajo para la fase de **Machine Learning** del proyecto final de la materia **Desarrollo de Inteligencia de Negocios**.

## Contexto

Este proyecto forma parte de una arquitectura por capas desarrollada entre varios equipos:

1. `OLTP`
2. `ETL`
3. `OLAP`
4. `Machine Learning`
5. `Visualizacion en Qlik`

El objetivo de este repositorio es construir la capa analitica/predictiva usando como fuente principal el modelo analitico ya generado por los equipos anteriores.

## Objetivo de esta fase

- Consumir el modelo OLAP / Data Warehouse del proyecto restaurante.
- Analizar los datos disponibles para definir uno o mas modelos de machine learning viables.
- Entrenar, validar y documentar los modelos seleccionados.
- Desarrollar la capa contemplando el uso de `4 modelos de machine learning`, aunque en esta etapa inicial todavia no se hayan definido exactamente cuales seran.
- Generar salidas finales que despues puedan ser utilizadas por el equipo de visualizacion en Qlik.
- Preparar la exportacion principal en formato `Parquet` para el equipo de Qlik.

## Fuente principal de datos

Actualmente la fuente principal identificada para esta fase es la base:

- `restaurante_dw`

Tablas principales detectadas:

- `fact_ventas`
- `dim_tiempo`
- `dim_cliente`
- `dim_empleado`
- `dim_platillo`
- `dim_pago`
- `dim_sucursal`

## Estructura inicial del repositorio

- `docs/` Documentacion, bitacoras y notas del proceso.
- `sql/` Consultas SQL, vistas y scripts de preparacion de datos.
- `scripts/` Scripts en Python para extraccion, modelado y exportacion.
- `notebooks/` Analisis exploratorio y experimentos.
- `models/` Modelos entrenados y metadatos.
- `reports/` Resultados, tablas y entregables.
- `data/` Archivos intermedios y exportaciones controladas.

Nota:

- Los archivos `.gitkeep` solo se usan para conservar carpetas vacias dentro de Git mientras el proyecto empieza.
- Cuando cada carpeta tenga archivos reales, esos `.gitkeep` se pueden dejar o eliminar sin problema.

## Forma de trabajo

Cada cambio importante se documentara en la bitacora del proyecto para dejar evidencia clara del proceso:

- que se hizo
- por que se hizo
- con que datos se trabajo
- que resultado se obtuvo

## Avance tecnico inicial

Hasta este momento ya se dejo preparado el entorno local de trabajo en PostgreSQL con dos bases:

- `restaurante` = capa `OLTP`
- `restaurante_dw` = capa analitica / `Data Warehouse`

Validaciones realizadas:

- `restaurante`
  - `pedido = 1200`
  - `pago = 1204`
  - `detallepedido = 5348`
  - `cliente = 800`
  - `platillo = 60`
- `restaurante_dw`
  - `fact_ventas = 1131`
  - `dim_tiempo = 365`
  - `dim_cliente = 800`
  - `dim_empleado = 50`
  - `dim_platillo = 60`
  - `dim_pago = 1149`
  - `dim_sucursal = 5`

Esto significa que la fase de machine learning ya tiene un punto de partida real y ya no depende de esperar a que se construya la base desde cero.

## Documentacion detallada

Si se necesita ver el proceso con mas detalle, la evidencia se ira concentrando en la carpeta:

- `docs/`

Documentos clave hasta ahora:

- `docs/bitacora.md`
- `docs/estado_tecnico_inicial.md`

## Estado actual

- [x] Se creo el repositorio base de la capa de machine learning.
- [x] Se definio la estructura inicial de trabajo.
- [x] Se identifico la base `restaurante_dw` como fuente principal.
- [x] Se prepararon y validaron localmente las bases `restaurante` y `restaurante_dw`.
- [x] Se definio `Parquet` como formato principal de salida para el equipo de Qlik.
- [x] Se definio que la capa trabajara con `4 modelos de machine learning` como alcance general.
- [ ] Se validaran consultas del modelo OLAP / DW.
- [ ] Se definira el primer problema de machine learning.
- [ ] Se construira la primera tabla base para modelado.
- [ ] Se entrenara el primer modelo.
- [ ] Se preparara la salida para el equipo de Qlik.
