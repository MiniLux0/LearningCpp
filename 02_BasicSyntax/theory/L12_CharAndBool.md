# Lesson 12 — Char, ASCII Table & Bool Types

Characters (`char`) and booleans (`bool`) are fundamental primitive types in C++.

---

## 🔤 1. Characters & ASCII Values

A `char` takes 1 Byte of memory and stores a single character enclosed in single quotes `'A'`.
Under the hood, C++ stores characters as **ASCII integer values** (e.g., `'A'` = 65, `'a'` = 97).

```cpp
char letter = 'A';
int ascii_value = (int)letter; // Explicit casting to int: 65
char next = letter + 1;       // ASCII math: 'B'
```

---

## 🔘 2. Booleans (`bool`)

Stores truth values: `true` (evaluates to `1`) or `false` (evaluates to `0`).

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L11 — Floating-Point Types**](L11_FloatingPointTypes.md) | [**Basic Syntax**](../) | [**L13 — Conditionals: if**](L13_If.md) |

