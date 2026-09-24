"""Calcula el número de días restantes para finalizar el año.

Se puede usar la fecha actual o ingresar una fecha en formato AAAA-MM-DD.
El cálculo no cuenta el día de la fecha dada (el 31 de diciembre devuelve 0).
"""

from datetime import date


def dias_restantes(fecha):
    """Retorna los días que faltan desde `fecha` hasta el 31 de diciembre."""
    fin_de_anio = date(fecha.year, 12, 31)
    return (fin_de_anio - fecha).days


def leer_fecha():
    """Retorna la fecha ingresada (hoy si se omite) o None si es inválida."""
    entrada = input(
        "Ingresa una fecha AAAA-MM-DD (Enter para usar hoy): ").strip()
    if not entrada:
        return date.today()
    try:
        return date.fromisoformat(entrada)
    except ValueError:
        return None


def main():
    print("=== Días restantes para terminar el año ===")
    fecha = leer_fecha()

    if fecha is None:
        print("Error: la fecha no es válida (usa el formato AAAA-MM-DD).")
        return

    print(f"Desde el {fecha.isoformat()} faltan {dias_restantes(fecha)} "
          "día(s) para terminar el año.")


if __name__ == "__main__":
    main()
