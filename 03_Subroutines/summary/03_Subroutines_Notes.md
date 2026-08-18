# 📝 Section 03: Subroutines and Functions — Study Summary and Notes

Study notes and executive summary for **Section 03: Subroutines and Functions** (MIT 6.096 Lecture 03 / Stanford CS106L Lectures 01 and 03 / Stanford CS106B Chapter 2).
Covers function anatomy in C++, return types, pass-by-value vs. pass-by-reference (`&`, `const &`), function overloading, separate compilation using header files (`.h` / `.cpp`), and variable scope management.

---

## 🧭 Table of Contents

1. [Lessons and Theory](#-lessons-and-theory)
2. [Practical Exercises (E01 – E05)](#-practical-exercises-e01--e05)
3. [Summary by Lesson](#-summary-by-lesson)
   - [L23 — Function Basics](#l23--function-basics)
   - [L24 — Return Values](#l24--return-values)
   - [L25 — Parameters and References](#l25--parameters-and-references)
   - [L26 — Headers and Prototypes](#l26--headers-and-prototypes)
4. [Best Practices and Key Patterns](#-best-practices-and-key-patterns)

---

## 📘 Lessons and Theory

| Lesson | Title | Theory Note | Code Lab |
| :--- | :--- | :--- | :--- |
| **L23** | Function Basics | 📘 [`L23_Functions.md`](../theory/L23_Functions.md) | 💻 [`L23_Functions.cpp`](../code/L23_Functions.cpp) |
| **L24** | Return Values | 📘 [`L24_ReturnValues.md`](../theory/L24_ReturnValues.md) | 💻 [`L24_ReturnValues.cpp`](../code/L24_ReturnValues.cpp) |
| **L25** | Parameters & References | 📘 [`L25_FunctionParameters.md`](../theory/L25_FunctionParameters.md) | 💻 [`L25_FunctionParameters.cpp`](../code/L25_FunctionParameters.cpp) |
| **L26** | Headers & Prototypes | 📘 [`L26_HeadersAndPrototypes.md`](../theory/L26_HeadersAndPrototypes.md) | 💻 [`L26_HeadersAndPrototypes.cpp`](../code/L26_HeadersAndPrototypes.cpp) |

---

## 🎯 Practical Exercises (E01 – E05)

| # | Exercise | Topic | Code File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **E01** | Function Basics | Declaration, invocation, and return | 💻 [`E01_FunctionBasics.cpp`](../exercise/E01_FunctionBasics.cpp) | ✅ |
| **E02** | Pass by Reference | Direct mutation using `&` | 💻 [`E02_PassByReference.cpp`](../exercise/E02_PassByReference.cpp) | ✅ |
| **E03** | Swap Function | Variable swap using references | 💻 [`E03_SwapFunction.cpp`](../exercise/E03_SwapFunction.cpp) | ✅ |
| **E04** | Function Overloading | Overloading by parameter type | 💻 [`E04_Overloading.cpp`](../exercise/E04_Overloading.cpp) | ✅ |
| **E05** | Header Prototypes | Prototypes and separate compilation | 💻 [`E05_HeaderPrototypes.cpp`](../exercise/E05_HeaderPrototypes.cpp) | ✅ |

---

## 💡 Summary by Lesson

### L23 — Function Basics
- A function is a reusable block of code.
- Basic signature: `returnType functionName(parameterList)`.
- If the function does not return any value, the return type is declared as `void`.
- Applies the **DRY (*Don't Repeat Yourself*)** principle.

### L24 — Return Values
- The `return` statement returns a value to the caller and terminates function execution immediately.
- **Function Overloading:** C++ allows defining multiple functions with the same name as long as their signatures differ in parameter count or types.

### L25 — Parameters and References
- **Pass-by-Value:** Copies the argument's value. Modifications inside the function do not affect the original variable.
- **Pass-by-Reference (`&`):** Passes an alias to the original memory cell. Allows mutating the caller's variable directly.
- **Constant Reference (`const &`):** Avoids copy overhead for large objects (e.g., `const string&`) while keeping the parameter immutable.

### L26 — Headers and Prototypes
- **Prototypes (*Forward Declarations*):** Inform the compiler of a function's signature before its definition, resolving order-of-declaration dependencies.
- **`.h` / `.cpp` Separation:** Declarations belong in header files (`.h`), whereas implementations reside in source files (`.cpp`).
- **Inclusion Guards:** Use `#pragma once` or `#ifndef` preprocessor directives to prevent double inclusion linking errors.

---

## 🛡️ Best Practices and Key Patterns

1. **Single Responsibility Principle:** Design short functions that perform a single, well-defined task.
2. **`using namespace std;` in source files:** Simplifies writing `cout`, `cin`, `endl`, `string`, `vector`.
3. **`const &` for efficiency:** Use constant references `const T&` to pass large objects without copy overhead.
4. **Header guards:** Always include `#pragma once` at the top of `.h` files.

---

*Section 03 100% completed*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>