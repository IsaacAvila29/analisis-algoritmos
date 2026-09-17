def main():
    print("=== División de dos números ===")
    try:
        numero1 = float(input("Ingresa el dividendo: "))
        numero2 = float(input("Ingresa el divisor: "))
    except ValueError:
        print("Error: debes ingresar valores numéricos válidos.")
        return

    if numero2 == 0:
        print("Error: no se puede dividir entre cero.")
        return

    resultado = numero1 / numero2
    print(f"Resultado: {numero1} / {numero2} = {resultado}")


main()
