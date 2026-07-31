<div align="center">

# 🚀 Section 03: Subroutines — Functions, References & Header Files

> **Lessons**: L23 – L26  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 03) / Stanford CS106L (Lectures 03 & 04)  
> 📖 **Theory Directory**: 📂 [**`03_Subroutines/theory/`**](theory/)  
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

This module covers function mechanics and procedural modularity: function declarations vs definitions, call stack allocation, parameter passing semantics (pass-by-value vs pass-by-reference), avoiding expensive copies with `const &`, function overloading, inline functions, multi-file compilation with headers (`.h`), and include guards (`#ifndef` / `#pragma once`).

---

## 📋 Lessons, Theory & Code Inventory

| # | Lesson Name | 📘 Theory Note | 💻 Code Lab | Key Technical Concepts | Status |
|---|-------------|----------------|-------------|------------------------|:------:|
| **L23** | **Functions Intro** | 📘 [`theory/L23_Functions.md`](theory/L23_Functions.md) | 💻 [`code/L23_Functions.cpp`](code/L23_Functions.cpp) | Function declaration, definition, void functions, stack scope. | ✅ |
| **L24** | **Return Values** | 📘 [`theory/L24_ReturnValues.md`](theory/L24_ReturnValues.md) | 💻 [`code/L24_ReturnValues.cpp`](code/L24_ReturnValues.cpp) | Returning values, early `return` statements, primitive/object return. | ✅ |
| **L25** | **Function Parameters** | 📘 [`theory/L25_FunctionParameters.md`](theory/L25_FunctionParameters.md) | 💻 [`code/L25_FunctionParameters.cpp`](code/L25_FunctionParameters.cpp) | Pass-by-value (copies) vs pass-by-reference (`&`), `const` references (`const &`). | ✅ |
| **L26** | **Headers & Prototypes** | 📘 [`theory/L26_HeadersAndPrototypes.md`](theory/L26_HeadersAndPrototypes.md) | 💻 [`code/L26_HeadersAndPrototypes.cpp`](code/L26_HeadersAndPrototypes.cpp) | Forward declarations, header file splitting (`.h`/`.cpp`), `#ifndef` guards. | ✅ |

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L23–L24** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) | Function prototypes, return type mechanics, call stack frame allocation, stack unwinding. |
| **L25** | 📄 [`Stanford CS106L Lecture 03`](../files/cs106l/lectures/WLecture_3_Init_and_Ref.pdf) | Pass-by-value vs pass-by-reference (`T&`), aliasing, `const` references (`const T&`) for zero-copy. |
| **L26** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) | Header separation (`utils.h` / `utils.cpp`), include guards (`#ifndef`), linker symbol resolution. |

---

## 🛠️ How to Compile & Run

```bash
# Navigate to the code directory
cd 03_Subroutines/code

# Compile all lessons using Makefile
make

# Run executables (Windows PowerShell / CMD)
.\L23_Functions.exe
.\L26_HeadersAndPrototypes.exe
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
