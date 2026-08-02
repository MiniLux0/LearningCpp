# Lesson 26 — Forward Declarations, Function Prototypes & Header Files (`.h` / `.hpp`)

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 03** ([`Lecture03_Functions.pdf`](../../files/mit6096/lectures/Lecture03_Functions.pdf)) and **Stanford CS106L Lecture 01** ([`WLecture1_intro.pdf`](../../files/cs106l/lectures/WLecture1_intro.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 03: Function Prototypes & Header Files](../../files/mit6096/lectures/Lecture03_Functions.pdf)
  - ⚙️ [Stanford CS106L — Lecture 01: Multi-File Compilation & Header Guards](../../files/cs106l/lectures/WLecture1_intro.pdf)
- 💻 **Code Lab:** [`L26_HeadersAndPrototypes.cpp`](../code/L26_HeadersAndPrototypes.cpp)

---

## Learning Objectives

- [ ] Declare **Function Prototypes** (Forward Declarations) to inform the compiler of signatures before definitions appear.
- [ ] Organize C++ projects into interface header files (`.h` / `.hpp`) and implementation files (`.cpp`).
- [ ] Implement **Header Guards (`#ifndef`, `#define`, `#endif`)** or `#pragma once` to prevent duplicate symbol compilation errors.

---

## 1. Function Prototypes (Forward Declarations)

The C++ compiler reads source files strictly from top to bottom. If `main()` calls a function defined lower down in the file, the compiler throws an `undeclared identifier` error.

A **Function Prototype** declares the signature (return type, name, parameters) ending with a semicolon `;` before `main()`:

```cpp
#include <iostream>

// 1. Function Prototype (Forward Declaration)
int add(int a, int b);

int main() {
    std::cout << "Result: " << add(5, 3) << "\n"; // Valid! Compiler knows add() exists.
    return 0;
}

// 2. Function Definition
int add(int a, int b) {
    return a + b;
}
```

---

## 2. Header Guards (`#pragma once`)

When splitting code across multiple header files, including the same header multiple times causes redefinition errors. Use `#pragma once` or traditional preprocessor guards:

```cpp
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

// Header declaration declarations here
int add(int a, int b);

#endif // MATH_UTILS_H
```

> [!TIP]
> **Modern Best Practice:**
> Modern compilers (GCC, Clang, MSVC) support `#pragma once` placed at the top of header files as a cleaner alternative to manual `#ifndef` guards.

---

## ❓ Self-Assessment Checkpoint #1 — Header File Role

Why should full function definitions (`{ ... }`) generally NOT be placed inside header files (`.h`)?

<details>
<summary>🔍 <strong>View Explanation & Answer</strong></summary>

> [!CAUTION]
> **Multiple Definition Linker Error:**
> If a header containing function definitions is `#include`d by multiple `.cpp` files, the compiler creates duplicate compiled function object symbols in each `.o` file. When the linker runs, it will fail with `multiple definition of 'func'` errors!

</details>

---

## 📝 Summary & Key Takeaways

1. **Prototypes:** Inform the compiler of function signatures before their full definitions.
2. **Headers (`.h`):** Store function declarations and interface contracts.
3. **Guards:** Use `#pragma once` to prevent duplicate header inclusion errors.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L25 — Function Parameters**](L25_FunctionParameters.md) | [**🏠 Subroutines**](../README.md) | [**Section 04: Arrays & Strings ➡️**](../../04_ArraysStrings/README.md) |

</div>

---
*MiniLux0 — Learning C++ Section 03 Capstone*