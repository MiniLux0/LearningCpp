# Lesson 05 — Mini-Project: Interactive Profile Generator

In this lesson, you will combine text printing, escape formatting, namespaces, and interactive user input into a complete console application.

---

## 🎯 Project Goal

Build a C++ program that:
1. Displays an ASCII banner header.
2. Prompts the user for their profile details (Name, Subject, Lucky Number).
3. Prints a neatly aligned summary profile card.

---

## 💻 Full Code Implementation

```cpp
#include <iostream>
#include <string>

int main() {
    // Banner Header
    std::cout << "========================================\n";
    std::cout << "    WELCOME TO C++ PROFILE GENERATOR    \n";
    std::cout << "========================================\n\n";

    // Variables to store user data
    std::string full_name;
    std::string favorite_subject;
    int lucky_number;

    // Collect user input
    std::cout << "1. Enter your name: ";
    std::cin >> full_name;

    std::cout << "2. Enter your favorite subject: ";
    std::cin >> favorite_subject;

    std::cout << "3. Enter your lucky number: ";
    std::cin >> lucky_number;

    // Output Formatted Summary Card
    std::cout << "\n----------------------------------------\n";
    std::cout << "          USER PROFILE CARD             \n";
    std::cout << "----------------------------------------\n";
    std::cout << " Name            : " << full_name << "\n";
    std::cout << " Favorite Topic  : " << favorite_subject << "\n";
    std::cout << " Lucky Number    : " << lucky_number << "\n";
    std::cout << " Status          : Ready to master C++!\n";
    std::cout << "----------------------------------------\n";

    return 0;
}
```

---

## 🏆 Concept Review
- [x] `#include <iostream>` and `#include <string>` headers
- [x] Banner formatting using `std::cout` and newlines `\n`
- [x] Variable declaration (`std::string`, `int`)
- [x] User input capture with `std::cin >>`
- [x] Output chaining `std::cout << "Text: " << variable << "\n";`

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Module |
|:------------------:|:---------------:|:--------------:|
| [**L04 — Interactive User Input**](L04_UserInputCin.md) | [**Getting Started**](../) | [**L06 — Variables & Data Types**](../../02_BasicSyntax/theory/L06_Variables.md) |

