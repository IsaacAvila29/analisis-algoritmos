def sumar_lista(lista):
    total = 0
    for numero in lista:
        total += numero
    return total


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
    print("=== Suma manual de los elementos de una lista ===")
    lista = leer_lista()

    if not lista:
        print("Error: no se ingresó ningún número válido.")
        return

    print(f"Lista: {lista}")
    print(f"La suma total es: {sumar_lista(lista)}")


main()
