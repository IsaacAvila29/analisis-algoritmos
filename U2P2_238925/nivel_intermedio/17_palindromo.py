"""Determina si una palabra (o frase) es un palíndromo.

Se ignoran mayúsculas, espacios, signos de puntuación y acentos, de modo que
"Anita lava la tina" y "Oso" se reconocen como palíndromos.

Complejidad: O(n) en tiempo y espacio.
"""

import unicodedata


def normalizar(texto):
    """Retorna `texto` en minúsculas, sin acentos y solo alfanumérico."""
    descompuesto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in descompuesto if c.isalnum())


def es_palindromo(texto):
    """Retorna True si `texto` se lee igual al derecho y al revés."""
    limpio = normalizar(texto)
    izquierda, derecha = 0, len(limpio) - 1
    while izquierda < derecha:
        if limpio[izquierda] != limpio[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True


def main():
    print("=== Verificación de palíndromo ===")
    texto = input("Ingresa una palabra o frase: ").strip()

    if not normalizar(texto):
        print("Error: el texto debe contener al menos una letra o dígito.")
        return

    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo.")
    else:
        print(f"'{texto}' NO es un palíndromo.")


if __name__ == "__main__":
    main()
