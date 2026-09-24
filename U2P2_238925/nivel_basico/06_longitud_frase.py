"""Calcula la longitud (número de caracteres) de una frase."""


def main():
    print("=== Longitud de una frase ===")
    frase = input("Ingresa una frase: ").strip()

    if not frase:
        print("Error: la frase no puede estar vacía.")
        return

    sin_espacios = len(frase.replace(" ", ""))
    print(f"La frase tiene {len(frase)} carácter(es) "
          f"({sin_espacios} sin contar espacios).")


if __name__ == "__main__":
    main()
