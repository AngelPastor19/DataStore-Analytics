
from datetime import datetime

venta = {
    "Fecha": "2026-02-30",
    "Producto": "Laptop Lenovo",
    "Cantidad": "2",
    "PrecioUnitario": "2500"
}

print("DIAGNOSTICO DE VENTA")

try:
    datetime.strptime(venta["Fecha"], "%Y-%m-%d")
    print("Fecha: CORRECTA")
except ValueError:
    print("Fecha: ERROR - fecha invalida")

try:
    cantidad = int(venta["Cantidad"])
    if cantidad > 0:
        print("Cantidad: CORRECTA")
    else:
        print("Cantidad: ERROR - debe ser mayor que cero")
except ValueError:
    print("Cantidad: ERROR - no es un entero")

try:
    precio = float(venta["PrecioUnitario"])
    if precio > 0:
        print("Precio: CORRECTO")
    else:
        print("Precio: ERROR - debe ser mayor que cero")
except ValueError:
    print("Precio: ERROR - no es numerico")
