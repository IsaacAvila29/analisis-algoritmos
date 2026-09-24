"""Convierte grados Celsius a Fahrenheit: F = C * 9/5 + 32."""

import math

CERO_ABSOLUTO_C = -273.15


def celsius_a_fahrenheit(celsius):
    """Retorna la temperatura `celsius` expresada en grados Fahrenheit."""
    return celsius * 9 / 5 + 32


def main():
    print("=== Conversión de Celsius a Fahrenheit ===")
    try:
        celsius = float(input("Ingresa la temperatura en °C: "))
    except ValueError:
        print("Error: debes ingresar un número válido.")
        return

    if not math.isfinite(celsius):
        print("Error: la temperatura debe ser un número finito.")
        return

    if celsius < CERO_ABSOLUTO_C:
        print("Error: la temperatura no puede ser menor al cero absoluto "
              f"({CERO_ABSOLUTO_C} °C).")
        return

    print(f"{celsius:g} °C = {celsius_a_fahrenheit(celsius):.2f} °F")


if __name__ == "__main__":
    main()
