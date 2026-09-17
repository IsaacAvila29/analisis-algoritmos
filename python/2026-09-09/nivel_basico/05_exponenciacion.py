def main():
    print("=== Exponenciación ===")
    try:
        base = float(input("Ingresa la base: "))
        exponente = float(input("Ingresa el exponente: "))
    except ValueError:
        print("Error: debes ingresar valores numéricos válidos.")
        return

    resultado = base ** exponente
    print(f"Resultado: {base} ** {exponente} = {resultado}")


main()
