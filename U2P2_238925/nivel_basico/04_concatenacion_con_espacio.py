"""Concatena dos cadenas de texto agregando un espacio entre ellas."""


def main():
    print("=== Concatenación de cadenas con espacio ===")
    texto1 = input("Ingresa el primer texto: ").strip()
    texto2 = input("Ingresa el segundo texto: ").strip()

    if not texto1 or not texto2:
        print("Error: ambos textos deben contener al menos un carácter.")
        return

    print(f"Resultado: {texto1 + ' ' + texto2}")


if __name__ == "__main__":
    main()
