# 03 Tickets Clasíficados

## Qué contiene esta etapa

Esta carpeta concentra los resultados del modelo de **Regresión Logística** para clasificar tickets altos.

## Archivos esperados

- `03_tickets_clasificados.parquet`

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
- `líneas_ticket`
- `cantidad_total`
- `platillos_distintos`
- `categorias_distintas`
- `incluye_bebida`
- `incluye_postre`
- `incluye_entrada`
- `incluye_platillo_fuerte`

## Por que se eligió este modelo

Se eligió **Regresión Logística** porque el objetivo de esta etapa es responder una pregunta binaria:

- si un ticket puede considerarse `alto` o `normal`

Este modelo conviene porque:

- es fácil de interpretar
- funciona bien como primera referencia para clasificación
- permite obtener una probabilidad, no solo una clase final
- ayuda a explicar qué variables se relaciónan con tickets de mayor valor

## Resultado validado

Métricas obtenidas en la prueba:

- `accuracy = 0.6282`
- `precision = 0.3710`
- `recall = 0.8364`
- `f1 = 0.5140`
- `roc_auc = 0.7278`

## Archivo que interesa a Qlik

El archivo principal para Qlik en esta etapa es:

- `03_tickets_clasificados.parquet`

## Por qué le sirve al restaurante

Este modelo le sirve al restaurante porque ayuda a detectar condiciones relaciónadas con tickets altos, por ejemplo:

- turnos donde se vende ms
- combinaciones de consumo que elevan el ticket
- ciudades o sucursales con mayor probabilidad de venta alta
- contextos donde conviene poner atencion operativa o comercial

## Interpretación rápida

- el modelo recupera bien los tickets altos
- tiene mejor `recall` que `precision`
- como primer modelo exploratorio es funcional y útil para seguimiento en Qlik

## Como se debería ver en Qlik

En Qlik esta salida debería servir para:

- comparar clase real vs clase predicha
- mostrar la probabilidad de `ticket_alto`
- filtrar tickets por ciudad, turno y metodo de pago
- construir semaforos o alertas de probabilidad alta
