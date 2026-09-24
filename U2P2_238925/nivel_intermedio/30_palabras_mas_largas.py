"""Identifica la(s) palabra(s) de mayor longitud dentro de una frase.

Se ignoran los signos de puntuación y, en caso de empate, se retornan todas
las palabras de longitud máxima (sin repetir) en el orden en que aparecen.

Complejidad: O(n) en tiempo y espacio.
"""

import string

SIGNOS = string.punctuation + "¿¡«»"


def extraer_palabras(frase):
    """Retorna las palabras de `frase` sin signos de puntuación en extremos."""
    palabras = (palabra.strip(SIGNOS) for palabra in frase.split())
    return [palabra for palabra in palabras if palabra]


def palabras_mas_largas(frase):
    """Retorna (longitud_maxima, palabras); (0, []) si no hay palabras."""
    maxima = 0
    resultado = []
    for palabra in extraer_palabras(frase):
        longitud = len(palabra)
        if longitud > maxima:
            maxima = longitud
            resultado = [palabra]
        elif longitud == maxima and palabra not in resultado:
            resultado.append(palabra)
    return maxima, resultado


def main():
    print("=== Palabras más largas de una frase ===")
    frase = input("Ingresa una frase: ").strip()

    longitud, palabras = palabras_mas_largas(frase)
    if not palabras:
        print("Error: la frase no contiene palabras.")
        return

    print(f"Longitud máxima: {longitud} carácter(es).")
    print(f"Palabra(s) más larga(s): {', '.join(palabras)}")


if __name__ == "__main__":
    main()
