"""Calcula base^exponente mediante recursión (exponenciación rápida).

Recurrencia:
    b^0 = 1                          (caso base)
    b^e = (b^(e/2))^2                si e es par
    b^e = b * b^(e-1)                si e es impar
    b^-e = 1 / b^e                   para exponentes negativos

Complejidad: O(log e) en tiempo y en profundidad de pila.
"""

import math

# Evita cálculos muy costosos y enteros con más dígitos de los que
# Python permite imprimir
MAX_EXPONENTE = 1000


def potencia(base, exponente):
    """Retorna `base` elevado al entero `exponente`.

    Lanza ZeroDivisionError si la base es 0 y el exponente es negativo.
    """
    if exponente < 0:
        if base == 0:
            raise ZeroDivisionError(
                "0 no puede elevarse a un exponente negativo")
        return 1 / potencia(base, -exponente)
    if exponente == 0:
        return 1
    if exponente % 2 == 0:
        mitad = potencia(base, exponente // 2)
        return mitad * mitad
    return base * potencia(base, exponente - 1)


def convertir_base(texto):
    """Convierte `texto` a int si representa un entero y a float si no.

    Lanza ValueError si el texto no es numérico o no es finito.
    """
    try:
        return int(texto)
    except ValueError:
        numero = float(texto)
    if not math.isfinite(numero):
        raise ValueError("la base debe ser un número finito")
    return numero


def main():
    print("=== Potencia mediante recursión ===")
    try:
        base = convertir_base(input("Ingresa la base: ").strip())
        exponente = int(input("Ingresa el exponente (entero): "))
    except ValueError:
        print("Error: la base debe ser numérica y el exponente un entero.")
        return

    if abs(exponente) > MAX_EXPONENTE:
        print(f"Error: el exponente debe estar entre -{MAX_EXPONENTE} "
              f"y {MAX_EXPONENTE}.")
        return

    try:
        resultado = potencia(base, exponente)
    except ZeroDivisionError as error:
        print(f"Error: {error}.")
        return
    except OverflowError:
        print("Error: el resultado es demasiado grande para representarse.")
        return

    if isinstance(resultado, float) and math.isinf(resultado):
        print("Error: el resultado es demasiado grande para representarse.")
        return

    print(f"{base} ^ {exponente} = {resultado}")


if __name__ == "__main__":
    main()
