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
| **L06** | **Variables** | 📘 [`theory/L06_Variables.md`](theory/L06_Variables.md) | 💻 [`code/L06_Variables.cpp`](code/L06_Variables.cpp) | Variable declaration, assignment, Lvalues, initial values. | ✅ |
| **L07** | **Strings Intro** | 📘 [`theory/L07_Strings.md`](theory/L07_Strings.md) | 💻 [`code/L07_Strings.cpp`](code/L07_Strings.cpp) | Basic `string` concatenation and output. | ✅ |
| **L08** | **User Input** | 📘 [`theory/L08_UserInput.md`](theory/L08_UserInput.md) | 💻 [`code/L08_UserInput.cpp`](code/L08_UserInput.cpp) | Reading typed inputs, prompt string chaining. | ✅ |
| **L09** | **Binary Numbers** | 📘 [`theory/L09_BinaryNumbers.md`](theory/L09_BinaryNumbers.md) | 💻 [`code/L09_BinaryNumbers.cpp`](code/L09_BinaryNumbers.cpp) | Bit representations, 2's complement, binary layout. | ✅ |
| **L10** | **Integer Types** | 📘 [`theory/L10_IntegerTypes.md`](theory/L10_IntegerTypes.md) | 💻 [`code/L10_IntegerTypes.cpp`](code/L10_IntegerTypes.cpp) | `short`, `int`, `long`, `long long`, `unsigned`, `sizeof()`, overflow. | ✅ |
| **L11** | **Floating-Point** | 📘 [`theory/L11_FloatingPointTypes.md`](theory/L11_FloatingPointTypes.md) | 💻 [`code/L11_FloatingPointTypes.cpp`](code/L11_FloatingPointTypes.cpp) | `float`, `double`, scientific notation, IEEE 754 precision limit. | ✅ |
| **L12** | **Char and Bool** | 📘 [`theory/L12_CharAndBool.md`](theory/L12_CharAndBool.md) | 💻 [`code/L12_CharAndBool.cpp`](code/L12_CharAndBool.cpp) | ASCII character encoding, `bool` truth values, `boolalpha`. | ✅ |
| **L13** | **If Statements** | 📘 [`theory/L13_If.md`](theory/L13_If.md) | 💻 [`code/L13_If.cpp`](code/L13_If.cpp) | Basic conditional evaluation, boolean expressions. | ✅ |
| **L14** | **If-Else** | 📘 [`theory/L14_IfElse.md`](theory/L14_IfElse.md) | 💻 [`code/L14_IfElse.cpp`](code/L14_IfElse.cpp) | Binary decision branching, alternative execution paths. | ✅ |
| **L15** | **If-Else-If** | 📘 [`theory/L15_IfElseIfElse.md`](theory/L15_IfElseIfElse.md) | 💻 [`code/L15_IfElseIfElse.cpp`](code/L15_IfElseIfElse.cpp) | Multi-way decision trees, mutually exclusive checks. | ✅ |
| **L16** | **Comparing Floats** | 📘 [`theory/L16_ComparingFloats.md`](theory/L16_ComparingFloats.md) | 💻 [`code/L16_ComparingFloats.cpp`](code/L16_ComparingFloats.cpp) | Floating-point rounding errors, epsilon $\epsilon$ thresholding. | ✅ |
| **L17** | **Conditions** | 📘 [`theory/L17_Conditions.md`](theory/L17_Conditions.md) | 💻 [`code/L17_Conditions.cpp`](code/L17_Conditions.cpp) | Complex expressions, logical AND `&&`, OR `\|\|`, NOT `!`. | ✅ |
| **L18** | **While Loops** | 📘 [`theory/L18_WhileLoops.md`](theory/L18_WhileLoops.md) | 💻 [`code/L18_WhileLoops.cpp`](code/L18_WhileLoops.cpp) | Pre-test iterative execution, loop counters. | ✅ |
| **L19** | **Do-While Loops** | 📘 [`theory/L19_DoWhileLoops.md`](theory/L19_DoWhileLoops.md) | 💻 [`code/L19_DoWhileLoops.cpp`](code/L19_DoWhileLoops.cpp) | Post-test iterative execution, input validation loop. | ✅ |
| **L20** | **For Loops** | 📘 [`theory/L20_ForLoops.md`](theory/L20_ForLoops.md) | 💻 [`code/L20_ForLoops.cpp`](code/L20_ForLoops.cpp) | Counter-controlled iterations, initialization, condition, step. | ✅ |
| **L21** | **Break & Continue**| 📘 [`theory/L21_BreakAndContinue.md`](theory/L21_BreakAndContinue.md) | 💻 [`code/L21_BreakAndContinue.cpp`](code/L21_BreakAndContinue.cpp) | Loop control flow alteration, early termination, skipping steps. | ✅ |
| **L22** | **Switch Case** | 📘 [`theory/L22_Switch.md`](theory/L22_Switch.md) | 💻 [`code/L22_Switch.cpp`](code/L22_Switch.cpp) | Discrete integral branching, `case`, `break`, `default`. | ✅ |

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
| **E10** | **Simple Calculator**| Multi-way `switch` & loop control | 💻 [`exercise/E10_SimpleCalculator.cpp`](exercise/E10_SimpleCalculator.cpp) | ✅ |

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
*MiniLux0 — Learning C++ Section 02*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>