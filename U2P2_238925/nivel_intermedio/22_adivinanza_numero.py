"""Juego de adivinanza de un número aleatorio entre 1 y 10.

Tras cada intento se indica si el número secreto es mayor o menor. Las entradas
inválidas o fuera de rango no consumen intentos.
"""

import random

MINIMO = 1
MAXIMO = 10
MAX_INTENTOS = 4  # ceil(log2(10)) = 4 bastan con búsqueda binaria


def evaluar_intento(secreto, intento):
    """Retorna 'correcto', o bien 'mayor'/'menor' según el número secreto."""
    if intento == secreto:
        return "correcto"
    return "mayor" if secreto > intento else "menor"


def leer_intento():
    """Solicita un entero en [MINIMO, MAXIMO] hasta recibir uno válido."""
    while True:
        try:
            intento = int(input(f"Tu intento ({MINIMO}-{MAXIMO}): "))
        except ValueError:
            print("Aviso: debes ingresar un número entero.")
            continue
        if MINIMO <= intento <= MAXIMO:
            return intento
        print(f"Aviso: el número debe estar entre {MINIMO} y {MAXIMO}.")


def main():
    print("=== Adivina el número ===")
    print(f"Pensé un número entre {MINIMO} y {MAXIMO}. "
          f"Tienes {MAX_INTENTOS} intentos.")
    secreto = random.randint(MINIMO, MAXIMO)

    for numero_intento in range(1, MAX_INTENTOS + 1):
        resultado = evaluar_intento(secreto, leer_intento())
        if resultado == "correcto":
            print(f"¡Correcto! Lo adivinaste en {numero_intento} intento(s).")
            return
        print(f"El número secreto es {resultado}.")

    print(f"Se acabaron los intentos. El número era {secreto}.")


if __name__ == "__main__":
    main()
