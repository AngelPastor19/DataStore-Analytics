
import csv
import pyodbc
from decimal import Decimal
from pathlib import Path

# CONFIGURACION DE RUTAS
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

print("=== DATASTORE - VERIFICACION DE DUPLICADOS ===")

conexion = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=localhost\SQLEXPRESS;"
    "DATABASE=DataStoreDB;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;",
    timeout=10
)

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

            coincidencias = cursor.fetchone()[0]

            if coincidencias > 0:
                print(producto, "- YA EXISTE EN SQL SERVER")
            else:
                print(producto, "- NUEVA VENTA")

    cursor.close()

finally:
    conexion.close()

print("\nVERIFICACION FINALIZADA")
