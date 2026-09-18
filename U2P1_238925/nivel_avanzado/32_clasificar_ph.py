def clasificar_ph(ph):
    if ph < 7:
        return "Ácido"
    elif ph == 7:
        return "Neutro"
    else:
        return "Básico (alcalino)"


def main():
    print("=== Clasificación de nivel de pH ===")
    try:
        ph = float(input("Ingresa el valor de pH (0-14): "))
    except ValueError:
        print("Error: debes ingresar un valor numérico válido.")
        return

    if ph < 0 or ph > 14:
        print("Error: el pH debe estar en el rango de 0 a 14.")
        return

    clasificacion = clasificar_ph(ph)
    print(f"El pH {ph} se clasifica como: {clasificacion}")


main()
