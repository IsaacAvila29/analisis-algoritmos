def duplicar_valores(lista):
    resultado = []
    for numero in lista:
        resultado.append(numero * 2)
    return resultado


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
    print("=== Multiplicación por 2 de los valores de una lista ===")
    lista = leer_lista()

    if not lista:
        print("Error: no se ingresó ningún número válido.")
        return

    duplicados = duplicar_valores(lista)
    print(f"Lista original: {lista}")
    print(f"Lista duplicada: {duplicados}")


main()
