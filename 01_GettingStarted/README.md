# 🚀 Section 01: Getting Started — C++ Fundamentals

> **Lessons**: L01 – L05  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 01) / Stanford CS106L (Lecture 01 & 02)  
> 📖 **Theory Documentation Directory**: 📂 [**`01_GettingStarted/theory/`**](theory/)  
> 🎯 **Primary Focus**: C++ program anatomy, compilation pipeline, namespaces, formatting, user input (`std::cin`), and initial interactive applications.

---

## 📌 Module Overview

This module covers the first steps of C++ programming. It introduces the GCC compilation model, preprocessor directives (`#include`), entry point mechanics (`int main()`), output formatting (`std::cout`, `\n`, `std::endl`), scope management via namespaces (`std::`), and interactive console input (`std::cin`).

---

## 📖 Theory & Conceptual Documentation (`01_GettingStarted/theory/`)

All theoretical concepts, compiler diagrams, and syntax rules for this module are documented in dedicated markdown notes:

- 📘 [**`theory/L01_HelloWorld.md`**](theory/L01_HelloWorld.md) — Program anatomy, `#include <iostream>`, `int main()`, and compilation phases.
- 📘 [**`theory/L02_NamespacesAndStd.md`**](theory/L02_NamespacesAndStd.md) — Scope resolution `::`, `using namespace std;` risks, and explicit namespace qualification.
- 📘 [**`theory/L03_CommentsAndFormatting.md`**](theory/L03_CommentsAndFormatting.md) — Commenting standards, escape sequences (`\n`, `\t`), and `std::endl` vs `\n` performance.
- 📘 [**`theory/L04_UserInputCin.md`**](theory/L04_UserInputCin.md) — Stream extraction `std::cin >>`, type safety, and buffer management.
- 📘 [**`theory/L05_InteractiveProfileApp.md`**](theory/L05_InteractiveProfileApp.md) — Profile card application design, string input, and stream formatting.

---

## 📚 Academic Source & PDF Alignment

| Lesson | Academic PDF Source | Key Theoretical Topics Covered |
|--------|---------------------|--------------------------------|
| **L01–L03** | 📄 [`MIT 6.096 Lecture 01`](../files/mit6096/lectures/Lecture01_Introduction.pdf) | C++ compilation pipeline (Source $\rightarrow$ Preprocessor $\rightarrow$ Compiler $\rightarrow$ Linker $\rightarrow$ Binary), `main()` return codes, namespaces, escape sequences (`\n`, `\t`). |
| **L04–L05** | 📄 [`Stanford CS106L Lecture 01-02`](../files/cs106l/lectures/WLecture1_intro.pdf) | Interactive stream I/O (`std::cin`), stream extraction operator (`>>`), type safety, handling console buffers. |

---

## 💻 Lessons, Code & Theory Inventory (`01_GettingStarted/`)

| # | Lesson | Theory Note | Code Implementation | Key Technical Concepts | Status |
|---|--------|-------------|---------------------|------------------------|:------:|
| **L01** | **Hello World** | 📘 [`theory/L01_HelloWorld.md`](theory/L01_HelloWorld.md) | 💻 [`L01_HelloWorld.cpp`](code/L01_HelloWorld.cpp) | Entry point `main()`, `#include <iostream>`, `std::cout`, stream insertion `<<`, return status `0`. | ✅ |
| **L02** | **Namespaces** | 📘 [`theory/L02_NamespacesAndStd.md`](theory/L02_NamespacesAndStd.md) | 💻 [`L02_Namespaces.cpp`](code/L02_Namespaces.cpp) | Scope resolution `::`, `using namespace std;` vs explicit `std::`, preventing symbol naming collisions. | ✅ |
| **L03** | **Comments & Formatting** | 📘 [`theory/L03_CommentsAndFormatting.md`](theory/L03_CommentsAndFormatting.md) | 💻 [`L03_CommentsAndFormatting.cpp`](code/L03_CommentsAndFormatting.cpp) | Single-line `//` and multi-line `/* */` comments, escape sequences (`\n`, `\t`, `\"`), `std::endl` vs `\n`. | ✅ |
| **L04** | **Interactive User Input** | 📘 [`theory/L04_UserInputCin.md`](theory/L04_UserInputCin.md) | 💻 [`L04_UserInputCin.cpp`](code/L04_UserInputCin.cpp) | `std::cin` stream input, variable binding, combining `cin` and `cout` for interactive CLI prompts. | ✅ |
| **L05** | **Profile Generator App** | 📘 [`theory/L05_InteractiveProfileApp.md`](theory/L05_InteractiveProfileApp.md) | 💻 [`L05_InteractiveProfileApp.cpp`](code/L05_InteractiveProfileApp.cpp) | Capstone mini-project combining user inputs, formatted output cards, and interactive variables. | ✅ |

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
├── theory/                 # 📘 Detailed Markdown theory notes (L01–L05)
│   ├── L01_HelloWorld.md
│   ├── L02_NamespacesAndStd.md
│   ├── L03_CommentsAndFormatting.md
│   ├── L04_UserInputCin.md
│   └── L05_InteractiveProfileApp.md
├── code/                   # 💻 C++ source files (L01–L05) & Makefile
│   ├── L01_HelloWorld.cpp ... L05_InteractiveProfileApp.cpp
│   └── makefile
└── exercise/               # ✏️ Practical exercises and self-assessment challenges
```

---

## 🔗 Navigation & Quick Links

- ⬅️ [Back to Repository Root (`README.md`)](../README.md)
- 📋 [Master Syllabus (`TEMARIO.md`)](../TEMARIO.md)
- 🌐 [Academic Files Hub (`files/README.md`)](../files/README.md)
- ➡️ [Next Module: Section 02 — Basic Syntax](../02_BasicSyntax/README.md)

---
*MiniLux0 — Learning C++ Section 01*
