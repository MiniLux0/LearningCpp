# Lesson 12 — Character Types, ASCII & Booleans

In this lesson, we cover two fundamental primitive types: `char` (for individual characters) and `bool` (for logical true/false flags).

---

## 🔤 1. Characters (`char`) & The ASCII Table

A `char` variable stores a **single character** inside single quotes (`'A'`, `'7'`, `'#'`).

Under the hood, computers store characters as numbers using the **ASCII Table** (American Standard Code for Information Interchange). For example:
- Letter `'A'` has an ASCII numeric value of `65`.
- Letter `'a'` has an ASCII numeric value of `97`.
- Character `'0'` has an ASCII numeric value of `48`.

### ASCII Math Code Example:
```cpp
#include <iostream>
using namespace std;

int main() {
    char letter = 'A';

    cout << "Character: " << letter << "\n";
    cout << "ASCII Numeric Value: " << (int)letter << "\n"; // Casting char to int

    // Adding 1 to 'A' (65 + 1 = 66 -> 'B')
    char next_letter = letter + 1;
    cout << "Next Character: " << next_letter << "\n";

    return 0;
}
```

---

## 🔘 2. Booleans (`bool`)

A `bool` variable stores a binary logical state: either `true` or `false`.

```cpp
bool is_logged_in = true;
bool has_admin_access = false;

cout << "Logged In: " << is_logged_in << "\n";       // Prints 1
cout << "Admin Access: " << has_admin_access << "\n"; // Prints 0
```

> [!NOTE]
> By default, `cout` prints `1` for `true` and `0` for `false`. If you want it to print `"true"` or `"false"` as text, add `cout << boolalpha;`!

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L11 — Floating-Point Types**](L11_FloatingPointTypes.md) | [**Basic Syntax**](../) | [**L13 — Conditionals: if**](L13_If.md) |
