# Lesson 15 — Conditionals: `if-else if-else` & Logical Operators

Real life isn't always a simple black-and-white choice between two options. Often, we have **multiple possibilities** or need to combine multiple conditions together.

In this lesson, you will learn:
1. Multi-branch logic using `else if`.
2. Logical Operators: `&&` (AND), `||` (OR), `!` (NOT).

---

## 🔗 1. Logical Operators

Logical operators allow you to combine multiple conditions inside a single `if` statement:

| Operator | Name | Rule | Example |
|:--------:|------|------|---------|
| `&&` | **AND** | `true` ONLY IF **both** conditions are true | `(age >= 18 && score >= 70)` |
| `\|\|` | **OR** | `true` IF **at least one** condition is true | `(is_student \|\| has_coupon)` |
| `!` | **NOT** | Inverts a boolean (`true` becomes `false`) | `(!is_logged_in)` |

---

## 🔀 2. Multi-Branch Logic (`else if`)

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 22;
    int score = 85;

    // Checking applicant eligibility using logical AND (&&) and multi-branching
    if (age >= 18 && score >= 70) {
        cout << "Passed qualification!\n";
    } else if (age < 18) {
        cout << "Underage applicant.\n";
    } else {
        cout << "Score insufficient.\n";
    }

    return 0;
}
```

### Expected Output:
```text
Passed qualification!
```

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L14 — Conditionals: if-else**](L14_IfElse.md) | [**Basic Syntax**](../) | [**L16 — Comparing Floats**](L16_ComparingFloats.md) |
