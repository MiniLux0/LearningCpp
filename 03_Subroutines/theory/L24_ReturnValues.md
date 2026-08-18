# L24 — Return Values and Data Flow

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 03** ([`Lecture03_Functions.pdf`](../../files/mit6096/lectures/Lecture03_Functions.pdf)) and **Stanford CS106B Textbook Chapter 2 (*Functional Composition*)** (*Programming Abstractions in C++* by Eric Roberts).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 03: Function Return Values & Type Matching](../../files/mit6096/lectures/Lecture03_Functions.pdf)
  - 🌲 [Stanford CS106B — Chapter 2: Functional Composition](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`L24_ReturnValues.cpp`](../code/L24_ReturnValues.cpp)

---

## Learning Objectives

- [ ] Declare non-void return types (`int`, `double`, `string`, `bool`).
- [ ] Return computed data to the calling function using the `return` keyword.
- [ ] Implement early termination in functions using conditional statements (*Early Return*).
- [ ] Diagnose Undefined Behavior errors caused by missing `return` statements.

---

## 1. Returning Data with the `return` Statement

A function can compute a value and transmit it back to the calling function using the `return` statement:

<div align="center">
  <img src="assets/l24_return_values_manim.gif" alt="function return values trace">
  <p><em><strong>State Propagation (Return Values):</strong> Notice how the subroutine computes an internal result (<code>25</code>) and, right before "dying", delivers that value to the variable <code>res</code> that was waiting for it in the caller's memory (<code>main</code>).</em></p>
</div>

```cpp
#include <iostream>
using namespace std;

// Returns a computed integer
int square(int number) {
    return number * number;
}

int main() {
    int val = 5;
    int result = square(val); // result receives 25
    cout << "The square of " << val << " is " << result << endl;
    return 0;
}
```

> [!IMPORTANT]
> **Immediate Termination:**  
> When the `return` statement is executed, the function terminates **immediately**. Any statement located below the `return` statement in the function body will be completely ignored.

---

## 2. Early Return

```cpp
#include <iostream>
using namespace std;

int getMax(int a, int b) {
    if (a > b) {
        return a; // Exits immediately if a is greater
    }
    return b; // Otherwise returns b
}
```

---

## ❓ Self-Assessment Checkpoint #1 — Omitting `return`

What happens if a function declared with a non-void return type (e.g., `int calculate()`) reaches the closing brace `}` without executing a `return` statement?

<details>
<summary>🔍 <strong>View Explanation & Diagnosis</strong></summary>

> [!CAUTION]
> **Undefined Behavior (UB):**  
> In C++, failing to return a value from a non-`void` function causes Undefined Behavior. The caller will receive garbage values left over in the system registers. Modern compilers will issue a warning (`warning: control reaches end of non-void function`).

</details>

---

## 📝 Summary & Key Takeaways

1. **Type Matching:** The type of the value returned must match the return type specified in the function signature.
2. **Immediate Termination:** `return` interrupts the function instantly.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:-------------------:|:------------------:|
| [**⬅️ L23 — Function Basics**](L23_Functions.md) | [**🏠 Subroutines**](../README.md) | [**L25 — Parameters and References ➡️**](L25_FunctionParameters.md) |

</div>

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>