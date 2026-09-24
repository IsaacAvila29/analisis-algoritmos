"""Imprime una palabra en orden invertido."""


def main():
    print("=== Palabra invertida ===")
    palabra = input("Ingresa una palabra: ").strip()

    if not palabra:
        print("Error: la palabra no puede estar vacía.")
        return

    # El slicing con paso -1 recorre la cadena de atrás hacia adelante
    print(f"Invertida: {palabra[::-1]}")


if __name__ == "__main__":
    main()
