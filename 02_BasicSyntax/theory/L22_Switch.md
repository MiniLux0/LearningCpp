# Lesson 22 — The `switch-case` Statement & Fall-Through

When you need to choose between many fixed integer or character values, an `if-else if-else` chain with 10 branches can get messy.

The **`switch` statement** provides a clean, organized alternative for multi-value selection.

---

## 🔀 1. Syntax of `switch`

```cpp
switch (expression) {
    case value1:
        // Executed if expression == value1
        break; // Crucial! Prevents falling into case value2
    case value2:
        // Executed if expression == value2
        break;
    default:
        // Default fallback if no cases match
        break;
}
```

---

## 💻 2. Code Example: Menu Selection

```cpp
#include <iostream>
using namespace std;

int main() {
    char option = 'B';

    switch (option) {
        case 'A':
            cout << "Selected: Start New Game\n";
            break;
        case 'B':
            cout << "Selected: Load Saved Game\n";
            break;
        case 'C':
            cout << "Selected: Display Settings\n";
            break;
        default:
            cout << "Invalid Selection!\n";
            break;
    }

    return 0;
}
```

### Expected Output:
```text
Selected: Load Saved Game
```

---

## ⚠️ 3. What is Fall-Through?

If you forget to write `break;` at the end of a `case`, execution **falls through** and executes all subsequent `case` blocks below it!

In C++17, if you intend for a case to fall through deliberately, add `[[fallthrough]];` to signal your intention cleanly to the compiler.

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Module |
|:------------------:|:---------------:|:--------------:|
| [**L21 — break and continue**](L21_BreakAndContinue.md) | [**Basic Syntax**](../) | [**L23 — Functions & Subroutines**](../../03_Subroutines/theory/L23_Functions.md) |
