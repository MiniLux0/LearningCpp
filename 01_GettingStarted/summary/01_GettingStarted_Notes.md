# 📝 Section 01: Getting Started — Study Notes and Executive Summary

Study notes and executive summary for **Section 01: Getting Started and C++ Fundamentals**.
Covers the internal structure of a C++ program, preprocessor `#include` directives, the `main()` function, `std::cout` output stream, namespaces, comments and formatting, and user interaction via `std::cin`.

---

## 🧭 Table of Contents

1. [Lessons and Theory](#-lessons-and-theory)
2. [Practical Exercises (E01 – E05)](#-practical-exercises-e01--e05)
3. [Summary by Lesson](#-summary-by-lesson)
   - [L01 — Hello World & C++ Anatomy](#l01--hello-world--c-anatomy)
   - [L02 — Namespaces & std::](#l02--namespaces--std)
   - [L03 — Comments & Formatting](#l03--comments--formatting)
   - [L04 — Interactive User Input](#l04--interactive-user-input)
   - [L05 — Interactive Profile Generator](#l05--interactive-profile-generator)
4. [Best Practices and Key Patterns](#-best-practices-and-key-patterns)

---

## 📘 Lessons and Theory

| Lesson | Title | Theory Note | Code Lab |
| :--- | :--- | :--- | :--- |
| **L01** | Hello World | 📘 [`L01_HelloWorld.md`](../theory/L01_HelloWorld.md) | 💻 [`L01_HelloWorld.cpp`](../code/L01_HelloWorld.cpp) |
| **L02** | Namespaces & `std::` | 📘 [`L02_NamespacesAndStd.md`](../theory/L02_NamespacesAndStd.md) | 💻 [`L02_NamespacesAndStd.cpp`](../code/L02_NamespacesAndStd.cpp) |
| **L03** | Comments & Formatting | 📘 [`L03_CommentsAndFormatting.md`](../theory/L03_CommentsAndFormatting.md) | 💻 [`L03_CommentsAndFormatting.cpp`](../code/L03_CommentsAndFormatting.cpp) |
| **L04** | User Input (`cin`) | 📘 [`L04_UserInputCin.md`](../theory/L04_UserInputCin.md) | 💻 [`L04_UserInputCin.cpp`](../code/L04_UserInputCin.cpp) |
| **L05** | Interactive Profile Generator | 📘 [`L05_InteractiveProfileApp.md`](../theory/L05_InteractiveProfileApp.md) | 💻 [`L05_InteractiveProfileApp.cpp`](../code/L05_InteractiveProfileApp.cpp) |

---

## 🎯 Practical Exercises (E01 – E05)

| # | Exercise | Topic | Code File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **E01** | Hello World | Basic structure and `cout` | 💻 [`E01_HelloWorld.cpp`](../exercise/E01_HelloWorld.cpp) | ✅ |
| **E02** | Escape Sequences | Text formatting and `\n` vs `endl` | 💻 [`E02_EscapeSequences.cpp`](../exercise/E02_EscapeSequences.cpp) | ✅ |
| **E03** | Namespaces | `using namespace std;` vs `std::` | 💻 [`E03_Namespaces.cpp`](../exercise/E03_Namespaces.cpp) | ✅ |
| **E04** | Interactive Greeting | Data input with `cin` | 💻 [`E04_InteractiveGreeting.cpp`](../exercise/E04_InteractiveGreeting.cpp) | ✅ |
| **E05** | Formatted Receipt | Integration of input, output and formatting | 💻 [`E05_FormattedReceipt.cpp`](../exercise/E05_FormattedReceipt.cpp) | ✅ |

---

## 💡 Summary by Lesson

### L01 — Hello World & C++ Anatomy
- A C++ program begins its execution in the `int main()` entry point function.
- The `#include <iostream>` directive includes the standard input and output library.
- `std::cout` uses the insertion operator `<<` to print text to the console.
- `return 0;` tells the operating system that the program finished successfully.

### L02 — Namespaces & `std::`
- Namespaces prevent naming collisions between different libraries.
- The standard library resides in the `std::` namespace.
- The `using namespace std;` statement allows omitting the `std::` prefix in simple source files, although professional headers prefer using the explicit qualification `std::cout`.

### L03 — Comments & Formatting
- Single-line (`//`) and multi-line (`/* ... */`) comments are used to document code intentions.
- `\n` is a fast newline character, while `std::endl` forces the output buffer flush.
- Common escape sequences include `\t` (tab) and `\"` (double quotes).

### L04 — Interactive User Input
- `std::cin` uses the extraction operator `>>` to read data from the console into variables.
- `cin` automatically skips whitespaces, tabs, and newlines when reading native types.

### L05 — Interactive Profile Generator
- Integrating mini-project that combines interactive input, variables, console formatting, and good code structure practices.

---

## 🛡️ Best Practices and Key Patterns

1. **Explicit return:** Always include `return 0;` at the end of `main()`.
2. **Clean formatting:** Use `\n` for continuous newlines and reserve `std::endl` when you need to ensure the output is printed immediately.
3. **Clear prompts:** Print a descriptive message before calling `cin >> variable` to guide the user.

---

*Last update: Section 01 completed at 100%*
