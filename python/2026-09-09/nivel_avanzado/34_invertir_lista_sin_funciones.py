def invertir_lista(lista):
    # sin reversed(), slicing [::-1] ni list.reverse()
    invertida = []
    indice = len(lista) - 1
    while indice >= 0:
        invertida.append(lista[indice])
        indice -= 1
    return invertida


def leer_lista():
    entrada = input("Ingresa elementos separados por espacio: ").strip()
    return entrada.split()


def main():
    print("=== Inversión de lista sin funciones automáticas ===")
    lista = leer_lista()

    if not lista:
        print("Error: no se ingresó ningún elemento.")
        return

    invertida = invertir_lista(lista)
    print(f"Lista original: {lista}")
    print(f"Lista invertida: {invertida}")


main()
