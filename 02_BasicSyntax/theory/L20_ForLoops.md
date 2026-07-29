# Lesson 20 — The `for` Loop & Nested Loops

When you know exact starting and ending points for a count, the **`for` loop** is the cleanest and most popular loop in C++.

It packages initialization, condition checking, and counter updating into **a single line**.

---

## 🔄 1. Syntax of `for`

```cpp
for (initialization; condition; update) {
    // Loop body executed on each iteration
}
```

### Order of Execution:
1. `initialization` (`int i = 0`): Executed once before loop starts.
2. `condition` (`i < 5`): Evaluated before each iteration.
3. **Loop Body**: Executed if condition is `true`.
4. `update` (`++i`): Executed after loop body finishes.

---

## 💻 2. Code Example: Counting and Nested Grids

```cpp
#include <iostream>
using namespace std;

int main() {
    // 1. Simple Counting Loop
    cout << "1. Counting from 1 to 5:\n  ";
    for (int i = 1; i <= 5; ++i) {
        cout << i << " ";
    }
    cout << "\n\n";

    // 2. Nested Loops (Creating a 3x3 Grid Pattern)
    cout << "2. 3x3 Grid Coordinate Pattern:\n";
    for (int row = 1; row <= 3; ++row) {       // Outer loop controls rows
        for (int col = 1; col <= 3; ++col) {   // Inner loop controls columns
            cout << "(" << row << "," << col << ") ";
        }
        cout << "\n"; // Newline after each row
    }

    return 0;
}
```

### Expected Output:
```text
1. Counting from 1 to 5:
  1 2 3 4 5 

2. 3x3 Grid Coordinate Pattern:
(1,1) (1,2) (1,3) 
(2,1) (2,2) (2,3) 
(3,1) (3,2) (3,3) 
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L19 — The do-while Loop**](L19_DoWhileLoops.md) | [**Basic Syntax**](../) | [**L21 — break and continue**](L21_BreakAndContinue.md) |
