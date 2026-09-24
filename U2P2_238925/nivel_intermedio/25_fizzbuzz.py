"""Implementa FizzBuzz del 1 al 100.

Múltiplos de 3 -> "Fizz", de 5 -> "Buzz", de ambos (15) -> "FizzBuzz".

Complejidad: O(n) en tiempo y espacio.
"""


def fizzbuzz(numero):
    """Retorna la palabra de FizzBuzz correspondiente a `numero`."""
    resultado = ""
    if numero % 3 == 0:
        resultado += "Fizz"
    if numero % 5 == 0:
        resultado += "Buzz"
    return resultado or str(numero)


def generar_fizzbuzz(inicio, fin):
    """Retorna los valores FizzBuzz del intervalo cerrado [inicio, fin]."""
    return [fizzbuzz(n) for n in range(inicio, fin + 1)]


def main():
    print("=== FizzBuzz del 1 al 100 ===")
    for valor in generar_fizzbuzz(1, 100):
        print(valor)


if __name__ == "__main__":
    main()
