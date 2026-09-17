def interseccion(lista1, lista2):
    comunes = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in comunes:
            comunes.append(elemento)
    return comunes


def leer_lista(mensaje):
    entrada = input(mensaje).strip()
    return entrada.split()


def main():
    print("=== Intersección de elementos entre dos listas ===")
    lista1 = leer_lista("Ingresa los elementos de la primera lista separados por espacio: ")
    lista2 = leer_lista("Ingresa los elementos de la segunda lista separados por espacio: ")

    if not lista1 or not lista2:
        print("Error: ambas listas deben contener al menos un elemento.")
        return

    resultado = interseccion(lista1, lista2)
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")

    if resultado:
        print(f"Elementos comunes: {resultado}")
    else:
        print("No hay elementos comunes entre ambas listas.")


main()
