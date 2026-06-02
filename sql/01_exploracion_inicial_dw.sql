-- Exploracion inicial del Data Warehouse / modelo analitico
-- Base de trabajo: restaurante_dw
-- Objetivo: validar estructura, revisar fact_ventas y entender el modelo como negocio

-- 1. Vista rapida de la tabla de hechos
SELECT *
FROM fact_ventas
LIMIT 10;


-- 2. Vista de negocio uniendo la tabla de hechos con las dimensiones principales
SELECT
    f.id_pedido_src,
    t.fecha,
    t.anio,
    t.mes,
    t.nombre_dia,
    s.ciudad,
    c.segmento,
    c.total_visitas_historicas,
    e.tipo AS tipo_empleado,
    e.turno,
    p.nombre AS platillo_principal,
    p.categoria,
    pg.metodo_pago,
    f.monto_total,
    f.monto_pagado,
    f.cantidad_items,
    f.cantidad_platillos_distintos,
    f.descuento
FROM fact_ventas f
JOIN dim_tiempo t   ON f.sk_tiempo = t.sk_tiempo
JOIN dim_sucursal s ON f.sk_sucursal = s.sk_sucursal
JOIN dim_cliente c  ON f.sk_cliente = c.sk_cliente
JOIN dim_empleado e ON f.sk_empleado = e.sk_empleado
JOIN dim_platillo p ON f.sk_platillo = p.sk_platillo
LEFT JOIN dim_pago pg ON f.sk_pago = pg.sk_pago
LIMIT 30;


-- 3. Conteo rapido de las tablas principales del modelo
SELECT 'fact_ventas' AS tabla, COUNT(*) AS total FROM fact_ventas
UNION ALL
SELECT 'dim_tiempo', COUNT(*) FROM dim_tiempo
UNION ALL
SELECT 'dim_cliente', COUNT(*) FROM dim_cliente
UNION ALL
SELECT 'dim_empleado', COUNT(*) FROM dim_empleado
UNION ALL
SELECT 'dim_platillo', COUNT(*) FROM dim_platillo
UNION ALL
SELECT 'dim_pago', COUNT(*) FROM dim_pago
UNION ALL
SELECT 'dim_sucursal', COUNT(*) FROM dim_sucursal;
