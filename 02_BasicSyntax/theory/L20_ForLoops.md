# Lesson 20 — The `for` Loop & Nested Loops

The `for` loop consolidates loop initialization, condition testing, and increment/decrement into a single line.

---

## 🔄 1. Syntax of `for`

```cpp
for (initialization; condition; increment) {
    // Loop body
}
```

### Example & Execution Sequence:
1. **Initialization** (`int i = 0`): Executed once before loop starts.
2. **Condition** (`i < 5`): Tested before each iteration.
3. **Loop Body**: Executed if condition is true.
4. **Increment** (`++i`): Executed after loop body completes.

---

## 🔲 2. Nested Loops (Matrices / Grids)
```cpp
for (int row = 1; row <= 3; ++row) {
    for (int col = 1; col <= 4; ++col) {
        cout << "(" << row << "," << col << ") ";
    }
    cout << "\n";
}

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L19 — The do-while Loop**](L19_DoWhileLoops.md) | [**Basic Syntax**](../) | [**L21 — break and continue**](L21_BreakAndContinue.md) |

```
