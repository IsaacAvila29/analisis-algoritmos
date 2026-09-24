"""Verifica si dos palabras (o frases) son anagramas.

Se ignoran mayúsculas, espacios, signos y acentos. Se comparan las frecuencias
de cada letra con un diccionario en lugar de ordenar.

Complejidad: O(n + m) en tiempo, O(k) en espacio (k = letras distintas).
"""

import unicodedata


def normalizar(texto):
    """Retorna `texto` en minúsculas, sin acentos y solo alfanumérico."""
    descompuesto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in descompuesto if c.isalnum())


def contar_caracteres(texto):
    """Retorna un diccionario {caracter: frecuencia} de `texto`."""
    frecuencias = {}
    for caracter in texto:
        frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    return frecuencias


def son_anagramas(texto1, texto2):
    """Retorna True si ambos textos tienen exactamente las mismas letras."""
    limpio1, limpio2 = normalizar(texto1), normalizar(texto2)
    if len(limpio1) != len(limpio2):
        return False
    return contar_caracteres(limpio1) == contar_caracteres(limpio2)


def main():
    print("=== Verificación de anagramas ===")
    texto1 = input("Ingresa la primera palabra: ").strip()
    texto2 = input("Ingresa la segunda palabra: ").strip()

    if not normalizar(texto1) or not normalizar(texto2):
        print("Error: ambas entradas deben tener al menos una letra o dígito.")
        return

    if son_anagramas(texto1, texto2):
        print(f"'{texto1}' y '{texto2}' son anagramas.")
    else:
        print(f"'{texto1}' y '{texto2}' NO son anagramas.")


if __name__ == "__main__":
    main()
