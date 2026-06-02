-- Exploracion inicial del modelo OLAP de Victor
-- Base: restaurante
-- Esquema: olap

-- 1. Conteo rapido de las tablas del esquema
SELECT 'dim_tiempo' AS tabla, COUNT(*) AS total FROM olap.dim_tiempo
UNION ALL
SELECT 'dim_cliente', COUNT(*) FROM olap.dim_cliente
UNION ALL
SELECT 'dim_platillo', COUNT(*) FROM olap.dim_platillo
UNION ALL
SELECT 'dim_sucursal', COUNT(*) FROM olap.dim_sucursal
UNION ALL
SELECT 'dim_empleado', COUNT(*) FROM olap.dim_empleado
UNION ALL
SELECT 'dim_mesa', COUNT(*) FROM olap.dim_mesa
UNION ALL
SELECT 'dim_metodo_pago', COUNT(*) FROM olap.dim_metodo_pago
UNION ALL
SELECT 'fact_ventas', COUNT(*) FROM olap.fact_ventas;

-- 2. Vista rapida de la tabla de hechos
SELECT *
FROM olap.fact_ventas
LIMIT 10;

-- 3. Vista de negocio uniendo lineas de venta con dimensiones
SELECT
    t.fecha,
    t.anio,
    t.nombre_mes,
    t.dia_semana,
    t.fin_semana,
    c.nombre AS cliente,
    p.nombre AS platillo,
    p.categoria,
    s.ciudad,
    e.tipo AS tipo_empleado,
    e.turno,
    m.capacidad AS capacidad_mesa,
    mp.metodo_pago,
    f.cantidad,
    f.precio_unitario,
    f.subtotal,
    f.total_pedido,
    f.monto_pago
FROM olap.fact_ventas f
JOIN olap.dim_tiempo t
    ON f.id_tiempo = t.id_tiempo
JOIN olap.dim_cliente c
    ON f.id_cliente = c.id_cliente
JOIN olap.dim_platillo p
    ON f.id_platillo = p.id_platillo
JOIN olap.dim_sucursal s
    ON f.id_sucursal = s.id_sucursal
JOIN olap.dim_empleado e
    ON f.id_empleado = e.id_empleado
JOIN olap.dim_mesa m
    ON f.id_mesa = m.id_mesa
JOIN olap.dim_metodo_pago mp
    ON f.id_metodo_pago = mp.id_metodo_pago
LIMIT 20;

-- 4. Reconstruccion aproximada de tickets
SELECT COUNT(*) AS tickets_reconstruidos
FROM (
    SELECT
        f.id_tiempo,
        f.id_cliente,
        f.id_sucursal,
        f.id_empleado,
        f.id_mesa,
        f.id_metodo_pago,
        f.total_pedido,
        f.monto_pago
    FROM olap.fact_ventas f
    GROUP BY
        f.id_tiempo,
        f.id_cliente,
        f.id_sucursal,
        f.id_empleado,
        f.id_mesa,
        f.id_metodo_pago,
        f.total_pedido,
        f.monto_pago
) tickets;

-- 5. Estadisticas clave para definir el primer target
SELECT
    MIN(total_pedido) AS minimo_total,
    percentile_cont(0.25) WITHIN GROUP (ORDER BY total_pedido) AS q1,
    percentile_cont(0.50) WITHIN GROUP (ORDER BY total_pedido) AS mediana,
    percentile_cont(0.75) WITHIN GROUP (ORDER BY total_pedido) AS q3,
    MAX(total_pedido) AS maximo_total
FROM olap.fact_ventas;
