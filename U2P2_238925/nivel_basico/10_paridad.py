"""Determina si un número entero es par o impar."""


def main():
    print("=== Paridad de un número ===")
    try:
        numero = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")


if __name__ == "__main__":
    main()
