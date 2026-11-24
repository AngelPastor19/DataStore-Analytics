
import csv
from datetime import datetime

ventas_validas = 0
ventas_rechazadas = 0

print("VALIDACION INTEGRAL DESDE CSV")

with open("ventas_pruebas.csv", "r", encoding="utf-8-sig") as archivo:
    lector = csv.DictReader(archivo)

    for venta in lector:
        producto = venta["Producto"]

        try:
            datetime.strptime(venta["Fecha"], "%Y-%m-%d")
            cantidad = int(venta["Cantidad"])
            precio = float(venta["PrecioUnitario"])

            if cantidad <= 0:
                print(producto, "- RECHAZADO: cantidad invalida")
                ventas_rechazadas += 1

            elif precio <= 0:
                print(producto, "- RECHAZADO: precio invalido")
                ventas_rechazadas += 1

            else:
                print(producto, "- ACEPTADO")
                ventas_validas += 1

        except ValueError:
            print(producto, "- RECHAZADO: fecha o numero incorrecto")
            ventas_rechazadas += 1

print("\nRESUMEN FINAL")
print("Ventas validas:", ventas_validas)
print("Ventas rechazadas:", ventas_rechazadas)
