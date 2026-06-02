# 04 Tickets Regresion

## Que contiene esta etapa

Esta carpeta concentra los resultados del modelo de **Regresion Lineal** para estimar el `total_pedido`.

## Archivos esperados

- `04_tickets_regresion.parquet`

## Fuente de datos

El modelo usa como entrada:

- `parquets/02_EDA_Base_Tickets/02_base_eda_tickets.parquet`

## Variables usadas por el modelo

- `dia`
- `mes`
- `trimestre`
- `dia_semana`
- `dia_tipo`
- `fin_semana`
- `ciudad`
- `capacidad_sucursal`
- `tipo_empleado`
- `salario`
- `turno`
- `numero_mesa`
- `capacidad_mesa`
- `metodo_pago`
- `lineas_ticket`
- `cantidad_total`
- `platillos_distintos`
- `categorias_distintas`
- `incluye_bebida`
- `incluye_postre`
- `incluye_entrada`
- `incluye_platillo_fuerte`

## Por que se eligio este modelo

Se eligio **Regresion Lineal** porque en esta etapa la meta es estimar una variable numerica:

- `total_pedido`

Este modelo conviene porque:

- da una base simple y facil de explicar
- funciona como punto de partida para medir error
- permite comparar valor real contra valor estimado
- ayuda a detectar si el contexto del ticket explica parte del monto final

## Resultado validado

Metricas obtenidas en la prueba:

- `mae = 92.3532`
- `rmse = 111.6319`
- `r2 = 0.2364`

## Archivo que interesa a Qlik

El archivo principal para Qlik en esta etapa es:

- `04_tickets_regresion.parquet`

## Por que le sirve al restaurante

Este modelo le sirve al restaurante porque permite estimar cuanto podria valer un pedido segun su contexto. Eso ayuda para:

- proyectar el valor esperado de un ticket
- detectar pedidos atipicos
- revisar donde el modelo falla mas
- identificar turnos, ciudades o formas de consumo con mayor impacto en el total

## Interpretacion rapida

- el modelo ya logra aproximar el total del pedido
- el error promedio absoluto es util para comparar mejoras futuras
- como primer modelo de regresion deja una base clara para Qlik y para el reporte final

## Como se deberia ver en Qlik

En Qlik esta salida deberia servir para:

- comparar `total_pedido` real vs `pred_total_pedido`
- revisar residuos por ciudad, turno y metodo de pago
- detectar tickets donde el error del modelo sea mas alto
