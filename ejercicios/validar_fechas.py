
from datetime import datetime

fechas = [
    "2026-11-20",
    "2026-11-21",
    "2026-15-40",
    "2026-02-30",
    "error"
]

print("VALIDACION DE FECHAS")

for fecha in fechas:
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        print(fecha, "- ACEPTADA")

    except ValueError:
        print(fecha, "- RECHAZADA: fecha no valida")
