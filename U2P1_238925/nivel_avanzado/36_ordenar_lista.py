def ordenar_ascendente(lista):
    # bubble sort
    ordenada = lista.copy()
    n = len(ordenada)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if ordenada[j] > ordenada[j + 1]:
                ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]

    return ordenada


def leer_lista():
    entrada = input("Ingresa números enteros separados por espacio: ").strip()
    valores = entrada.split()

    lista = []
    for valor in valores:
        try:
            lista.append(int(valor))
        except ValueError:
            print(f"Aviso: '{valor}' no es un entero válido y será ignorado.")
    return lista


def main():
    print("=== Ordenamiento de lista de menor a mayor ===")
    lista = leer_lista()

    if not lista:
        print("Error: no se ingresó ningún número válido.")
        return

    ordenada = ordenar_ascendente(lista)
    print(f"Lista original: {lista}")
    print(f"Lista ordenada: {ordenada}")


main()
