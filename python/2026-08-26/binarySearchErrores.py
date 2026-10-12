"""Busqueda binaria con errores comunes (a proposito).

Cada funcion introduce UN solo error respecto a la version correcta
de `binarySearch.py`, para ver como falla:

1. Usar una lista sin ordenar.
2. Usar izquierda < derecha.
3. Asignar izquierda = medio.
4. Usar / en lugar de //.
"""

MAX_PASOS = 50  # Freno para que el error 3 no se quede en un ciclo infinito


def busqueda_binaria(lista: list[int], objetivo: int) -> int:
    """Version correcta (referencia)."""
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        if lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


# Error 1: el algoritmo esta bien, pero la lista NO esta ordenada.
# Al descartar mitades asume un orden que no existe, asi que puede
# tirar justo la mitad donde estaba el objetivo.
def error_lista_sin_ordenar(lista: list[int], objetivo: int) -> int:
    return busqueda_binaria(lista, objetivo)


# Error 2: `<` en lugar de `<=`.
# Cuando izquierda == derecha queda UN candidato por revisar,
# pero el ciclo termina antes de compararlo.
def error_menor_estricto(lista: list[int], objetivo: int) -> int:
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda < derecha:  # ERROR: deberia ser <=
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        if lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


# Error 3: `izquierda = medio` en lugar de `medio + 1`.
# Si izquierda y derecha son vecinos, medio == izquierda y el rango
# nunca se achica: ciclo infinito.
def error_izquierda_igual_medio(lista: list[int], objetivo: int) -> int:
    izquierda = 0
    derecha = len(lista) - 1
    pasos = 0

    while izquierda <= derecha:
        pasos += 1
        if pasos > MAX_PASOS:
            raise RuntimeError(
                f"ciclo infinito: izquierda={izquierda}, derecha={derecha} no cambian"
            )

        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        if lista[medio] < objetivo:
            izquierda = medio  # ERROR: deberia ser medio + 1
        else:
            derecha = medio - 1

    return -1


# Error 4: `/` en lugar de `//`.
# En Python 3, `/` siempre devuelve float (7 / 2 = 3.5) y una lista
# no se puede indexar con float -> TypeError.
def error_division_flotante(lista: list[int], objetivo: int) -> int:
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) / 2  # ERROR: deberia ser //

        if lista[medio] == objetivo:
            return medio
        if lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


def probar(nombre: str, funcion, lista: list[int], objetivo: int) -> None:
    print(f"{nombre}")
    print(f"  Buscando {objetivo} en {lista}")
    try:
        indice = funcion(lista, objetivo)
        if indice == -1:
            print(f"  Resultado: {objetivo} no esta en la lista")
        else:
            print(f"  Resultado: {objetivo} encontrado en el indice {indice}")
    except Exception as e:
        print(f"  Fallo con {type(e).__name__}: {e}")
    print(f"  Esperado:  indice {lista.index(objetivo)}\n")


def main() -> None:
    ordenada = [1, 2, 3, 4, 5, 6, 7, 8]
    desordenada = [7, 3, 8, 1, 6, 2, 5, 4]

    probar("1. Lista sin ordenar", error_lista_sin_ordenar, desordenada, 7)
    probar("2. izquierda < derecha", error_menor_estricto, ordenada, 8)
    probar("3. izquierda = medio", error_izquierda_igual_medio, ordenada, 8)
    probar("4. / en lugar de //", error_division_flotante, ordenada, 6)


if __name__ == "__main__":
    main()
