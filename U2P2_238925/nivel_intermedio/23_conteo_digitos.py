"""Cuenta el total de dígitos presentes en un número entero.

Se usa división entera sucesiva entre 10. El signo no cuenta como dígito
y el número 0 tiene un dígito.

Complejidad: O(d) en tiempo, donde d es el número de dígitos; O(1) en espacio.
"""


def contar_digitos(numero):
    """Retorna la cantidad de dígitos del entero `numero`."""
    numero = abs(numero)
    if numero == 0:
        return 1

    total = 0
    while numero > 0:
        numero //= 10
        total += 1
    return total


def main():
    print("=== Conteo de dígitos de un número ===")
    try:
        numero = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    print(f"{numero} tiene {contar_digitos(numero)} dígito(s).")


if __name__ == "__main__":
    main()
