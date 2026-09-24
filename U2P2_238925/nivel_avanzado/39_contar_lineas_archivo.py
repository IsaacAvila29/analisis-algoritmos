"""Cuenta el total de líneas presentes en un archivo de texto.

El archivo se recorre línea por línea (sin cargarlo completo en memoria) y se
reportan también las líneas que no están en blanco. Una última línea sin salto
final se cuenta igualmente.

Complejidad: O(n) en tiempo, O(1) en espacio adicional.
"""

import os


def contar_lineas(ruta, codificacion="utf-8"):
    """Retorna (total_lineas, lineas_no_vacias) del archivo en `ruta`.

    Propaga OSError (archivo inexistente, sin permisos, etc.) y
    UnicodeDecodeError.
    """
    total = 0
    no_vacias = 0
    with open(ruta, encoding=codificacion) as archivo:
        for linea in archivo:
            total += 1
            if linea.strip():
                no_vacias += 1
    return total, no_vacias


def main():
    print("=== Conteo de líneas de un archivo de texto ===")
    ruta = input("Ingresa la ruta del archivo: ").strip().strip("'\"")

    if not ruta:
        print("Error: la ruta no puede estar vacía.")
        return

    ruta = os.path.expanduser(ruta)
    try:
        total, no_vacias = contar_lineas(ruta)
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.")
        return
    except IsADirectoryError:
        print(f"Error: '{ruta}' es un directorio, no un archivo.")
        return
    except PermissionError:
        print(f"Error: no tienes permisos para leer '{ruta}'.")
        return
    except UnicodeDecodeError:
        print("Error: el archivo no parece ser de texto "
              "(codificación UTF-8 inválida).")
        return
    except OSError as error:
        print(f"Error al leer el archivo: {error}")
        return

    print(f"Total de líneas: {total}")
    print(f"Líneas con contenido: {no_vacias}")
    print(f"Líneas en blanco: {total - no_vacias}")


if __name__ == "__main__":
    main()
