def es_par(numero):
    return numero % 2 == 0


def main():
    print("=== Evaluación de paridad de un número ===")
    try:
        numero = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if es_par(numero):
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")


main()
