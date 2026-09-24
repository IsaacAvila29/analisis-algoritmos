"""Filtra, dentro de una lista, las palabras con más de 5 caracteres.

La lista original no se modifica: se construye una nueva.

Complejidad: O(n) en tiempo y espacio, donde n es el número de palabras.
"""


def filtrar_palabras_largas(palabras, longitud_minima=5):
    """Retorna una nueva lista con las palabras más largas que el mínimo."""
    return [palabra for palabra in palabras if len(palabra) > longitud_minima]


def leer_palabras():
    """Lee palabras separadas por espacios o comas y retorna la lista."""
    entrada = input("Ingresa palabras separadas por espacio o coma: ")
    return entrada.replace(",", " ").split()


def main():
    print("=== Filtrado de palabras con más de 5 caracteres ===")
    palabras = leer_palabras()

    if not palabras:
        print("Error: no se ingresó ninguna palabra.")
        return

    largas = filtrar_palabras_largas(palabras)
    print(f"Lista original: {palabras}")
    if largas:
        print(f"Palabras con más de 5 caracteres: {largas}")
    else:
        print("Ninguna palabra tiene más de 5 caracteres.")


if __name__ == "__main__":
    main()
