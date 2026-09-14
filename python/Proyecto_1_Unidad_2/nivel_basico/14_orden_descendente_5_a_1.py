#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicio 14: Impresión en orden descendente de los valores del 5 al 1"""


def main():
    print("=== Números en orden descendente del 5 al 1 ===")
    for numero in range(5, 0, -1):
        print(numero, end=" ")
    print()


if __name__ == "__main__":
    main()
