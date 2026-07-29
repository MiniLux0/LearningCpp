# Lesson 19 — The `do-while` Loop

Standard `while` loops check their condition **before** running the loop body. If the condition starts as `false`, the loop body never runs at all.

However, sometimes you want a loop body to execute **at least once** before checking the condition (for example, displaying a game menu or asking for a password).

In C++, we use the **`do-while` loop**.

---

## 🔄 1. Syntax of `do-while`

```cpp
do {
    // Code block executed AT LEAST ONCE
} while (condition); // Notice the required semicolon at the end!
```

---

## 💻 2. Code Example: Interactive Menu Input Validation

```cpp
#include <iostream>
using namespace std;

int main() {
    int choice;

    do {
        cout << "\n=== MAIN MENU ===\n";
        cout << "1. Start New Game\n";
        cout << "2. Exit Program\n";
        cout << "Enter your choice (1 or 2): ";
        cin >> choice;

        if (choice != 1 && choice != 2) {
            cout << "Invalid choice! Please try again.\n";
        }
    } while (choice != 1 && choice != 2);

    cout << "Valid option " << choice << " selected!\n";
    return 0;
}
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L18 — The while Loop**](L18_WhileLoops.md) | [**Basic Syntax**](../) | [**L20 — The for Loop**](L20_ForLoops.md) |
