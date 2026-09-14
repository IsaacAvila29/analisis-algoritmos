#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicio 15: Función para generar un mensaje de saludo dinámico con un nombre"""


def generar_saludo(nombre):
    return f"¡Hola, {nombre}! Bienvenido/a."


def main():
    print("=== Mensaje de saludo dinámico ===")
    nombre = input("Ingresa tu nombre: ").strip()

    if not nombre:
        print("Error: el nombre no puede estar vacío.")
        return

    print(generar_saludo(nombre))


if __name__ == "__main__":
    main()
