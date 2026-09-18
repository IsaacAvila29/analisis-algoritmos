def encontrar_mayor(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor


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
    print("=== Número mayor de una lista ===")
    lista = leer_lista()

    if not lista:
        print("Error: no se ingresó ningún número válido.")
        return

    print(f"Lista: {lista}")
    print(f"El número mayor es: {encontrar_mayor(lista)}")


main()
