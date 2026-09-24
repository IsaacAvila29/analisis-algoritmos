"""Calcula la división entera (cociente sin decimales) entre dos enteros."""


def main():
    print("=== División entera ===")
    try:
        dividendo = int(input("Ingresa el dividendo (entero): "))
        divisor = int(input("Ingresa el divisor (entero): "))
    except ValueError:
        print("Error: debes ingresar números enteros válidos.")
        return

    if divisor == 0:
        print("Error: no se puede dividir entre cero.")
        return

    # '//' redondea hacia menos infinito: -7 // 2 == -4
    print(f"Resultado: {dividendo} // {divisor} = {dividendo // divisor}")


if __name__ == "__main__":
    main()
