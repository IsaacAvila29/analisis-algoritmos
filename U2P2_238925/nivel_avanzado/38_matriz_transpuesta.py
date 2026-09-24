"""Calcula la matriz transpuesta de una matriz dada.

La transpuesta intercambia filas por columnas: T[j][i] = M[i][j]. Se construye
una matriz nueva, por lo que la original no se modifica.

Complejidad: O(filas * columnas) en tiempo y espacio.
"""


def es_rectangular(matriz):
    """Retorna True si la matriz no está vacía y sus filas miden lo mismo."""
    if not matriz or not matriz[0]:
        return False
    columnas = len(matriz[0])
    return all(len(fila) == columnas for fila in matriz)


def transponer(matriz):
    """Retorna la transpuesta de `matriz`; ValueError si no es rectangular."""
    if not es_rectangular(matriz):
        raise ValueError("la matriz debe ser rectangular y no estar vacía")
    filas, columnas = len(matriz), len(matriz[0])
    return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]


def convertir_numero(texto):
    """Convierte `texto` a int si es entero o a float en otro caso.

    Lanza ValueError si el texto no es numérico.
    """
    numero = float(texto)
    return int(numero) if numero.is_integer() else numero


def leer_matriz():
    """Lee la matriz fila por fila hasta recibir una línea vacía.

    Las filas con valores no numéricos se descartan con un aviso.
    """
    print("Ingresa cada fila con valores separados por espacio "
          "(línea vacía para terminar):")
    matriz = []
    while True:
        linea = input(f"Fila {len(matriz) + 1}: ").strip()
        if not linea:
            return matriz
        try:
            matriz.append([convertir_numero(valor) for valor in linea.split()])
        except ValueError:
            print("Aviso: la fila tiene valores no numéricos; se descartó.")


def imprimir_matriz(matriz):
    """Imprime la matriz con columnas alineadas a la derecha."""
    ancho = max(len(str(valor)) for fila in matriz for valor in fila)
    for fila in matriz:
        print(" ".join(f"{valor:>{ancho}}" for valor in fila))


def main():
    print("=== Matriz transpuesta ===")
    matriz = leer_matriz()

    try:
        transpuesta = transponer(matriz)
    except ValueError as error:
        print(f"Error: {error}.")
        return

    print(f"\nMatriz original ({len(matriz)}x{len(matriz[0])}):")
    imprimir_matriz(matriz)
    print(f"\nMatriz transpuesta ({len(transpuesta)}x{len(transpuesta[0])}):")
    imprimir_matriz(transpuesta)


if __name__ == "__main__":
    main()
