def sumar_digitos(numero):
    if numero < 10:
        return numero
    return numero % 10 + sumar_digitos(numero // 10)


def main():
    print("=== Suma recursiva de los dígitos de un número ===")
    try:
        numero = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    numero_absoluto = abs(numero)
    resultado = sumar_digitos(numero_absoluto)
    print(f"La suma de los dígitos de {numero} es: {resultado}")


main()
