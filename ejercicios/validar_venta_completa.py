
# Laboratorio 7: Validacion de una venta


producto = "Laptop Lenovo"
cantidad = "2"
precio = "-80"


print("VALIDACION DE VENTA")

try:
    cantidad_numero = int(cantidad)
    precio_numero = float(precio)

    if cantidad_numero <= 0:
        print("RECHAZADO: cantidad no valida")

    elif precio_numero <= 0:
        print("RECHAZADO: precio no valido")

    else:
        total = cantidad_numero * precio_numero
        print("Producto:", producto)
        print("VENTA ACEPTADA")
        print("Total: S/", total)

except ValueError:
    print("RECHAZADO: cantidad o precio no numerico")
