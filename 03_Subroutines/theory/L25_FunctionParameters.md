# L25 — Function Parameters: Pass-by-Value vs. Pass-by-Reference (`&`)

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 03** ([`Lecture03_Functions.pdf`](../../files/mit6096/lectures/Lecture03_Functions.pdf)) and **Stanford CS106B Textbook Chapter 2 (*Reference Parameters & Aliasing*)** (*Programming Abstractions in C++* by Eric Roberts).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 03: Pass-by-Value vs. Reference Mechanics](../../files/mit6096/lectures/Lecture03_Functions.pdf)
  - 🌲 [Stanford CS106B — Chapter 2: Reference Parameters & Aliasing](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`L25_FunctionParameters.cpp`](../code/L25_FunctionParameters.cpp)

---

## Learning Objectives

- [ ] Differentiate between **Pass-by-Value** (copying data) and **Pass-by-Reference (`&`)** (sharing memory locations).
- [ ] Mutate variables in the calling function using reference parameters.
- [ ] Apply constant references (**`const string&`**) to avoid expensive memory copies while prohibiting modifications.

---

## 1. Pass-by-Value

By default, C++ passes arguments by **value**. The compiler creates an independent, local copy of the variable inside the function's stack frame:

```cpp
#include <iostream>
using namespace std;

void tryToModify(int x) { // x is an independent local copy
    x = 99; // Modifies only the local copy
}

int main() {
    int num = 10;
    tryToModify(num);
    cout << num << endl; // Prints 10 (the original value did NOT change!)
    return 0;
}
```

---

## 2. Pass-by-Reference (`&`)

By appending an ampersand `&` to the parameter type (`int& x`), the parameter becomes a **reference alias** pointing directly to the same RAM memory cell as the caller's variable:

<div align="center">
  <img src="assets/l25_pass_by_ref_manim.gif" alt="pass by reference memory trace">
  <p><em><strong>Pass-by-Reference in Memory:</strong> Pay close attention to how, when using <code>&amp;</code>, the function <code>mutate()</code> does not create a new variable. Instead, the alias <code>ref</code> is literally an invisible arrow pointing directly to the original box in <code>main</code>. When you mutate <code>ref</code>, you are mutating the original data!</em></p>
</div>

```cpp
#include <iostream>
using namespace std;

void modifyForReal(int& x) { // x is a reference to the original memory
    x = 99; // Mutates main's 'num' variable directly!
}

int main() {
    int num = 10;
    modifyForReal(num);
    cout << num << endl; // Prints 99!
    return 0;
}
```

---

## 3. Passing by Constant Reference (`const Type&`)

Copying large objects (such as a `string` with 1,000 characters) by value requires allocating memory and copying characters one by one. Using `const string&` passes the address by reference for maximum speed, while the compiler guarantees that the text cannot be modified:

```cpp
#include <iostream>
#include <string>
using namespace std;

void printLargeString(const string& text) {
    // Efficient! Zero memory copies, and compiler prohibits modifying 'text'
    cout << text << endl;
}
```

---

## ❓ Self-Assessment Checkpoint #1 — Swapping Values

Why does a `swap(int a, int b)` function fail to swap two integers in `main()` unless it is declared as `swap(int& a, int& b)`?

<details>
<summary>🔍 <strong>View Explanation & Answer</strong></summary>

> [!NOTE]
> **Answer:** Because without `&`, `swap` only exchanges temporary copies isolated inside its own call stack frame.
>
> **Explanation:**  
> When `swap(int a, int b)` terminates, its local copies are destroyed from RAM, leaving the original variables in `main()` completely intact. With `int& a, int& b`, the contents of the original memory addresses are swapped directly.

</details>

---

## 📝 Summary & Key Takeaways

1. **Pass-by-Value (`int x`):** Creates an independent copy; modifications do not affect the caller.
2. **Pass-by-Reference (`int& x`):** Shares the caller's RAM memory cell; allows mutating the original variable.
3. **Constant Reference (`const string&`):** Eliminates memory copy overhead while ensuring read-only safety.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:-------------------:|:------------------:|
| [**⬅️ L24 — Return Values**](L24_ReturnValues.md) | [**🏠 Subroutines**](../README.md) | [**L26 — Headers and Prototypes ➡️**](L26_HeadersAndPrototypes.md) |

</div>

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>