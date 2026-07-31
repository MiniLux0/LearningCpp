# 🚀 Section 03: Subroutines — Functions, References & Header Files

> **Lessons**: L23 – L26  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 03) / Stanford CS106L (Lecture 03 & 04)  
> 🎯 **Primary Focus**: Modular function design, return types, parameter passing (by-value, by-reference `&`, `const &`), header file separation (`.h` / `.cpp`), and preprocessor guards.

---

## 📌 Module Overview

This module focuses on function mechanics and procedural modularity. It covers function declarations vs definitions, return values, call stack allocation, parameter passing semantics (pass-by-value vs pass-by-reference), avoiding expensive copies with `const &`, function overloading, inline functions, and multi-file compilation using header files (`.h`) and include guards (`#ifndef` / `#define` / `#pragma once`).

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L23–L24** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) | Function prototypes, return type mechanics, call stack frame allocation, stack unwinding. |
| **L25** | 📄 [`Stanford CS106L Lecture 03`](../files/cs106l/lectures/WLecture_3_Init_and_Ref.pdf) | Pass-by-value vs pass-by-reference (`T&`), aliasing, `const` references (`const T&`) for zero-copy read-only parameters. |
| **L26** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) | Header separation (`utils.h` / `utils.cpp`), include guards (`#ifndef`), linker symbol resolution, compilation units. |

---

## 💻 Lessons & Code Inventory (`03_Subroutines/code/`)

| # | Lesson | Code File | Key Technical Concepts | Status |
|---|--------|-----------|------------------------|:------:|
| **L23** | **Functions Intro** | [`L23_Functions.cpp`](code/L23_Functions.cpp) | Function declaration, definition, void functions, argument passing, function scope. | ✅ |
| **L24** | **Return Values** | [`L24_ReturnValues.cpp`](code/L24_ReturnValues.cpp) | Returning values, early `return` statements, primitive and object return mechanics. | ✅ |
| **L25** | **Function Parameters** | [`L25_FunctionParameters.cpp`](code/L25_FunctionParameters.cpp) | Pass-by-value (copies) vs pass-by-reference (`&`), `const` references (`const &`), parameter mutation. | ✅ |
| **L26** | **Headers & Prototypes** | [`L26_HeadersAndPrototypes.cpp`](code/L26_HeadersAndPrototypes.cpp) | Forward declarations, function prototypes, multi-file code splitting (`.h` and `.cpp`), include guards `#ifndef`. | ✅ |

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
├── code/                   # C++ source files (L23–L26) & Makefile
│   ├── L23_Functions.cpp
│   ├── L24_ReturnValues.cpp
│   ├── L25_FunctionParameters.cpp
│   ├── L26_HeadersAndPrototypes.cpp
│   └── makefile
├── theory/                 # Detailed Markdown notes & theory docs
└── exercise/               # Practical exercises and function challenges
```

---

## 🔗 Navigation & Quick Links

- ⬅️ [Previous Module: Section 02 — Basic Syntax](../02_BasicSyntax/README.md)
- 📋 [Master Syllabus (`TEMARIO.md`)](../TEMARIO.md)
- 🌐 [Academic Files Hub (`files/README.md`)](../files/README.md)
- ➡️ [Next Module: Section 04 — Arrays & Strings](../04_ArraysStrings/README.md)

---
*MiniLux0 — Learning C++ Section 03*
