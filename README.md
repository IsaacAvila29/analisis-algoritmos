# Análisis de Algoritmos — C++

Repositorio de ejercicios de la materia. Cada ejercicio es un `.cpp` independiente dentro de una carpeta por tema.

## Estructura

```
00-plantilla/plantilla.cpp   # punto de partida para cada ejercicio
01-<tema>/ejercicio.cpp      # un programa por archivo
include/timer.hpp            # medición de tiempos (std::chrono)
Makefile                     # compila cualquier archivo suelto
bin/                         # binarios (ignorado por git)
```

Convención: carpetas con prefijo numérico (`01-ordenamiento`, `02-recursion`, …) y archivos en `snake_case.cpp`.

## Compilar y ejecutar

```sh
make run     FILE=01-ordenamiento/bubble_sort.cpp   # -O0 -g (desarrollo)
make release FILE=01-ordenamiento/bubble_sort.cpp   # -O2   (medir tiempos)
make debug   FILE=01-ordenamiento/bubble_sort.cpp   # AddressSanitizer + UBSan
make build   FILE=...                               # solo compilar → bin/bubble_sort
make clean
```

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

## Herramientas

Ya instaladas en macOS: `clang++` (Apple clang), `make`, `clangd`, `lldb`.

Recomendado instalar:

```sh
brew install clang-format
code --install-extension llvm-vs-code-extensions.vscode-clangd
code --install-extension usernamehw.errorlens
code --install-extension EditorConfig.EditorConfig
```

`clangd` reemplaza el IntelliSense de la extensión *C/C++* de Microsoft (ya está desactivado en `.vscode/settings.json`). Se recomienda desinstalar *CMake Tools* y *C/C++ Runner*, no se usan aquí.

El formato se aplica al guardar usando `.clang-format` (estilo Google, 4 espacios, 100 columnas).

## Buenas prácticas para los ejercicios

- Copia `00-plantilla/plantilla.cpp` para empezar.
- `ios::sync_with_stdio(false); cin.tie(nullptr);` para entrada grande.
- Compila siempre con `-Wall -Wextra -Wpedantic` (ya en el Makefile) y corrige los warnings.
- Prefiere `size_t`/`long long` donde pueda haber overflow; `int` de 32 bits se desborda en ~2.1e9.
- Comenta la complejidad (tiempo y espacio) al inicio de cada algoritmo.
