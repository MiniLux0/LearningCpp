# Lesson 21 — Loop Control: `break` and `continue`

Sometimes during a loop iteration, you need to alter the standard flow:
- You want to **exit the loop immediately** when a specific condition occurs (e.g., target item found).
- You want to **skip the current item** and jump straight to the next iteration (e.g., ignore negative numbers).

In C++, we use **`break`** and **`continue`**.

---

## ⏹️ 1. `break`: Early Exit

The `break` statement instantly terminates the entire loop, jumping out to the code after the loop body.

```cpp
#include <iostream>
using namespace std;

int main() {
    int target = 3;

    for (int i = 1; i <= 5; ++i) {
        if (i == target) {
            cout << "Target " << target << " found! Exiting loop early.\n";
            break; // Exits loop immediately
        }
        cout << "Checking " << i << "...\n";
    }

    return 0;
}
```

---

## ⏭️ 2. `continue`: Skip Iteration

The `continue` statement skips the rest of the code inside the loop for the current iteration and jumps directly to the next iteration.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Printing ODD numbers (skipping even numbers):\n  ";
    for (int i = 1; i <= 10; ++i) {
        if (i % 2 == 0) {
            continue; // Skip even numbers!
        }
        cout << i << " ";
    }
    cout << "\n";

    return 0;
}
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L20 — The for Loop**](L20_ForLoops.md) | [**Basic Syntax**](../) | [**L22 — switch-case Statement**](L22_Switch.md) |
