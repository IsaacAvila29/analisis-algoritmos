"""Calcula el área de un círculo a partir de su radio: A = pi * r^2."""

import math


def area_circulo(radio):
    """Retorna el área del círculo; lanza ValueError si `radio` es negativo."""
    if radio < 0:
        raise ValueError("el radio no puede ser negativo")
    return math.pi * radio ** 2


def main():
    print("=== Área de un círculo ===")
    try:
        radio = float(input("Ingresa el radio: "))
        if not math.isfinite(radio):
            raise ValueError("el radio debe ser un número finito")
        area = area_circulo(radio)
    except ValueError as error:
        print(f"Error: {error}.")
        return

    print(f"El área de un círculo de radio {radio:g} es {area:.4f}")


if __name__ == "__main__":
    main()
