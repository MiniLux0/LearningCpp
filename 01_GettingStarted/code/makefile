# ============================================================
# COMPILADOR
# ============================================================
CXX = g++

# ============================================================
# FLAGS DE COMPILACION
# ============================================================
BASE_FLAGS      = -std=c++17 -Wall -Wextra -Wshadow -Wpedantic -g
SANFLAGS        = -fsanitize=address,undefined
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
# DEPENDENCY FILES
# ============================================================
DEPS = $(patsubst %.cpp, $(BUILD_NORMAL)/%.d, $(SOURCES))
-include $(DEPS)

# ============================================================
# REGLAS PRINCIPALES
# ============================================================
.DEFAULT_GOAL := all
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
# EJECUTAR
# ============================================================
run-%: $(BUILD_NORMAL)/%
	@echo ">>> Ejecutando $*"
	./$(BUILD_NORMAL)/$*

run-asan-%: $(BUILD_ASAN)/%
	@echo ">>> Ejecutando $* (ASan)"
	./$(BUILD_ASAN)/$*

# ============================================================
# LIMPIEZA
# ============================================================
clean:
	rm -rf $(BUILD_NORMAL) $(BUILD_ASAN)

# ============================================================
# AYUDA
# ============================================================
help:
	@echo "Uso:"
	@echo "  make                    → compilar todo"
	@echo "  make asan               → compilar todo con ASan"
	@echo "  make run-<nombre>       → compilar y ejecutar"
	@echo "  make run-asan-<nombre>  → ídem con ASan"
	@echo "  make clean              → limpiar builds"

# ============================================================
# PHONY
# ============================================================
.PHONY: all asan clean help