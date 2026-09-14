#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicio 13: Impresión individual de cada carácter contenido en una cadena"""


def main():
    print("=== Impresión de caracteres individuales ===")
    cadena = input("Ingresa una cadena de texto: ")

    for caracter in cadena:
        print(caracter)


if __name__ == "__main__":
    main()
