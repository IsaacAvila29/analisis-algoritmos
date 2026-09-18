def es_perfecto(numero):
    if numero <= 0:
        return False

    # un número perfecto es igual a la suma de sus divisores propios (ej. 28 = 1+2+4+7+14)
    suma_divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor

    return suma_divisores == numero


def main():
    print("=== Determinación de número perfecto ===")
    try:
        numero = int(input("Ingresa un número entero positivo: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if numero <= 0:
        print("Error: el número debe ser positivo.")
        return

    if es_perfecto(numero):
        print(f"El número {numero} ES perfecto.")
    else:
        print(f"El número {numero} NO es perfecto.")


main()
