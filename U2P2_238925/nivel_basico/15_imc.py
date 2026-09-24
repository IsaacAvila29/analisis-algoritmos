"""Calcula el Índice de Masa Corporal (IMC) y lo interpreta según la OMS.

IMC = peso (kg) / estatura (m)^2
"""


def main():
    print("=== Cálculo del Índice de Masa Corporal ===")
    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        estatura = float(input("Ingresa tu estatura en metros (ej. 1.75): "))
    except ValueError:
        print("Error: debes ingresar valores numéricos válidos.")
        return

    if peso <= 0 or estatura <= 0:
        print("Error: el peso y la estatura deben ser mayores que cero.")
        return

    if estatura > 3:
        print("Aviso: la estatura parece estar en centímetros; "
              "se convertirá a metros.")
        estatura /= 100

    imc = peso / estatura ** 2

    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    print(f"Tu IMC es {imc:.2f}: {categoria}.")


if __name__ == "__main__":
    main()
