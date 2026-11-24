
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

# DATASTORE ANALYTICS - PROCESO ETL

# CONFIGURACION DE RUTAS
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

archivo_entrada = DATA_DIR / "ventas_pruebas.csv"

ventas_validas = []
ventas_rechazadas = []

columnas = [
    "Fecha",
    "Producto",
    "Cantidad",
    "PrecioUnitario"
]

print("=== DATASTORE ANALYTICS - ETL ===")

# 1. EXTRACCION
with open(archivo_entrada, "r", encoding="utf-8-sig", newline="") as archivo:
    lector = csv.DictReader(archivo)

    if lector.fieldnames != columnas:
        raise ValueError("El CSV no tiene los encabezados esperados")

    for venta in lector:
        errores = []

        # 2. VALIDACION DE FECHA
        try:
            fecha = datetime.strptime(venta["Fecha"], "%Y-%m-%d")

            if fecha.strftime("%Y-%m-%d") != venta["Fecha"]:
                errores.append("Formato de fecha incorrecto")

        except (ValueError, TypeError):
            errores.append("Fecha invalida")

        # 3. VALIDACION DE PRODUCTO
        if not venta["Producto"] or not venta["Producto"].strip():
            errores.append("Producto vacio")

        # 4. VALIDACION DE CANTIDAD
        try:
            cantidad = int(venta["Cantidad"])

            if cantidad <= 0:
                errores.append("Cantidad no valida")

        except (ValueError, TypeError):
            errores.append("Cantidad no numerica")

        # 5. VALIDACION DE PRECIO
        try:
            precio = Decimal(venta["PrecioUnitario"])

            if not precio.is_finite() or precio <= 0:
                errores.append("Precio no valido")

        except (InvalidOperation, TypeError):
            errores.append("Precio no numerico")

        # 6. CLASIFICACION
        if errores:
            venta["MotivoRechazo"] = "; ".join(errores)
            ventas_rechazadas.append(venta)

        else:
            ventas_validas.append(venta)

# 7. EXPORTAR VENTAS VALIDAS
with open(DATA_DIR / "ventas_limpias.csv", "w", newline="", encoding="utf-8-sig") as archivo:

    escritor = csv.DictWriter(
        archivo,
        fieldnames=columnas
    )

    escritor.writeheader()
    escritor.writerows(ventas_validas)

# 8. EXPORTAR VENTAS RECHAZADAS
with open(DATA_DIR / "ventas_errores.csv", "w", newline="", encoding="utf-8-sig") as archivo:

    escritor = csv.DictWriter(
        archivo,
        fieldnames=columnas + ["MotivoRechazo"]
    )

    escritor.writeheader()
    escritor.writerows(ventas_rechazadas)

# 9. REPORTE FINAL
print("\nPROCESO ETL FINALIZADO")
print("Registros procesados:", len(ventas_validas) + len(ventas_rechazadas))
print("Ventas validas:", len(ventas_validas))
print("Ventas rechazadas:", len(ventas_rechazadas))
print("Archivos generados correctamente")
