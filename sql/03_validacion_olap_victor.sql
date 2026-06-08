-- Validacion basica del modelo OLAP de Victor
-- Base objetivo: restaurante
-- Esquema analitico: olap

-- 1. Confirmar las tablas del esquema
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'olap'
ORDER BY table_name;

-- 2. Conteo rapido por tabla
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

-- 3. Revisar los metodos de pago cargados
SELECT *
FROM olap.dim_metodo_pago
ORDER BY id_metodo_pago;

-- 4. Vista rapida de la fact table
SELECT *
FROM olap.fact_ventas
LIMIT 10;

-- 5. Conteo aproximado de tickets reconstruibles para ML
SELECT COUNT(*) AS tickets_reconstruibles
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
