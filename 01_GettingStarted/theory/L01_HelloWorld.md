# Lesson 01 — Hello World & C++ Program Anatomy

Welcome to C++! In this lesson, you will learn what C++ is, how a basic program works, and dissect the line-by-line structure of your first program.

---

## 📖 1. What is C++?

C++ is a high-performance, compiled programming language created by Bjarne Stroustrup in 1979. It is widely used in:
- Game Engines (Unreal Engine)
- Operating Systems (Windows, macOS, Linux kernels)
- High-Frequency Trading & Financial Systems
- Scientific Computing & Physics Simulations

---

## 💻 2. The Hello World Program

Here is the most basic, complete C++ program:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!\n";
    return 0;
}
```

---

## 🔍 3. Line-by-Line Breakdown

### Line 1: `#include <iostream>`
- `#include` is a **preprocessor directive**. It tells the compiler to include external tools before compiling.
- `<iostream>` stands for **Input/Output Stream**. It grants access to `std::cout` (outputting to screen) and `std::cin` (reading from keyboard).

### Line 3: `int main()`
- `main()` is the **entry point function** of every C++ program. When you run an executable, the Operating System executes `main()` first.
- `int` means that when `main()` finishes, it returns an integer status code to the OS (`0` means success).

### Line 3 & 6: `{ ... }`
- Curly braces define the **code block** (body) of a function. Everything inside `{}` belongs to `main()`.

### Line 4: `std::cout << "Hello, World!\n";`
- `std::cout`: The Standard Output Stream object ("console out").
- `<<`: The **insertion operator**. It sends whatever is on its right side into the output stream.
- `"Hello, World!\n"`: A **string literal** (text enclosed in double quotes).
- `\n`: The **newline character**, moving the cursor to the next line on screen.
- `;`: The **semicolon**. Every statement in C++ MUST end with a semicolon `;`.

### Line 5: `return 0;`
- Signals to the Operating System that the program completed without errors.

---

## 💡 Summary Checklist
- [x] `#include <iostream>` is required for console I/O.
- [x] Every C++ program must have a `main()` function.
- [x] Statements must end with a semicolon `;`.

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| *First Lesson* | [**Getting Started**](../) | [**L02 — Namespaces & std::**](L02_NamespacesAndStd.md) |

