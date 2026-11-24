
import csv

print("VALIDACION DE VENTAS DESDE CSV")

ventas_validas = 0
ventas_invalidas = 0

with open("ventas_pruebas.csv", mode="r", encoding="utf-8-sig") as archivo:

    lector = csv.DictReader(archivo)

    for venta in lector:
        producto = venta["Producto"]

        try:
            cantidad = int(venta["Cantidad"])

            if cantidad <= 0:
                print(producto, "- RECHAZADO: cantidad no valida")
                ventas_invalidas += 1
            else:
                print(producto, "- ACEPTADO")
                ventas_validas += 1

        except ValueError:
            print(producto, "- RECHAZADO: cantidad no numerica")
            ventas_invalidas += 1

print("\nRESUMEN DE VALIDACION")
print("Ventas validas:", ventas_validas)
print("Ventas invalidas:", ventas_invalidas)
