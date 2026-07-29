# Lesson 23 — Introduction to Functions (Subroutines)

Imagine you are building a house. Instead of manufacturing every brick, pipe, and window from scratch every single time, you use pre-built components that do specific jobs.

In programming, **functions** (also called subroutines) are reusable blocks of code designed to perform a specific task.

---

## 🛠️ 1. Why Do We Need Functions?

Without functions, if you need to calculate a tax 10 times in your code, you would have to copy and paste the same 5 lines of math 10 times.
- If the tax formula changes, you have to update it in 10 different places!
- Functions follow the **DRY Principle** (*Don't Repeat Yourself*).

---

## 💻 2. Function Syntax & Anatomy

```cpp
#include <iostream>
using namespace std;

// 1. Defining a Function
void showWelcomeBanner() {
    cout << "========================================\n";
    cout << "   WELCOME TO SUBROUTINES IN C++        \n";
    cout << "========================================\n";
}

int main() {
    // 2. Calling (Invoking) the Function
    showWelcomeBanner();
    cout << "Program logic running...\n";
    showWelcomeBanner(); // Called again!

    return 0;
}
```

### Breakdown:
- **`void`**: Return type indicating this function performs an action but does **not** return a value.
- **`showWelcomeBanner()`**: Function name followed by parentheses `()`.
- **`showWelcomeBanner();`**: Function call executing the body.

### Expected Output:
```text
========================================
   WELCOME TO SUBROUTINES IN C++        
========================================
Program logic running...
========================================
   WELCOME TO SUBROUTINES IN C++        
========================================
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Module | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L22 — switch-case Statement**](../../02_BasicSyntax/theory/L22_Switch.md) | [**Subroutines**](../) | [**L24 — Return Values**](L24_ReturnValues.md) |