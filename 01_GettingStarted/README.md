<div align="center">

# 🚀 Section 01: Getting Started — C++ Fundamentals

> **Lessons**: L01 – L05  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 01) / Stanford CS106L (Lectures 01 & 02)  
> 📖 **Theory Directory**: 📂 [**`01_GettingStarted/theory/`**](theory/)  
> 🎯 **Primary Focus**: Program anatomy, compilation pipeline, namespaces, formatting, user input (`std::cin`), and initial interactive applications.

---

### 🧭 Module Navigation Hub

[![Root README](https://img.shields.io/badge/🏠_Root-README-00599C?style=for-the-badge)](../README.md)
[![Master Syllabus](https://img.shields.io/badge/📜_Master-TEMARIO-F16822?style=for-the-badge)](../TEMARIO.md)
[![Academic Guide](https://img.shields.io/badge/🌐_Academic-Guide-007ACC?style=for-the-badge)](../files/Master_Academic_Guide.md)
[![Resources](https://img.shields.io/badge/📚_Resources-Catalog-2ea44f?style=for-the-badge)](../RESOURCES.md)

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| 🏠 [**Root Index**](../README.md) | **Section 01: Getting Started** | [**Section 02: Basic Syntax ➡️**](../02_BasicSyntax/README.md) |

</div>

---

## 📌 Module Overview

This module covers the first steps of C++ programming. It introduces the GCC compilation model, preprocessor directives (`#include`), entry point mechanics (`int main()`), output formatting (`std::cout`, `\n`, `std::endl`), scope management via namespaces (`std::`), and interactive console input (`std::cin`).

---

## 📋 Lessons, Theory & Code Inventory

| # | Lesson Name | 📘 Theory Note | 💻 Code Lab | Key Technical Concepts | Status |
|---|-------------|----------------|-------------|------------------------|:------:|
| **L01** | **Hello World** | 📘 [`theory/L01_HelloWorld.md`](theory/L01_HelloWorld.md) | 💻 [`code/L01_HelloWorld.cpp`](code/L01_HelloWorld.cpp) | Entry point `main()`, `#include <iostream>`, `std::cout`, return status `0`. | ✅ |
| **L02** | **Namespaces** | 📘 [`theory/L02_NamespacesAndStd.md`](theory/L02_NamespacesAndStd.md) | 💻 [`code/L02_NamespacesAndStd.cpp`](code/L02_NamespacesAndStd.cpp) | Scope resolution `::`, `using namespace std;` vs explicit `std::`, naming collisions. | ✅ |
| **L03** | **Comments & Formatting** | 📘 [`theory/L03_CommentsAndFormatting.md`](theory/L03_CommentsAndFormatting.md) | 💻 [`code/L03_CommentsAndFormatting.cpp`](code/L03_CommentsAndFormatting.cpp) | Comments (`//`, `/* */`), escape sequences (`\n`, `\t`), `std::endl` vs `\n`. | ✅ |
| **L04** | **Interactive User Input** | 📘 [`theory/L04_UserInputCin.md`](theory/L04_UserInputCin.md) | 💻 [`code/L04_UserInputCin.cpp`](code/L04_UserInputCin.cpp) | `std::cin` stream input, variable binding, interactive CLI prompts. | ✅ |
| **L05** | **Profile Generator App** | 📘 [`theory/L05_InteractiveProfileApp.md`](theory/L05_InteractiveProfileApp.md) | 💻 [`code/L05_InteractiveProfileApp.cpp`](code/L05_InteractiveProfileApp.cpp) | Mini-project combining user inputs, formatted cards, and interactive variables. | ✅ |

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L01–L03** | 📄 [`MIT 6.096 Lecture 01`](../files/mit6096/lectures/Lecture01_Introduction.pdf) | C++ compilation pipeline (Source $\rightarrow$ Preprocessor $\rightarrow$ Compiler $\rightarrow$ Linker $\rightarrow$ Binary), `main()` return codes, namespaces, escape sequences. |
| **L04–L05** | 📄 [`Stanford CS106L Lecture 01-02`](../files/cs106l/lectures/WLecture1_intro.pdf) | Interactive stream I/O (`std::cin`), stream extraction operator (`>>`), type safety, handling console buffers. |

---

## 🛠️ How to Compile & Run

```bash
# Navigate to the code directory
cd 01_GettingStarted/code

# Compile all lessons using Makefile
make

# Run executables (Windows PowerShell / CMD)
.\L01_HelloWorld.exe
.\L05_InteractiveProfileApp.exe
```

---

<div align="center">

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| 🏠 [**Root Index**](../README.md) | **Section 01: Getting Started** | [**Section 02: Basic Syntax ➡️**](../02_BasicSyntax/README.md) |

</div>

---
*MiniLux0 — Learning C++ Section 01*
