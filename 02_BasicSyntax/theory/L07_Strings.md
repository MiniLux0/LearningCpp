# Lesson 07 — Working with Strings (`std::string`)

Strings represent sequences of text characters in C++.

---

## 🧵 1. The `std::string` Class

Unlike C-style character arrays, `std::string` is a modern object provided by `#include <string>`:

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string firstName = "John";
    string lastName = "Doe";

    // String Concatenation using '+'
    string fullName = firstName + " " + lastName;
    cout << "Full Name: " << fullName << "\n";
    cout << "Length: " << fullName.length() << " characters\n";

    return 0;
}

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L06 — Variables & Data Types**](L06_Variables.md) | [**Basic Syntax**](../) | [**L08 — Advanced User Input**](L08_UserInput.md) |

```
