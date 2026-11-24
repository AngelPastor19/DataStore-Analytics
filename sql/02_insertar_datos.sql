
-- ==========================================
-- PROYECTO: DataStore Analytics
-- OBJETIVO: Insertar datos iniciales
-- ==========================================

USE DataStoreDB;
GO

IF NOT EXISTS (SELECT 1 FROM dbo.Ventas)
BEGIN

    INSERT INTO dbo.Ventas
        (Fecha, Producto, Cantidad, PrecioUnitario)
    VALUES
        ('2026-11-20', 'Laptop Lenovo', 2, 2500),
        ('2026-11-20', 'Mouse Logitech', 5, 80),
        ('2026-11-20', 'Teclado Redragon', 3, 150),
        ('2026-11-20', 'Monitor Samsung', 2, 750),
        ('2026-11-20', 'Audífonos Sony', 4, 200),
        ('2026-11-21', 'Laptop Lenovo', 1, 2500),
        ('2026-11-21', 'Mouse Logitech', 3, 80),
        ('2026-11-21', 'Monitor Samsung', 2, 750),
        ('2026-11-21', 'Audífonos Sony', 2, 200),
        ('2026-11-21', 'Teclado Redragon', 4, 150);

    PRINT 'Datos iniciales insertados correctamente';

END
ELSE
BEGIN

    PRINT 'La tabla ya contiene datos. Carga omitida';

END;
GO

-- Verificar los registros
SELECT * FROM dbo.Ventas;
GO
