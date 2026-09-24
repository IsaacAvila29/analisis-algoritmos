"""Determina el valor máximo entre tres números mediante comparaciones."""


def main():
    print("=== Mayor de tres números ===")
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        c = float(input("Ingresa el tercer número: "))
    except ValueError:
        print("Error: debes ingresar valores numéricos válidos.")
        return

    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c

    print(f"El número mayor es: {mayor:g}")


if __name__ == "__main__":
    main()
