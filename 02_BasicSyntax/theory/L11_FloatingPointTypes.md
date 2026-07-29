# Lesson 11 — Floating-Point Types & Precision

When working with measurements, scientific data, money, or physics, numbers require decimal points (e.g., `3.14159`, `-0.005`). In C++, numbers with decimal places are called **floating-point numbers**.

---

## 🔬 1. `float` vs `double`

C++ provides two primary floating-point types:

| Data Type | Memory Size | Precision (Decimal Digits) | Usage |
|-----------|:-----------:|:--------------------------:|-------|
| `float` | 4 Bytes (32 bits) | $\approx 7$ digits | Graphics/Games (saving memory when high precision isn't critical) |
| `double` | 8 Bytes (64 bits) | $\approx 15$ digits | **Default standard choice** for scientific and mathematical code |

---

## ⚙️ 2. Formatting Decimal Output with `<iomanip>`

By default, `std::cout` only prints up to 6 significant digits. To control how many decimal places are displayed, use `std::setprecision()` from `<iomanip>`:

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double pi = 3.141592653589793;

    cout << "Default output:   " << pi << "\n";
    cout << "Fixed (2 decimals): " << fixed << setprecision(2) << pi << "\n";
    cout << "Fixed (8 decimals): " << fixed << setprecision(8) << pi << "\n";

    return 0;
}
```

### Expected Output:
```text
Default output:   3.14159
Fixed (2 decimals): 3.14
Fixed (8 decimals): 3.14159265
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L10 — Integer Data Types**](L10_IntegerTypes.md) | [**Basic Syntax**](../) | [**L12 — Char & Bool Types**](L12_CharAndBool.md) |
