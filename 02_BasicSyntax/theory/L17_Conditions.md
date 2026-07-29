# Lesson 17 — Complex Logical Conditions & Short-Circuit Evaluation

In this lesson, you will learn truth tables and short-circuit evaluation in boolean expressions.

---

## ⚡ Short-Circuit Evaluation

- In `A && B`: If `A` is `false`, `B` is **never evaluated** (because the result is guaranteed to be `false`).
- In `A || B`: If `A` is `true`, `B` is **never evaluated** (because the result is guaranteed to be `true`).

### Safe Division Guard Example:
```cpp
int divisor = 0;

// Safe! 'divisor != 0' is false, so (100 / divisor) is NEVER executed, avoiding divide-by-zero crash!
if (divisor != 0 && (100 / divisor > 5)) {
    // Process calculation
}

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L16 — Comparing Floats**](L16_ComparingFloats.md) | [**Basic Syntax**](../) | [**L18 — The while Loop**](L18_WhileLoops.md) |

```
