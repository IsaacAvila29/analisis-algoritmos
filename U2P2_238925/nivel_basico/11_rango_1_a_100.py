"""Comprueba si un número se ubica en el rango cerrado [1, 100]."""


def main():
    print("=== Comprobación de rango (1 a 100) ===")
    try:
        numero = float(input("Ingresa un número: "))
    except ValueError:
        print("Error: debes ingresar un número válido.")
        return

    if 1 <= numero <= 100:
        print(f"{numero:g} está dentro del rango de 1 a 100.")
    else:
        print(f"{numero:g} está fuera del rango de 1 a 100.")


if __name__ == "__main__":
    main()
