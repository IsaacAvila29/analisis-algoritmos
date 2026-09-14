"""Clasifica a una persona por etapa de vida segun su edad (version match/case).

Es el mismo ejercicio que edades.py, resuelto con `match` en lugar de if/elif.
Reutiliza `pedir_edad` de edades.py para no duplicar la lectura por teclado.
"""

from edades import pedir_edad


def clasificar_edad(edad: int) -> str:
    """Devuelve la etapa de vida que corresponde a `edad`.

    Lanza ValueError si la edad es negativa.
    """
    match edad:
        case _ if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        case _ if edad <= 5:
            return "Eres un niño pequeño"
        case _ if edad <= 11:
            return "Eres un niño"
        case _ if edad <= 14:
            return "Eres un puberto"
        case _ if edad <= 17:
            return "Eres un adolescente"
        case _ if edad <= 35:
            return "Eres un adulto joven"
        case _ if edad <= 65:
            return "Eres tercera edad"
        case _:
            return "Eres veterano"


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
