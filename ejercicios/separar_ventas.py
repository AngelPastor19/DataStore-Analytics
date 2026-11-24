import csv

print("PROCESO DE SEPARACION DE VENTAS")

ventas_validas = []
ventas_rechazadas = []

# 1. Leer los datos originales
with open("ventas_pruebas.csv", "r", encoding="utf-8-sig") as archivo:
    lector = csv.DictReader(archivo)

    for venta in lector:
        try:
            cantidad = int(venta["Cantidad"])

            if cantidad > 0:
                ventas_validas.append(venta)
            else:
                venta["MotivoRechazo"] = "Cantidad menor o igual a cero"
                ventas_rechazadas.append(venta)

        except ValueError:
            venta["MotivoRechazo"] = "Cantidad no numerica"
            ventas_rechazadas.append(venta)

# 2. Guardar las ventas validas
with open("ventas_validas.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    columnas = ["Fecha", "Producto", "Cantidad", "PrecioUnitario"]
    escritor = csv.DictWriter(archivo, fieldnames=columnas)

    escritor.writeheader()
    escritor.writerows(ventas_validas)

# 3. Guardar las ventas rechazadas
with open("ventas_rechazadas.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    columnas = ["Fecha", "Producto", "Cantidad", "PrecioUnitario", "MotivoRechazo"]
    escritor = csv.DictWriter(archivo, fieldnames=columnas)

    escritor.writeheader()
    escritor.writerows(ventas_rechazadas)

print("\nPROCESO FINALIZADO")
print("Ventas validas:", len(ventas_validas))
print("Ventas rechazadas:", len(ventas_rechazadas))
