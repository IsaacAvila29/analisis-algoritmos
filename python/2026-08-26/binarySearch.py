"""Busqueda binaria sobre una lista ordenada.

Complejidad: O(log n) en tiempo, O(1) en espacio.
Precondicion: `lista` debe estar ordenada de forma ascendente.
"""


def busqueda_binaria(lista: list[int], objetivo: int, traza: bool = False) -> int:
    """Devuelve el indice de `objetivo` en `lista`, o -1 si no existe.

    Con traza=True imprime cada paso (util para ver como se parte el rango).
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if traza:
            print(f"  izquierda={izquierda} derecha={derecha} medio={medio} valor={lista[medio]}")

        if lista[medio] == objetivo:
            return medio
        if lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


def main() -> None:
    datos = [1, 2, 3, 4, 5, 6, 7, 8]

    for objetivo in (6, 9):
        print(f"Buscando {objetivo} en {datos}")
        indice = busqueda_binaria(datos, objetivo, traza=True)

        if indice == -1:
            print(f"  {objetivo} no esta en la lista\n")
        else:
            print(f"  {objetivo} encontrado en el indice {indice}\n")


if __name__ == "__main__":
    main()
