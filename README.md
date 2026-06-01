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
- Generar salidas finales que despues puedan ser utilizadas por el equipo de visualizacion en Qlik.

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

## Forma de trabajo

Cada cambio importante se documentara en la bitacora del proyecto para dejar evidencia clara del proceso:

- que se hizo
- por que se hizo
- con que datos se trabajo
- que resultado se obtuvo

## Estado actual

- [x] Se creo el repositorio base de la capa de machine learning.
- [x] Se definio la estructura inicial de trabajo.
- [x] Se identifico la base `restaurante_dw` como fuente principal.
- [ ] Se validaran consultas del modelo OLAP / DW.
- [ ] Se definira el primer problema de machine learning.
- [ ] Se construira la primera tabla base para modelado.
- [ ] Se entrenara el primer modelo.
- [ ] Se preparara la salida para el equipo de Qlik.
