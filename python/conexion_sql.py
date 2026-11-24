
import pyodbc

print("=== DATASTORE ANALYTICS ===")
print("Conectando Python con SQL Server...")

servidor = r"localhost\SQLEXPRESS"
base_datos = "DataStoreDB"

try:
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={servidor};"
        f"DATABASE={base_datos};"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;",
        timeout=10
    )

    print("CONEXION EXITOSA")

    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM dbo.Ventas")

    resultado = cursor.fetchone()

    print("Ventas registradas en SQL Server:", resultado[0])

    cursor.close()
    conexion.close()

    print("Conexion cerrada correctamente")

except pyodbc.Error as error:
    print("ERROR AL CONECTAR CON SQL SERVER")
    print(error)
