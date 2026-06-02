-- Montaje local del modelo OLAP de Victor
-- Base objetivo: restaurante
-- Esquema analitico: olap
--
-- Nota:
-- Este script respeta la idea general del modelo OLAP compartido por el equipo OLAP,
-- pero corrige y completa lo necesario para que pueda ejecutarse localmente y ser
-- consumido por la capa de Machine Learning.

DROP SCHEMA IF EXISTS olap CASCADE;
CREATE SCHEMA olap;

-- Dimension de tiempo
CREATE TABLE olap.dim_tiempo (
    id_tiempo SERIAL PRIMARY KEY,
    fecha DATE,
    dia INT,
    mes INT,
    nombre_mes VARCHAR(20),
    trimestre INT,
    anio INT,
    dia_semana VARCHAR(20),
    fin_semana BOOLEAN
);

-- Dimension de clientes
CREATE TABLE olap.dim_cliente (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20)
);

-- Dimension de platillos
CREATE TABLE olap.dim_platillo (
    id_platillo INT PRIMARY KEY,
    nombre VARCHAR(100),
    precio_actual DECIMAL(10,2),
    categoria VARCHAR(100),
    descripcion TEXT
);

-- Dimension de sucursales
CREATE TABLE olap.dim_sucursal (
    id_sucursal INT PRIMARY KEY,
    direccion VARCHAR(200),
    telefono VARCHAR(20),
    ciudad VARCHAR(100),
    capacidad INT
);

-- Dimension de empleados
CREATE TABLE olap.dim_empleado (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50),
    telefono VARCHAR(20),
    salario DECIMAL(10,2),
    turno VARCHAR(50)
);

-- Dimension de mesas
CREATE TABLE olap.dim_mesa (
    id_mesa INT PRIMARY KEY,
    numero_mesa INT,
    capacidad INT,
    estado VARCHAR(50)
);

-- Dimension de metodo de pago
CREATE TABLE olap.dim_metodo_pago (
    id_metodo_pago SERIAL PRIMARY KEY,
    metodo_pago VARCHAR(50) UNIQUE
);

-- Tabla de hechos del cubo de ventas
CREATE TABLE olap.fact_ventas (
    id_fact_venta SERIAL PRIMARY KEY,
    id_tiempo INT,
    id_cliente INT,
    id_platillo INT,
    id_sucursal INT,
    id_empleado INT,
    id_mesa INT,
    id_metodo_pago INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    subtotal DECIMAL(10,2),
    total_pedido DECIMAL(10,2),
    monto_pago DECIMAL(10,2),
    FOREIGN KEY (id_tiempo) REFERENCES olap.dim_tiempo(id_tiempo),
    FOREIGN KEY (id_cliente) REFERENCES olap.dim_cliente(id_cliente),
    FOREIGN KEY (id_platillo) REFERENCES olap.dim_platillo(id_platillo),
    FOREIGN KEY (id_sucursal) REFERENCES olap.dim_sucursal(id_sucursal),
    FOREIGN KEY (id_empleado) REFERENCES olap.dim_empleado(id_empleado),
    FOREIGN KEY (id_mesa) REFERENCES olap.dim_mesa(id_mesa),
    FOREIGN KEY (id_metodo_pago) REFERENCES olap.dim_metodo_pago(id_metodo_pago)
);

-- Carga de dimensiones
INSERT INTO olap.dim_tiempo (
    fecha, dia, mes, nombre_mes, trimestre, anio, dia_semana, fin_semana
)
SELECT DISTINCT
    DATE(p.fecha_hora) AS fecha,
    EXTRACT(DAY FROM p.fecha_hora)::INT AS dia,
    EXTRACT(MONTH FROM p.fecha_hora)::INT AS mes,
    TO_CHAR(p.fecha_hora, 'TMMonth') AS nombre_mes,
    EXTRACT(QUARTER FROM p.fecha_hora)::INT AS trimestre,
    EXTRACT(YEAR FROM p.fecha_hora)::INT AS anio,
    TO_CHAR(p.fecha_hora, 'TMDay') AS dia_semana,
    EXTRACT(ISODOW FROM p.fecha_hora) IN (6, 7) AS fin_semana
FROM public.pedido p
ORDER BY fecha;

INSERT INTO olap.dim_cliente (id_cliente, nombre, telefono)
SELECT
    c.id_cliente,
    c.nombre,
    c.telefono
FROM public.cliente c;

INSERT INTO olap.dim_platillo (id_platillo, nombre, precio_actual, categoria, descripcion)
SELECT
    p.id_platillo,
    p.nombre,
    p.precio,
    c.nombre AS categoria,
    p.descripcion
FROM public.platillo p
LEFT JOIN public.categoria c
    ON c.id_categoria = p.id_categoria;

INSERT INTO olap.dim_sucursal (id_sucursal, direccion, telefono, ciudad, capacidad)
SELECT
    s.id_sucursal,
    s.direccion,
    s.telefono,
    s.ciudad,
    s.capacidad
FROM public.sucursal s;

INSERT INTO olap.dim_empleado (id_empleado, nombre, tipo, telefono, salario, turno)
SELECT
    e.id_empleado,
    e.nombre,
    e.tipo,
    e.telefono,
    e.salario,
    e.turno
FROM public.empleado e;

INSERT INTO olap.dim_mesa (id_mesa, numero_mesa, capacidad, estado)
SELECT
    m.id_mesa,
    m.numero_mesa,
    m.capacidad,
    m.estado
FROM public.mesa m;

INSERT INTO olap.dim_metodo_pago (metodo_pago)
SELECT DISTINCT
    pa.metodo_pago
FROM public.pago pa
WHERE pa.metodo_pago IS NOT NULL
ORDER BY pa.metodo_pago;

-- Carga de la tabla de hechos
-- Se sigue la logica del script del equipo OLAP: una fila por detalle de pedido
-- unido con pedido, mesa, pago y dimensiones.
INSERT INTO olap.fact_ventas (
    id_tiempo,
    id_cliente,
    id_platillo,
    id_sucursal,
    id_empleado,
    id_mesa,
    id_metodo_pago,
    cantidad,
    precio_unitario,
    subtotal,
    total_pedido,
    monto_pago
)
SELECT
    dt.id_tiempo,
    p.id_cliente,
    dp.id_platillo,
    m.id_sucursal,
    p.id_empleado,
    p.id_mesa,
    mp.id_metodo_pago,
    dp.cantidad,
    dp.precio_unitario,
    dp.subtotal,
    p.total,
    pa.monto
FROM public.detallepedido dp
JOIN public.pedido p
    ON dp.id_pedido = p.id_pedido
JOIN public.mesa m
    ON p.id_mesa = m.id_mesa
JOIN public.pago pa
    ON pa.id_pedido = p.id_pedido
JOIN olap.dim_tiempo dt
    ON dt.fecha = DATE(p.fecha_hora)
JOIN olap.dim_metodo_pago mp
    ON mp.metodo_pago = pa.metodo_pago;

-- Indices analiticos
CREATE INDEX idx_fact_tiempo
ON olap.fact_ventas(id_tiempo);

CREATE INDEX idx_fact_cliente
ON olap.fact_ventas(id_cliente);

CREATE INDEX idx_fact_platillo
ON olap.fact_ventas(id_platillo);

CREATE INDEX idx_fact_sucursal
ON olap.fact_ventas(id_sucursal);
