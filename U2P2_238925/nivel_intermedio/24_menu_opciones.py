"""Despliega un menú de opciones (calculadora) que se repite hasta salir.

Cada operación está en una función independiente y el despacho se hace con un
diccionario, lo que evita una cadena larga de if/elif.
"""


def sumar(a, b):
    """Retorna a + b."""
    return a + b


def restar(a, b):
    """Retorna a - b."""
    return a - b


def multiplicar(a, b):
    """Retorna a * b."""
    return a * b


def dividir(a, b):
    """Retorna a / b; lanza ZeroDivisionError si b es cero."""
    if b == 0:
        raise ZeroDivisionError("no se puede dividir entre cero")
    return a / b


OPCIONES = {
    "1": ("Sumar", sumar),
    "2": ("Restar", restar),
    "3": ("Multiplicar", multiplicar),
    "4": ("Dividir", dividir),
}
OPCION_SALIR = "5"


def mostrar_menu():
    print("\n--- Menú ---")
    for clave, (nombre, _) in OPCIONES.items():
        print(f"{clave}. {nombre}")
    print(f"{OPCION_SALIR}. Salir")


def leer_numero(mensaje):
    """Solicita un número real hasta que la entrada sea válida."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Aviso: debes ingresar un número válido.")


def main():
    print("=== Menú de opciones: calculadora ===")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == OPCION_SALIR:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        if opcion not in OPCIONES:
            print("Opción no válida, intenta de nuevo.")
            continue

        nombre, operacion = OPCIONES[opcion]
        a = leer_numero("Primer número: ")
        b = leer_numero("Segundo número: ")
        try:
            print(f"Resultado de {nombre.lower()}: {operacion(a, b):g}")
        except ZeroDivisionError as error:
            print(f"Error: {error}.")


if __name__ == "__main__":
    main()
