"""Cuenta la frecuencia de aparición de cada palabra de un texto (diccionario).

Las palabras se normalizan a minúsculas y sin signos de puntuación en los
extremos, para que "Hola," y "hola" cuenten como la misma palabra.

Complejidad: O(n) en tiempo para contar, O(k log k) para ordenar el reporte.
"""

import string

SIGNOS = string.punctuation + "¿¡«»"


def contar_frecuencias(texto):
    """Retorna un diccionario {palabra: número de apariciones} de `texto`."""
    frecuencias = {}
    for palabra in texto.lower().split():
        palabra = palabra.strip(SIGNOS)
        if palabra:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def ordenar_por_frecuencia(frecuencias):
    """Retorna pares (palabra, frecuencia) de mayor a menor frecuencia.

    Los empates se ordenan alfabéticamente.
    """
    return sorted(frecuencias.items(), key=lambda par: (-par[1], par[0]))


def main():
    print("=== Frecuencia de palabras ===")
    texto = input("Ingresa un texto: ")

    frecuencias = contar_frecuencias(texto)
    if not frecuencias:
        print("Error: el texto no contiene palabras.")
        return

    ancho = max(len(palabra) for palabra in frecuencias)
    print(f"Palabras distintas: {len(frecuencias)}")
    for palabra, cantidad in ordenar_por_frecuencia(frecuencias):
        print(f"  {palabra:<{ancho}} : {cantidad}")


if __name__ == "__main__":
    main()
