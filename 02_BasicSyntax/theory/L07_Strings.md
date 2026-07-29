# Lesson 07 — Working with Text Strings (`std::string`)

In real-world applications, programs spend a lot of time processing words, sentences, email addresses, and usernames. In C++, we use **`std::string`** to store text.

---

## 🧵 1. What is a String?

A **string** is simply a sequence of characters glued together. While a `char` stores a single letter inside single quotes (`'A'`), a `string` stores words or sentences inside double quotes (`"Hello World"`).

To use strings, we include the `<string>` library header at the top of our file: `#include <string>`.

---

## 💻 2. Combining and Manipulating Strings

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string first_name = "Ada";
    string last_name = "Lovelace";

    // 1. Concatenation: Joining strings together using '+'
    string full_name = first_name + " " + last_name;
    cout << "Full Name: " << full_name << "\n";

    // 2. Length: Finding how many characters are in a string
    cout << "Character Count: " << full_name.length() << " characters\n";

    // 3. Accessing Individual Characters using zero-based index []
    cout << "First Letter: " << full_name[0] << "\n"; // 'A'
    cout << "Second Letter: " << full_name[1] << "\n"; // 'd'

    return 0;
}
```

### Expected Output:
```text
Full Name: Ada Lovelace
Character Count: 12 characters
First Letter: A
Second Letter: d
```

> [!TIP]
> **Zero-Based Indexing**: In programming, we always start counting positions from `0`. The 1st letter is at index `0`, the 2nd letter is at index `1`, and so on.

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L06 — Variables & Data Types**](L06_Variables.md) | [**Basic Syntax**](../) | [**L08 — Advanced User Input**](L08_UserInput.md) |
