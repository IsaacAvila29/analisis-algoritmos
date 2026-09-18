import random


def lanzar_dado():
    return random.randint(1, 6)


def main():
    print("=== Lanzamiento de dado hasta obtener un 6 ===")
    intentos = 0
    resultado = 0

    while resultado != 6:
        resultado = lanzar_dado()
        intentos += 1
        print(f"Intento {intentos}: salió {resultado}")

    print(f"\n¡Se obtuvo un 6 después de {intentos} intento(s)!")


main()
