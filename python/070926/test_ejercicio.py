"""
Suite de tests para Ejercicio.py

Ejercicio.py es un script de arriba a abajo: usa random para generar 9 numeros,
los ordena, y pide un numero por teclado con input(). No define funciones, asi
que no se puede importar (importarlo lo ejecuta y se cuelga esperando stdin).

Por eso estos tests lo ejecutan como SUBPROCESO:
  - se siembra random.seed() antes de correrlo, para que los numeros generados
    sean siempre los mismos y los casos sean deterministas
  - se le inyecta la respuesta del usuario por stdin
  - se verifica lo que imprime

Los tests documentan el comportamiento ACTUAL del script. Los casos marcados
con @pytest.mark.xfail describen bugs reales: el test falla a proposito hoy y
pasara a XPASS el dia que se corrija el bug.

Correr con:
    ../../.venv/bin/python -m pytest test_ejercicio.py -v
"""

import random
import re
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent / "Ejercicio.py"

# Ejecuta el script sembrando random primero, para que sea reproducible.
RUNNER = textwrap.dedent("""
    import random, runpy, sys
    random.seed(int(sys.argv[1]))
    runpy.run_path(sys.argv[2], run_name="__main__")
""")

SEED = 1
# Numeros que produce el script con SEED=1, ya ordenados (ver test_numeros_deterministas).
NUMEROS_SEED1 = [9, 16, 18, 33, 58, 64, 73, 98, 98]


def correr(entrada, seed=SEED):
    """Ejecuta Ejercicio.py con una semilla fija y la entrada dada por stdin."""
    return subprocess.run(
        [sys.executable, "-c", RUNNER, str(seed), str(SCRIPT)],
        input=f"{entrada}\n",
        capture_output=True,
        text=True,
        timeout=30,
    )


def numeros_generados(salida):
    """Extrae los numeros que el script reporto haber generado."""
    return [int(m) for m in re.findall(r"numeroRandom en +\d+ *: *(\d+)", salida)]


def numeros_ordenados(salida):
    """Extrae la lista que el script imprime bajo 'Números ordenados:'."""
    bloque = salida.split("Números ordenados:")[1]
    bloque = bloque.split("Elige un numero")[0]
    return [int(l) for l in bloque.strip().splitlines() if l.strip().isdigit()]


# ---------------------------------------------------------------------------
# Generacion y ordenamiento (lineas 3-13)
# ---------------------------------------------------------------------------

def test_genera_nueve_numeros():
    """El bucle range(1, 10) genera 9 numeros, no 10."""
    r = correr(50)
    assert len(numeros_generados(r.stdout)) == 9


def test_numeros_dentro_del_rango():
    """randint(1, 100) debe dar valores entre 1 y 100 inclusive."""
    r = correr(50)
    for n in numeros_generados(r.stdout):
        assert 1 <= n <= 100


def test_numeros_quedan_ordenados():
    """Despues de .sort() la lista impresa debe estar en orden ascendente."""
    r = correr(50)
    ordenados = numeros_ordenados(r.stdout)
    assert ordenados == sorted(ordenados)


def test_ordenar_conserva_los_mismos_numeros():
    """.sort() reordena in-place: no debe perder ni inventar numeros."""
    r = correr(50)
    assert sorted(numeros_generados(r.stdout)) == numeros_ordenados(r.stdout)


def test_numeros_deterministas_con_semilla():
    """Con la misma semilla el script siempre produce los mismos numeros.

    Este test ancla NUMEROS_SEED1, del que dependen los demas casos.
    """
    r = correr(50)
    assert numeros_ordenados(r.stdout) == NUMEROS_SEED1


def test_dos_corridas_con_misma_semilla_son_iguales():
    assert correr(50).stdout == correr(50).stdout


# ---------------------------------------------------------------------------
# Busqueda de posicion: casos que SI funcionan (lineas 17-23)
# ---------------------------------------------------------------------------

def test_numero_igual_al_primero():
    """pick == numeros[0] entra por la rama 'igual a', posicion 0."""
    r = correr(NUMEROS_SEED1[0])  # 9
    assert "es igual a 9" in r.stdout
    assert "posición 0" in r.stdout


def test_numero_entre_los_dos_primeros():
    """pick estrictamente entre numeros[0] y numeros[1] -> posicion 1."""
    pick = 12  # entre 9 y 16
    r = correr(pick)
    assert "está entre 9 y 16" in r.stdout
    assert "posicion 1" in r.stdout


def test_numero_igual_al_segundo():
    """pick == numeros[1] entra por la tercera rama, posicion 1."""
    r = correr(NUMEROS_SEED1[1])  # 16
    assert "es igual a 16" in r.stdout


def test_menor_que_todos_reporta_fuera_de_rango():
    """Un numero por debajo del minimo cae en el else y corta con break."""
    r = correr(1)  # menor que 9
    assert "por encima del ultimo o por debajo del primero" in r.stdout


def test_el_script_termina_sin_error():
    """Con entrada valida el script no debe lanzar excepcion."""
    r = correr(50)
    assert r.returncode == 0
    assert "Traceback" not in r.stderr


def test_solo_imprime_un_veredicto():
    """El break garantiza que se imprima una sola conclusion, no varias."""
    r = correr(50)
    tramo = r.stdout.split("Elige un numero")[1]
    veredictos = (
        tramo.count("está entre")
        + tramo.count("es igual a")
        + tramo.count("no se que hacer")
    )
    assert veredictos == 1


# ---------------------------------------------------------------------------
# BUGS DOCUMENTADOS
# ---------------------------------------------------------------------------

@pytest.mark.xfail(
    reason="BUG: el else con break corta en la primera vuelta. Cualquier numero "
           "que no caiga entre numeros[0] y numeros[1] se reporta como "
           "'fuera de rango', aunque este dentro de la lista.",
    strict=True,
)
def test_numero_intermedio_deberia_encontrar_su_lugar():
    """58 es numeros[4], claramente dentro de la lista.

    El script deberia decir que va en la posicion 4, pero como no cae entre
    numeros[0]=9 y numeros[1]=16, la primera iteracion entra al else e imprime
    'no se que hacer'. Se rinde antes de haber buscado.
    """
    r = correr(58)
    assert "no se que hacer" not in r.stdout
    assert "es igual a 58" in r.stdout


@pytest.mark.xfail(
    reason="BUG: mismo break prematuro; el ultimo elemento nunca se alcanza.",
    strict=True,
)
def test_numero_igual_al_ultimo_deberia_reconocerse():
    """98 es el maximo de la lista, pero se reporta como fuera de rango."""
    r = correr(NUMEROS_SEED1[-1])  # 98
    assert "no se que hacer" not in r.stdout


@pytest.mark.xfail(
    reason="BUG: range(1, 10) llega a i=9, pero la lista tiene indices 0..8. "
           "numeros[9] seria IndexError. Hoy el break lo tapa; si se quita el "
           "break sin corregir el rango, el script crashea.",
    strict=True,
)
def test_recorrer_sin_break_no_deberia_desbordar():
    """Replica el bucle sin el break para exponer el IndexError latente."""
    numeros = list(NUMEROS_SEED1)
    assert len(numeros) == 9
    for i in range(1, 10):
        numeros[i]  # revienta en i=9


def test_rama_muerta_numeropick_indexado():
    """BUG: la linea 25 hace numeroPick[i+1] sobre un int.

    Es codigo muerto: la condicion se evalua de izquierda a derecha y su primera
    mitad (numeroPick == numeros[i-1]) ya fue capturada por la rama anterior en
    la linea 20, asi que nunca se llega a indexar. Si se alcanzara, seria
    TypeError. Este test fija esa realidad.
    """
    with pytest.raises(TypeError, match="not subscriptable"):
        pick = 42
        pick[1]


# ---------------------------------------------------------------------------
# Entrada del usuario (linea 15)
# ---------------------------------------------------------------------------

def test_entrada_no_numerica_revienta():
    """int(input(...)) sin try/except: texto no numerico lanza ValueError.

    Documenta que el script no valida la entrada del usuario.
    """
    r = correr("abc")
    assert "ValueError" in r.stderr


def test_entrada_vacia_revienta():
    r = correr("")
    assert "ValueError" in r.stderr


@pytest.mark.parametrize("pick", [0, -5, 101, 9999])
def test_fuera_del_rango_pedido_no_crashea(pick):
    """El script pide 'un numero del i al 100' pero no lo valida.

    No se cae; simplemente cae en el else. Se documenta que no hay validacion.
    """
    r = correr(pick)
    assert r.returncode == 0
    assert "no se que hacer" in r.stdout


# ---------------------------------------------------------------------------
# Referencia: como deberia comportarse una busqueda correcta
# ---------------------------------------------------------------------------

def posicion_de_insercion(pick, numeros):
    """Implementacion correcta, para contrastar con la del script."""
    for i, n in enumerate(numeros):
        if pick <= n:
            return i
    return len(numeros)


@pytest.mark.parametrize(
    "pick, esperado",
    [
        (1, 0),    # antes de todos
        (9, 0),    # igual al primero
        (12, 1),   # entre el primero y el segundo
        (58, 4),   # en medio: el script falla aqui
        (98, 7),   # igual al ultimo (primera de las dos apariciones)
        (100, 9),  # despues de todos
    ],
)
def test_referencia_posicion_correcta(pick, esperado):
    """Fija cual es la respuesta correcta en cada caso.

    Sirve de contraste: el script solo acierta los tres primeros.
    """
    assert posicion_de_insercion(pick, NUMEROS_SEED1) == esperado
