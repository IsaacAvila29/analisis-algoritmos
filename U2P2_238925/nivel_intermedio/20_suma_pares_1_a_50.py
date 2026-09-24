"""Suma los números pares comprendidos entre 1 y 50 (inclusive).

Se incluye el cálculo iterativo y su verificación con la fórmula cerrada
2 + 4 + ... + 2k = k(k + 1).

Complejidad: O(n) la versión iterativa, O(1) la fórmula.
"""


def sumar_pares(inicio, fin):
    """Retorna la suma de los pares en el intervalo cerrado [inicio, fin]."""
    primer_par = inicio if inicio % 2 == 0 else inicio + 1
    total = 0
    for numero in range(primer_par, fin + 1, 2):
        total += numero
    return total


def sumar_pares_formula(limite):
    """Retorna la suma de los pares en [1, limite] con la fórmula k(k + 1)."""
    k = limite // 2
    return k * (k + 1)


def main():
    print("=== Suma de números pares entre 1 y 50 ===")
    total = sumar_pares(1, 50)
    print(f"Suma (iterativa): {total}")
    print(f"Verificación con fórmula k(k+1): {sumar_pares_formula(50)}")


if __name__ == "__main__":
    main()
