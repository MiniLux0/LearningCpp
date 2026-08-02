# 📝 Section 03: Subroutines — Study Summary and Notes

Study notes and executive summary for **Section 03: Subroutines and Functions**.
Covers function anatomy in C++, return types, pass-by-value vs pass-by-reference (`&`, `const &`), function overloading, separation into prototypes and header files (`.h` / `.cpp`), and variable scope/lifetime.

---

## 🧭 Table of Contents

1. [Lessons and Theory](#-lessons-and-theory)
2. [Practical Exercises (E01 – E05)](#-practical-exercises-e01--e05)
3. [Summary by Lesson](#-summary-by-lesson)
   - [L23 — Functions Anatomy](#l23--functions-anatomy)
   - [L24 — Return Values & Overloading](#l24--return-values--overloading)
   - [L25 — Function Parameters & References](#l25--function-parameters--references)
   - [L26 — Headers & Prototypes](#l26--headers--prototypes)
4. [Best Practices and Key Patterns](#-best-practices-and-key-patterns)

---

## 📘 Lessons and Theory

| Lesson | Title | Theory Note | Code Lab |
| :--- | :--- | :--- | :--- |
| **L23** | Functions Anatomy | 📘 [`L23_Functions.md`](../theory/L23_Functions.md) | 💻 [`L23_Functions.cpp`](../code/L23_Functions.cpp) |
| **L24** | Return Values | 📘 [`L24_ReturnValues.md`](../theory/L24_ReturnValues.md) | 💻 [`L24_ReturnValues.cpp`](../code/L24_ReturnValues.cpp) |
| **L25** | Function Parameters | 📘 [`L25_FunctionParameters.md`](../theory/L25_FunctionParameters.md) | 💻 [`L25_FunctionParameters.cpp`](../code/L25_FunctionParameters.cpp) |
| **L26** | Headers & Prototypes | 📘 [`L26_HeadersAndPrototypes.md`](../theory/L26_HeadersAndPrototypes.md) | 💻 [`L26_HeadersAndPrototypes.cpp`](../code/L26_HeadersAndPrototypes.cpp) |

---

## 🎯 Practical Exercises (E01 – E05)

| # | Exercise | Topic | Code File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **E01** | Function Basics | Declaration, calls, and return | 💻 [`E01_FunctionBasics.cpp`](../exercise/E01_FunctionBasics.cpp) | ✅ |
| **E02** | Pass by Reference | Direct modification using `&` | 💻 [`E02_PassByReference.cpp`](../exercise/E02_PassByReference.cpp) | ✅ |
| **E03** | Swap Function | Variable swapping with references | 💻 [`E03_SwapFunction.cpp`](../exercise/E03_SwapFunction.cpp) | ✅ |
| **E04** | Overloading | Function overloading by parameter type | 💻 [`E04_Overloading.cpp`](../exercise/E04_Overloading.cpp) | ✅ |
| **E05** | Header Prototypes | Prototypes and separate compilation | 💻 [`E05_HeaderPrototypes.cpp`](../exercise/E05_HeaderPrototypes.cpp) | ✅ |

---

## 💡 Summary by Lesson

### L23 — Functions Anatomy
- A function is a reusable block of code.
- Basic signature: `returnType functionName(parameterList)`.
- If the function does not return any value, the return type is specified as `void`.

### L24 — Return Values & Overloading
- The `return` statement sends a value back to the caller and terminates the function's execution.
- **Function Overloading:** C++ allows defining multiple functions with the same name as long as their signatures differ by the number or type of their parameters (the return type alone is not enough).

### L25 — Function Parameters & References
- **Pass-by-value:** Copies the argument's value. Changes made inside the function do not affect the original variable.
- **Pass-by-reference (`&`):** Passes an alias to the original variable. Allows the function to directly modify the caller's variable.
- **Constant reference (`const &`):** Avoids copying heavy data while keeping the original variable immutable (ideal for large structures and efficient reading).

### L26 — Headers & Prototypes
- **Prototypes (Declarations):** Allow the compiler to know a function's signature before it is called, resolving order dependencies.
- **`.h` / `.cpp` Separation:** Declarations go in header files (`.h`), while the implementation resides in `.cpp` files. Include guards (`#ifndef`, `#define`, `#endif` or `#pragma once`) are used to prevent duplicate inclusions.

---

## 🛡️ Best Practices and Key Patterns

1. **Single Responsibility Principle:** Design short functions that perform a single, well-defined task.
2. **`const &` for efficient reading:** Use constant references `const T&` to pass objects or non-primitive types without copying costs.
3. **Include guards:** Always include `#ifndef MY_HEADER_H` in `.h` files to prevent symbol redefinition errors.

---

*Last updated: Section 03 completed 100%*
