# 📝 Section 02: Basic Syntax — Study Summary and Notes

Study notes and executive summary for **Section 02: Basic C++ Syntax**.
Covers variables, primitive types (`int`, `float`, `double`, `char`, `bool`), binary representation and 2's complement, overflow, type casting, safe floating-point comparison with epsilon ( $\epsilon$ ), conditionals (`if`, `else`, `switch`), and loop control structures (`while`, `do-while`, `for`, `break`, `continue`).

---

## 🧭 Table of Contents

1. [Lessons and Theory](#-lessons-and-theory)
2. [Practical Exercises (E01 – E10)](#-practical-exercises-e01--e10)
3. [Summary by Lesson](#-summary-by-lesson)
   - [L06 – L12: Variables, Primitive Types, and Memory](#l06--l12-variables-primitive-types-and-memory)
   - [L13 – L17: Conditional Flow Control](#l13--l17-conditional-flow-control)
   - [L18 – L22: Repetitive Structures and Loops](#l18--l22-repetitive-structures-and-loops)
4. [Best Practices and Key Patterns](#-best-practices-and-key-patterns)

---

## 📘 Lessons and Theory

| Lesson | Title | Theory Note | Code Lab |
| :--- | :--- | :--- | :--- |
| **L06** | Variables | 📘 [`l06_variables.md`](../theory/l06_variables.md) | 💻 [`l06_variables.cpp`](../code/l06_variables.cpp) |
| **L07** | Strings Intro | 📘 [`l07_strings.md`](../theory/l07_strings.md) | 💻 [`l07_strings.cpp`](../code/l07_strings.cpp) |
| **L08** | User Input | 📘 [`l08_user_input.md`](../theory/l08_user_input.md) | 💻 [`l08_user_input.cpp`](../code/l08_user_input.cpp) |
| **L09** | Binary Numbers | 📘 [`l09_binary_numbers.md`](../theory/l09_binary_numbers.md) | 💻 [`l09_binary_numbers.cpp`](../code/l09_binary_numbers.cpp) |
| **L10** | Integer Types | 📘 [`l10_integer_types.md`](../theory/l10_integer_types.md) | 💻 [`l10_integer_types.cpp`](../code/l10_integer_types.cpp) |
| **L11** | Floating-Point | 📘 [`L11_FloatingPointTypes.md`](../theory/L11_FloatingPointTypes.md) | 💻 [`L11_FloatingPointTypes.cpp`](../code/L11_FloatingPointTypes.cpp) |
| **L12** | Char & Bool | 📘 [`l12_char_and_bool.md`](../theory/l12_char_and_bool.md) | 💻 [`l12_char_and_bool.cpp`](../code/l12_char_and_bool.cpp) |
| **L13** | If Statements | 📘 [`l13_if.md`](../theory/l13_if.md) | 💻 [`l13_if.cpp`](../code/l13_if.cpp) |
| **L14** | If-Else | 📘 [`l14_if_else.md`](../theory/l14_if_else.md) | 💻 [`l14_if_else.cpp`](../code/l14_if_else.cpp) |
| **L15** | If-Else-If | 📘 [`l15_if_else_if_else.md`](../theory/l15_if_else_if_else.md) | 💻 [`l15_if_else_if_else.cpp`](../code/l15_if_else_if_else.cpp) |
| **L16** | Comparing Floats | 📘 [`L16_ComparingFloats.md`](../theory/L16_ComparingFloats.md) | 💻 [`L16_ComparingFloats.cpp`](../code/L16_ComparingFloats.cpp) |
| **L17** | Conditions | 📘 [`l17_conditions.md`](../theory/l17_conditions.md) | 💻 [`l17_conditions.cpp`](../code/l17_conditions.cpp) |
| **L18** | While Loops | 📘 [`l18_while_loops.md`](../theory/l18_while_loops.md) | 💻 [`l18_while_loops.cpp`](../code/l18_while_loops.cpp) |
| **L19** | Do-While Loops | 📘 [`l19_do_while_loops.md`](../theory/l19_do_while_loops.md) | 💻 [`l19_do_while_loops.cpp`](../code/l19_do_while_loops.cpp) |
| **L20** | For Loops | 📘 [`l20_for_loops.md`](../theory/l20_for_loops.md) | 💻 [`l20_for_loops.cpp`](../code/l20_for_loops.cpp) |
| **L21** | Break & Continue | 📘 [`l21_break_and_continue.md`](../theory/l21_break_and_continue.md) | 💻 [`l21_break_and_continue.cpp`](../code/l21_break_and_continue.cpp) |
| **L22** | Switch Case | 📘 [`l22_switch.md`](../theory/l22_switch.md) | 💻 [`l22_switch.cpp`](../code/l22_switch.cpp) |

---

## 🎯 Practical Exercises (E01 – E10)

| # | Exercise | Topic | Code File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **E01** | Variable Types | Declaration and initialization | 💻 [`E01_VariableTypes.cpp`](../exercise/E01_VariableTypes.cpp) | ✅ |
| **E02** | Name and Age | Input and data combination | 💻 [`E02_NameAndAge.cpp`](../exercise/E02_NameAndAge.cpp) | ✅ |
| **E03** | Sizeof Types | Memory size inspection | 💻 [`E03_SizeofTypes.cpp`](../exercise/E03_SizeofTypes.cpp) | ✅ |
| **E04** | Float Precision | Precision and comparison with $\epsilon$ | 💻 [`E04_FloatPrecision.cpp`](../exercise/E04_FloatPrecision.cpp) | ✅ |
| **E05** | Integer Division | Integer division vs `double` | 💻 [`E05_IntegerDivision.cpp`](../exercise/E05_IntegerDivision.cpp) | ✅ |
| **E06** | Char ASCII | Character encoding | 💻 [`E06_CharASCII.cpp`](../exercise/E06_CharASCII.cpp) | ✅ |
| **E07** | Grade Check | Simple conditionals | 💻 [`E07_GradeCheck.cpp`](../exercise/E07_GradeCheck.cpp) | ✅ |
| **E08** | Age Classifier | Nested conditionals (`if-else if`) | 💻 [`E08_AgeClassifier.cpp`](../exercise/E08_AgeClassifier.cpp) | ✅ |
| **E09** | Compare Numbers | Logical and relational operators | 💻 [`E09_CompareNumbers.cpp`](../exercise/E09_CompareNumbers.cpp) | ✅ |
| **E10** | Simple Calculator | Flow control with `switch` and loops | 💻 [`E10_SimpleCalculator.cpp`](../exercise/E10_SimpleCalculator.cpp) | ✅ |

---

## 💡 Summary by Lesson

### L06 – L12: Variables, Primitive Types, and Memory
- C++ is a strongly typed language. Each variable reserves a fixed space in RAM defined by its type.
- **Integer types:** `short` (2 bytes), `int` (4 bytes), `long long` (8 bytes). They can be `signed` or `unsigned` (positive only).
- **Overflow:** Occurs when a calculation exceeds the maximum value the type can store. In `signed` integers, it produces undefined behavior.
- **Floating-point:** `float` (4 bytes, ~7 digits of precision) and `double` (8 bytes, ~15 digits). 
- **Safe float comparison:** Never compare `a == b` directly in floating-point due to IEEE 754 binary rounding errors. Use `abs(a - b) < 1e-9`.
- **`char` and `bool`:** `char` stores an ASCII character (1 byte). `bool` stores true (`true`) or false (`false`).

### L13 – L17: Conditional Flow Control
- `if`, `else if`, and `else` allow branching program execution based on boolean expressions.
- Relational operators: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- Logical operators: AND (`&&`), OR (`||`), NOT (`!`). They have short-circuit evaluation.

### L18 – L22: Repetitive Structures and Loops
- `while`: Evaluates the condition before each iteration (0 or more times).
- `do-while`: Executes the body at least once before evaluating the condition.
- `for`: Ideal for iterations with a counter (`for (int i = 0; i < limit; i++)`).
- `break` interrupts the loop immediately; `continue` skips to the next iteration.
- `switch-case`: Clean structure for selecting among multiple integer values or enumeration constants.

---

## 🛡️ Best Practices and Key Patterns

1. **Uniform Initialization (C++11):** Use brace syntax `int x{0};` to prevent narrowing conversions.
2. **Safe floating-point comparison:** Use an epsilon value ( $\epsilon$ ) when evaluating decimal numbers.
3. **Floating-point division:** Ensure at least one operand is a `double` when dividing numbers to avoid integer truncation (`5.0 / 2` $\rightarrow$ `2.5`).

---

*Last update: Section 02 100% completed*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>