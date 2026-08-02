# ============================================================
# COMPILER
# ============================================================
CXX = g++

# ============================================================
# COMPILATION FLAGS
# ============================================================
BASE_FLAGS      = -std=c++17 -Wall -Wextra -Wshadow -Wpedantic -g
SANFLAGS        = -fsanitize=address,undefined
CXXFLAGS_NORMAL = $(BASE_FLAGS)
CXXFLAGS_ASAN   = $(BASE_FLAGS) $(SANFLAGS)

# ============================================================
# DIRECTORIES
# ============================================================
BUILD_NORMAL = build
BUILD_ASAN   = buildasan

# ============================================================
# SOURCE FILES AND TARGETS
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
# MAIN RULES
# ============================================================
.DEFAULT_GOAL := all
MAKEFLAGS += --no-builtin-rules
.SUFFIXES:

all: $(TARGETS_NORMAL)
asan: $(TARGETS_ASAN)

# ============================================================
# COMPILATION
# ============================================================
$(BUILD_NORMAL)/%: %.cpp | $(BUILD_NORMAL)
	$(CXX) $(CXXFLAGS_NORMAL) -MMD -MP $< -o $@

$(BUILD_ASAN)/%: %.cpp | $(BUILD_ASAN)
	$(CXX) $(CXXFLAGS_ASAN) $< -o $@

$(BUILD_NORMAL) $(BUILD_ASAN):
	mkdir -p $@

# ============================================================
# EXECUTE
# ============================================================
run-%: $(BUILD_NORMAL)/%
	@echo ">>> Executing $*"
	./$(BUILD_NORMAL)/$*

run-asan-%: $(BUILD_ASAN)/%
	@echo ">>> Executing $* (ASan)"
	./$(BUILD_ASAN)/$*

# ============================================================
# CLEAN UP
# ============================================================
clean:
	rm -rf $(BUILD_NORMAL) $(BUILD_ASAN)

# ============================================================
# HELP
# ============================================================
help:
	@echo "Usage:"
	@echo "  make                    → compile all"
	@echo "  make asan               → compile all with ASan"
	@echo "  make run-<name>         → compile and execute"
	@echo "  make run-asan-<name>    → compile and execute with ASan"
	@echo "  make clean              → clean build files"

# ============================================================
# PHONY
# ============================================================
.PHONY: all asan clean help