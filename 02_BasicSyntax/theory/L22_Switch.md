# Lesson 22 — The `switch-case` Statement & Fall-Through

The `switch` statement selects one of many code blocks for execution based on an integer or character expression.

---

## 🔀 1. Syntax

```cpp
switch (expression) {
    case value1:
        // Code for value1
        break;
    case value2:
        // Code for value2
        break;
    default:
        // Default fallback if no case matches
        break;
    }
```

---

## ⚠️ 2. Fall-Through Behavior
If `break` is omitted, execution "falls through" into subsequent case statements regardless of their conditions.
Use `[[fallthrough]];` attribute in C++17 to indicate intentional fall-through cleanly.

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Module |
|:------------------:|:---------------:|:--------------:|
| [**L21 — break and continue**](L21_BreakAndContinue.md) | [**Basic Syntax**](../) | [**L23 — Functions & Subroutines**](../../03_Subroutines/theory/L23_Functions.md) |

