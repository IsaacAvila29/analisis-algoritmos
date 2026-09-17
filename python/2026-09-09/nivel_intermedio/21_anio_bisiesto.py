def es_bisiesto(anio):
    # bisiesto si es divisible entre 4, salvo los siglos que no sean divisibles entre 400
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def main():
    print("=== Validación de año bisiesto ===")
    try:
        anio = int(input("Ingresa un año: "))
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    if anio <= 0:
        print("Error: el año debe ser un número positivo.")
        return

    if es_bisiesto(anio):
        print(f"El año {anio} SÍ es bisiesto.")
    else:
        print(f"El año {anio} NO es bisiesto.")


main()
