"""Merge Sort iterativo (bottom-up) implementado a mano sobre 1,000,000 de datos.

Complejidad: O(n log n) en tiempo, O(n) en espacio extra.

Por que bottom-up: no usa recursion, asi que no hay riesgo de exceder el
limite de pila de Python, y cada "paso" queda muy claro: en cada pasada se
mezclan bloques ordenados de tamano `ancho` para formar bloques de 2*ancho.

Mostrar cada comparacion de un millon de datos imprimiria ~20 millones de
lineas, asi que con n grande se muestra cada PASADA (~20 pasadas). Con un
arreglo pequeno (--detalle) se muestra cada mezcla individual.

Uso:
    python mergeSortMillon.py              # 1,000,000 de datos, traza por pasada
    python mergeSortMillon.py 50000        # otra cantidad de datos
    python mergeSortMillon.py --detalle    # 16 datos, traza de cada mezcla
"""

import random
import sys
import time


def mezclar(origen: list[int], destino: list[int], ini: int, mitad: int, fin: int) -> None:
    """Mezcla origen[ini:mitad] y origen[mitad:fin] (ya ordenados) en destino[ini:fin]."""
    i, j, k = ini, mitad, ini

    while i < mitad and j < fin:
        if origen[i] <= origen[j]:
            destino[k] = origen[i]
            i += 1
        else:
            destino[k] = origen[j]
            j += 1
        k += 1

    while i < mitad:
        destino[k] = origen[i]
        i += 1
        k += 1

    while j < fin:
        destino[k] = origen[j]
        j += 1
        k += 1


def contar_tramos_ordenados(arr: list[int]) -> int:
    """Cuantos tramos ascendentes consecutivos hay (1 = totalmente ordenado)."""
    tramos = 1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            tramos += 1
    return tramos


def vista_previa(arr: list[int], cuantos: int = 10) -> str:
    if len(arr) <= cuantos * 2:
        return str(arr)
    inicio = ", ".join(map(str, arr[:cuantos]))
    final = ", ".join(map(str, arr[-cuantos:]))
    return f"[{inicio}, ..., {final}]"


def merge_sort(arr: list[int], detalle: bool = False) -> list[int]:
    n = len(arr)
    origen = arr[:]
    destino = [0] * n
    ancho = 1
    pasada = 0
    inicio_total = time.perf_counter()

    while ancho < n:
        pasada += 1
        inicio_pasada = time.perf_counter()

        if detalle:
            print(f"\n--- Pasada {pasada}: mezclando bloques de {ancho} -> bloques de {ancho * 2} ---")

        for ini in range(0, n, 2 * ancho):
            mitad = min(ini + ancho, n)
            fin = min(ini + 2 * ancho, n)
            mezclar(origen, destino, ini, mitad, fin)

            if detalle:
                izq = origen[ini:mitad]
                der = origen[mitad:fin]
                print(f"  {izq} + {der} -> {destino[ini:fin]}")

        # El destino de esta pasada es el origen de la siguiente.
        origen, destino = destino, origen
        ancho *= 2

        if detalle:
            print(f"  Estado: {origen}")
        else:
            duracion = time.perf_counter() - inicio_pasada
            tramos = contar_tramos_ordenados(origen)
            print(
                f"Pasada {pasada:>2} | bloques de {min(ancho, n):>9,} | "
                f"tramos ordenados: {tramos:>9,} | {duracion:6.2f}s | {vista_previa(origen, 5)}"
            )

    total = time.perf_counter() - inicio_total
    print(f"\nTotal: {pasada} pasadas en {total:.2f}s")
    return origen


def main() -> None:
    detalle = "--detalle" in sys.argv
    numeros = [a for a in sys.argv[1:] if a.isdigit()]
    n = 16 if detalle else int(numeros[0]) if numeros else 1_000_000

    print(f"Generando {n:,} datos aleatorios entre 0 y {n * 10:,}...")
    datos = [random.randint(0, n * 10) for _ in range(n)]
    print(f"Arreglo original: {vista_previa(datos)}")
    print(f"Tramos ordenados al inicio: {contar_tramos_ordenados(datos):,}\n")

    ordenado = merge_sort(datos, detalle=detalle)

    print(f"\nArreglo ordenado: {vista_previa(ordenado)}")
    correcto = ordenado == sorted(datos)
    print(f"Verificacion contra sorted(): {'CORRECTO' if correcto else 'ERROR'}")


if __name__ == "__main__":
    main()
