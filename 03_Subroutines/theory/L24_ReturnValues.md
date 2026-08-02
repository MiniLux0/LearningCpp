# Lesson 24 — Return Values & Function Types

Consider a function similar to a calculator or a coffee machine: you press a button or provide it with data, it performs its work, and it **returns a result** (a number or a cup of coffee).

In C++, functions can return data back to the location where they were called using the **`return`** keyword.

---

## ↩️ 1. Return Types

To return a value, you replace `void` with the **data type** of the value the function is expected to return:

```cpp
#include <iostream>
using namespace std;

// Function returning an integer (int)
int calculateSquare(int number) {
    return number * number; // Sends the result back to the caller
}

// Function returning a boolean (bool)
bool isEven(int number) {
    return (number % 2 == 0);
}

int main() {
    int val = 7;

    // Storing the returned value in a variable
    int result = calculateSquare(val);
    cout << "Square of " << val << " = " << result << "\n";

    // Using the return value directly inside an if condition
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
> Once a function executes a `return` statement, it **immediately exits**. Any code written below a `return` statement inside that function will never be executed!

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L23 — Introduction to Functions**](L23_Functions.md) | [**Subroutines**](../) | [**L25 — Function Parameters**](L25_FunctionParameters.md) |