"""Calcula el Máximo Común Divisor (MCD) de dos enteros con Euclides.

mcd(a, b) = mcd(b, a mod b), con caso base mcd(a, 0) = |a|.
Por convención mcd(0, 0) no está definido.

Complejidad: O(log(min(a, b))) en tiempo, O(1) en espacio.
"""


def mcd(a, b):
    """Retorna el MCD de `a` y `b`; lanza ValueError si ambos son cero."""
    if a == 0 and b == 0:
        raise ValueError("el MCD de 0 y 0 no está definido")
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def main():
    print("=== Máximo Común Divisor (algoritmo de Euclides) ===")
    try:
        a = int(input("Ingresa el primer número entero: "))
        b = int(input("Ingresa el segundo número entero: "))
    except ValueError:
        print("Error: debes ingresar números enteros válidos.")
        return

    try:
        resultado = mcd(a, b)
    except ValueError as error:
        print(f"Error: {error}.")
        return

    print(f"MCD({a}, {b}) = {resultado}")


if __name__ == "__main__":
    main()
