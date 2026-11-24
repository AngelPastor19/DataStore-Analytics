# Proyecto DataStore Analytics
# Laboratorio 5: Python


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


empresa = "DataStore Perú"
ingresos_dia_1 = 8150
ingresos_dia_2 = 5240

ingresos_totales = ingresos_dia_1 + ingresos_dia_2

print("Empresa:", empresa)
print("Ingresos totales: S/", ingresos_totales)



# Actividad 2: Análisis de productos

productos = [
    "Laptop Lenovo",
    "Mouse Logitech",
    "Teclado Redragon",
    "Monitor Samsung",
    "Audífonos Sony"
]

cantidades = [2, 5, 3, 2, 4]
precios = [2500, 80, 150, 750, 200]

print("\nREPORTE DE VENTAS POR PRODUCTO")

for i in range(len(productos)):
    total = cantidades[i] * precios[i]
    print(productos[i], "- S/", total)



# Actividad 3: Leer un archivo CSV


# Actividad 3: Leer un archivo CSV

import csv


print("\nVENTAS LEIDAS DESDE CSV")

ingresos_csv = 0
numero_ventas = 0

with open(DATA_DIR / "ventas.csv", mode="r", encoding="utf-8-sig") as archivo:

    lector = csv.DictReader(archivo)

    for venta in lector:
        producto = venta["Producto"]
        cantidad = int(venta["Cantidad"])
        precio = float(venta["PrecioUnitario"])

        total = cantidad * precio

        ingresos_csv += total
        numero_ventas += 1

        print(producto, "- S/", total)

print("\nRESUMEN AUTOMATICO")
print("Numero de ventas:", numero_ventas)
print("Ingresos calculados desde CSV: S/", ingresos_csv)

