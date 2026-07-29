# Lesson 17 — Complex Conditions & Short-Circuit Evaluation

In C++, boolean expressions inside `if` statements are evaluated efficiently using **Short-Circuit Evaluation**.

Understanding short-circuiting is crucial because it allows you to write safe code that avoids runtime crashes (like dividing by zero)!

---

## ⚡ 1. How Short-Circuit Evaluation Works

- **In `A && B` (AND)**: If `A` is `false`, C++ stops immediately and evaluates the entire expression as `false`. `B` is **never executed**.
- **In `A || B` (OR)**: If `A` is `true`, C++ stops immediately and evaluates the entire expression as `true`. `B` is **never executed**.

---

## 🛡️ 2. Real-World Use Case: Crash Guarding

Suppose you want to divide numbers, but you must prevent a **divide-by-zero crash**:

```cpp
#include <iostream>
using namespace std;

int main() {
    int divisor = 0;

    // Safe! 'divisor != 0' is FALSE, so (100 / divisor) is NEVER evaluated!
    if (divisor != 0 && (100 / divisor > 5)) {
        cout << "Calculation successful.\n";
    } else {
        cout << "Safe Guard Activated: Division by zero avoided!\n";
    }

    return 0;
}
```

### Expected Output:
```text
Safe Guard Activated: Division by zero avoided!
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L16 — Comparing Floats**](L16_ComparingFloats.md) | [**Basic Syntax**](../) | [**L18 — The while Loop**](L18_WhileLoops.md) |
