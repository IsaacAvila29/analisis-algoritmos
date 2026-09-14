#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicio 3: Multiplicación de dos números con el operador *"""


def main():
    print("=== Multiplicación de dos números ===")
    try:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: debes ingresar valores numéricos válidos.")
        return

    resultado = numero1 * numero2
    print(f"Resultado: {numero1} * {numero2} = {resultado}")


if __name__ == "__main__":
    main()
