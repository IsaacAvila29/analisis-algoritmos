"""Determina si un número entero es primo.

Se prueban solo divisores impares hasta la raíz cuadrada del número.

Complejidad: O(sqrt(n)) en tiempo, O(1) en espacio.
"""


def es_primo(numero):
    """Retorna True si `numero` es primo; los menores que 2 no lo son."""
    if numero < 2:
        return False
    if numero < 4:
        return True
    if numero % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True


def main():
    print("=== Verificación de número primo ===")
    try:
        numero = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if es_primo(numero):
        print(f"{numero} es primo.")
    else:
        print(f"{numero} NO es primo.")


if __name__ == "__main__":
    main()
