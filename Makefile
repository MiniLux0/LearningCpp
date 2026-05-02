# ============================================================
# COMPILADOR
# ============================================================
CXX = g++

# ============================================================
# FLAGS DE COMPILACION
# ============================================================
BASE_FLAGS = -std=c++17 -Wall -Wextra -Wshadow -Wpedantic -g

SANFLAGS = -fsanitize=address,undefined

CXXFLAGS_NORMAL = $(BASE_FLAGS)
CXXFLAGS_ASAN   = $(BASE_FLAGS) $(SANFLAGS)

# ============================================================
# DIRECTORIOS
# ============================================================
BUILD_NORMAL = build
BUILD_ASAN   = buildasan

# ============================================================
# ARCHIVOS FUENTE Y TARGETS
# ============================================================
SOURCES        = $(wildcard *.cpp)
TARGETS_NORMAL = $(patsubst %.cpp, $(BUILD_NORMAL)/%, $(SOURCES))
TARGETS_ASAN   = $(patsubst %.cpp, $(BUILD_ASAN)/%, $(SOURCES))

# ============================================================
# DEPENDENCY FILES (.d)
# ============================================================
DEPS = $(patsubst %.cpp, $(BUILD_NORMAL)/%.d, $(SOURCES))
-include $(DEPS)

# ============================================================
# REGLAS PRINCIPALES
# ============================================================
.DEFAULT_GOAL := all

# Desactiva reglas implícitas built-in (evita que Make compile en el root)
MAKEFLAGS += --no-builtin-rules
.SUFFIXES:

all: $(TARGETS_NORMAL)

asan: $(TARGETS_ASAN)

# ============================================================
# COMPILACION
# ============================================================
$(BUILD_NORMAL)/%: %.cpp | $(BUILD_NORMAL)
	$(CXX) $(CXXFLAGS_NORMAL) -MMD -MP $< -o $@

$(BUILD_ASAN)/%: %.cpp | $(BUILD_ASAN)
	$(CXX) $(CXXFLAGS_ASAN) $< -o $@

$(BUILD_NORMAL) $(BUILD_ASAN):
	mkdir -p $@

# ============================================================
# EJECUTAR PROGRAMAS
# ============================================================
run-%: $(BUILD_NORMAL)/%
	@echo ">>> Ejecutando $*"
	./$(BUILD_NORMAL)/$*

run-asan-%: $(BUILD_ASAN)/%
	@echo ">>> Ejecutando $* (ASan)"
	./$(BUILD_ASAN)/$*

run-all-normal: $(TARGETS_NORMAL)
	@for exe in $(TARGETS_NORMAL); do \
		echo ">>> $$exe"; \
		./$$exe; \
	done

run-all-asan: $(TARGETS_ASAN)
	@for exe in $(TARGETS_ASAN); do \
		echo ">>> $$exe"; \
		./$$exe; \
	done

# ============================================================
# COMPILE COMMANDS
# ============================================================
compile_commands:
	compiledb make

# ============================================================
# LIMPIEZA
# ============================================================
clean:
	rm -rf $(BUILD_NORMAL) $(BUILD_ASAN)

# ============================================================
# SHORTCUT: make <nombre> compila en build/
# ============================================================
%: $(BUILD_NORMAL)/%
	@:

# ============================================================
# AYUDA
# ============================================================
help:
	@echo "Targets disponibles:"
	@echo "  make                    → compilar todo (normal)"
	@echo "  make asan               → compilar todo (ASan)"
	@echo "  make run-<nombre>       → compilar y ejecutar <nombre>.cpp"
	@echo "  make run-asan-<nombre>  → ídem con ASan"
	@echo "  make clean              → eliminar builds"

# ============================================================
# PHONY
# ============================================================
.PHONY: all asan run-all-normal run-all-asan compile_commands clean help