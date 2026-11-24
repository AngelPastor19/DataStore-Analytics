
-- ==========================================
-- PROYECTO: DataStore Analytics
-- OBJETIVO: Analisis empresarial de ventas
-- ==========================================

USE DataStoreDB;
GO

-- 1. Indicadores generales
SELECT
    COUNT(*) AS NumeroVentas,
    SUM(Cantidad) AS UnidadesVendidas,
    SUM(Cantidad * PrecioUnitario) AS IngresosTotales
FROM dbo.Ventas;

-- 2. Ingresos por producto
SELECT
    Producto,
    SUM(Cantidad * PrecioUnitario) AS Ingresos
FROM dbo.Ventas
GROUP BY Producto
ORDER BY Ingresos DESC;

-- 3. Unidades vendidas por producto
SELECT
    Producto,
    SUM(Cantidad) AS UnidadesVendidas
FROM dbo.Ventas
GROUP BY Producto
ORDER BY UnidadesVendidas DESC;

-- 4. Ingresos por fecha
SELECT
    Fecha,
    SUM(Cantidad * PrecioUnitario) AS Ingresos
FROM dbo.Ventas
GROUP BY Fecha
ORDER BY Fecha;

-- 5. Producto con mayores ingresos
SELECT TOP 1
    Producto,
    SUM(Cantidad * PrecioUnitario) AS Ingresos
FROM dbo.Ventas
GROUP BY Producto
ORDER BY Ingresos DESC;

-- 6. Importe promedio por venta
SELECT
    CAST(
        AVG(Cantidad * PrecioUnitario)
        AS DECIMAL(10,2)
    ) AS ImportePromedio
FROM dbo.Ventas;
GO
