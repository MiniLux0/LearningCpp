# 🚀 Section 02: Basic Syntax — Variables, Types, Control Flow & Loops

> **Lessons**: L06 – L22  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 02) / Stanford CS106L (Lectures 02 & 03)  
> 📖 **Theory Documentation Directory**: 📂 [**`02_BasicSyntax/theory/`**](theory/)  
> 🎯 **Primary Focus**: Primitive data types, memory representations, floating-point comparison, Uniform Initialization `{}`, conditional branching, and loop control structures.

---

## 📌 Module Overview

This module covers the core syntax of C++. It explores primitive types (`int`, `float`, `double`, `char`, `bool`), binary memory representations, integer overflow/underflow, floating-point precision hazards, Uniform Initialization `{}` (C++11/17), safe float comparisons using $\epsilon$, conditional execution (`if`, `else if`, `else`, `switch`), and loop iteration (`while`, `do-while`, `for`, `break`, `continue`).

---

## 📖 Theory & Conceptual Documentation (`02_BasicSyntax/theory/`)

All theoretical concepts, memory layouts, and control flow diagrams for this module are documented in dedicated markdown notes:

| Theory Note | Main Concepts Documented |
|-------------|--------------------------|
| 📘 [**`theory/L06_Variables.md`**](theory/L06_Variables.md) | Variable declarations, initialization, lvalue vs rvalue memory concepts. |
| 📘 [**`theory/L07_Strings.md`**](theory/L07_Strings.md) | String mechanics, string literals, and concatenation. |
| 📘 [**`theory/L08_UserInput.md`**](theory/L08_UserInput.md) | Reading multiple inputs, stream state behavior. |
| 📘 [**`theory/L09_BinaryNumbers.md`**](theory/L09_BinaryNumbers.md) | 2's complement representation, binary layout, sign bit. |
| 📘 [**`theory/L10_IntegerTypes.md`**](theory/L10_IntegerTypes.md) | Integer sizes (`short`, `int`, `long`, `long long`), unsigned types, overflow. |
| 📘 [**`theory/L11_FloatingPointTypes.md`**](theory/L11_FloatingPointTypes.md) | IEEE 754 float/double representation, precision limits. |
| 📘 [**`theory/L12_CharAndBool.md`**](theory/L12_CharAndBool.md) | ASCII encoding, boolean truth values, `std::boolalpha`. |
| 📘 [**`theory/L13_If.md`**](theory/L13_If.md) | Single-branch conditional statements. |
| 📘 [**`theory/L14_IfElse.md`**](theory/L14_IfElse.md) | Two-way decision branching logic. |
| 📘 [**`theory/L15_IfElseIfElse.md`**](theory/L15_IfElseIfElse.md) | Multi-branch conditional chains. |
| 📘 [**`theory/L16_ComparingFloats.md`**](theory/L16_ComparingFloats.md) | Floating-point rounding errors, epsilon $\epsilon$ comparison. |
| 📘 [**`theory/L17_Conditions.md`**](theory/L17_Conditions.md) | Logical operators (`&&`, `||`, `!`), short-circuit evaluation. |
| 📘 [**`theory/L18_WhileLoops.md`**](theory/L18_WhileLoops.md) | Pre-test iteration loops, termination criteria. |
| 📘 [**`theory/L19_DoWhileLoops.md`**](theory/L19_DoWhileLoops.md) | Post-test loops with guaranteed initial execution. |
| 📘 [**`theory/L20_ForLoops.md`**](theory/L20_ForLoops.md) | Counter-controlled loops, loop variable scope. |
| 📘 [**`theory/L21_BreakAndContinue.md`**](theory/L21_BreakAndContinue.md) | Loop control flow jumps (`break`, `continue`). |
| 📘 [**`theory/L22_Switch.md`**](theory/L22_Switch.md) | Jump tables, `switch-case` statements, `default` branch. |

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L06–L12** | 📄 [`MIT 6.096 Lecture 01-02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) \| [`CS106L Lecture 03`](../files/cs106l/lectures/WL2-Structures.pdf) | Primitive data types, integer bit widths, 2's complement binary layout, float IEEE 754 precision, Uniform Initialization `{}` to prevent narrowing conversions. |
| **L13–L17** | 📄 [`MIT 6.096 Lecture 02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) | Relational operators, logical short-circuit evaluation (`&&`, `||`), safe floating-point comparison with epsilon limits. |
| **L18–L22** | 📄 [`MIT 6.096 Lecture 02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) | `while`, `do-while` (guaranteed execution), counter-controlled `for` loops, loop variable scope, `break`, `continue`, `switch-case` dispatch. |

---

## 💻 Lessons, Code & Theory Inventory (`02_BasicSyntax/`)

| # | Lesson | Theory Note | Code Implementation | Key Technical Concepts | Status |
|---|--------|-------------|---------------------|------------------------|:------:|
| **L06** | **Variables** | 📘 [`theory/L06_Variables.md`](theory/L06_Variables.md) | 💻 [`L06_Variables.cpp`](code/L06_Variables.cpp) | Variable declaration, assignment, Lvalues, initial values. | ✅ |
| **L07** | **Strings Intro** | 📘 [`theory/L07_Strings.md`](theory/L07_Strings.md) | 💻 [`L07_Strings.cpp`](code/L07_Strings.cpp) | Basic `std::string` concatenation and output. | ✅ |
| **L08** | **User Input** | 📘 [`theory/L08_UserInput.md`](theory/L08_UserInput.md) | 💻 [`L08_UserInput.cpp`](code/L08_UserInput.cpp) | Reading typed inputs, prompt string chaining. | ✅ |
| **L09** | **Binary Numbers** | 📘 [`theory/L09_BinaryNumbers.md`](theory/L09_BinaryNumbers.md) | 💻 [`L09_BinaryNumbers.cpp`](code/L09_BinaryNumbers.cpp) | Bit representations, 2's complement, binary to decimal layout. | ✅ |
| **L10** | **Integer Types** | 📘 [`theory/L10_IntegerTypes.md`](theory/L10_IntegerTypes.md) | 💻 [`L10_IntegerTypes.cpp`](code/L10_IntegerTypes.cpp) | `short`, `int`, `long`, `long long`, `unsigned`, `sizeof()` checks, overflow. | ✅ |
| **L11** | **Floating-Point** | 📘 [`theory/L11_FloatingPointTypes.md`](theory/L11_FloatingPointTypes.md) | 💻 [`L11_FloatingPointTypes.cpp`](code/L11_FloatingPointTypes.cpp) | `float`, `double`, `long double`, scientific notation, precision limits. | ✅ |
| **L12** | **Char and Bool** | 📘 [`theory/L12_CharAndBool.md`](theory/L12_CharAndBool.md) | 💻 [`L12_CharAndBool.cpp`](code/L12_CharAndBool.cpp) | ASCII character encoding, `bool` truth values (`true`/`false`), `std::boolalpha`. | ✅ |
| **L13** | **If Statements** | 📘 [`theory/L13_If.md`](theory/L13_If.md) | 💻 [`L13_If.cpp`](code/L13_If.cpp) | Basic conditional evaluation, boolean expressions. | ✅ |
| **L14** | **If-Else** | 📘 [`theory/L14_IfElse.md`](theory/L14_IfElse.md) | 💻 [`L14_IfElse.cpp`](code/L14_IfElse.cpp) | Binary decision branching, alternative execution paths. | ✅ |
| **L15** | **If-Else-If** | 📘 [`theory/L15_IfElseIfElse.md`](theory/L15_IfElseIfElse.md) | 💻 [`L15_IfElseIfElse.cpp`](code/L15_IfElseIfElse.cpp) | Multi-way conditional chains, default fallthrough. | ✅ |
| **L16** | **Comparing Floats** | 📘 [`theory/L16_ComparingFloats.md`](theory/L16_ComparingFloats.md) | 💻 [`L16_ComparingFloats.cpp`](code/L16_ComparingFloats.cpp) | Floating-point rounding errors, safe comparison using epsilon `abs(a - b) < eps`. | ✅ |
| **L17** | **Complex Conditions** | 📘 [`theory/L17_Conditions.md`](theory/L17_Conditions.md) | 💻 [`L17_Conditions.cpp`](code/L17_Conditions.cpp) | Logical AND `&&`, OR `||`, NOT `!`, short-circuit evaluation rules. | ✅ |
| **L18** | **While Loops** | 📘 [`theory/L18_WhileLoops.md`](theory/L18_WhileLoops.md) | 💻 [`L18_WhileLoops.cpp`](code/L18_WhileLoops.cpp) | Condition-controlled pre-test loops, loop counters. | ✅ |
| **L19** | **Do-While Loops** | 📘 [`theory/L19_DoWhileLoops.md`](theory/L19_DoWhileLoops.md) | 💻 [`L19_DoWhileLoops.cpp`](code/L19_DoWhileLoops.cpp) | Post-test loops guaranteed to run at least once. | ✅ |
| **L20** | **For Loops** | 📘 [`theory/L20_ForLoops.md`](theory/L20_ForLoops.md) | 💻 [`L20_ForLoops.cpp`](code/L20_ForLoops.cpp) | Init, condition, increment counter-controlled loop anatomy. | ✅ |
| **L21** | **Break & Continue** | 📘 [`theory/L21_BreakAndContinue.md`](theory/L21_BreakAndContinue.md) | 💻 [`L21_BreakAndContinue.cpp`](code/L21_BreakAndContinue.cpp) | Early loop exit (`break`) and iteration skipping (`continue`). | ✅ |
| **L22** | **Switch Statements** | 📘 [`theory/L22_Switch.md`](theory/L22_Switch.md) | 💻 [`L22_Switch.cpp`](code/L22_Switch.cpp) | Constant jump-table evaluation, `case` labels, `break` prevention of fallthrough, `default`. | ✅ |

---

## 🛠️ How to Compile & Run

To compile and run the code files in this module:

```bash
# Navigate to the code directory
cd 02_BasicSyntax/code

# Compile all lessons using Makefile
make

# Run a specific lesson executable
.\L06_Variables.exe
.\L16_ComparingFloats.exe
.\L22_Switch.exe
```

---

## 📁 Directory Structure

```
02_BasicSyntax/
├── README.md               # 📄 Module guide (this file)
├── theory/                 # 📘 Detailed Markdown theory notes (L06–L22)
│   ├── L06_Variables.md ... L22_Switch.md
├── code/                   # 💻 C++ source files (L06–L22) & Makefile
│   ├── L06_Variables.cpp ... L22_Switch.cpp
│   └── makefile
└── exercise/               # ✏️ Practical exercises (E01–E10)
```

---

## 🔗 Navigation & Quick Links

- ⬅️ [Previous Module: Section 01 — Getting Started](../01_GettingStarted/README.md)
- 📋 [Master Syllabus (`TEMARIO.md`)](../TEMARIO.md)
- 🌐 [Academic Files Hub (`files/README.md`)](../files/README.md)
- ➡️ [Next Module: Section 03 — Subroutines](../03_Subroutines/README.md)

---
*MiniLux0 — Learning C++ Section 02*
