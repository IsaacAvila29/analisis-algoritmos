"""Compara dos palabras para determinar si son idénticas.

Se reporta tanto la comparación exacta como la que ignora mayúsculas.
"""


def main():
    print("=== Comparación de palabras ===")
    palabra1 = input("Ingresa la primera palabra: ").strip()
    palabra2 = input("Ingresa la segunda palabra: ").strip()

    if not palabra1 or not palabra2:
        print("Error: ambas palabras deben contener al menos un carácter.")
        return

    if palabra1 == palabra2:
        print("Las palabras son idénticas.")
    elif palabra1.casefold() == palabra2.casefold():
        print("Las palabras son iguales, salvo por mayúsculas/minúsculas.")
    else:
        print("Las palabras son diferentes.")


if __name__ == "__main__":
    main()
