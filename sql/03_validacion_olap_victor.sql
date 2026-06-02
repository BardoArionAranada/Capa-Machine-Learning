-- Validacion basica del modelo OLAP de Victor
-- Base objetivo: restaurante
-- Esquema analitico: olap

SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'olap'
ORDER BY table_name;

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

SELECT *
FROM olap.fact_ventas
LIMIT 10;
