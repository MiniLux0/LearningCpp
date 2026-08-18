# Lesson 07 — Working with Text Strings (`string`)

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **Stanford CS106L Lecture 06** ([`Lecture06_Containers.pdf`](../../files/cs106l/lectures/Lecture06_Containers.pdf)) and **Stanford CS106B Textbook Chapter 3** ([`CS106BX-Reader.pdf`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - ⚙️ [Stanford CS106L — Lecture 06: STL String Containers](../../files/cs106l/lectures/Lecture06_Containers.pdf)
  - 🌲 [Stanford CS106B — Chapter 3: Strings & Characters](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`L07_Strings.cpp`](../code/L07_Strings.cpp)

---

## Learning Objectives

- [ ] Understand `string` as a dynamic C++ Standard Library container class (`#include <string>`).
- [ ] Differentiate between single characters (`char` in `' '`) and string objects (`string` in `" "`).
- [ ] Perform string concatenation using `operator+`.
- [ ] Query string length (`.length()` / `.size()`) and index characters using `operator[]`.

---

## 1. What is `string`?

A `string` is an object representing a dynamic sequence of characters. Unlike legacy C-style character arrays (`char[]`), `string` manages its own memory automatically on the heap as text grows or shrinks.

<div align="center">
  <img src="assets/l07_strings_manim.gif" alt="l07_strings">
</div>

---

## 2. String Concatenation & Traversal

```cpp
#include <iostream>
#include <string>

int main() {
    string firstName = "Ada";
    string lastName = "Lovelace";

    // 1. Concatenation (+)
    string fullName = firstName + " " + lastName;
    cout << "Full Name: " << fullName << "\n";

    // 2. Length Inspection (.length() / .size())
    cout << "Total Characters: " << fullName.length() << "\n";

    // 3. Zero-indexed Character Access ([])
    cout << "First Character : " << fullName[0] << "\n"; // 'A'
    cout << "Last Character  : " << fullName[fullName.length() - 1] << "\n"; // 'e'

    return 0;
}
```

> [!IMPORTANT]
> **Zero-Based Indexing:**
> Like arrays, string indexing starts at `0`. The first character of a string `s` is `s[0]`, and the last valid character is `s[s.length() - 1]`.

---

## ❓ Self-Assessment Checkpoint #1 — Single vs. Double Quotes

What is the difference between `'A'` and `"A"` in C++?

<details>
<summary>🔍 <strong>View Explanation & Answer</strong></summary>

> [!WARNING]
> **Syntax Breakdown:**
> - `'A'` is a **`char` literal** representing a single character value stored as 1 byte of ASCII (`65`).
> - `"A"` is a **string literal** (a null-terminated sequence of characters containing `'A'` and `'\0'`) stored as 2 bytes in memory.
> Assigning `"A"` to a `char` variable (`char c = "A";`) will result in a compile-time type mismatch error.

</details>

---

## 📝 Summary & Key Takeaways

1. **Header:** Include `<string>` to use `string`.
2. **Operators:** Use `+` for concatenation and `[]` for character indexing.
3. **Methods:** `.length()` and `.size()` both return the character count in $O(1)$ time.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L06 — Variables & Types**](L06_Variables.md) | [**🏠 Basic Syntax**](../README.md) | [**L08 — Advanced User Input ➡️**](L08_UserInput.md) |

</div>


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>