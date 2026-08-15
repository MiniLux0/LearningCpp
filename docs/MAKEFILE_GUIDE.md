# 🛠️ C++ Makefile & Build System Guide

A comprehensive guide explaining how the automated build system works in this repository, how to use it, and how to adopt it as a professional template for any C++ project.

---

## 📌 What is a Makefile?

A `Makefile` is an automation script used by the `make` utility. Instead of manually invoking compiler commands like:
```bash
g++ -std=c++17 -Wall -Wextra L01_HelloWorld.cpp -o L01_HelloWorld
```
The `Makefile` automates compilation, manages build artifacts, tracks header dependencies, and provides memory sanitizer tooling with single-word terminal commands (e.g., `make`).

---

## 🚩 Deep-Dive: Compiler Flags Explained

Here is an explicit breakdown of the compiler flags enforced in this build system:

| Compiler Flag | Purpose | Why It Matters |
|---------------|---------|----------------|
| `-std=c++17` | Standard Enforcer | Sets the ISO C++ language version to **C++17**, enabling modern features like structured bindings, `std::optional`, and `if` init-statements. |
| `-Wall` | All Warnings | Enables a broad set of standard warnings (e.g., uninitialized variables, unused functions, missing return statements). |
| `-Wextra` | Extra Warnings | Enables additional strict warnings not covered by `-Wall` (e.g., signed/unsigned comparison mismatches, unused parameters). |
| `-Wshadow` | Shadowing Warning | Warns whenever a local variable name shadows/hides a variable from an outer scope, preventing subtle scope bugs. |
| `-Wpedantic` | ISO Compliance | Rejects non-standard compiler extensions and enforces strict compliance with the ISO C++ standard for maximum portability. |
| `-g` | Debug Symbols | Emits DWARF debugging symbols into the executable, allowing step-by-step debugging with GDB, LLDB, or VSCode. |
| `-MMD -MP` | Dependency Tracking | Instructs GCC to output `.d` files containing header file dependencies so `make` re-compiles only changed files. |
| `-fsanitize=address` | AddressSanitizer (ASan) | Instruments memory operations to detect **Memory Leaks**, **Use-After-Free**, and **Out-of-Bounds Buffer Access** at runtime. |
| `-fsanitize=undefined` | UndefinedBehaviorSanitizer (UBSan) | Detects runtime **Undefined Behavior** (e.g., signed integer overflow, null pointer dereferences, divide-by-zero). |

---

## 🚀 Key Features of This Makefile Template

1. **Automatic Source Discovery**: Uses `$(wildcard *.cpp)` to detect all `.cpp` files in a directory automatically — no hardcoding filenames required.
2. **Modern C++ Standard**: Enforces C++17 (`-std=c++17`).
3. **Strict Industrial Warnings**: Compiles with `-Wall -Wextra -Wshadow -Wpedantic` to catch subtle bugs, uninitialized variables, and non-portable code early.
4. **Dual Build Target Engine**:
   - **Normal Build (`make`)**: Fast, optimized build stored in `build/`.
   - **AddressSanitizer Build (`make asan`)**: Instrumentation build stored in `buildasan/` compiled with `-fsanitize=address,undefined` to catch memory leaks, out-of-bounds access, and use-after-free bugs.
5. **Automatic Dependency Tracking (`.d`)**: Generates dependency files so modifying a `.h` file only recompiles the `.cpp` files that include it.
6. **One-Command Execution**: Run any program instantly with `make run-<filename>`.

---

## 📋 Command Reference

Run these commands from any module directory containing the `makefile`:

| Command | Action | Description |
|---------|--------|-------------|
| `make` | Build All | Compiles all `.cpp` files into the `build/` directory |
| `make asan` | Build with Sanitizers | Compiles all `.cpp` files with **AddressSanitizer** into `buildasan/` |
| `make run-<filename>` | Build & Run | Compiles and executes `build/<filename>` (e.g., `make run-L01_HelloWorld`) |
| `make run-asan-<filename>` | Build & Run (ASan) | Compiles and executes with AddressSanitizer active |
| `make clean` | Clean Artifacts | Deletes `build/` and `buildasan/` build directories |
| `make help` | View Help | Displays interactive usage instructions in terminal |

---

## 🔍 Line-by-Line Architecture

Here is how the template is configured:

```makefile
# 1. Compiler Selection
CXX = g++

# 2. Strict Flag Configuration
BASE_FLAGS      = -std=c++17 -Wall -Wextra -Wshadow -Wpedantic -g
SANFLAGS        = -fsanitize=address,undefined
CXXFLAGS_NORMAL = $(BASE_FLAGS)
CXXFLAGS_ASAN   = $`(BASE_FLAGS) `$(SANFLAGS)

# 3. Output Directories
BUILD_NORMAL = build
BUILD_ASAN   = buildasan

# 4. Automatic Source & Target Mapping
SOURCES        = $(wildcard *.cpp)
TARGETS_NORMAL = $`(patsubst %.cpp, `$(BUILD_NORMAL)/%, $(SOURCES))
TARGETS_ASAN   = $`(patsubst %.cpp, `$(BUILD_ASAN)/%, $(SOURCES))

# 5. Dependency File Generation
DEPS = $`(patsubst %.cpp, `$(BUILD_NORMAL)/%.d, $(SOURCES))
-include $(DEPS)

# 6. Compilation Rules
$`(BUILD_NORMAL)/%: %.cpp | `$(BUILD_NORMAL)
	$`(CXX) `$(CXXFLAGS_NORMAL) -MMD -MP $`< -o `$@

# 7. One-Touch Execution Rule
run-%: $(BUILD_NORMAL)/%
	@echo ">>> Executing $*"
	./$`(BUILD_NORMAL)/`$*

# 8. Clean Rule
clean:
	rm -rf $`(BUILD_NORMAL) `$(BUILD_ASAN)

.PHONY: all asan clean help
```

---

## 💡 How to Re-use This Template in Your Own C++ Projects

You can copy the root `makefile` into **any directory containing `.cpp` files**. It requires **zero modifications** to work out-of-the-box!

```bash
# Example: Copying Makefile to a new project folder
cp /path/to/LearningCpp/makefile ./MyProject/makefile
cd MyProject
make
```

---

*MiniLux0 — C++ Build System Guide*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>