# Lesson 10 — Integer Types, Ranges & Memory Limits

In C++, not all integer numbers require the same amount of memory. A small counter from 1 to 10 doesn't need as much space as the population of Earth (8 billion people)!

C++ gives you different integer data types so you can choose the right tool for the job.

---

## 📊 1. Integer Types & Memory Sizes

| Data Type | Memory Size | Minimum Value | Maximum Value | Best Used For |
|-----------|:-----------:|:-------------:|:-------------:|---------------|
| `short` | 2 Bytes (16 bits) | -32,768 | 32,767 | Small numbers (e.g., age, day of month) |
| `int` | 4 Bytes (32 bits) | -2,147,483,648 | 2,147,483,647 | Default choice for general counting |
| `long long` | 8 Bytes (64 bits) | $\approx -9 \times 10^{18}$ | $\approx 9 \times 10^{18}$ | Huge numbers (e.g., world population, bytes in terabytes) |

---

## ➕ 2. Signed vs Unsigned Integers

By default, integer types are **signed** (they can store both positive and negative values).

If you know a value will **never be negative** (like inventory count or pixel coordinates), you can prefix it with `unsigned`:

```cpp
unsigned int score = 5000; // Stores only 0 and positive numbers (up to 4.2 billion!)
```

---

## 💥 3. What is Integer Overflow?

When a number exceeds the maximum value its type can hold, it "overflows" and wraps around to negative values!

```cpp
#include <iostream>
#include <climits>
using namespace std;

int main() {
    int max_int = INT_MAX; // 2,147,483,647
    cout << "Max Int: " << max_int << "\n";

    // Adding 1 causes integer overflow!
    max_int = max_int + 1;
    cout << "After +1 (Overflow!): " << max_int << "\n";

    return 0;
}
```

### Expected Output:
```text
Max Int: 2147483647
After +1 (Overflow!): -2147483648
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L09 — Binary & Memory Layout**](L09_BinaryNumbers.md) | [**Basic Syntax**](../) | [**L11 — Floating-Point Types**](L11_FloatingPointTypes.md) |
