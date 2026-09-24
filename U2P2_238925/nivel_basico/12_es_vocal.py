"""Verifica si un carácter ingresado es una vocal (incluye acentuadas y ü)."""

VOCALES = "aeiouáéíóúü"


def main():
    print("=== Verificación de vocal ===")
    caracter = input("Ingresa un solo carácter: ").strip()

    if len(caracter) != 1:
        print("Error: debes ingresar exactamente un carácter.")
        return

    if not caracter.isalpha():
        print(f"'{caracter}' no es una letra, por lo tanto no es vocal.")
    elif caracter.lower() in VOCALES:
        print(f"'{caracter}' es una vocal.")
    else:
        print(f"'{caracter}' es una consonante.")


if __name__ == "__main__":
    main()
