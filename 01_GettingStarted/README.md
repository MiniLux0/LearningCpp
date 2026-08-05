<div align="center">

# 🚀 Section 01: Getting Started — C++ Fundamentals for Beginners

> **Lessons**: L01 – L05  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 01) / Stanford CS106L (Lecture 01)  
> 📝 **Executive Summary**: 📝 [**`summary/01_GettingStarted_Notes.md`**](summary/01_GettingStarted_Notes.md)  
> 🎯 **Primary Focus**: Program structure, GCC compilation, namespaces, formatting, comments, `std::cin` & `std::cout` I/O streams.

---

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| **Start of Course** | **Section 01: Getting Started** | [**Section 02: Basic Syntax ➡️**](../02_BasicSyntax/README.md) |

</div>

---

## 📌 Module Overview

This module introduces the basic syntax and structure of a C++ program: `#include` directives, `main()` entry point, output streams (`std::cout`), namespaces (`std::`), code comments, output formatting, and interactive input reading (`std::cin`).

---

## 📋 Lessons, Theory & Code Inventory

| # | Lesson Name | 📘 Theory Note | 💻 Code Lab | Key Technical Concepts | Status |
|---|-------------|----------------|-------------|------------------------|:------:|
| **L01** | **Hello World** | 📘 [`theory/L01_HelloWorld.md`](theory/L01_HelloWorld.md) | 💻 [`code/L01_HelloWorld.cpp`](code/L01_HelloWorld.cpp) | Entry point `main()`, `#include <iostream>`, `cout`, `return 0`. | ✅ |
| **L02** | **Namespaces** | 📘 [`theory/L02_NamespacesAndStd.md`](theory/L02_NamespacesAndStd.md) | 💻 [`code/L02_NamespacesAndStd.cpp`](code/L02_NamespacesAndStd.cpp) | Scope resolution `std::`, `using namespace std`, avoiding collisions. | ✅ |
| **L03** | **Comments & Formatting** | 📘 [`theory/L03_CommentsAndFormatting.md`](theory/L03_CommentsAndFormatting.md) | 💻 [`code/L03_CommentsAndFormatting.cpp`](code/L03_CommentsAndFormatting.cpp) | Line `//` and block `/* */` comments, `\n` vs `endl`, escape sequences. | ✅ |
| **L04** | **User Input** | 📘 [`theory/L04_UserInputCin.md`](theory/L04_UserInputCin.md) | 💻 [`code/L04_UserInputCin.cpp`](code/L04_UserInputCin.cpp) | Input stream `std::cin`, extraction operator `>>`, interactive prompts. | ✅ |
| **L05** | **Profile App** | 📘 [`theory/L05_InteractiveProfileApp.md`](theory/L05_InteractiveProfileApp.md) | 💻 [`code/L05_InteractiveProfileApp.cpp`](code/L05_InteractiveProfileApp.cpp) | Mini-project combining I/O, formatting, and standard namespaces. | ✅ |

---

## 🎯 Practical Exercises (E01 – E05)

> 📖 **Exercise Guide**: 📂 [**`exercise/README.md`**](exercise/README.md)

| # | Exercise Name | Topic | 💻 Solution File | Status |
|---|---------------|-------|------------------|:------:|
| **E01** | **Hello World** | Program structure & `cout` | 💻 [`exercise/E01_HelloWorld.cpp`](exercise/E01_HelloWorld.cpp) | ✅ |
| **E02** | **Escape Sequences** | Text formatting & `\n` | 💻 [`exercise/E02_EscapeSequences.cpp`](exercise/E02_EscapeSequences.cpp) | ✅ |
| **E03** | **Namespaces** | `using namespace std;` vs `std::` | 💻 [`exercise/E03_Namespaces.cpp`](exercise/E03_Namespaces.cpp) | ✅ |
| **E04** | **Interactive Greeting** | Input reading with `cin` | 💻 [`exercise/E04_InteractiveGreeting.cpp`](exercise/E04_InteractiveGreeting.cpp) | ✅ |
| **E05** | **Formatted Receipt** | Formatting & input/output integration | 💻 [`exercise/E05_FormattedReceipt.cpp`](exercise/E05_FormattedReceipt.cpp) | ✅ |

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L01–L03** | 📄 [`MIT 6.096 Lecture 01`](../files/mit6096/lectures/Lecture01_Introduction.pdf) | C++ compilation pipeline, anatomy of `main()`, streams, namespaces. |
| **L04–L05** | 📄 [`CS106L Lecture 01`](../files/cs106l/lectures/WLecture1_intro.pdf) | Standard stream abstractions, `cin` extraction, console formatting. |

---

## 🛠️ Build & Compilation Guides

Both `code/` and `exercise/` subdirectories contain automated `makefile` scripts:
- ⚙️ **Compilation Tutorial**: [`docs/COMPILATION_GUIDE.md`](../docs/COMPILATION_GUIDE.md)
- 🛠️ **Makefile & Sanitizer Reference**: [`docs/MAKEFILE_GUIDE.md`](../docs/MAKEFILE_GUIDE.md)

> [!TIP]
> **New to C++ compilation?**
> If you don't know how to compile or run C++ code from your terminal, refer to the documentation hub in 📂 [**`docs/README.md`**](../docs/README.md).

---
*MiniLux0 — Learning C++ Section 01*
