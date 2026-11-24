
from datetime import datetime

venta = {
    "Fecha": "2026-11-20",
    "Producto": "Laptop Lenovo",
    "Cantidad": "2",
    "PrecioUnitario": "2500"
}

print("VALIDACION INTEGRAL DE VENTA")

try:
    fecha = datetime.strptime(venta["Fecha"], "%Y-%m-%d")
    cantidad = int(venta["Cantidad"])
    precio = float(venta["PrecioUnitario"])

    if cantidad <= 0:
        print("RECHAZADO: cantidad no valida")

    elif precio <= 0:
        print("RECHAZADO: precio no valido")

    else:
        total = cantidad * precio
        print("VENTA ACEPTADA")
        print("Producto:", venta["Producto"])
        print("Fecha:", fecha.date())
        print("Total: S/", total)

except ValueError:
    print("RECHAZADO: fecha, cantidad o precio incorrecto")
