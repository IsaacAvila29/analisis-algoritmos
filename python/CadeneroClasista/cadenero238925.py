# El Cadenero Clasista
# Muy clasista
# Isaac Avila Saenz 238925

import random

# ---------- Colecciones de datos ----------

# Lista VIP: entran sin importar ningun otro filtro (nepotismo puro).
LISTA_VIP = {
    "el profe heriberto",
    "el santi",
    "ana sofi",
    "frank de la o",
}

# Nombres tradicionales que el cadenero rechaza por prejuicio sociocultural.
NOMBRES_RESTRINGIDOS = {
    "guadalupe",
    "xochitl",
    "citlalli",
    "cuauhtemoc",
    "tonantzin",
    "petra",
    "juana",
    "epifanio",
    "crescencio",
    "hermenegildo",
}

# Formas en que alguien puede indicar que es mujer.
GENEROS_MUJER = {"f", "fem", "femenino", "mujer", "chica", "dama"}

FRASES_VIP = [
    "Pase, VIP",
    "Subele, rey",
    "Adelante, crack",
    "Cruza, jefe",
    "Pasate, maquina",
]

FRASES_ACCESO = [
    "Pasa raspando.",
    "Estas en lista, camina.",
    "Pase con 6.0.",
    "Autorizado, siguele.",
    "Entra al fondo.",
    "Aprobado, no hagas bulto.",
    "Tienes sello, pasale.",
    "Apenas, pero entras.",
]

FRASES_GENERO = [
    "Solo chicas hoy.",
    "Hombres no pasan.",
    "Solo mujeres, compa.",
    "Noche de chicas.",
    "Varones afuera.",
    "Puro estrogeno hoy.",
    "Los hombres no.",
    "Solo ellas entran.",
]

FRASES_EDAD = [
    "Vayase al kinder.",
    "A mimir, nino.",
    "Aqui no hay Choco Milk.",
    "Panalera afuera.",
    "Trae a tu tutor.",
    "Pasate a la primaria.",
    "Llego la hora de dormir.",
]

FRASES_ONOMASTICO = [
    "No malinches",
    "No malinches, aqui no.",
    "Con ese nombre no, malinches.",
    "Hoy no, no malinches.",
    "Ay no, malinches, para atras.",
]

EDAD_MINIMA = 18
COMANDO_SALIR = "salir"


# ---------- Normalizacion ----------

def normalizar(texto):
    """Deja el texto en minusculas, sin espacios sobrantes ni acentos.

    Asi "  XÓCHITL " y "xochitl" se comparan igual.
    """
    limpio = texto.strip().lower()
    tabla = str.maketrans("áéíóúüñ", "aeiouun")
    return " ".join(limpio.translate(tabla).split())


# ---------- Captura de datos ----------

def pedir_nombre():
    return input(f"Nombre del solicitante (o '{COMANDO_SALIR}' para cerrar): ").strip()


def pedir_genero():
    return input("Genero (F / M / mujer / hombre): ").strip()


def pedir_edad():
    """Pide la edad hasta que el usuario escriba un entero valido."""
    while True:
        try:
            edad = int(input("Edad: ").strip())
        except ValueError:
            print("El cadenero: eso no es un numero, tu edad en digitos.")
            continue

        if edad < 0 or edad > 120:
            print("El cadenero: no te pases de vivo, dame una edad real.")
            continue

        return edad


# ---------- Logica de negocio ----------

def es_vip(nombre):
    """True si el nombre esta en la lista de invitados por nepotismo."""
    return normalizar(nombre) in LISTA_VIP


def es_mujer(genero):
    """True si el genero capturado cuenta como mujer."""
    return normalizar(genero) in GENEROS_MUJER


def tiene_nombre_restringido(nombre):
    """True si alguna palabra del nombre esta en la lista de prejuicio."""
    for palabra in normalizar(nombre).split():
        if palabra in NOMBRES_RESTRINGIDOS:
            return True
    return False


def evaluar(nombre, genero, edad):
    """Aplica la jerarquia del proyecto y regresa (acceso, mensaje).

    El orden es el que pide la rubrica:
        1. Lista VIP    -> entra sin importar lo demas
        2. Genero       -> solo mujeres
        3. Mayoria de edad
        4. Filtro onomastico
    """
    if es_vip(nombre):
        return True, random.choice(FRASES_VIP)

    if not es_mujer(genero):
        return False, random.choice(FRASES_GENERO)

    if edad < EDAD_MINIMA:
        return False, random.choice(FRASES_EDAD)

    if tiene_nombre_restringido(nombre):
        return False, random.choice(FRASES_ONOMASTICO)

    return True, random.choice(FRASES_ACCESO)


# ---------- Flujo principal ----------

def anunciar(nombre, acceso, mensaje):
    """Imprime el veredicto del cadenero para una persona."""
    print("-" * 45)
    print(f"{nombre.title()}: {mensaje}")
    #Si, estos emojis fueron asi puestos a proposito
    print("✅ ACCESO AUTORIZADO" if acceso else "❌ ACCESO DENEGADO")
    print("-" * 45 + "\n")


def atender_persona(nombre):
    """Captura los datos que hagan falta y regresa True si la persona entra.

    Los datos se piden solo mientras sirvan: al VIP no se le pregunta nada,
    y a quien no pasa el filtro de genero no se le pide la edad.
    """
    if es_vip(nombre):
        acceso, mensaje = evaluar(nombre, "", 0)
        anunciar(nombre, acceso, mensaje)
        return acceso

    genero = pedir_genero()
    if not es_mujer(genero):
        anunciar(nombre, False, random.choice(FRASES_GENERO))
        return False

    edad = pedir_edad()
    acceso, mensaje = evaluar(nombre, genero, edad)
    anunciar(nombre, acceso, mensaje)
    return acceso


def atender_fila():
    """Atiende personas una tras otra hasta que alguien escriba 'salir'."""
    admitidos = 0
    rechazados = 0

    print("=" * 45)
    print("   PASAR LA MATERIA (Night Club)")
    print(f"   Escribe '{COMANDO_SALIR}' en el nombre para cerrar")
    print("=" * 45)

    while True:
        nombre = pedir_nombre()



        if normalizar(nombre) == COMANDO_SALIR:
            break

        if nombre == "":
            print("El cadenero: sin nombre no hay entrada.\n")
            continue

        if atender_persona(nombre):
            admitidos += 1
        else:
            rechazados += 1

    print("\nFin de la jornada.")
    print(f"Admitidos:  {admitidos}")
    print(f"Rechazados: {rechazados}")


# Esto hace que la fila solo corra si ejecutas el archivo directamente,
# y no cuando alguien lo importa para usar sus funciones (como los tests).
if __name__ == "__main__":
    atender_fila()
