def calcular_factorial(numero):
    resultado = 1
    for valor in range(2, numero + 1):
        resultado *= valor
    return resultado


def main():
    print("=== Cálculo de factorial ===")
    try:
        numero = int(input("Ingresa un número entero no negativo: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if numero < 0:
        print("Error: no se puede calcular la factorial de un número negativo.")
        return

    print(f"{numero}! = {calcular_factorial(numero)}")


main()
