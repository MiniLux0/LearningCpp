# 🚀 Section 01: Getting Started — C++ Fundamentals

> **Lessons**: L01 – L05  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 01) / Stanford CS106L (Lecture 01 & 02)  
> 🎯 **Primary Focus**: C++ program anatomy, compilation pipeline, namespaces, formatting, user input (`std::cin`), and initial interactive applications.

---

## 📌 Module Overview

This module covers the first steps of C++ programming. It introduces the GCC compilation model, preprocessor directives (`#include`), entry point mechanics (`int main()`), output formatting (`std::cout`, `\n`, `std::endl`), scope management via namespaces (`std::`), and interactive console input (`std::cin`).

---

## 📚 Academic Source & PDF Alignment

| Lesson | Academic PDF Source | Key Theoretical Topics Covered |
|--------|---------------------|--------------------------------|
| **L01–L03** | 📄 [`MIT 6.096 Lecture 01`](../files/mit6096/lectures/Lecture01_Introduction.pdf) | C++ compilation pipeline (Source $\rightarrow$ Preprocessor $\rightarrow$ Compiler $\rightarrow$ Linker $\rightarrow$ Binary), `main()` return codes, namespaces, escape sequences (`\n`, `\t`). |
| **L04–L05** | 📄 [`Stanford CS106L Lecture 01-02`](../files/cs106l/lectures/WLecture1_intro.pdf) | Interactive stream I/O (`std::cin`), stream extraction operator (`>>`), type safety, handling console buffers. |

---

## 💻 Lessons & Code Inventory (`01_GettingStarted/code/`)

| # | Lesson | Code File | Key Technical Concepts | Status |
|---|--------|-----------|------------------------|:------:|
| **L01** | **Hello World** | [`L01_HelloWorld.cpp`](code/L01_HelloWorld.cpp) | Entry point `main()`, `#include <iostream>`, `std::cout`, stream insertion `<<`, return status `0`. | ✅ |
| **L02** | **Namespaces** | [`L02_Namespaces.cpp`](code/L02_Namespaces.cpp) | Scope resolution `::`, `using namespace std;` vs explicit `std::`, preventing symbol naming collisions. | ✅ |
| **L03** | **Comments & Formatting** | [`L03_CommentsAndFormatting.cpp`](code/L03_CommentsAndFormatting.cpp) | Single-line `//` and multi-line `/* */` comments, escape sequences (`\n`, `\t`, `\"`), `std::endl` vs `\n`. | ✅ |
| **L04** | **Interactive User Input** | [`L04_UserInputCin.cpp`](code/L04_UserInputCin.cpp) | `std::cin` stream input, variable binding, combining `cin` and `cout` for interactive CLI prompts. | ✅ |
| **L05** | **Profile Generator App** | [`L05_InteractiveProfileApp.cpp`](code/L05_InteractiveProfileApp.cpp) | Capstone mini-project combining user inputs, formatted output cards, and interactive variables. | ✅ |

---

## 🛠️ How to Compile & Run

To compile and run the code files in this module:

```bash
# Navigate to the code directory
cd 01_GettingStarted/code

# Compile all lessons using Makefile
make

# Run a specific lesson executable
.\L01_HelloWorld.exe
.\L05_InteractiveProfileApp.exe
```

---

## 📁 Directory Structure

```
01_GettingStarted/
├── README.md               # 📄 Module guide (this file)
├── code/                   # C++ source files (L01–L05) & Makefile
│   ├── L01_HelloWorld.cpp
│   ├── L02_Namespaces.cpp
│   ├── L03_CommentsAndFormatting.cpp
│   ├── L04_UserInputCin.cpp
│   ├── L05_InteractiveProfileApp.cpp
│   └── makefile
├── theory/                 # Detailed Markdown notes & theory docs
└── exercise/               # Practical exercises and self-assessment challenges
```

---

## 🔗 Navigation & Quick Links

- ⬅️ [Back to Repository Root (`README.md`)](../README.md)
- 📋 [Master Syllabus (`TEMARIO.md`)](../TEMARIO.md)
- 🌐 [Academic Files Hub (`files/README.md`)](../files/README.md)
- ➡️ [Next Module: Section 02 — Basic Syntax](../02_BasicSyntax/README.md)

---
*MiniLux0 — Learning C++ Section 01*
