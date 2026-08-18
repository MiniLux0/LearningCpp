# L23 — Subroutine and Function Basics

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 03** ([`Lecture03_Functions.pdf`](../../files/mit6096/lectures/Lecture03_Functions.pdf)) and **Stanford CS106B Textbook Chapter 2 (*Procedural Abstraction*, pp. 55–90)** (*Programming Abstractions in C++* by Eric Roberts).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 03: Function Definitions & Call Stack Frames](../../files/mit6096/lectures/Lecture03_Functions.pdf)
  - 🌲 [Stanford CS106B — Chapter 2: Procedural Abstraction](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`L23_Functions.cpp`](../code/L23_Functions.cpp)

---

## Learning Objectives

- [ ] Understand procedural abstraction and the **DRY (*Don't Repeat Yourself*)** engineering principle.
- [ ] Declare and define functions by specifying return type, name, and parameter list.
- [ ] Understand the behavior of `void` functions (subroutines without return values).
- [ ] Trace subroutine execution and call stack frame allocation/deallocation.

---

## 1. What is a Function or Subroutine?

A **function** is a reusable block of code designed to perform a specific task. Functions allow breaking down complex, monolithic programs into independent, maintainable modules.

<div align="center">
  <img src="assets/l23_functions_manim.gif" alt="function call stack trace">
  <p><em><strong>Execution Trace & Call Stack (LIFO):</strong> Notice how the linear execution of <code>main()</code> is temporarily <strong>suspended</strong> when it encounters <code>printHello()</code>. Control jumps up to the subroutine, executes it, and once complete, the subroutine "dies" (is popped from the stack), returning control exactly to where <code>main()</code> left off.</em></p>
</div>

```cpp
#include <iostream>
using namespace std;

// Definition of a void function (no return value)
void showWelcome() {
    cout << "====================================\n";
    cout << "    C++ SUBROUTINES MODULE L23      \n";
    cout << "====================================\n";
}

int main() {
    showWelcome(); // Invocation 1
    showWelcome(); // Invocation 2
    return 0;
}
```

> [!TIP]
> **The DRY (*Don't Repeat Yourself*) Principle:**
> If you find yourself duplicating the same 5 lines of code in multiple places, encapsulate them inside a function with a descriptive name.

---

## 2. Anatomy of a Function Declaration

Every function consists of three main parts:

```cpp
//  ReturnType   FunctionName  ( Parameters )
        void     printSum      ( int a, int b ) {
            cout << "Sum: " << (a + b) << endl;
        }
```

- **Return Type:** Indicates what type of data the function returns (`int`, `double`, `string`, `void`).
- **Name:** Descriptive identifier written in *camelCase* notation.
- **Parameters:** Local input variables enclosed within parentheses `()`.

---

## ❓ Self-Assessment Checkpoint #1 — The `void` Return Type

What does it mean when a function is declared with a `void` return type (e.g., `void printHeader()`)?

<details>
<summary>🔍 <strong>View Explanation & Answer</strong></summary>

> [!NOTE]
> **Answer:** It indicates that the function does NOT return any data value to the caller.
>
> **Explanation:**  
> `void` tells the compiler that the subroutine executes actions or side effects (like printing to screen with `cout` or modifying memory), but does not compute a value to be assigned to variables in `main()`.

</details>

---

## 📝 Summary & Key Takeaways

1. **Modularity:** Functions divide code into named, reusable subroutines.
2. **`void`:** Indicates the function does not return data to the caller.
3. **Reusability:** Prevents duplicate code and makes debugging easier.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:-------------------:|:------------------:|
| [**⬅️ Section 02 Capstone**](../../02_BasicSyntax/theory/L22_Switch.md) | [**🏠 Subroutines**](../README.md) | [**L24 — Return Values ➡️**](L24_ReturnValues.md) |

</div>

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>