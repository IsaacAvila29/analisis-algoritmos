"""Verifica el balance de paréntesis en una expresión matemática.

Se usa una pila: cada símbolo de apertura se apila y cada cierre debe coincidir
con el tope. Soporta (), [] y {}. Además de indicar si la expresión está
balanceada, se reporta la posición del primer error.

Complejidad: O(n) en tiempo y espacio.
"""

PARES = {")": "(", "]": "[", "}": "{"}
APERTURAS = frozenset(PARES.values())


def verificar_balance(expresion):
    """Retorna (True, None) si está balanceada o (False, posicion) del error.

    Si sobra un símbolo de apertura, la posición es la del último que quedó
    sin cerrar.
    """
    pila = []  # guarda (simbolo, posicion)
    for posicion, caracter in enumerate(expresion):
        if caracter in APERTURAS:
            pila.append((caracter, posicion))
        elif caracter in PARES:
            if not pila or pila[-1][0] != PARES[caracter]:
                return False, posicion
            pila.pop()

    if pila:
        return False, pila[-1][1]
    return True, None


def main():
    print("=== Balance de paréntesis ===")
    expresion = input("Ingresa una expresión matemática: ").strip()

    if not expresion:
        print("Error: la expresión no puede estar vacía.")
        return

    balanceada, posicion = verificar_balance(expresion)
    if balanceada:
        print("La expresión está balanceada.")
    else:
        print("La expresión NO está balanceada.")
        print(expresion)
        print(" " * posicion + "^ error en la posición " + str(posicion + 1))


if __name__ == "__main__":
    main()
