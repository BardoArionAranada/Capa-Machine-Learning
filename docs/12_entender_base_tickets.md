# 12 Entender la Base de Tickets

## Objetivo de esta guía

Este documento explica por qué el proyecto trabaja con una **base por ticket**, qué hace el archivo `sql/04_base_tickets_modelado.sql` y cómo se relaciona con el notebook `01`.

## Qué significa ticket en este proyecto

En este proyecto, un **ticket** representa una compra resumida del restaurante.

No se usa la palabra ticket como algo distinto a una compra, sino como una forma de decir:

- una cuenta
- un pedido resumido
- una compra analítica reconstruida

## Por qué se reconstruyen tickets

La tabla `olap.fact_ventas` no guarda una fila por compra completa.

Lo que guarda normalmente es un nivel más detallado, donde una misma compra puede aparecer en varias filas porque incluye varios platillos.

Entonces ocurre esto:

- una compra puede tener varios platillos
- cada platillo puede ocupar una fila distinta en `olap.fact_ventas`
- una sola compra puede repetirse en varias filas

Para Machine Learning conviene trabajar con una unidad más resumida:

- `1 fila = 1 compra`

Esa compra resumida es lo que en el proyecto se llama **ticket modelado**.

## Diferencia entre fact_ventas y ticket modelado

- `olap.fact_ventas` = detalle de venta
- `ticket modelado` = compra reconstruida y resumida

## Qué hace `04_base_tickets_modelado.sql`

Este archivo **no genera el parquet por si solo**.

Su función es definir la consulta SQL que:

1. toma los datos de `olap.fact_ventas`
2. une la tabla `olap.dim_platillo`
3. agrupa varias filas que pertenecen a una misma compra
4. calcula variables de negocio
5. deja lista una base analítica con una fila por ticket

## Entonces, filtra o transforma

El archivo no está pensado para filtrar por ciudad, por mes o por una sola sucursal.

Lo que hace principalmente es:

- agrupar
- resumir
- enriquecer
- crear variables

## Variables que genera esa base

Algunos ejemplos directos que salen de `04_base_tickets_modelado.sql` son:

- `líneas_ticket`
- `cantidad_total`
- `platillos_distintos`
- `categorias_distintas`
- `subtotal_ticket`
- `incluye_bebida`
- `incluye_postre`
- `incluye_entrada`
- `incluye_platillo_fuerte`
- `ticket_alto`

Eso convierte el detalle de venta en una base mucho más útil para modelar.

## Ejemplo sencillo

Imagina una compra con:

- `2 tacos`
- `1 refresco`
- `1 postre`

En `olap.fact_ventas`, esa compra puede aparecer en varias filas.

El archivo `04_base_tickets_modelado.sql` junta esas filas y las resume en un solo ticket con campos como:

- `total_pedido`
- `cantidad_total`
- `platillos_distintos`
- `incluye_bebida`
- `incluye_postre`
- `metodo_pago`
- `sucursal`
- `empleado`
- `fecha`

## Relación entre SQL, notebook y parquet

La relación correcta del paso `01` es esta:

1. `sql/04_base_tickets_modelado.sql` define la consulta
2. `notebooks/01_Carga_y_Validacion_Parquet/01_Carga_y_Validacion_Parquet.ipynb` ejecuta esa consulta
3. el notebook guarda el resultado en:
   - `parquets/01_Carga_y_Validacion_Parquet/01_base_tickets_modelado.parquet`

En resumen:

- el SQL prepara la base
- el notebook la ejecuta y la exporta
- el parquet guarda el resultado final de la etapa

## Flujo completo del proyecto

La secuencia completa queda así:

1. `01` se conecta a la base de datos y genera `01_base_tickets_modelado.parquet`
2. `02` lee el parquet `01` y genera `02_base_eda_tickets.parquet`
3. `03` lee el parquet `02` y genera `03_tickets_clasificados.parquet`
4. `04` lee el parquet `02` y genera `04_tickets_regresion.parquet`
5. `05` lee el parquet `02` y genera `05_clientes_segmentados.parquet`

## Datos de conexión para DBeaver

Para revisar el OLAP desde DBeaver:

- `Host = localhost`
- `Port = 5432`
- `Database = restaurante`
- `Username = postgres`
- `Password = postgres`
- `Schema = olap`

## Qué SQL se puede ejecutar en DBeaver

Estos archivos si se pueden usar normalmente en DBeaver:

- `sql/01_exploracion_inicial_olap_victor.sql`
- `sql/03_validación_olap_victor.sql`
- `sql/04_base_tickets_modelado.sql`

## Qué SQL no conviene ejecutar por rutina

- `sql/02_montaje_olap_victor.sql`

Ese archivo reconstruye el esquema `olap` desde cero, por lo que solo sirve para montar otra vez el OLAP si fuera necesario.

## Por qué esto le sirve al restaurante

Trabajar por ticket permite responder preguntas útiles para el negocio, por ejemplo:

- qué condiciones se relaciónan con compras altas
- cuánto podría valer un pedido según su contexto
- que patrones de compra se repiten en ciertas sucursales o turnos
- cómo se comportan los clientes según su historial de consumo

## Qué se debe ver al ejecutar los notebooks

Al correr los notebooks no solo se generan parquets, también se deben ver resultados visuales y tablas de validación:

- `01` muestra validaciónes de estructura y forma del dataset
- `02` muestra exploración con histogramas y boxplots
- `03` muestra métricas, matriz de confusión y curva ROC
- `04` muestra métricas de regresión, comparativos y residuos
- `05` muestra clusters, conteos y dispersión de clientes
