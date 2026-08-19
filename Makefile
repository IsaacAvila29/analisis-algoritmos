# Makefile genérico: compila cualquier .cpp suelto a bin/<nombre>
#
#   make build   FILE=01-tema/ejercicio.cpp   -> bin/ejercicio (debug, -O0 -g)
#   make run     FILE=01-tema/ejercicio.cpp   -> compila y ejecuta
#   make release FILE=01-tema/ejercicio.cpp   -> -O2 (para medir tiempos)
#   make debug   FILE=01-tema/ejercicio.cpp   -> con AddressSanitizer + UBSan
#   make clean

CXX      := clang++
CXXFLAGS := -std=c++20 -Wall -Wextra -Wpedantic -Iinclude
DEBUG    := -g -O0
RELEASE  := -O2 -DNDEBUG
SANITIZE := -g -O1 -fsanitize=address,undefined -fno-omit-frame-pointer

BIN_DIR  := bin
NAME     := $(basename $(notdir $(FILE)))
OUT      := $(BIN_DIR)/$(NAME)

.PHONY: build run release debug clean check-file

check-file:
ifndef FILE
	$(error Falta FILE. Uso: make run FILE=01-tema/ejercicio.cpp)
endif

$(BIN_DIR):
	@mkdir -p $(BIN_DIR)

build: check-file | $(BIN_DIR)
	$(CXX) $(CXXFLAGS) $(DEBUG) $(FILE) -o $(OUT)

run: build
	@echo "── ejecutando $(OUT) ──"
	@./$(OUT)

release: check-file | $(BIN_DIR)
	$(CXX) $(CXXFLAGS) $(RELEASE) $(FILE) -o $(OUT)
	@echo "── ejecutando $(OUT) (release) ──"
	@./$(OUT)

debug: check-file | $(BIN_DIR)
	$(CXX) $(CXXFLAGS) $(SANITIZE) $(FILE) -o $(OUT)
	@echo "── ejecutando $(OUT) (sanitizers) ──"
	@./$(OUT)

clean:
	rm -rf $(BIN_DIR)
