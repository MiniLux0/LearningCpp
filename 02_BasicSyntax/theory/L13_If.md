# Lesson 13 — Conditionals: The `if` Statement

Up until now, our programs executed code sequentially from top to bottom. But what if we want our program to make decisions?

For example: *"IF the user's balance is greater than $50, allow them to buy the game."*

In C++, we use the **`if` statement** to execute code conditionally.

---

## 🔀 1. Syntax of `if`

```cpp
if (condition) {
    // Code block inside {} is executed ONLY IF condition is TRUE
}
```

---

## ⚖️ 2. Relational Comparison Operators

To build conditions inside `if (...)`, we use comparison operators:

| Operator | Meaning | Example (`age = 20`) | Evaluates To |
|:--------:|---------|----------------------|:------------:|
| `>` | Greater than | `age > 18` | `true` |
| `<` | Less than | `age < 18` | `false` |
| `>=` | Greater than or equal to | `age >= 20` | `true` |
| `<=` | Less than or equal to | `age <= 15` | `false` |
| `==` | Equal to | `age == 20` | `true` |
| `!=` | Not equal to | `age != 20` | `false` |

> [!WARNING]
> **The Common `=` vs `==` Bug**:
> - `x = 5` is **assignment** (stores 5 into x).
> - `x == 5` is **comparison** (checks if x equals 5).
> 
> Writing `if (x = 5)` instead of `if (x == 5)` is one of the most common beginner bugs in C++!

---

## 💻 3. Code Example

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 20;

    if (age >= 18) {
        cout << "Access Granted: You are an adult!\n";
    }

    return 0;
}
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L12 — Char & Bool Types**](L12_CharAndBool.md) | [**Basic Syntax**](../) | [**L14 — Conditionals: if-else**](L14_IfElse.md) |
