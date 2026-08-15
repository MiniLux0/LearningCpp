# Lesson 13 — Control Flow: `if` Statements & Comparison Operators

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 02** ([`Lecture02_FlowOfControl.pdf`](../../files/mit6096/lectures/Lecture02_FlowOfControl.pdf)) and **Stanford CS106B Textbook Chapter 1** ([`CS106BX-Reader.pdf`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 02: Branching & Conditional Execution](../../files/mit6096/lectures/Lecture02_FlowOfControl.pdf)
  - 🌲 [Stanford CS106B — Chapter 1: Control Statements in C++](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`l13_if.cpp`](../code/l13_if.cpp)

---

## Learning Objectives

- [ ] Divert linear instruction execution using conditional branching (`if`).
- [ ] Evaluate Boolean relational operators (`>`, `<`, `>=`, `<=`, `==`, `!=`).
- [ ] Identify and avoid the classic **Assignment inside Condition Bug** (`if (x = 5)`).

---

## 1. Conditional Branching Mechanics

Programs often require executing specific blocks of code only when dynamic runtime conditions are met. The `if` statement evaluates a boolean expression:

![l13_if](assets/l13_if.svg)

```cpp
#include <iostream>

int main() {
    int score = 85;

    if (score >= 70) {
        cout << "Congratulations! You passed the assessment.\n";
    }

    return 0;
}
```

---

## 2. Relational Comparison Operators

| Operator | Comparison Name | Evaluation Example ( $x = 20$ ) | Boolean Result |
| :---: | :--- | :--- | :---: |
| **`>`** | Greater Than | `x > 18` | `true` |
| **`<`** | Less Than | `x < 18` | `false` |
| **`>=`** | Greater Than or Equal To | `x >= 20` | `true` |
| **`<=`** | Less Than or Equal To | `x <= 15` | `false` |
| **`==`** | Equality | `x == 20` | `true` |
| **`!=`** | Inequality | `x != 20` | `false` |

> [!CAUTION]
> **The `=` vs. `==` Disaster:**
> - `x = 5` (Single Equals) is the **Assignment Operator**. It overwrites `x` with `5` and returns `5` (which evaluates as `true`!).
> - `x == 5` (Double Equals) is the **Equality Comparison Operator**.
>
> Writing `if (x = 5)` instead of `if (x == 5)` will mutate your variable and always evaluate to `true`!

---

## ❓ Self-Assessment Checkpoint #1 — The Single Equals Trap

What happens if you write `if (age = 18)` when `age` was previously `10`?

<details>
<summary>🔍 <strong>View Explanation & Output</strong></summary>

> [!WARNING]
> **Behavior:**
> 1. `age` is mutated to `18`.
> 2. `18` is non-zero, so the condition evaluates as `true`.
> 3. The `if` block executes every single time, regardless of what `age` was before!

</details>

---

## 📝 Summary & Key Takeaways

1. **`if`:** Diverts execution based on boolean truth values.
2. **Relational Operators:** Return `true` or `false`.
3. **Comparison:** Always use `==` for testing equality.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L12 — Char & Bool Types**](l12_char_and_bool.md) | [**🏠 Basic Syntax**](../README.md) | [**L14 — Control Flow: if-else ➡️**](l14_if_else.md) |

</div>


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>