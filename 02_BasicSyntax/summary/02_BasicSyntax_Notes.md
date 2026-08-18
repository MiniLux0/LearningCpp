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
| **L06** | Variables | 📘 [`L06_Variables.md`](../theory/L06_Variables.md) | 💻 [`L06_Variables.cpp`](../code/L06_Variables.cpp) |
| **L07** | Strings Intro | 📘 [`L07_Strings.md`](../theory/L07_Strings.md) | 💻 [`L07_Strings.cpp`](../code/L07_Strings.cpp) |
| **L08** | User Input | 📘 [`L08_UserInput.md`](../theory/L08_UserInput.md) | 💻 [`L08_UserInput.cpp`](../code/L08_UserInput.cpp) |
| **L09** | Binary Numbers | 📘 [`L09_BinaryNumbers.md`](../theory/L09_BinaryNumbers.md) | 💻 [`L09_BinaryNumbers.cpp`](../code/L09_BinaryNumbers.cpp) |
| **L10** | Integer Types | 📘 [`L10_IntegerTypes.md`](../theory/L10_IntegerTypes.md) | 💻 [`L10_IntegerTypes.cpp`](../code/L10_IntegerTypes.cpp) |
| **L11** | Floating-Point | 📘 [`L11_FloatingPointTypes.md`](../theory/L11_FloatingPointTypes.md) | 💻 [`L11_FloatingPointTypes.cpp`](../code/L11_FloatingPointTypes.cpp) |
| **L12** | Char & Bool | 📘 [`L12_CharAndBool.md`](../theory/L12_CharAndBool.md) | 💻 [`L12_CharAndBool.cpp`](../code/L12_CharAndBool.cpp) |
| **L13** | If Statements | 📘 [`L13_If.md`](../theory/L13_If.md) | 💻 [`L13_If.cpp`](../code/L13_If.cpp) |
| **L14** | If-Else | 📘 [`L14_IfElse.md`](../theory/L14_IfElse.md) | 💻 [`L14_IfElse.cpp`](../code/L14_IfElse.cpp) |
| **L15** | If-Else-If | 📘 [`L15_IfElseIfElse.md`](../theory/L15_IfElseIfElse.md) | 💻 [`L15_IfElseIfElse.cpp`](../code/L15_IfElseIfElse.cpp) |
| **L16** | Comparing Floats | 📘 [`L16_ComparingFloats.md`](../theory/L16_ComparingFloats.md) | 💻 [`L16_ComparingFloats.cpp`](../code/L16_ComparingFloats.cpp) |
| **L17** | Conditions | 📘 [`L17_Conditions.md`](../theory/L17_Conditions.md) | 💻 [`L17_Conditions.cpp`](../code/L17_Conditions.cpp) |
| **L18** | While Loops | 📘 [`L18_WhileLoops.md`](../theory/L18_WhileLoops.md) | 💻 [`L18_WhileLoops.cpp`](../code/L18_WhileLoops.cpp) |
| **L19** | Do-While Loops | 📘 [`L19_DoWhileLoops.md`](../theory/L19_DoWhileLoops.md) | 💻 [`L19_DoWhileLoops.cpp`](../code/L19_DoWhileLoops.cpp) |
| **L20** | For Loops | 📘 [`L20_ForLoops.md`](../theory/L20_ForLoops.md) | 💻 [`L20_ForLoops.cpp`](../code/L20_ForLoops.cpp) |
| **L21** | Break & Continue | 📘 [`L21_BreakAndContinue.md`](../theory/L21_BreakAndContinue.md) | 💻 [`L21_BreakAndContinue.cpp`](../code/L21_BreakAndContinue.cpp) |
| **L22** | Switch Case | 📘 [`L22_Switch.md`](../theory/L22_Switch.md) | 💻 [`L22_Switch.cpp`](../code/L22_Switch.cpp) |

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