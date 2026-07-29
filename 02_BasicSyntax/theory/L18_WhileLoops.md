# Lesson 18 — The `while` Loop

Imagine you want to print numbers from 1 to 100. Writing `cout << 1; cout << 2; ...` would take a hundred lines of tedious code!

In programming, **loops** allow us to repeat a block of code automatically as long as a condition remains true.

---

## 🔄 1. Syntax of `while`

```cpp
while (condition) {
    // Code block repeated as long as condition evaluates to true
    // Remember to update your counter inside to avoid INFINITE LOOPS!
}
```

---

## 💻 2. Code Example: Counting from 1 to 5

```cpp
#include <iostream>
using namespace std;

int main() {
    int counter = 1; // 1. Loop variable initialization

    while (counter <= 5) { // 2. Condition check
        cout << "Count: " << counter << "\n";
        counter++; // 3. Update step (counter = counter + 1)
    }

    cout << "Loop Finished!\n";
    return 0;
}
```

### Expected Output:
```text
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
Loop Finished!
```

> [!WARNING]
> **Infinite Loop Hazard**: If you forget to update the counter (`counter++`), the condition `counter <= 5` will remain `true` forever, freezing your program in an infinite loop! Press `Ctrl + C` in terminal to terminate an infinite loop.

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L17 — Complex Logical Conditions**](L17_Conditions.md) | [**Basic Syntax**](../) | [**L19 — The do-while Loop**](L19_DoWhileLoops.md) |
