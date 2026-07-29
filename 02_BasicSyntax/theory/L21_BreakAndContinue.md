# Lesson 21 — Loop Control: `break` and `continue`

Flow control statements allow altering standard loop iteration sequences dynamically.

---

## ⏹️ 1. `break`
Exits the loop immediately, transferring control to the statement after the loop.

```cpp
for (int i = 1; i <= 10; ++i) {
    if (i == 5) break; // Exits loop when i reaches 5
}
```

---

## ⏭️ 2. `continue`
Skips the remainder of the current loop body and proceeds directly to the next iteration.

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 3) continue; // Skips printing 3
    cout << i << " ";
}

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L20 — The for Loop**](L20_ForLoops.md) | [**Basic Syntax**](../) | [**L22 — switch-case Statement**](L22_Switch.md) |

```
