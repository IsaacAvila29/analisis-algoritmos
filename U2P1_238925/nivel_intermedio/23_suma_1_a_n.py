def sumar_hasta_n(n):
    total = 0
    for numero in range(1, n + 1):
        total += numero
    return total


def main():
    print("=== Suma de enteros desde 1 hasta N ===")
    try:
        n = int(input("Ingresa el valor de N: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if n < 1:
        print("Error: N debe ser un número entero positivo.")
        return

    print(f"La suma de 1 hasta {n} es: {sumar_hasta_n(n)}")


main()
