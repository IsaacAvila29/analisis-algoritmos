def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)


def main():
    print("=== Conteo de palabras en una frase ===")
    frase = input("Ingresa una frase: ").strip()

    if not frase:
        print("Error: la frase no puede estar vacía.")
        return

    total = contar_palabras(frase)
    print(f"La frase contiene {total} palabra(s).")


main()
