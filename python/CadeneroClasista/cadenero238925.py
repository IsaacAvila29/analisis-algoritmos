# El Cadenero Clasista
# Muy clasista
# Isaac Avila Saenz 238925

import random

# ---------- Colecciones de datos ----------

LISTA_VIP = {
    "el profe heriberto",
    "el santi",
    "ana sofi",
    "frank de la o",
}

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

GENEROS_MUJER = {"f", "fem", "femenino", "mujer", "m u j e r", "chica", "dama"}

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
    "A mimir, niño.",
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


# ---------- Normalizacion ----------

def normalizar(texto):
    """Deja el texto en minusculas, sin espacios sobrantes ni acentos."""
    limpio = texto.strip().lower()
    tabla = str.maketrans("áéíóúüñ", "aeiouun")
    return limpio.translate(tabla)


# ---------- Captura de datos ----------

def pedir_nombre():
    return input("Nombre del solicitante (o 'salir' para cerrar): ").strip()


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


def pedir_genero():
    return input("Genero (F / M / mujer / hombre): ").strip()


# ---------- Logica de negocio ----------

def es_vip(nombre):
    return normalizar(nombre) in LISTA_VIP


def es_mujer(genero):
    return normalizar(genero) in GENEROS_MUJER


def tiene_nombre_restringido(nombre):
    """Revisa si alguna palabra del nombre esta en la lista de prejuicio."""
    palabras = normalizar(nombre).split()
    for palabra in palabras:
        if palabra in NOMBRES_RESTRINGIDOS:
            return True
    return False


def veredicto_por_genero(genero):
    """Regresa el mensaje de rechazo si el genero no pasa, o None si pasa."""
    if not es_mujer(genero):
        return random.choice(FRASES_GENERO)
    return None


def veredicto_por_edad(edad):
    """Regresa el mensaje de rechazo si es menor de edad, o None si pasa."""
    if edad < 18:
        return random.choice(FRASES_EDAD)
    return None


def veredicto_por_nombre(nombre):
    """Regresa el mensaje de rechazo por prejuicio, o None si pasa."""
    if tiene_nombre_restringido(nombre):
        return random.choice(FRASES_ONOMASTICO)
    return None


# ---------- Flujo principal ----------

def anunciar(nombre, acceso, mensaje):
    """Imprime el veredicto del cadenero para una persona."""
    print("-" * 45)
    print(f"{nombre.title()}: {mensaje}")
    print("ACCESO AUTORIZADO" if acceso else "ACCESO DENEGADO")
    print("-" * 45 + "\n")


def atender_persona(nombre):
    """Captura los datos que hagan falta y regresa True si la persona entra.

    Los datos se piden conforme se necesitan: si el genero ya la descalifica,
    el cadenero la bota sin molestarse en preguntarle la edad.
    """
    vip = es_vip(nombre)

    genero = pedir_genero()
    rechazo = veredicto_por_genero(genero)
    if rechazo is not None and not vip:
        anunciar(nombre, False, rechazo)
        return False

    edad = pedir_edad()
    rechazo = veredicto_por_edad(edad)
    if rechazo is not None and not vip:
        anunciar(nombre, False, rechazo)
        return False

    # El VIP se salta cualquier filtro por nepotismo.
    if vip:
        anunciar(nombre, True, random.choice(FRASES_VIP))
        return True

    rechazo = veredicto_por_nombre(nombre)
    if rechazo is not None:
        anunciar(nombre, False, rechazo)
        return False

    anunciar(nombre, True, random.choice(FRASES_ACCESO))
    return True


def atender_fila():
    admitidos = 0
    rechazados = 0

    print("=" * 45)
    print("   PASAR LA MATERIA (Night Club)")
    print("   Escribe 'salir' en el nombre para cerrar")
    print("=" * 45)

    while True:
        nombre = pedir_nombre()

        if normalizar(nombre) == "salir":
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



#no termino de entender porque la IA hace esto
#Segun la explicacion es para que el script se ejecute directamente desde la terminal y no al ser importado como módulo.
if __name__ == "__main__":
    atender_fila()
#Si funciona no le muevo
