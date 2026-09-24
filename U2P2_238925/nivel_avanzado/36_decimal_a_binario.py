"""Convierte un número entero decimal a su representación en binario.

Se aplican divisiones sucesivas entre 2 y se leen los residuos en orden
inverso, sin usar la función integrada bin(). Los negativos se representan
con signo.

Complejidad: O(log n) en tiempo y espacio.
"""


def decimal_a_binario(numero):
    """Retorna la cadena binaria de `numero` (10 -> '1010', -5 -> '-101')."""
    if numero == 0:
        return "0"

    signo = "-" if numero < 0 else ""
    numero = abs(numero)

    bits = []
    while numero > 0:
        bits.append(str(numero % 2))
        numero //= 2
    return signo + "".join(reversed(bits))


def main():
    print("=== Conversión de decimal a binario ===")
    try:
        numero = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    print(f"{numero} en binario es {decimal_a_binario(numero)}")


if __name__ == "__main__":
    main()
