# L26 — Forward Declarations, Function Prototypes, and Header Files (`.h` / `.hpp`)

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 03** ([`Lecture03_Functions.pdf`](../../files/mit6096/lectures/Lecture03_Functions.pdf)) and **Stanford CS106L Lecture 01** ([`Lecture01_WelcomeToCpp.pdf`](../../files/cs106l/lectures/Lecture01_WelcomeToCpp.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 03: Function Prototypes & Header Files](../../files/mit6096/lectures/Lecture03_Functions.pdf)
  - ⚙️ [Stanford CS106L — Lecture 01: Multi-File Compilation & Header Guards](../../files/cs106l/lectures/Lecture01_WelcomeToCpp.pdf)
- 💻 **Code Lab:** [`L26_HeadersAndPrototypes.cpp`](../code/L26_HeadersAndPrototypes.cpp)

---

## Learning Objectives

- [ ] Declare **Function Prototypes (*Forward Declarations*)** to inform the compiler of function signatures before their definitions.
- [ ] Organize C++ projects by separating code into interface files (`.h` / `.hpp`) and implementation files (`.cpp`).
- [ ] Implement **Inclusion Guards (*Header Guards*)** using `#ifndef` or `#pragma once` to prevent compilation errors caused by double inclusion of symbols.

---

## 1. Function Prototypes (*Forward Declarations*)

The C++ compiler reads source files strictly from top to bottom (*top-to-bottom*). If `main()` invokes a function defined further down in the file, the compiler will generate an undeclared identifier error.

A **Function Prototype** declares only the signature (return type, name, and parameters) ending with a semicolon `;` before `main()`:

```cpp
#include <iostream>
using namespace std;

// 1. Function Prototype (Forward Declaration)
int sum(int a, int b);

int main() {
    cout << "Result: " << sum(5, 3) << endl; // Valid! The compiler knows sum() exists.
    return 0;
}

// 2. Function Definition
int sum(int a, int b) {
    return a + b;
}
```

---

## 2. Header Files and Inclusion Guards (`#pragma once`)

When splitting code into multiple `.h` files, including the same header multiple times in different translation units generates symbol redefinition errors at link time (*linker*). Using `#pragma once` or traditional preprocessor guards resolves this issue:

```cpp
#ifndef MATH_UTILITIES_H
#define MATH_UTILITIES_H

// Prototype declarations in the header file (.h)
int sum(int a, int b);

#endif // MATH_UTILITIES_H
```

> [!TIP]
> **Modern Practice:**  
> Modern compilers (GCC, Clang, MSVC) support the `#pragma once` directive placed at the very first line of header files as a cleaner alternative to `#ifndef` guards.

---

## ❓ Self-Assessment Checkpoint #1 — Definitions in Header `.h` Files

Why should full function definitions (`{ ... }`) generally NOT be placed inside header files (`.h`)?

<details>
<summary>🔍 <strong>View Explanation & Diagnosis</strong></summary>

> [!CAUTION]
> **Linker Multiple Definition Error:**  
> If a header containing function bodies with executable code is included in multiple `.cpp` source files, the compiler generates duplicate binary symbols in each object file (`.o` / `.obj`). When the linker runs, it will fail with a `multiple definition of 'functionName'` error.

</details>

---

## 🎬 Visualización

<div align="center">
  <img src="assets/l26_headers_prototypes_manim.gif" alt="L26 Headers and Prototypes animation">
  <p><em><strong>The Sequential Reader Problem:</strong> The C++ compiler reads code from top to bottom. If you call a function before defining it, compilation fails. The <strong>Prototype</strong> tells the compiler "trust me, this function exists further down." Additionally, by moving these prototypes to <code>.h</code> files and adding <code>#pragma once</code> protection, we can share them without colliding on duplicate symbol errors.</em></p>
</div>

---

## 📝 Summary & Key Takeaways

1. **Prototypes:** Inform the compiler of function signatures before their full definitions.
2. **Headers (`.h`):** Store interface contracts and declarations.
3. **Guards:** Use `#pragma once` to prevent duplicate inclusion of header files.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:-------------------:|:------------------:|
| [**⬅️ L25 — Function Parameters**](L25_FunctionParameters.md) | [**🏠 Subroutines**](../README.md) | [**Section 04: Arrays and Strings ➡️**](../../04_ArraysStrings/README.md) |

</div>

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>