# Análisis de Algoritmos

Repositorio de ejercicios de la materia. Hay dos partes independientes:

- **C++** — ejercicios compilados, un `.cpp` por programa, organizados en carpetas por tema.
- **Python** — ejercicios y notebooks de clase, en `python/`.

## Estructura

```
00-plantilla/plantilla.cpp     # punto de partida para cada ejercicio en C++
01-algoritmosFaciles/*.cpp     # un programa por archivo
include/timer.hpp              # medición de tiempos (std::chrono)
Makefile                       # compila cualquier .cpp suelto
compile_flags.txt              # flags que lee clangd
bin/                           # binarios (ignorado por git)
python/                        # ejercicios y notebooks de Python
```

Convención: carpetas con prefijo numérico (`01-algoritmosFaciles`, `02-recursion`, …) y archivos en `camelCase` (`conversorDivisas.cpp`, `binarySearch.py`).

---

# C++

## Compilar y ejecutar

```sh
make run     FILE=01-algoritmosFaciles/imc.cpp   # -O0 -g (desarrollo)
make release FILE=01-algoritmosFaciles/imc.cpp   # -O2   (medir tiempos)
make debug   FILE=01-algoritmosFaciles/imc.cpp   # AddressSanitizer + UBSan
make build   FILE=...                            # solo compilar → bin/imc
make clean
```

`FILE` es obligatorio: el Makefile compila un archivo suelto a `bin/<nombre>`.

En VS Code con el archivo abierto:

| Acción | Atajo |
|---|---|
| Compilar | `Cmd+Shift+B` |
| Compilar y ejecutar | `Cmd+Shift+P` → *Run Test Task* (o asigna atajo a `workbench.action.tasks.test`) |
| Depurar con breakpoints | `F5` (CodeLLDB) |

Para leer entrada desde archivo: `./bin/ejercicio < entrada.txt`.

## Medir tiempos

```cpp
#include "timer.hpp"

Timer t;
algoritmo(v);
std::cout << t.elapsed_ms() << " ms\n";

{ TIME_BLOCK("merge sort n=1e6"); merge_sort(v); }   // imprime al salir del bloque
```

Reglas:
- Mide con `make release` (`-O2`); con `-O0` los tiempos no son representativos.
- Repite varias veces y toma promedio/mediana; usa `n` crecientes (1e3, 1e4, 1e5…) para verificar el orden de crecimiento.
- Usa `std::mt19937` con semilla fija para datos reproducibles.

## Depuración

- `make debug` detecta accesos fuera de rango, use-after-free y overflow con signo (UB) — muy útil en algoritmos con índices.
- `F5` en VS Code lanza lldb. Desde terminal: `lldb bin/ejercicio` → `b main`, `r`, `n`, `s`, `p variable`, `bt`.
- Para ver cómo se ve un `std::vector` u otros contenedores, CodeLLDB ya trae visualizadores.

## Buenas prácticas para los ejercicios

- Copia `00-plantilla/plantilla.cpp` para empezar.
- `ios::sync_with_stdio(false); cin.tie(nullptr);` para entrada grande.
- Compila siempre con `-Wall -Wextra -Wpedantic` (ya en el Makefile) y corrige los warnings.
- Prefiere `size_t`/`long long` donde pueda haber overflow; `int` de 32 bits se desborda en ~2.1e9.
- Comenta la complejidad (tiempo y espacio) al inicio de cada algoritmo.

---

# Python

Los ejercicios viven en `python/`. No hay dependencias externas: todo corre con la librería estándar.

```sh
python3 python/edades.py          # ejecutar un ejercicio
python3 python/binarySearch.py
```

Los `.ipynb` se abren directamente en VS Code (o con `jupyter notebook`); cada ejercicio está en su propia celda.

| Archivo | Contenido |
|---|---|
| `binarySearch.py` | Búsqueda binaria sobre lista ordenada, con traza opcional de cada paso |
| `edades.py` | Clasificación por etapa de vida con `if`/`elif` |
| `edades2.py` | El mismo ejercicio con `match`/`case`; reutiliza `pedir_edad` de `edades.py` |
| `238925.py` | Sombrero Seleccionador de Hogwarts (test de personalidad por puntajes) |
| `Edades1.ipynb` | Versión en notebook del ejercicio de edades |
| `EjerciciosFuncionesNativas_238925.ipynb` | Ejercicios de funciones nativas y variables |
| `260826.ipynb` | Notas de la clase del 26/08 |

`edades2.py` importa `pedir_edad` de `edades.py`; ambos archivos deben quedar en la misma carpeta.

Convenciones: docstring al inicio con la complejidad cuando el archivo implementa un algoritmo, nombres de funciones y variables en español, y type hints donde ayuden a leer la firma.

---

## Herramientas

Ya instaladas en macOS: `clang++` (Apple clang), `make`, `clangd`, `lldb`, `python3`.

Recomendado instalar:

```sh
brew install clang-format
code --install-extension llvm-vs-code-extensions.vscode-clangd
code --install-extension usernamehw.errorlens
code --install-extension EditorConfig.EditorConfig
code --install-extension ms-python.python
```

`clangd` reemplaza el IntelliSense de la extensión *C/C++* de Microsoft (ya está desactivado en `.vscode/settings.json`). Se recomienda desinstalar *CMake Tools* y *C/C++ Runner*, no se usan aquí.

La indentación base (4 espacios, LF, sin espacios al final) la fija `.editorconfig`.
Aún no hay un `.clang-format` en el repo: si quieres formato automático de C++, crea uno con
`clang-format -style=Google -dump-config > .clang-format` y activa `"editor.formatOnSave": true`
en `.vscode/settings.json`.
