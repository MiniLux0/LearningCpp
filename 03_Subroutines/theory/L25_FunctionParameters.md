# Lesson 25 — Function Parameters: Pass by Value vs Pass by Reference

This is one of the most important lessons in your C++ journey!

When you pass a variable into a function, does the function work on a **copy** of the variable, or on the **original variable** itself?

---

## 📋 1. Pass by Value (Default Behavior)

By default in C++, parameters are **passed by value**. This means C++ creates an independent **copy** of the argument inside the function.

- Any changes made inside the function affect **ONLY the copy**.
- The original variable outside in `main()` remains completely untouched!

```cpp
void incrementByValue(int x) {
    x = x + 10; // Modifies local copy 'x'
}

int main() {
    int num = 5;
    incrementByValue(num);
    // num is STILL 5!
}
```

---

## 🔗 2. Pass by Reference (Using `&`)

If you want a function to **modify the original variable**, you pass it **by reference** using the ampersand `&`.

The `&` tells C++: *"Don't make a copy! Use the original variable directly as an alias."*

```cpp
#include <iostream>
using namespace std;

// Pass by Value (Copy)
void tryToChange(int a) {
    a = 100;
}

// Pass by Reference (Alias using &)
void reallyChange(int &a) {
    a = 100;
}

int main() {
    int num = 10;

    tryToChange(num);
    cout << "After tryToChange:  num = " << num << " (Unchanged!)\n";

    reallyChange(num);
    cout << "After reallyChange: num = " << num << " (Changed!)\n";

    return 0;
}
```

### Expected Output:
```text
After tryToChange:  num = 10 (Unchanged!)
After reallyChange: num = 100 (Changed!)
```

---

## 🔄 3. Classic Example: The `swap` Function

Swapping two variables is **impossible** with pass-by-value because you'd only swap copies!

```cpp
void swapNumbers(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L24 — Return Values**](L24_ReturnValues.md) | [**Subroutines**](../) | [**L26 — Headers & Prototypes**](L26_HeadersAndPrototypes.md) |