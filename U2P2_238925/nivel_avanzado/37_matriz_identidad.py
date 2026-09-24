"""Genera una matriz identidad de tamaño N x N.

Cada fila se crea de forma independiente para evitar el error clásico de
[[0] * n] * n, donde todas las filas comparten la misma referencia.

Complejidad: O(n^2) en tiempo y espacio.
"""

TAMANIO_MAXIMO = 20


def matriz_identidad(n):
    """Retorna la matriz identidad de orden `n` como lista de listas."""
    if n < 1:
        raise ValueError("el tamaño debe ser un entero positivo")
    return [[1 if fila == columna else 0 for columna in range(n)]
            for fila in range(n)]


def imprimir_matriz(matriz):
    """Imprime la matriz con columnas alineadas."""
    for fila in matriz:
        print(" ".join(str(valor) for valor in fila))


def main():
    print("=== Matriz identidad N x N ===")
    try:
        n = int(input(f"Ingresa el tamaño N (1-{TAMANIO_MAXIMO}): "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if not 1 <= n <= TAMANIO_MAXIMO:
        print(f"Error: N debe estar entre 1 y {TAMANIO_MAXIMO}.")
        return

    imprimir_matriz(matriz_identidad(n))


if __name__ == "__main__":
    main()
