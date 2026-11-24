
# Laboratorio 6: Validacion de cantidades

cantidad = "-5"

try:
    cantidad_numero = int(cantidad)

    if cantidad_numero <= 0:
        print("ERROR: La cantidad debe ser mayor que cero")
    else:
        print("Cantidad valida:", cantidad_numero)

except ValueError:
    print("ERROR: La cantidad debe ser un numero entero")


# Actividad 3: Validar multiples cantidades

cantidades = ["5", "-3", "0", "8", "error", "12"]

print("\nVALIDACION DE CANTIDADES")

for cantidad in cantidades:
    try:
        cantidad_numero = int(cantidad)

        if cantidad_numero <= 0:
            print(cantidad, "- RECHAZADO: cantidad no valida")
        else:
            print(cantidad, "- ACEPTADO")

    except ValueError:
        print(cantidad, "- RECHAZADO: no es un numero entero")
