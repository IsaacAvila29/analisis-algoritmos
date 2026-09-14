#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicio 9: Evaluación de la cantidad de caracteres de una cadena respecto a 10"""


def main():
    print("=== Evaluación de longitud de cadena ===")
    cadena = input("Ingresa una cadena de texto: ")
    longitud = len(cadena)

    print(f"La cadena tiene {longitud} caracteres.")
    if longitud > 10:
        print("La cadena tiene MÁS de 10 caracteres.")
    elif longitud == 10:
        print("La cadena tiene EXACTAMENTE 10 caracteres.")
    else:
        print("La cadena tiene MENOS de 10 caracteres.")


if __name__ == "__main__":
    main()
