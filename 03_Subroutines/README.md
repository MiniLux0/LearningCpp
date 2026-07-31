<div align="center">

# 🚀 Section 03: Subroutines — Functions, References & Header Files

> **Lessons**: L23 – L26  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 03) / Stanford CS106L (Lecture 03 & 04)  
> 📖 **Theory Documentation**: 📂 [**`03_Subroutines/theory/`**](theory/)  
> 🎯 **Primary Focus**: Modular function design, return types, parameter passing (by-value, by-reference `&`, `const &`), header file separation (`.h` / `.cpp`), and preprocessor guards.

---

### 🧭 Module Navigation Hub

[![Root README](https://img.shields.io/badge/🏠_Root-README-00599C?style=for-the-badge)](../README.md)
[![Master Syllabus](https://img.shields.io/badge/📜_Master-TEMARIO-F16822?style=for-the-badge)](../TEMARIO.md)
[![Academic Guide](https://img.shields.io/badge/🌐_Academic-Guide-007ACC?style=for-the-badge)](../files/Master_Academic_Guide.md)
[![Resources](https://img.shields.io/badge/📚_Resources-Catalog-2ea44f?style=for-the-badge)](../RESOURCES.md)

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| [**⬅️ Section 02: Basic Syntax**](../02_BasicSyntax/README.md) | **Section 03: Subroutines** | [**Section 04: Arrays & Strings ➡️**](../04_ArraysStrings/README.md) |

</div>

---

## 📌 Module Overview

This module focuses on function mechanics and procedural modularity. It covers function declarations vs definitions, return values, call stack allocation, parameter passing semantics (pass-by-value vs pass-by-reference), avoiding expensive copies with `const &`, function overloading, inline functions, and multi-file compilation using header files (`.h`) and include guards (`#ifndef` / `#define` / `#pragma once`).

---

## 📖 Theory & Conceptual Documentation (`03_Subroutines/theory/`)

All theoretical concepts, stack frame diagrams, and parameter passing rules for this module are documented in dedicated markdown notes:

- 📘 [**`theory/L23_Functions.md`**](theory/L23_Functions.md) — Function declarations, definitions, return types, argument passing, and stack frames.
- 📘 [**`theory/L24_ReturnValues.md`**](theory/L24_ReturnValues.md) — Return type mechanics, early returns, returning values vs returning references.
- 📘 [**`theory/L25_FunctionParameters.md`**](theory/L25_FunctionParameters.md) — Pass-by-value (copies) vs pass-by-reference (`T&`) vs `const` references (`const T&`).
- 📘 [**`theory/L26_HeadersAndPrototypes.md`**](theory/L26_HeadersAndPrototypes.md) — Forward declarations, header guards (`#ifndef`), multi-file compilation units, and linking.

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L23–L24** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) | Function prototypes, return type mechanics, call stack frame allocation, stack unwinding. |
| **L25** | 📄 [`Stanford CS106L Lecture 03`](../files/cs106l/lectures/WLecture_3_Init_and_Ref.pdf) | Pass-by-value vs pass-by-reference (`T&`), aliasing, `const` references (`const T&`) for zero-copy read-only parameters. |
| **L26** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) | Header separation (`utils.h` / `utils.cpp`), include guards (`#ifndef`), linker symbol resolution, compilation units. |

---

## 💻 Lessons, Code & Theory Inventory (`03_Subroutines/`)

| # | Lesson | Theory Note | Code Implementation | Key Technical Concepts | Status |
|---|--------|-------------|---------------------|------------------------|:------:|
| **L23** | **Functions Intro** | 📘 [`theory/L23_Functions.md`](theory/L23_Functions.md) | 💻 [`L23_Functions.cpp`](code/L23_Functions.cpp) | Function declaration, definition, void functions, argument passing, function scope. | ✅ |
| **L24** | **Return Values** | 📘 [`theory/L24_ReturnValues.md`](theory/L24_ReturnValues.md) | 💻 [`L24_ReturnValues.cpp`](code/L24_ReturnValues.cpp) | Returning values, early `return` statements, primitive and object return mechanics. | ✅ |
| **L25** | **Function Parameters** | 📘 [`theory/L25_FunctionParameters.md`](theory/L25_FunctionParameters.md) | 💻 [`L25_FunctionParameters.cpp`](code/L25_FunctionParameters.cpp) | Pass-by-value (copies) vs pass-by-reference (`&`), `const` references (`const &`), parameter mutation. | ✅ |
| **L26** | **Headers & Prototypes** | 📘 [`theory/L26_HeadersAndPrototypes.md`](theory/L26_HeadersAndPrototypes.md) | 💻 [`L26_HeadersAndPrototypes.cpp`](code/L26_HeadersAndPrototypes.cpp) | Forward declarations, function prototypes, multi-file code splitting (`.h` and `.cpp`), include guards `#ifndef`. | ✅ |

---

## 🛠️ How to Compile & Run

To compile and run the code files in this module:

```bash
# Navigate to the code directory
cd 03_Subroutines/code

# Compile all lessons using Makefile
make

# Run a specific lesson executable
.\L23_Functions.exe
.\L26_HeadersAndPrototypes.exe
```

---

## 📁 Directory Structure

```
03_Subroutines/
├── README.md               # 📄 Module guide (this file)
├── theory/                 # 📘 Detailed Markdown theory notes (L23–L26)
│   ├── L23_Functions.md
│   ├── L24_ReturnValues.md
│   ├── L25_FunctionParameters.md
│   └── L26_HeadersAndPrototypes.md
├── code/                   # 💻 C++ source files (L23–L26) & Makefile
│   ├── L23_Functions.cpp ... L26_HeadersAndPrototypes.cpp
│   └── makefile
└── exercise/               # ✏️ Practical exercises and function challenges
```

---

<div align="center">

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| [**⬅️ Section 02: Basic Syntax**](../02_BasicSyntax/README.md) | **Section 03: Subroutines** | [**Section 04: Arrays & Strings ➡️**](../04_ArraysStrings/README.md) |

</div>

---
*MiniLux0 — Learning C++ Section 03*
