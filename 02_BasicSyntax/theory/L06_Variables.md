# Lesson 06 — Variables & Basic Data Types

Imagine you have a set of labeled boxes in your room. One box is for storing shoes, another is for books, and another is for coins. You wouldn't put soup inside a shoe box! 

In C++, **variables** are like labeled memory boxes inside your computer's RAM. Before you put anything inside a box, C++ requires you to declare **what type of item** the box can hold.

---

## 📦 1. Declaring and Initializing Variables

In C++, creating a variable requires two pieces of information:
1. **Data Type**: Tells the computer how much memory space to reserve and what kind of data is allowed.
2. **Variable Name**: A unique identifier you choose to access the data later.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // 1. Integer (Whole numbers without decimals)
    int age = 20;

    // 2. Double (Numbers with decimal places)
    double height_meters = 1.75;

    // 3. Character (A single letter or symbol inside single quotes '')
    char grade = 'A';

    // 4. Boolean (True or false status)
    bool is_student = true;

    // 5. String (Text message inside double quotes "")
    string name = "Alice";

    // Printing our variables to the screen
    cout << "Name: " << name << "\n";
    cout << "Age: " << age << " years old\n";
    cout << "Height: " << height_meters << "m\n";
    cout << "Grade: " << grade << "\n";
    cout << "Student Status: " << is_student << " (1 means true)\n";

    return 0;
}
```

### Expected Output:
```text
Name: Alice
Age: 20 years old
Height: 1.75m
Grade: A
Student Status: 1 (1 means true)
```

---

## 🧮 2. Basic Arithmetic Operations

C++ lets you perform mathematical calculations using standard operators:

| Operator | Math Action | Example | Result |
|:--------:|-------------|---------|:------:|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `4 * 3` | `12` |
| `/` | Division | `10 / 2` | `5` |
| `%` | Modulo (Remainder) | `10 % 3` | `1` (10 divided by 3 leaves a remainder of 1) |

> [!WARNING]
> **Integer Division Trap**: Dividing two integers (`int / int`) discards the decimal part! For example, `7 / 2` results in `3`, not `3.5`. To get `3.5`, at least one number must be a decimal: `7.0 / 2`.

---

### 🧭 Navigation & Progression
| ⬅️ Previous Module | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L05 — Profile Generator**](../../01_GettingStarted/theory/L05_InteractiveProfileApp.md) | [**Basic Syntax**](../) | [**L07 — Working with Strings**](L07_Strings.md) |
