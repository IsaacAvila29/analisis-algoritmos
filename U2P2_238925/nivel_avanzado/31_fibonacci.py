"""Imprime los primeros 10 términos de la sucesión de Fibonacci.

La sucesión inicia en 0, 1 y cada término es la suma de los dos anteriores.

Se usa un enfoque iterativo que mantiene solo los dos últimos términos,
evitando el costo exponencial de la recursión ingenua.

Complejidad: O(n) en tiempo y espacio (O(1) adicional sin contar la lista
resultado).
"""

TERMINOS = 10


def fibonacci(n):
    """Retorna los primeros `n` términos de Fibonacci; [] si n <= 0."""
    terminos = []
    a, b = 0, 1
    for _ in range(n):
        terminos.append(a)
        a, b = b, a + b
    return terminos


def main():
    print(f"=== Primeros {TERMINOS} términos de Fibonacci ===")
    print(", ".join(str(t) for t in fibonacci(TERMINOS)))


if __name__ == "__main__":
    main()
