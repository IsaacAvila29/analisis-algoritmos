def leer_lista():
    entrada = input("Ingresa elementos separados por espacio: ").strip()
    return entrada.split()


def main():
    print("=== Impresión de elementos de una lista ===")
    lista = leer_lista()

    if not lista:
        print("Error: no se ingresó ningún elemento.")
        return

    print("Elementos de la lista:")
    for elemento in lista:
        print(f"- {elemento}")


main()
