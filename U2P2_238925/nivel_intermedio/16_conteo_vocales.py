"""Cuenta el total de vocales presentes en una frase.

Complejidad: O(n) en tiempo, donde n es la longitud de la frase;
O(1) en espacio.
"""

VOCALES = frozenset("aeiouáéíóúü")


def contar_vocales(frase):
    """Retorna el número de vocales (con o sin acento) de `frase`."""
    total = 0
    for caracter in frase.lower():
        if caracter in VOCALES:
            total += 1
    return total


def main():
    print("=== Conteo de vocales en una frase ===")
    frase = input("Ingresa una frase: ").strip()

    if not frase:
        print("Error: la frase no puede estar vacía.")
        return

    print(f"La frase contiene {contar_vocales(frase)} vocal(es).")


if __name__ == "__main__":
    main()
