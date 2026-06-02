# 04 Tickets Regresion

## Que contiene esta etapa

Esta carpeta concentra los resultados del modelo de **Regresion Lineal** para estimar el `total_pedido`.

## Archivos esperados

- `04_tickets_regresion.parquet`
- `04_metricas_regresion.parquet`

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

## Resultado validado

Metricas obtenidas en la prueba:

- `mae = 92.3532`
- `rmse = 111.6319`
- `r2 = 0.2364`

## Interpretacion rapida

- el modelo ya logra aproximar el total del pedido
- el error promedio absoluto es util para comparar mejoras futuras
- como primer modelo de regresion deja una base clara para Qlik y para el reporte final

## Como se deberia ver en Qlik

En Qlik esta salida deberia servir para:

- comparar `total_pedido` real vs `pred_total_pedido`
- revisar residuos por ciudad, turno y metodo de pago
- detectar tickets donde el error del modelo sea mas alto
