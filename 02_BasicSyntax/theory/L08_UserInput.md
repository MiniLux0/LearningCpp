# Lesson 08 — Advanced User Input (`std::cin` & `std::getline`)

In this lesson, you will learn how to handle single-word input vs full sentence reading with spaces.

---

## ⌨️ 1. Reading Input with Spaces (`std::getline`)

`cin >> variable` stops reading at the first space. To read an entire line including spaces, use `getline(cin, variable)`:

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string full_sentence;
    cout << "Enter a complete sentence: ";
    getline(cin, full_sentence);

    cout << "You entered: " << full_sentence << "\n";
    return 0;
}

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L07 — Working with Strings**](L07_Strings.md) | [**Basic Syntax**](../) | [**L09 — Binary & Memory Layout**](L09_BinaryNumbers.md) |

```
