"""Clasifica a una persona por etapa de vida segun su edad (version if/elif).

La misma logica resuelta con match/case esta en edades2.py.
"""


def clasificar_edad(edad: int) -> str:
    """Devuelve la etapa de vida que corresponde a `edad`.

    Lanza ValueError si la edad es negativa.
    """
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    if edad <= 5:
        return "Eres un niño pequeño"
    elif edad <= 11:
        return "Eres un niño"
    elif edad <= 14:
        return "Eres un puberto"
    elif edad <= 17:
        return "Eres un adolescente"
    elif edad <= 35:
        return "Eres un adulto joven"
    elif edad <= 65:
        return "Eres tercera edad"
    else:
        return "Eres veterano"


def pedir_edad() -> int | None:
    """Pide una edad por teclado. Devuelve None cuando el usuario quiere salir."""
    entrada = input("Introduce tu edad (Enter para salir): ").strip()
    if entrada == "":
        return None
    return int(entrada)


def main() -> None:
    while True:
        try:
            edad = pedir_edad()
            if edad is None:
                break
            print(clasificar_edad(edad))
        except ValueError as error:
            print(f"Entrada invalida: {error}")


if __name__ == "__main__":
    main()
