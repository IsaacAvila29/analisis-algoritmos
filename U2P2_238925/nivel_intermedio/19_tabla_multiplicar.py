"""Genera la tabla de multiplicar de un número (del 1 al 10 por defecto).

Complejidad: O(k) en tiempo y espacio, donde k es el límite de la tabla.
"""


def generar_tabla(numero, limite=10):
    """Retorna tuplas (multiplicador, producto) desde 1 hasta `limite`."""
    return [(i, numero * i) for i in range(1, limite + 1)]


def main():
    print("=== Tabla de multiplicar ===")
    try:
        numero = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    for multiplicador, producto in generar_tabla(numero):
        print(f"{numero} x {multiplicador:>2} = {producto}")


if __name__ == "__main__":
    main()
