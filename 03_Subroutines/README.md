<div align="center">

# 🚀 Section 03: Subroutines — Functions, Pass-by-Reference & Header Files

> **Lessons**: L23 – L26  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 03) / Stanford CS106L (Lectures 03 & 04)  
> 📝 **Executive Summary**: 📝 [**`summary/03_Subroutines_Notes.md`**](summary/03_Subroutines_Notes.md)  
> 🎯 **Primary Focus**: Subroutines, return types, pass-by-value vs pass-by-reference (`&`, `const &`), function overloading, header prototypes (`.h`), and variable scope/lifetime.

---

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| [**⬅️ Section 02: Basic Syntax**](../02_BasicSyntax/README.md) | **Section 03: Subroutines** | [**Section 04: Arrays & Strings ➡️**](../04_ArraysStrings/README.md) |

</div>

---

## 📌 Module Overview

This module covers code modularization in C++: function declarations and signatures, return types, value vs reference passing (`&`, `const &`), function overloading, separate compilation using header files (`.h` / `.cpp`), and scope/lifetime management.

---

## 📋 Lessons, Theory & Code Inventory

| # | Lesson Name | 📘 Theory Note | 💻 Code Lab | Key Technical Concepts | Status |
|---|-------------|----------------|-------------|------------------------|:------:|
| **L23** | **Functions Anatomy** | 📘 [`theory/L23_Functions.md`](theory/L23_Functions.md) | 💻 [`code/L23_Functions.cpp`](code/L23_Functions.cpp) | Function declaration, parameters, return type, `void`. | ✅ |
| **L24** | **Return Values** | 📘 [`theory/L24_ReturnValues.md`](theory/L24_ReturnValues.md) | 💻 [`code/L24_ReturnValues.cpp`](code/L24_ReturnValues.cpp) | `return` statement, return values, function overloading rules. | ✅ |
| **L25** | **Parameters & References** | 📘 [`theory/L25_FunctionParameters.md`](theory/L25_FunctionParameters.md) | 💻 [`code/L25_FunctionParameters.cpp`](code/L25_FunctionParameters.cpp) | Pass-by-value vs pass-by-reference (`&`), `const &` efficiency. | ✅ |
| **L26** | **Headers & Prototypes** | 📘 [`theory/L26_HeadersAndPrototypes.md`](theory/L26_HeadersAndPrototypes.md) | 💻 [`code/L26_HeadersAndPrototypes.cpp`](code/L26_HeadersAndPrototypes.cpp) | Function prototypes, `.h` and `.cpp` separation, include guards. | ✅ |

---

## 🎯 Practical Exercises (E01 – E05)

> 📖 **Exercise Guide**: 📂 [**`exercise/README.md`**](exercise/README.md)

| # | Exercise Name | Topic | 💻 Solution File | Status |
|---|---------------|-------|------------------|:------:|
| **E01** | **Function Basics** | Function declarations & returns | 💻 [`exercise/E01_FunctionBasics.cpp`](exercise/E01_FunctionBasics.cpp) | ✅ |
| **E02** | **Pass by Reference** | Direct parameter mutation via `&` | 💻 [`exercise/E02_PassByReference.cpp`](exercise/E02_PassByReference.cpp) | ✅ |
| **E03** | **Swap Function** | In-place variable swapping with references | 💻 [`exercise/E03_SwapFunction.cpp`](exercise/E03_SwapFunction.cpp) | ✅ |
| **E04** | **Overloading** | Function overloading by parameter types | 💻 [`exercise/E04_Overloading.cpp`](exercise/E04_Overloading.cpp) | ✅ |
| **E05** | **Header Prototypes** | Prototypes & separate compilation | 💻 [`exercise/E05_HeaderPrototypes.cpp`](exercise/E05_HeaderPrototypes.cpp) | ✅ |

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L23–L25** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) | Subroutine stack frames, return types, pass-by-value vs pass-by-reference, function overloading. |
| **L26** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) \| [`CS106L Lecture 03`](../files/cs106l/lectures/WLecture_3_Init_and_Ref.pdf) | Function prototypes, header file separation (`.h` / `.cpp`), `#ifndef` include guards, reference semantics. |

---

## 🛠️ Build & Compilation Guides

Both `code/` and `exercise/` subdirectories contain automated `makefile` scripts:
- ⚙️ **Compilation Tutorial**: [`docs/COMPILATION_GUIDE.md`](../docs/COMPILATION_GUIDE.md)
- 🛠️ **Makefile & Sanitizer Reference**: [`docs/MAKEFILE_GUIDE.md`](../docs/MAKEFILE_GUIDE.md)

> [!TIP]
> **New to C++ compilation?**
> If you don't know how to compile or run C++ code from your terminal, refer to the documentation hub in 📂 [**`docs/README.md`**](../docs/README.md).

---
*MiniLux0 — Learning C++ Section 03*
