# 03 Tickets Clasificados

## Que contiene esta etapa

Esta carpeta concentra los resultados del modelo de **Regresion Logistica** para clasificar tickets altos.

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

- `accuracy = 0.6282`
- `precision = 0.3710`
- `recall = 0.8364`
- `f1 = 0.5140`
- `roc_auc = 0.7278`

## Archivo que interesa a Qlik

El archivo principal para Qlik en esta etapa es:

- `03_tickets_clasificados.parquet`

## Interpretacion rapida

- el modelo recupera bien los tickets altos
- tiene mejor `recall` que `precision`
- como primer modelo exploratorio es funcional y util para seguimiento en Qlik

## Como se deberia ver en Qlik

En Qlik esta salida deberia servir para:

- comparar clase real vs clase predicha
- mostrar la probabilidad de `ticket_alto`
- filtrar tickets por ciudad, turno y metodo de pago
- construir semaforos o alertas de probabilidad alta
