# Lesson 02 — Namespaces & Understanding `using namespace std;`

In this lesson, you will learn what namespaces are, why `std::` appears everywhere in standard C++, and how to use `using namespace std;` safely.

---

## 🏷️ 1. What is a Namespace?

A **namespace** is a named container that groups related functions, variables, and classes. It acts like a family surname to prevent naming conflicts in software projects.

Imagine two different libraries both define a function named `print()`:
- `Graphics::print()`
- `Printer::print()`

Namespaces allow both libraries to coexist without causing a compiler collision!

---

## 📦 2. The `std` Namespace

All standard library tools in C++ (like `cout`, `cin`, `string`, `vector`) live inside the **`std`** (standard) namespace.

### Approach A: Explicit Scope Resolution (`std::cout`) — Recommended
```cpp
#include <iostream>

int main() {
    std::cout << "Explicit namespace usage is clean and safe.\n";
    return 0;
}
```
- **Pros**: Explicit, zero risk of naming conflicts. Best practice in production code and header files (`.h`).

### Approach B: Global Directive (`using namespace std;`)
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Global namespace directive allows writing cout directly.\n";
    return 0;
}
```
- **Pros**: Shorter to type in small beginner scripts.
- **Cons**: Brings hundreds of standard names into global scope, which can cause subtle naming collisions in large projects.

---

## 💡 Summary Checklist
- [x] Namespaces prevent name collisions.
- [x] Standard library tools live in namespace `std`.
- [x] Use `std::` explicitly in large projects; `using namespace std;` is fine for quick scripts.
