"""Transforma a mayúscula la primera letra de un texto, sin alterar el resto.

A diferencia de str.capitalize(), no convierte a minúsculas las demás letras
("iPhone de Juan" -> "IPhone de Juan") y salta espacios o signos iniciales
("¿hola?" -> "¿Hola?").
"""


def main():
    print("=== Primera letra en mayúscula ===")
    texto = input("Ingresa un texto: ")

    for indice, caracter in enumerate(texto):
        if caracter.isalpha():
            resultado = texto[:indice] + caracter.upper() + texto[indice + 1:]
            print(f"Resultado: {resultado}")
            return

    print("Error: el texto no contiene ninguna letra.")


if __name__ == "__main__":
    main()
