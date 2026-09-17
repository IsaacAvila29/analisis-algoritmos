def encontrar_menor(lista):
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor


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
    print("=== Número menor de una lista ===")
    lista = leer_lista()

    if not lista:
        print("Error: no se ingresó ningún número válido.")
        return

    print(f"Lista: {lista}")
    print(f"El número menor es: {encontrar_menor(lista)}")


main()
