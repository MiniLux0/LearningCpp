# 🚀 Section 02: Basic Syntax — Variables, Types, Control Flow & Loops

> **Lessons**: L06 – L22  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 02) / Stanford CS106L (Lectures 02 & 03)  
> 🎯 **Primary Focus**: Primitive data types, memory representations, floating-point comparison, Uniform Initialization `{}`, conditional branching, and loop control structures.

---

## 📌 Module Overview

This module covers the core syntax of C++. It explores primitive types (`int`, `float`, `double`, `char`, `bool`), binary memory representations, integer overflow/underflow, floating-point precision hazards, Uniform Initialization `{}` (C++11/17), safe float comparisons using $\epsilon$, conditional execution (`if`, `else if`, `else`, `switch`), and loop iteration (`while`, `do-while`, `for`, `break`, `continue`).

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L06–L12** | 📄 [`MIT 6.096 Lecture 01-02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) \| [`CS106L Lecture 03`](../files/cs106l/lectures/WL2-Structures.pdf) | Primitive data types, integer bit widths, 2's complement binary layout, float IEEE 754 precision, Uniform Initialization `{}` to prevent narrowing conversions. |
| **L13–L17** | 📄 [`MIT 6.096 Lecture 02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) | Relational operators, logical short-circuit evaluation (`&&`, `||`), safe floating-point comparison with epsilon limits. |
| **L18–L22** | 📄 [`MIT 6.096 Lecture 02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) | `while`, `do-while` (guaranteed execution), counter-controlled `for` loops, loop variable scope, `break`, `continue`, `switch-case` dispatch. |

---

## 💻 Lessons & Code Inventory (`02_BasicSyntax/code/`)

| # | Lesson | Code File | Key Technical Concepts | Status |
|---|--------|-----------|------------------------|:------:|
| **L06** | **Variables** | [`L06_Variables.cpp`](code/L06_Variables.cpp) | Variable declaration, assignment, Lvalues, initial values. | ✅ |
| **L07** | **Strings Intro** | [`L07_Strings.cpp`](code/L07_Strings.cpp) | Basic `std::string` concatenation and output. | ✅ |
| **L08** | **User Input** | [`L08_UserInput.cpp`](code/L08_UserInput.cpp) | Reading typed inputs, prompt string chaining. | ✅ |
| **L09** | **Binary Numbers** | [`L09_BinaryNumbers.cpp`](code/L09_BinaryNumbers.cpp) | Bit representations, 2's complement, binary to decimal layout. | ✅ |
| **L10** | **Integer Types** | [`L10_IntegerTypes.cpp`](code/L10_IntegerTypes.cpp) | `short`, `int`, `long`, `long long`, `unsigned`, `sizeof()` checks, overflow. | ✅ |
| **L11** | **Floating-Point** | [`L11_FloatingPointTypes.cpp`](code/L11_FloatingPointTypes.cpp) | `float`, `double`, `long double`, scientific notation, precision limits. | ✅ |
| **L12** | **Char and Bool** | [`L12_CharAndBool.cpp`](code/L12_CharAndBool.cpp) | ASCII character encoding, `bool` truth values (`true`/`false`), `std::boolalpha`. | ✅ |
| **L13** | **If Statements** | [`L13_If.cpp`](code/L13_If.cpp) | Basic conditional evaluation, boolean expressions. | ✅ |
| **L14** | **If-Else** | [`L14_IfElse.cpp`](code/L14_IfElse.cpp) | Binary decision branching, alternative execution paths. | ✅ |
| **L15** | **If-Else-If** | [`L15_IfElseIfElse.cpp`](code/L15_IfElseIfElse.cpp) | Multi-way conditional chains, default fallthrough. | ✅ |
| **L16** | **Comparing Floats** | [`L16_ComparingFloats.cpp`](code/L16_ComparingFloats.cpp) | Floating-point rounding errors, safe comparison using epsilon `abs(a - b) < eps`. | ✅ |
| **L17** | **Complex Conditions** | [`L17_Conditions.cpp`](code/L17_Conditions.cpp) | Logical AND `&&`, OR `||`, NOT `!`, short-circuit evaluation rules. | ✅ |
| **L18** | **While Loops** | [`L18_WhileLoops.cpp`](code/L18_WhileLoops.cpp) | Condition-controlled pre-test loops, loop counters. | ✅ |
| **L19** | **Do-While Loops** | [`L19_DoWhileLoops.cpp`](code/L19_DoWhileLoops.cpp) | Post-test loops guaranteed to run at least once. | ✅ |
| **L20** | **For Loops** | [`L20_ForLoops.cpp`](code/L20_ForLoops.cpp) | Init, condition, increment counter-controlled loop anatomy. | ✅ |
| **L21** | **Break & Continue** | [`L21_BreakAndContinue.cpp`](code/L21_BreakAndContinue.cpp) | Early loop exit (`break`) and iteration skipping (`continue`). | ✅ |
| **L22** | **Switch Statements** | [`L22_Switch.cpp`](code/L22_Switch.cpp) | Constant jump-table evaluation, `case` labels, `break` prevention of fallthrough, `default`. | ✅ |

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
├── code/                   # C++ source files (L06–L22) & Makefile
│   ├── L06_Variables.cpp ... L22_Switch.cpp
│   └── makefile
├── theory/                 # Detailed Markdown notes & theory docs
└── exercise/               # Practical exercises (E01–E10)
```

---

## 🔗 Navigation & Quick Links

- ⬅️ [Previous Module: Section 01 — Getting Started](../01_GettingStarted/README.md)
- 📋 [Master Syllabus (`TEMARIO.md`)](../TEMARIO.md)
- 🌐 [Academic Files Hub (`files/README.md`)](../files/README.md)
- ➡️ [Next Module: Section 03 — Subroutines](../03_Subroutines/README.md)

---
*MiniLux0 — Learning C++ Section 02*
