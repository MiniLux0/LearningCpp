# Lesson 16 — Comparing Floating-Point Numbers & Epsilon

Here is a classic surprise for beginners: in programming, `0.1 + 0.2` does **NOT** equal `0.3`!

Why? Because computers represent numbers using binary bits ($2^{-1}, 2^{-2}, 2^{-3}$), and fractions like `0.1` cannot be stored with exact mathematical precision in binary floating-point format (IEEE 754).

---

## 💥 1. The Floating-Point Precision Bug

```cpp
#include <iostream>
using namespace std;

int main() {
    double sum = 0.1 + 0.2; // Evaluates to 0.30000000000000004

    if (sum == 0.3) {
        cout << "Equal!\n";
    } else {
        cout << "NOT Equal! (sum = " << sum << ")\n";
    }

    return 0;
}
```

### Expected Output:
```text
NOT Equal! (sum = 0.30000000000000004)
```

---

## 💡 2. The Solution: Epsilon Comparison Threshold

Instead of checking if two floating-point numbers are *exactly* equal (`a == b`), we check if the **absolute difference** between them is smaller than a tiny threshold called **epsilon** ($\epsilon = 10^{-9}$):

$$\text{are equal}(a, b) = |a - b| < \epsilon$$

```cpp
#include <iostream>
#include <cmath> // Required for std::abs()
using namespace std;

bool are_equal(double a, double b, double epsilon = 1e-9) {
    return abs(a - b) < epsilon;
}

int main() {
    double sum = 0.1 + 0.2;

    if (are_equal(sum, 0.3)) {
        cout << "Safely Compared: Equal!\n";
    }

    return 0;
}
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L15 — Conditionals: if-else if-else**](L15_IfElseIfElse.md) | [**Basic Syntax**](../) | [**L17 — Complex Logical Conditions**](L17_Conditions.md) |
