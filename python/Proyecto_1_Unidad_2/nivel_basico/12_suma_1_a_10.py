#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicio 12: Suma de los números enteros del 1 al 10"""


def main():
    print("=== Suma de los números enteros del 1 al 10 ===")
    suma = 0
    for numero in range(1, 11):
        suma += numero

    print(f"La suma de los números del 1 al 10 es: {suma}")


if __name__ == "__main__":
    main()
