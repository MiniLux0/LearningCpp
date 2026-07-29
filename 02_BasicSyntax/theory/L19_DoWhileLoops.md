# Lesson 19 — The `do-while` Loop

Unlike a `while` loop, a `do-while` loop evaluates its condition **after** executing the loop body, guaranteeing at least one execution.

---

## 🔄 1. Syntax

```cpp
do {
    // Executed at least ONCE before condition check
} while (condition); // Semicolon required!
```

### Typical Use Case: Interactive Menus
```cpp
int choice;
do {
    cout << "1. Play\n2. Exit\nEnter choice: ";
    cin >> choice;
} while (choice != 1 && choice != 2);

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L18 — The while Loop**](L18_WhileLoops.md) | [**Basic Syntax**](../) | [**L20 — The for Loop**](L20_ForLoops.md) |

```
