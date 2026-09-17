import random


def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])


def main():
    print("=== Simulación de lanzamiento de moneda ===")
    continuar = True

    while continuar:
        resultado = lanzar_moneda()
        print(f"Resultado: {resultado}")

        respuesta = input("¿Deseas lanzar de nuevo? (s/n): ").strip().lower()
        continuar = respuesta == "s"

    print("Fin de la simulación.")


main()
