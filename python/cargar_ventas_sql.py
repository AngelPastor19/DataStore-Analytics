
import csv
import pyodbc
from decimal import Decimal
from pathlib import Path

# CONFIGURACION DE RUTAS
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

print("=== DATASTORE - CARGA DE VENTAS ===")

conexion = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=localhost\SQLEXPRESS;"
    "DATABASE=DataStoreDB;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;",
    timeout=10
)

ventas_insertadas = 0
ventas_omitidas = 0

try:
    cursor = conexion.cursor()

    with open(DATA_DIR / "ventas_limpias.csv", "r", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)

        for venta in lector:
            fecha = venta["Fecha"]
            producto = venta["Producto"]
            cantidad = int(venta["Cantidad"])
            precio = Decimal(venta["PrecioUnitario"])

            cursor.execute("""
                SELECT COUNT(*)
                FROM dbo.Ventas
                WHERE Fecha = ?
                  AND Producto = ?
                  AND Cantidad = ?
                  AND PrecioUnitario = ?
            """, fecha, producto, cantidad, precio)

            existe = cursor.fetchone()[0]

            if existe > 0:
                print(producto, "- OMITIDA: ya existe")
                ventas_omitidas += 1

            else:
                cursor.execute("""
                    INSERT INTO dbo.Ventas
                        (Fecha, Producto, Cantidad, PrecioUnitario)
                    VALUES (?, ?, ?, ?)
                """, fecha, producto, cantidad, precio)

                print(producto, "- INSERTADA")
                ventas_insertadas += 1

    conexion.commit()
    print("\nTRANSACCION CONFIRMADA")

except Exception as error:
    conexion.rollback()
    print("\nERROR: se revirtieron los cambios")
    print(error)
    raise

finally:
    conexion.close()

print("\nRESUMEN")
print("Ventas insertadas:", ventas_insertadas)
print("Ventas omitidas:", ventas_omitidas)
