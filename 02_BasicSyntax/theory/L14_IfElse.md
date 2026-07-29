# Lesson 14 — Conditionals: The `if-else` Structure

In Lesson 13, we learned how to execute code when a condition is true. But what if the condition is false? What if we want a fallback plan?

The **`if-else`** structure provides a two-way branch:
- **IF** the condition is true, execute Branch A.
- **ELSE** (otherwise), execute Branch B.

---

## 🔀 1. Syntax of `if-else`

```cpp
if (condition) {
    // Branch A: Executed ONLY if condition is TRUE
} else {
    // Branch B: Executed ONLY if condition is FALSE
}
```

---

## 💻 2. Code Example: Age Checker

```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age: ";
    cin >> age;

    if (age >= 18) {
        cout << "Status: Eligible to vote!\n";
    } else {
        cout << "Status: Too young to vote. Try again in " << (18 - age) << " years.\n";
    }

    return 0;
}
```

### Expected Output (User enters `15`):
```text
Enter your age: 15
Status: Too young to vote. Try again in 3 years.
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L13 — Conditionals: if**](L13_If.md) | [**Basic Syntax**](../) | [**L15 — Conditionals: if-else if-else**](L15_IfElseIfElse.md) |
