<div align="center">

# 🚀 Section 03: Subroutines — Functions, Pass by Reference & Headers

> **Lessons**: L23 – L26  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 03) / Stanford CS106L (Lectures 03 & 04) / Stanford CS106B (Chapter 2)  
> 📝 **Executive Summary**: 📝 [**`summary/03_Subroutines_Notes.md`**](summary/03_Subroutines_Notes.md)  
> 🎯 **Primary Focus**: Subroutines, return types, pass-by-value vs pass-by-reference (`&`, `const &`), function overloading, header prototypes (`.h`), and variable scope/lifetime.

---

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:-------------------:|:--------------:|
| [**⬅️ Section 02: Basic Syntax**](../02_BasicSyntax/README.md) | **Section 03: Subroutines** | [**Section 04: Arrays & Strings ➡️**](../04_ArraysStrings/README.md) |

</div>

---

## 📌 Module Overview

This module covers code modularization in C++: function declarations and signatures, return types, pass-by-value vs pass-by-reference (`&`, `const &`), function overloading, separate compilation using header files (`.h` / `.cpp`), and variable scope management.

---

## 📋 Lessons, Theory & Code Inventory

| # | Lesson Name | 📘 Theory Note | 💻 Code Lab | Key Technical Concepts | Status |
|---|-------------|----------------|-------------|------------------------|:------:|
| **L23** | **Function Basics** | 📘 [`theory/L23_Functions.md`](theory/L23_Functions.md) | 💻 [`code/L23_Functions.cpp`](code/L23_Functions.cpp) | Function declaration, parameters, return type, `void`, DRY principle. | ✅ |
| **L24** | **Return Values** | 📘 [`theory/L24_ReturnValues.md`](theory/L24_ReturnValues.md) | 💻 [`code/L24_ReturnValues.cpp`](code/L24_ReturnValues.cpp) | `return` statement, data flow, function overloading. | ✅ |
| **L25** | **Parameters & References** | 📘 [`theory/L25_FunctionParameters.md`](theory/L25_FunctionParameters.md) | 💻 [`code/L25_FunctionParameters.cpp`](code/L25_FunctionParameters.cpp) | Pass-by-value vs reference (`&`), optimization with `const &`. | ✅ |
| **L26** | **Headers & Prototypes** | 📘 [`theory/L26_HeadersAndPrototypes.md`](theory/L26_HeadersAndPrototypes.md) | 💻 [`code/L26_HeadersAndPrototypes.cpp`](code/L26_HeadersAndPrototypes.cpp) | Function prototypes, `.h` / `.cpp` separation, `#pragma once` guards. | ✅ |

---

## 🎯 Practical Exercises (E01 – E05)

> 📖 **Exercise Guide**: 📂 [**`exercise/README.md`**](exercise/README.md)

| # | Exercise Name | Topic | 💻 Solution File | Status |
|---|---------------|-------|------------------|:------:|
| **E01** | **Function Basics** | Declaration and returning values | 💻 [`exercise/E01_FunctionBasics.cpp`](exercise/E01_FunctionBasics.cpp) | ✅ |
| **E02** | **Pass by Reference** | Direct mutation with `&` | 💻 [`exercise/E02_PassByReference.cpp`](exercise/E02_PassByReference.cpp) | ✅ |
| **E03** | **Swap Function** | In-place variable swap with references | 💻 [`exercise/E03_SwapFunction.cpp`](exercise/E03_SwapFunction.cpp) | ✅ |
| **E04** | **Function Overloading** | Overloading by parameter type | 💻 [`exercise/E04_Overloading.cpp`](exercise/E04_Overloading.cpp) | ✅ |
| **E05** | **Header Prototypes** | Prototypes and separate compilation | 💻 [`exercise/E05_HeaderPrototypes.cpp`](exercise/E05_HeaderPrototypes.cpp) | ✅ |

---

## 📚 Academic Source Alignment

| Lessons | Academic Source PDF | Key Theoretical Topics |
|---------|---------------------|------------------------|
| **L23–L25** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) | Subroutine stack frames, return types, pass by value vs reference, overloading. |
| **L26** | 📄 [`MIT 6.096 Lecture 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) \| [`CS106L Lecture 03`](../files/cs106l/lectures/WLecture_3_Init_and_Ref.pdf) | Function prototypes, `.h` / `.cpp` separation, `#pragma once` guards. |

---

## 🛠️ Build & Compilation Guides

Both `code/` and `exercise/` subdirectories contain automated `makefile` scripts:
- ⚙️ **Compilation Tutorial**: [`docs/COMPILATION_GUIDE.md`](../docs/COMPILATION_GUIDE.md)
- 🛠️ **Makefile & Sanitizer Reference**: [`docs/MAKEFILE_GUIDE.md`](../docs/MAKEFILE_GUIDE.md)

> [!TIP]
> **New to C++ compilation?**
> If you don't know how to compile or run C++ code from your terminal, refer to the documentation hub in 📂 [**`docs/README.md`**](../docs/README.md).

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
