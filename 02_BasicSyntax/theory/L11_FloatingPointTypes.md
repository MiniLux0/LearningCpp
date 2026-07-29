# Lesson 11 — Floating-Point Types & Precision

Floating-point numbers represent real numbers with decimal points.

---

## 🔬 Float vs Double

- `float`: 4 Bytes (32 bits), $\approx 7$ decimal digits of precision.
- `double`: 8 Bytes (64 bits), $\approx 15$ decimal digits of precision (Standard choice).

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double pi = 3.141592653589793;
    std::cout << std::setprecision(10) << pi << "\n";
    return 0;
}
```
