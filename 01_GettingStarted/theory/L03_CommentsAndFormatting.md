# Lesson 03 — Comments, Newlines & Code Formatting

In this lesson, you will learn how to write comments, format text output using escape sequences, and follow clean code practices.

---

## 📝 1. Comments in C++

Comments are notes written for human developers. The compiler completely ignores them during compilation.

### Single-Line Comments (`//`)
```cpp
// This is a single-line comment
int x = 10; // Comment after code
```

### Multi-Line Comments (`/* ... */`)
```cpp
/*
   This is a multi-line comment.
   It can span as many lines as needed
   to explain complex algorithms.
*/
```

---

## 🔤 2. Newlines & Escape Sequences

Escape sequences are special characters preceded by a backslash `\` that control text formatting:

| Escape Sequence | Effect | Description |
|-----------------|--------|-------------|
| `\n` | Newline | Moves the cursor to the beginning of the next line |
| `std::endl` | Newline + Flush | Moves to next line AND flushes the output buffer |
| `\t` | Tab | Inserts a tab space for aligning text columns |
| `\"` | Double Quote | Prints a literal `"` character inside strings |
| `\\` | Backslash | Prints a literal `\` character |

### Example Code:
```cpp
#include <iostream>

int main() {
    std::cout << "Line 1\nLine 2\n";
    std::cout << "Column 1\tColumn 2\n";
    std::cout << "She said: \"C++ is awesome!\"\n";
    return 0;
}
```

---

## 🎨 3. Code Formatting Best Practices
1. **Consistent Indentation**: Always indent code inside `{}` blocks by 4 spaces.
2. **One Statement per Line**: Keep lines clean; don't pack multiple statements together.
3. **End with Semicolons**: Every statement MUST end with `;`.
