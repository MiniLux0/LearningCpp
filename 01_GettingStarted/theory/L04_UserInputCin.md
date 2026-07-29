# Lesson 04 — Interactive User Input (`std::cin`)

In this lesson, you will learn how to make your C++ programs interactive by capturing keyboard input from the user.

---

## 📥 1. The Input Stream (`std::cin`)

While `std::cout` pushes data **OUT** to the console, `std::cin` pulls data **IN** from the user's keyboard.

### Streams Comparison:

```
[Keyboard]  ===>  std::cin >> variable  ===>  [C++ Program]
[C++ Program] ===> std::cout << data     ===>  [Console Screen]
```

- Notice the operators:
  - `std::cout <<` (Insertion operator, pointing left towards output).
  - `std::cin >>` (Extraction operator, pointing right towards variable).

---

## 💻 2. Basic User Input Example

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name;
    int age;

    std::cout << "Enter your first name: ";
    std::cin >> name; // Reads a single word from keyboard into 'name'

    std::cout << "Enter your age: ";
    std::cin >> age;  // Reads an integer from keyboard into 'age'

    std::cout << "Hello, " << name << "! You are " << age << " years old.\n";
    return 0;
}
```

---

## ⚠️ 3. Important Rules for Beginners
1. **Declare Variables First**: You must declare a variable (e.g., `std::string name;`) before passing it to `std::cin >> name;`.
2. **Single-Word Reading**: `std::cin >>` reads up to the first whitespace (space, tab, newline). To read full sentences with spaces, we use `std::getline()`.
3. **Data Type Matching**: Make sure the user inputs the expected type (e.g., entering letters into an `int` variable will cause an input error).

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L03 — Comments & Formatting**](L03_CommentsAndFormatting.md) | [**Getting Started**](../) | [**L05 — Profile Generator Project**](L05_InteractiveProfileApp.md) |

