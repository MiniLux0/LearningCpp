# Lesson 16 — Safely Comparing Floating-Point Numbers (`Epsilon`)

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **Stanford CS106B Textbook Chapter 1** ([`CS106BX-Reader.pdf`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)) and **MIT 6.096 Lecture 01** ([`Lecture01_Introduction.pdf`](../../files/mit6096/lectures/Lecture01_Introduction.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🌲 [Stanford CS106B — Chapter 1: Floating-Point Roundoff Errors](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
  - 🏛️ [MIT 6.096 — Lecture 01: IEEE 754 Representation Traps](../../files/mit6096/lectures/Lecture01_Introduction.pdf)
- 💻 **Code Lab:** [`L16_ComparingFloats.cpp`](../code/L16_ComparingFloats.cpp)

---

## Learning Objectives

- [ ] Understand why direct equality operators (`a == b`) fail for floating-point calculations.
- [ ] Implement **Epsilon ( $\epsilon$ ) Tolerance Threshold Comparisons**.
- [ ] Utilize `<cmath>` functions (`abs()`) to perform safe floating-point equality checks.

---

## 1. The Floating-Point Equality Flaw

Due to IEEE 754 binary representation rounding, mathematical calculations like `0.1 + 0.2` do not produce exactly `0.3`:

```cpp
double a = 0.1 + 0.2; // Evaluates to 0.30000000000000004
double b = 0.3;

if (a == b) {
    cout << "Equal!\n";
} else {
    cout << "NOT Equal!\n"; // Execution falls here!
}
```

---

## 2. The Solution: Absolute Tolerance (`\text{Epsilon } \epsilon`)

Instead of checking exact binary equality (`a == b`), verify whether the absolute difference between `a` and `b` is smaller than a tiny tolerance value **Epsilon ( $\epsilon$ )**:

```math
\text{are equal}(a, b) = |a - b| < \epsilon
```

```cpp
#include <iostream>
#include <cmath> // Required for abs()

bool nearlyEqual(double a, double b, double epsilon = 1e-9) {
    return abs(a - b) < epsilon;
}

int main() {
    double a = 0.1 + 0.2;
    double b = 0.3;

    if (nearlyEqual(a, b)) {
        cout << "Safely verified as equal within epsilon tolerance!\n";
    }

    return 0;
}
```

> [!TIP]
> **Choosing Epsilon ( $\epsilon$ ):**
> For general 64-bit `double` calculations, an absolute epsilon threshold of `1e-9` ( $0.000000001$ ) or `1e-7` for `float` is standard in financial, physics, and game engines.

---

## ❓ Self-Assessment Checkpoint #1 — Epsilon Selection

Why is `abs()` required in `abs(a - b) < epsilon`?

<details>
<summary>🔍 <strong>View Explanation & Answer</strong></summary>

> [!IMPORTANT]
> **Answer:** To handle cases where $a < b$.
>
> **Explanation:**
> If $a = 0.299999$ and $b = 0.3$, then $a - b = -0.000001$. Without `abs()`, $-0.000001 < 1e-9$ would evaluate to `true` even if $a$ were $-1000.0$! Taking the absolute value guarantees checking distance regardless of which number is larger.

</details>

---

## 📝 Summary & Key Takeaways

1. **Rule:** NEVER compare floating-point numbers directly with `==` or `!=`.
2. **Tolerance:** Use `abs(a - b) < epsilon` with `#include <cmath>`.
3. **Epsilon:** `1e-9` provides a robust default tolerance for `double`.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L15 — Multi-Branch if-else-if**](l15_if_else_if_else.md) | [**🏠 Basic Syntax**](../README.md) | [**L17 — Conditions & Logical Operators ➡️**](l17_conditions.md) |

</div>


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>