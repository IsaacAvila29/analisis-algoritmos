"""Obtiene el residuo de una división entera usando el operador módulo '%'."""


def main():
    print("=== Residuo de una división ===")
    try:
        dividendo = int(input("Ingresa el dividendo (entero): "))
        divisor = int(input("Ingresa el divisor (entero): "))
    except ValueError:
        print("Error: debes ingresar números enteros válidos.")
        return

    if divisor == 0:
        print("Error: no se puede obtener el residuo de dividir entre cero.")
        return

    # En Python el residuo toma el signo del divisor: -7 % 2 == 1
    print(f"Resultado: {dividendo} % {divisor} = {dividendo % divisor}")


if __name__ == "__main__":
    main()
