# Lesson 24 — Return Values & Function Types

Think of a function like a calculator or a coffee machine: you press a button or feed it data, it performs work, and it **gives you back a result** (a number or a cup of coffee).

In C++, functions can return data back to the place where they were called using the **`return`** keyword.

---

## ↩️ 1. Return Types

Instead of `void`, you replace `void` with the **data type** of the value the function will return:

```cpp
#include <iostream>
using namespace std;

// Function returning an integer (int)
int calculateSquare(int number) {
    return number * number; // Sends result back to caller
}

// Function returning a boolean (bool)
bool isEven(int number) {
    return (number % 2 == 0);
}

int main() {
    int val = 7;

    // Storing returned value in a variable
    int result = calculateSquare(val);
    cout << "Square of " << val << " = " << result << "\n";

    // Using return value directly inside if condition
    if (isEven(val)) {
        cout << val << " is Even\n";
    } else {
        cout << val << " is Odd\n";
    }

    return 0;
}
```

### Expected Output:
```text
Square of 7 = 49
7 is Odd
```

> [!WARNING]
> Once a function executes a `return` statement, it **immediately exits**. Any code written below a `return` line inside that function will never be executed!

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L23 — Introduction to Functions**](L23_Functions.md) | [**Subroutines**](../) | [**L25 — Function Parameters**](L25_FunctionParameters.md) |