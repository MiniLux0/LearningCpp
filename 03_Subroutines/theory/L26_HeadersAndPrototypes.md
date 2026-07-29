# Lesson 26 — Function Prototypes & Header Files

In C++, the compiler reads your code strictly from **top to bottom**.

If you call a function in `main()` before it has been defined above `main()`, the compiler will throw an error: `error: 'myFunction' was not declared in this scope`.

---

## 📜 1. Function Prototypes (Forward Declarations)

A **function prototype** tells the compiler: *"Hey, a function with this name and signature exists! Its full implementation will be provided later."*

```cpp
#include <iostream>
using namespace std;

// 1. Function Prototype (Forward Declaration above main)
int add(int a, int b);

int main() {
    // 2. Calling the function (Compiler knows it exists!)
    cout << "5 + 3 = " << add(5, 3) << "\n";
    return 0;
}

// 3. Full Function Definition (Implementation below main)
int add(int a, int b) {
    return a + b;
}
```

---

## 📁 2. Header Files (`.h`) vs Source Files (`.cpp`)

In professional C++ software development:
- **Header Files (`.h`)**: Store function prototypes, constants, and class declarations (the "menu" / interface).
- **Source Files (`.cpp`)**: Store full function implementations (the "kitchen" / logic).

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Module |
|:------------------:|:---------------:|:--------------:|
| [**L25 — Function Parameters**](L25_FunctionParameters.md) | [**Subroutines**](../) | [**L27 — Arrays & Strings**](../../04_ArraysStrings/theory/L27_Arrays.md) |