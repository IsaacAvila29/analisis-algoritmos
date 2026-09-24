"""Verifica si un número entero es divisible simultáneamente entre 5 y 7."""


def main():
    print("=== Divisibilidad entre 5 y 7 ===")
    try:
        numero = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if numero % 5 == 0 and numero % 7 == 0:
        print(f"{numero} es divisible entre 5 y 7 (es múltiplo de 35).")
    else:
        print(f"{numero} NO es divisible simultáneamente entre 5 y 7.")


if __name__ == "__main__":
    main()
