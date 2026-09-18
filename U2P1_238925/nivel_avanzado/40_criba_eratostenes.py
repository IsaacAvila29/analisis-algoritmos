def criba_de_eratostenes(n):
    if n < 2:
        return []

    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False

    for numero in range(2, int(n ** 0.5) + 1):
        if es_primo[numero]:
            for multiplo in range(numero * numero, n + 1, numero):
                es_primo[multiplo] = False

    primos = []
    for numero in range(2, n + 1):
        if es_primo[numero]:
            primos.append(numero)

    return primos


def main():
    print("=== Criba de Eratóstenes ===")
    try:
        n = int(input("Ingresa el valor límite N: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if n < 2:
        print("Error: N debe ser mayor o igual a 2 para encontrar números primos.")
        return

    primos = criba_de_eratostenes(n)
    print(f"Números primos hasta {n}: {primos}")
    print(f"Cantidad de primos encontrados: {len(primos)}")


main()
