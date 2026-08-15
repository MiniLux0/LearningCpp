<div align="center">

# 🚀 Section 02: Basic Syntax — Variables, Types, Control Flow & Loops

> **Lessons**: L06 – L22  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 02) / Stanford CS106L (Lectures 02 & 03)  
> 📝 **Executive Summary**: 📝 [**`summary/02_BasicSyntax_Notes.md`**](summary/02_BasicSyntax_Notes.md)  
> 🎯 **Primary Focus**: Primitive data types, memory representations, floating-point comparison, Uniform Initialization `{}`, conditional branching, and loop control structures.

---

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| [**⬅️ Section 01: Getting Started**](../01_GettingStarted/README.md) | **Section 02: Basic Syntax** | [**Section 03: Subroutines ➡️**](../03_Subroutines/README.md) |

</div>

---

## 📌 Module Overview

This module covers core C++ syntax: primitive types (`int`, `float`, `double`, `char`, `bool`), binary memory layouts, integer overflow/underflow, floating-point precision hazards, Uniform Initialization `{}` (C++11/17), safe float comparisons using $\epsilon$, conditional branching (`if`, `else if`, `else`, `switch`), and loop control (`while`, `do-while`, `for`, `break`, `continue`).

---

## 📋 Lessons, Theory & Code Inventory

| # | Lesson Name | 📘 Theory Note | 💻 Code Lab | Key Technical Concepts | Status |
|---|-------------|----------------|-------------|------------------------|:------:|
| **L06** | **Variables** | 📘 [`theory/l06_variables.md`](theory/l06_variables.md) | 💻 [`code/l06_variables.cpp`](code/l06_variables.cpp) | Variable declaration, assignment, Lvalues, initial values. | ✅ |
| **L07** | **Strings Intro** | 📘 [`theory/l07_strings.md`](theory/l07_strings.md) | 💻 [`code/l07_strings.cpp`](code/l07_strings.cpp) | Basic `string` concatenation and output. | ✅ |
| **L08** | **User Input** | 📘 [`theory/l08_user_input.md`](theory/l08_user_input.md) | 💻 [`code/l08_user_input.cpp`](code/l08_user_input.cpp) | Reading typed inputs, prompt string chaining. | ✅ |
| **L09** | **Binary Numbers** | 📘 [`theory/l09_binary_numbers.md`](theory/l09_binary_numbers.md) | 💻 [`code/l09_binary_numbers.cpp`](code/l09_binary_numbers.cpp) | Bit representations, 2's complement, binary layout. | ✅ |
| **L10** | **Integer Types** | 📘 [`theory/l10_integer_types.md`](theory/l10_integer_types.md) | 💻 [`code/l10_integer_types.cpp`](code/l10_integer_types.cpp) | `short`, `int`, `long`, `long long`, `unsigned`, `sizeof()`, overflow. | ✅ |
| **L11** | **Floating-Point** | 📘 [`theory/L11_FloatingPointTypes.md`](theory/L11_FloatingPointTypes.md) | 💻 [`code/L11_FloatingPointTypes.cpp`](code/L11_FloatingPointTypes.cpp) | `float`, `double`, scientific notation, IEEE 754 precision limit. | ✅ |
| **L12** | **Char and Bool** | 📘 [`theory/l12_char_and_bool.md`](theory/l12_char_and_bool.md) | 💻 [`code/l12_char_and_bool.cpp`](code/l12_char_and_bool.cpp) | ASCII character encoding, `bool` truth values, `boolalpha`. | ✅ |
| **L13** | **If Statements** | 📘 [`theory/l13_if.md`](theory/l13_if.md) | 💻 [`code/l13_if.cpp`](code/l13_if.cpp) | Basic conditional evaluation, boolean expressions. | ✅ |
| **L14** | **If-Else** | 📘 [`theory/l14_if_else.md`](theory/l14_if_else.md) | 💻 [`code/l14_if_else.cpp`](code/l14_if_else.cpp) | Binary decision branching, alternative execution paths. | ✅ |
| **L15** | **If-Else-If** | 📘 [`theory/l15_if_else_if_else.md`](theory/l15_if_else_if_else.md) | 💻 [`code/l15_if_else_if_else.cpp`](code/l15_if_else_if_else.cpp) | Multi-way decision trees, mutually exclusive checks. | ✅ |
| **L16** | **Comparing Floats** | 📘 [`theory/L16_ComparingFloats.md`](theory/L16_ComparingFloats.md) | 💻 [`code/L16_ComparingFloats.cpp`](code/L16_ComparingFloats.cpp) | Floating-point rounding errors, epsilon $\epsilon$ thresholding. | ✅ |
| **L17** | **Conditions** | 📘 [`theory/l17_conditions.md`](theory/l17_conditions.md) | 💻 [`code/l17_conditions.cpp`](code/l17_conditions.cpp) | Complex expressions, logical AND `&&`, OR `\|\|`, NOT `!`. | ✅ |
| **L18** | **While Loops** | 📘 [`theory/l18_while_loops.md`](theory/l18_while_loops.md) | 💻 [`code/l18_while_loops.cpp`](code/l18_while_loops.cpp) | Pre-test iterative execution, loop counters. | ✅ |
| **L19** | **Do-While Loops** | 📘 [`theory/l19_do_while_loops.md`](theory/l19_do_while_loops.md) | 💻 [`code/l19_do_while_loops.cpp`](code/l19_do_while_loops.cpp) | Post-test iterative execution, input validation loop. | ✅ |
| **L20** | **For Loops** | 📘 [`theory/l20_for_loops.md`](theory/l20_for_loops.md) | 💻 [`code/l20_for_loops.cpp`](code/l20_for_loops.cpp) | Counter-controlled iterations, initialization, condition, step. | ✅ |
| **L21** | **Break & Continue** | 📘 [`theory/l21_break_and_continue.md`](theory/l21_break_and_continue.md) | 💻 [`code/l21_break_and_continue.cpp`](code/l21_break_and_continue.cpp) | Loop control flow alteration, early termination, skipping steps. | ✅ |
| **L22** | **Switch Case** | 📘 [`theory/l22_switch.md`](theory/l22_switch.md) | 💻 [`code/l22_switch.cpp`](code/l22_switch.cpp) | Discrete integral branching, `case`, `break`, `default`. | ✅ |

---

## 🎯 Practical Exercises (E01 – E10)

> 📖 **Exercise Guide**: 📂 [**`exercise/README.md`**](exercise/README.md)

| # | Exercise Name | Topic | 💻 Solution File | Status |
|---|---------------|-------|------------------|:------:|
| **E01** | **Variable Types** | Declarations & types | 💻 [`exercise/E01_VariableTypes.cpp`](exercise/E01_VariableTypes.cpp) | ✅ |
| **E02** | **Name and Age** | Data I/O & string combination | 💻 [`exercise/E02_NameAndAge.cpp`](exercise/E02_NameAndAge.cpp) | ✅ |
| **E03** | **Sizeof Types** | Memory size inspection | 💻 [`exercise/E03_SizeofTypes.cpp`](exercise/E03_SizeofTypes.cpp) | ✅ |
| **E04** | **Float Precision** | Floating-point $\epsilon$ comparison | 💻 [`exercise/E04_FloatPrecision.cpp`](exercise/E04_FloatPrecision.cpp) | ✅ |
| **E05** | **Integer Division** | Integer truncation vs `double` | 💻 [`exercise/E05_IntegerDivision.cpp`](exercise/E05_IntegerDivision.cpp) | ✅ |
| **E06** | **Char ASCII** | Character encoding & casting | 💻 [`exercise/E06_CharASCII.cpp`](exercise/E06_CharASCII.cpp) | ✅ |
| **E07** | **Grade Check** | Simple conditional branching | 💻 [`exercise/E07_GradeCheck.cpp`](exercise/E07_GradeCheck.cpp) | ✅ |
| **E08** | **Age Classifier** | Nested `if-else if` trees | 💻 [`exercise/E08_AgeClassifier.cpp`](exercise/E08_AgeClassifier.cpp) | ✅ |
| **E09** | **Compare Numbers** | Relational & logical operators | 💻 [`exercise/E09_CompareNumbers.cpp`](exercise/E09_CompareNumbers.cpp) | ✅ |
| **E10** | **Simple Calculator** | Multi-way `switch` & loop control | 💻 [`exercise/E10_SimpleCalculator.cpp`](exercise/E10_SimpleCalculator.cpp) | ✅ |

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L06–L12** | 📄 [`MIT 6.096 Lecture 02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) | Primitive types, binary representations, `sizeof()`, integer overflow, IEEE floating-point. |
| **L13–L22** | 📄 [`MIT 6.096 Lecture 02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) \| [`CS106L Lecture 02`](../files/cs106l/lectures/WL2-Structures.pdf) | Conditionals, logical operators, float comparison, loop control structures (`while`, `for`, `switch`). |

---

## 🛠️ Build & Compilation Guides

Both `code/` and `exercise/` subdirectories contain automated `makefile` scripts:
- ⚙️ **Compilation Tutorial**: [`docs/COMPILATION_GUIDE.md`](../docs/COMPILATION_GUIDE.md)
- 🛠️ **Makefile & Sanitizer Reference**: [`docs/MAKEFILE_GUIDE.md`](../docs/MAKEFILE_GUIDE.md)

> [!TIP]
> **New to C++ compilation?**
> If you don't know how to compile or run C++ code from your terminal, refer to the documentation hub in 📂 [**`docs/README.md`**](../docs/README.md).


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>