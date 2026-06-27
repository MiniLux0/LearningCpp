# Basic Syntax — Study Notes

Personal notes from section 02 of **John Purcell's** course on Udemy. Here I cover the fundamentals of the language: data types, variables, user input, and control structures.

---

## L06 — Variables

- Variables are containers for storing data in memory
- Each variable has a **type** that defines what it can hold (int, double, char, bool)
- They are declared with a name and assigned a value: `int age = 25;`
- Names should be descriptive and have no spaces
- They can be updated with operators like `+=`, `-=`, `*=`

## L07 — Strings

- A `string` is a text chain (collection of characters)
- You need to include `#include <string>`
- They can be concatenated with the `+` operator: `"Hello " + name`
- They are different from `char` (which holds only one character)

## L08 — User Input

- `cin >> variable` reads data from the user via keyboard
- Works with strings, ints, doubles, etc.
- Always show a message before requesting input with `cout`
- `cin` only reads until the first space; for full lines use `getline(cin, variable)`

## L09 — Binary Numbers and Computer Memory

- The computer only understands binary (0 and 1)
- **Bit**: smallest unit (0 or 1)
- **Byte**: 8 bits grouped together
- Each variable type occupies a certain number of bytes in memory
- int = 4 bytes, char = 1 byte, long long = 8 bytes
- If a number exceeds the type's range → **overflow**

## L10 — Integer Types

- Different integer types for different ranges:
  - `short` — 2 bytes (less range)
  - `int` — 4 bytes (most common)
  - `long` — 4 bytes (on Windows)
  - `long long` — 8 bytes (very large range)
- `sizeof(type)` shows how many bytes it occupies
- `<limits>` header provides `INT_MAX`, `INT_MIN`, etc.

## L11 — Floating Point Types

- `float` (4 bytes) and `double` (8 bytes) for decimal numbers
- `double` is more precise and commonly used
- **Integer division trap:** `1 / 3 = 0` because both are `int` → truncates decimals
- **Fix:** Make at least one operand a decimal: `1.0 / 3 = 0.333333`
- `float` has ~7 significant digits, `double` has ~15-17
- `<iomanip>` provides output manipulators:
  - `fixed` — forces decimal notation (e.g., `0.333333`)
  - `scientific` — forces scientific notation (e.g., `3.33e-01`)
  - `setprecision(n)` — controls number of decimal places
  - `defaultfloat` — returns to default behavior
- Manipulators are "sticky" — once set, they affect all subsequent output

## L12 — Char and Bool *(pending)*

- `char` holds a single character in single quotes: `'A'`
- `bool` holds `true` or `false`

## L13–L17 — Conditionals *(pending)*

- `if`, `if-else`, `if-else if-else`
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `&&` (AND), `||` (OR), `!` (NOT)

## L18–L21 — Loops *(pending)*

- `while` — repeats while the condition is true
- `do-while` — similar but always runs at least once
- `for` — when we know how many times to repeat
- `break` exits the loop, `continue` skips to the next iteration

## L22–L25 — Arrays *(pending)*

- Arrays store multiple values of the same type
- Accessed by index (starts at 0)
- Multidimensional arrays are "arrays of arrays"
- `sizeof` can be used to calculate the size of an array

## L26 — Switch *(pending)*

- Alternative to many `if-else if`
- Works with `int`, `char`, and `enum`

---

## Good practices so far

- Always initialize variables before using them
- Use descriptive names (`numberCats` instead of `n`)
- Include `<iostream>` and `<string>` when needed
- Use `\n` instead of `endl` for better performance

---

*Last updated: L11 — Floating Point Types*
