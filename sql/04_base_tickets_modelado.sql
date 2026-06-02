-- Base analitica por ticket para Machine Learning
-- Fuente: restaurante.olap
-- Objetivo: generar una fila por ticket reconstruido

WITH tickets_base AS (
    SELECT
        f.id_tiempo,
        f.id_cliente,
        f.id_sucursal,
        f.id_empleado,
        f.id_mesa,
        f.id_metodo_pago,
        f.total_pedido,
        f.monto_pago,
        COUNT(*) AS lineas_ticket,
        SUM(f.cantidad) AS cantidad_total,
        COUNT(DISTINCT f.id_platillo) AS platillos_distintos,
        COUNT(DISTINCT p.categoria) AS categorias_distintas,
        SUM(f.subtotal) AS subtotal_ticket,
        MAX(CASE WHEN p.categoria = 'Bebidas' THEN 1 ELSE 0 END) AS incluye_bebida,
        MAX(CASE WHEN p.categoria = 'Postres' THEN 1 ELSE 0 END) AS incluye_postre,
        MAX(CASE WHEN p.categoria = 'Entradas' THEN 1 ELSE 0 END) AS incluye_entrada,
        MAX(CASE WHEN p.categoria = 'Platillos Fuertes' THEN 1 ELSE 0 END) AS incluye_platillo_fuerte
    FROM olap.fact_ventas f
    JOIN olap.dim_platillo p
        ON f.id_platillo = p.id_platillo
    GROUP BY
        f.id_tiempo,
        f.id_cliente,
        f.id_sucursal,
        f.id_empleado,
        f.id_mesa,
        f.id_metodo_pago,
        f.total_pedido,
        f.monto_pago
)
SELECT
    ROW_NUMBER() OVER (
        ORDER BY
            t.fecha,
            tb.id_cliente,
            tb.id_sucursal,
            tb.id_empleado,
            tb.id_mesa,
            tb.id_metodo_pago,
            tb.total_pedido
    ) AS id_ticket_modelado,
    tb.id_tiempo,
    t.fecha,
    t.dia,
    t.mes,
    t.nombre_mes,
    t.trimestre,
    t.anio,
    t.dia_semana,
    t.fin_semana,
    tb.id_cliente,
    tb.id_sucursal,
    s.ciudad,
    s.capacidad AS capacidad_sucursal,
    tb.id_empleado,
    e.tipo AS tipo_empleado,
    e.salario,
    e.turno,
    tb.id_mesa,
    m.numero_mesa,
    m.capacidad AS capacidad_mesa,
    tb.id_metodo_pago,
    mp.metodo_pago,
    tb.lineas_ticket,
    tb.cantidad_total,
    tb.platillos_distintos,
    tb.categorias_distintas,
    tb.subtotal_ticket,
    tb.total_pedido,
    tb.monto_pago,
    tb.monto_pago - tb.total_pedido AS diferencia_pago,
    tb.incluye_bebida,
    tb.incluye_postre,
    tb.incluye_entrada,
    tb.incluye_platillo_fuerte,
    CASE
        WHEN tb.total_pedido >= 525 THEN 1
        ELSE 0
    END AS ticket_alto
FROM tickets_base tb
JOIN olap.dim_tiempo t
    ON tb.id_tiempo = t.id_tiempo
JOIN olap.dim_sucursal s
    ON tb.id_sucursal = s.id_sucursal
JOIN olap.dim_empleado e
    ON tb.id_empleado = e.id_empleado
JOIN olap.dim_mesa m
    ON tb.id_mesa = m.id_mesa
JOIN olap.dim_metodo_pago mp
    ON tb.id_metodo_pago = mp.id_metodo_pago
ORDER BY
    t.fecha,
    id_ticket_modelado;
