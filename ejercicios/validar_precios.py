
# Laboratorio 7: Validacion de precios

precios = ["2500", "-80", "0", "150.50", "error"]

print("VALIDACION DE PRECIOS")

for precio in precios:
    try:
        precio_numero = float(precio)

        if precio_numero <= 0:
            print(precio, "- RECHAZADO: precio no valido")
        else:
            print(precio, "- ACEPTADO")

    except ValueError:
        print(precio, "- RECHAZADO: precio no numerico")
