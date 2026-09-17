def calcular_tiempo(distancia, velocidad):
    return distancia / velocidad


def main():
    print("=== Cálculo del tiempo de viaje ===")
    try:
        distancia = float(input("Ingresa la distancia (km): "))
        velocidad = float(input("Ingresa la velocidad (km/h): "))
    except ValueError:
        print("Error: debes ingresar valores numéricos válidos.")
        return

    if distancia < 0:
        print("Error: la distancia no puede ser negativa.")
        return

    if velocidad <= 0:
        print("Error: la velocidad debe ser mayor a cero.")
        return

    tiempo = calcular_tiempo(distancia, velocidad)
    print(f"Tiempo de viaje: {tiempo:.2f} horas")


main()
