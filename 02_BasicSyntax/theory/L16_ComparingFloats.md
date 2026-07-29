# Lesson 16 — Comparing Floating-Point Numbers & Epsilon

Due to binary representation limits (IEEE 754), floating-point arithmetic introduces tiny precision errors.

---

## ⚠️ The Problem with `==` on Floats

```cpp
double a = 0.1 + 0.2; // May evaluate to 0.30000000000000004
if (a == 0.3) {
    // ❌ Might evaluate to FALSE!
}
```

---

## 💡 The Solution: Epsilon Threshold

Compare floating-point values using an **epsilon threshold** ($10^{-9}$):

```cpp
#include <iostream>
#include <cmath>

bool are_equal(double x, double y, double epsilon = 1e-9) {
    return std::abs(x - y) < epsilon;
}

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L15 — Conditionals: if-else if-else**](L15_IfElseIfElse.md) | [**Basic Syntax**](../) | [**L17 — Complex Logical Conditions**](L17_Conditions.md) |

```
