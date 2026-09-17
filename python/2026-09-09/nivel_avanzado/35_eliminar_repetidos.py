def eliminar_duplicados(lista):
    sin_duplicados = []
    for elemento in lista:
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)
    return sin_duplicados


def leer_lista():
    entrada = input("Ingresa elementos separados por espacio: ").strip()
    return entrada.split()


def main():
    print("=== Eliminación de elementos repetidos ===")
    lista = leer_lista()

    if not lista:
        print("Error: no se ingresó ningún elemento.")
        return

    resultado = eliminar_duplicados(lista)
    print(f"Lista original: {lista}")
    print(f"Lista sin duplicados: {resultado}")


main()
