
-- ==========================================
-- PROYECTO: DataStore Analytics
-- MOTOR: Microsoft SQL Server
-- OBJETIVO: Crear base de datos y tabla Ventas
-- ==========================================

IF DB_ID('DataStoreDB') IS NULL
BEGIN
    CREATE DATABASE DataStoreDB;
END;
GO

USE DataStoreDB;
GO

IF OBJECT_ID('dbo.Ventas', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Ventas (
        IdVenta INT IDENTITY(1,1) PRIMARY KEY,
        Fecha DATE NOT NULL,
        Producto VARCHAR(100) NOT NULL,
        Cantidad INT NOT NULL CHECK (Cantidad > 0),
        PrecioUnitario DECIMAL(10,2) NOT NULL
            CHECK (PrecioUnitario > 0)
    );

    PRINT 'Tabla Ventas creada correctamente';
END
ELSE
BEGIN
    PRINT 'La tabla Ventas ya existe';
END;
GO
