"""Reemplaza las vocales de una frase por asteriscos.

Complejidad: O(n) en tiempo y espacio.
"""

VOCALES = frozenset("aeiouáéíóúü")


def ocultar_vocales(frase, simbolo="*"):
    """Retorna una copia de `frase` con cada vocal sustituida por `simbolo`."""
    return "".join(simbolo if c.lower() in VOCALES else c for c in frase)


def main():
    print("=== Reemplazo de vocales por asteriscos ===")
    frase = input("Ingresa una frase: ").strip()

    if not frase:
        print("Error: la frase no puede estar vacía.")
        return

    print(f"Resultado: {ocultar_vocales(frase)}")


if __name__ == "__main__":
    main()
