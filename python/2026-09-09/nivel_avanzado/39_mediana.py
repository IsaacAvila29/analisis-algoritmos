def ordenar_ascendente(lista):
    ordenada = lista.copy()
    n = len(ordenada)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if ordenada[j] > ordenada[j + 1]:
                ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]

    return ordenada


def calcular_mediana(lista):
    ordenada = ordenar_ascendente(lista)
    n = len(ordenada)
    mitad = n // 2

    if n % 2 == 0:
        return (ordenada[mitad - 1] + ordenada[mitad]) / 2
    else:
        return ordenada[mitad]


def leer_lista():
    entrada = input("Ingresa números separados por espacio: ").strip()
    valores = entrada.split()

    lista = []
    for valor in valores:
        try:
            lista.append(float(valor))
        except ValueError:
            print(f"Aviso: '{valor}' no es un número válido y será ignorado.")
    return lista


def main():
    print("=== Cálculo de la mediana ===")
    lista = leer_lista()

    if not lista:
        print("Error: no se ingresó ningún número válido.")
        return

    mediana = calcular_mediana(lista)
    print(f"Lista: {lista}")
    print(f"La mediana es: {mediana}")


main()
