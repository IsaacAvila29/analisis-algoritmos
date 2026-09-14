#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicio 10: Validación de coincidencia exacta con el término 'python'"""


def main():
    print("=== Validación de coincidencia exacta con 'python' ===")
    palabra = input("Ingresa una palabra: ")

    if palabra == "python":
        print("Coincidencia exacta: la palabra ingresada es 'python'.")
    else:
        print("No hay coincidencia: la palabra ingresada no es 'python'.")


if __name__ == "__main__":
    main()
