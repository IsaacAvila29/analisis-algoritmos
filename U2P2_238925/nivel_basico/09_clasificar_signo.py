"""Clasifica un número como positivo, cero o negativo."""


def main():
    print("=== Clasificación de un número por su signo ===")
    try:
        numero = float(input("Ingresa un número: "))
    except ValueError:
        print("Error: debes ingresar un número válido.")
        return

    if numero > 0:
        print(f"{numero:g} es positivo.")
    elif numero < 0:
        print(f"{numero:g} es negativo.")
    else:
        print("El número es cero.")


if __name__ == "__main__":
    main()
