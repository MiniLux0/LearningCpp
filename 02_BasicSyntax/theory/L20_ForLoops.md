# Lesson 20 — Count-Controlled Iteration (`for` Loops)

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 02** ([`Lecture02_FlowOfControl.pdf`](../../files/mit6096/lectures/Lecture02_FlowOfControl.pdf)) and **Stanford CS106B Textbook Chapter 1** ([`CS106BX-Reader.pdf`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 02: Count-Controlled Loop Structures](../../files/mit6096/lectures/Lecture02_FlowOfControl.pdf)
  - 🌲 [Stanford CS106B — Chapter 1: The for Loop Header](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`L20_ForLoops.cpp`](../code/L20_ForLoops.cpp)

---

## Learning Objectives

- [ ] Consolidate initialization, condition check, and step increment in a single `for` loop header.
- [ ] Understand loop counter scope isolation inside `for(int i = 0; ...)`.
- [ ] Implement incremental, decremental, and custom step iteration patterns.

---

## 1. The Anatomy of a `for` Loop (1-2-3-4 Sequence)

For a beginner, a `for` loop header can look like a soup of semicolons. The correct way to understand it is to mentally map its parts in the exact order the computer executes them:

```text
       (1)             (2)             (4)
for (  INIT ;      CONDITION ;        STEP ) {
    
    // (3) LOOP BODY
    cout << "Iterating...\n";

}
```

### The Exact Lifecycle:
1. **[1] INIT (`int i = 0`)**: Executes **ONLY ONCE** at the very beginning. It creates and prepares your counter variable.
2. **[2] CONDITION (`i < 5`)**: The gatekeeper. It is evaluated *before* entering. If `true`, it lets you proceed to step 3. If `false`, it exits the loop entirely.
3. **[3] BODY**: Executes all the code inside the curly braces `{ ... }`.
4. **[4] STEP (`i++`)**: After completing the body, control jumps back up to update the counter.
5. **Repeat starting from [2]**. The initialization step [1] is never touched again!

<div align="center">
  <img src="assets/l20_for_loops_manim.gif" alt="for loop execution trace">
  <p><em><strong>Execution Trace:</strong> Look closely at the animation above. Notice how the highlighter jumps in the exact order 1 → 2 → 3 → 4, and then loops in the cycle 2 → 3 → 4 until the condition becomes false.</em></p>
</div>

```cpp
#include <iostream>

int main() {
    // 1. Init i=0 | 2. Check i<5 | 4. Increment i++
    for (int i = 0; i < 5; i++) {
        // 3. Print
        cout << "Iteration i = " << i << "\n";
    }
    return 0;
}
```

> [!TIP]
> **Loop Variable Scope:**
> Declaring `int i` inside the `for` header isolates `i` to that loop's scope. Once the loop finishes, `i` is destroyed, allowing you to reuse `i` safely in subsequent loops without variable name conflicts.

---

## ❓ Self-Assessment Checkpoint #1 — Decremental Counting

How do you write a `for` loop header that counts down from `10` to `1` inclusive?

<details>
<summary>🔍 <strong>View Explanation & Header</strong></summary>

> [!NOTE]
> **Header:** `for (int i = 10; i >= 1; i--)`
>
> **Explanation:**
> `int i = 10` initializes the counter at 10. `i >= 1` keeps the loop active through 1. `i--` decrements the counter by 1 after each iteration pass.

</details>

---

## 📝 Summary & Key Takeaways

1. **Header:** Combines `(Init; Condition; Step)` into a compact, readable line.
2. **Scope:** Counter variables declared inside the header exist only during loop execution.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L19 — Post-Test do-while Loops**](L19_DoWhileLoops.md) | [**🏠 Basic Syntax**](../README.md) | [**L21 — Loop Interruptions: break & continue ➡️**](L21_BreakAndContinue.md) |

</div>


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>