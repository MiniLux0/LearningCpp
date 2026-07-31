<div align="center">

# 🚀 Section 02: Basic Syntax — Variables, Types, Control Flow & Loops

> **Lessons**: L06 – L22  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 02) / Stanford CS106L (Lectures 02 & 03)  
> 📖 **Theory Directory**: 📂 [**`02_BasicSyntax/theory/`**](theory/)  
> 🎯 **Primary Focus**: Primitive data types, memory representations, floating-point comparison, Uniform Initialization `{}`, conditional branching, and loop control structures.

---

### 🧭 Module Navigation Hub

[![Root README](https://img.shields.io/badge/🏠_Root-README-00599C?style=for-the-badge)](../README.md)
[![Master Syllabus](https://img.shields.io/badge/📜_Master-TEMARIO-F16822?style=for-the-badge)](../TEMARIO.md)
[![Academic Guide](https://img.shields.io/badge/🌐_Academic-Guide-007ACC?style=for-the-badge)](../files/Master_Academic_Guide.md)
[![Resources](https://img.shields.io/badge/📚_Resources-Catalog-2ea44f?style=for-the-badge)](../RESOURCES.md)

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
| **L07** | **Strings Intro** | 📘 [`theory/L07_Strings.md`](theory/L07_Strings.md) | 💻 [`code/L07_Strings.cpp`](code/L07_Strings.cpp) | Basic `std::string` concatenation and output. | ✅ |
| **L08** | **User Input** | 📘 [`theory/L08_UserInput.md`](theory/L08_UserInput.md) | 💻 [`code/L08_UserInput.cpp`](code/L08_UserInput.cpp) | Reading typed inputs, prompt string chaining. | ✅ |
| **L09** | **Binary Numbers** | 📘 [`theory/L09_BinaryNumbers.md`](theory/L09_BinaryNumbers.md) | 💻 [`code/L09_BinaryNumbers.cpp`](code/L09_BinaryNumbers.cpp) | Bit representations, 2's complement, binary layout. | ✅ |
| **L10** | **Integer Types** | 📘 [`theory/L10_IntegerTypes.md`](theory/L10_IntegerTypes.md) | 💻 [`code/L10_IntegerTypes.cpp`](code/L10_IntegerTypes.cpp) | `short`, `int`, `long`, `long long`, `unsigned`, `sizeof()`, overflow. | ✅ |
| **L11** | **Floating-Point** | 📘 [`theory/L11_FloatingPointTypes.md`](theory/L11_FloatingPointTypes.md) | 💻 [`code/L11_FloatingPointTypes.cpp`](code/L11_FloatingPointTypes.cpp) | `float`, `double`, scientific notation, IEEE 754 precision limit. | ✅ |
| **L12** | **Char and Bool** | 📘 [`theory/L12_CharAndBool.md`](theory/L12_CharAndBool.md) | 💻 [`code/L12_CharAndBool.cpp`](code/L12_CharAndBool.cpp) | ASCII character encoding, `bool` truth values, `std::boolalpha`. | ✅ |
| **L13** | **If Statements** | 📘 [`theory/L13_If.md`](theory/L13_If.md) | 💻 [`code/L13_If.cpp`](code/L13_If.cpp) | Basic conditional evaluation, boolean expressions. | ✅ |
| **L14** | **If-Else** | 📘 [`theory/L14_IfElse.md`](theory/L14_IfElse.md) | 💻 [`code/L14_IfElse.cpp`](code/L14_IfElse.cpp) | Binary decision branching, alternative execution paths. | ✅ |
| **L15** | **If-Else-If** | 📘 [`theory/L15_IfElseIfElse.md`](theory/L15_IfElseIfElse.md) | 💻 [`code/L15_IfElseIfElse.cpp`](code/L15_IfElseIfElse.cpp) | Multi-way conditional chains, default fallthrough. | ✅ |
| **L16** | **Comparing Floats** | 📘 [`theory/L16_ComparingFloats.md`](theory/L16_ComparingFloats.md) | 💻 [`code/L16_ComparingFloats.cpp`](code/L16_ComparingFloats.cpp) | Floating-point rounding errors, safe comparison using epsilon $\epsilon$. | ✅ |
| **L17** | **Complex Conditions** | 📘 [`theory/L17_Conditions.md`](theory/L17_Conditions.md) | 💻 [`code/L17_Conditions.cpp`](code/L17_Conditions.cpp) | Logical AND `&&`, OR `||`, NOT `!`, short-circuit evaluation. | ✅ |
| **L18** | **While Loops** | 📘 [`theory/L18_WhileLoops.md`](theory/L18_WhileLoops.md) | 💻 [`code/L18_WhileLoops.cpp`](code/L18_WhileLoops.cpp) | Pre-test condition loops, loop counters. | ✅ |
| **L19** | **Do-While Loops** | 📘 [`theory/L19_DoWhileLoops.md`](theory/L19_DoWhileLoops.md) | 💻 [`code/L19_DoWhileLoops.cpp`](code/L19_DoWhileLoops.cpp) | Post-test loops guaranteed to run at least once. | ✅ |
| **L20** | **For Loops** | 📘 [`theory/L20_ForLoops.md`](theory/L20_ForLoops.md) | 💻 [`code/L20_ForLoops.cpp`](code/L20_ForLoops.cpp) | Init, condition, increment counter-controlled loop anatomy. | ✅ |
| **L21** | **Break & Continue** | 📘 [`theory/L21_BreakAndContinue.md`](theory/L21_BreakAndContinue.md) | 💻 [`code/L21_BreakAndContinue.cpp`](code/L21_BreakAndContinue.cpp) | Early loop exit (`break`) and iteration skipping (`continue`). | ✅ |
| **L22** | **Switch Statements** | 📘 [`theory/L22_Switch.md`](theory/L22_Switch.md) | 💻 [`code/L22_Switch.cpp`](code/L22_Switch.cpp) | Constant jump-table evaluation, `case` labels, `default`. | ✅ |

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L06–L12** | 📄 [`MIT 6.096 Lecture 01-02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) \| [`CS106L Lecture 03`](../files/cs106l/lectures/WL2-Structures.pdf) | Primitive data types, integer bit widths, 2's complement binary layout, float IEEE 754 precision, Uniform Initialization `{}`. |
| **L13–L17** | 📄 [`MIT 6.096 Lecture 02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) | Relational operators, logical short-circuit evaluation (`&&`, `||`), safe floating-point comparison with epsilon. |
| **L18–L22** | 📄 [`MIT 6.096 Lecture 02`](../files/mit6096/lectures/Lecture02_FlowOfControl.pdf) | Pre-test vs post-test loops, `for` loop variable scope, `break`, `continue`, `switch-case` dispatch. |

---

## 🛠️ How to Compile & Run

```bash
# Navigate to the code directory
cd 02_BasicSyntax/code

# Compile all lessons using Makefile
make

# Run executables (Windows PowerShell / CMD)
.\L06_Variables.exe
.\L16_ComparingFloats.exe
.\L22_Switch.exe
```

---

<div align="center">

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| [**⬅️ Section 01: Getting Started**](../01_GettingStarted/README.md) | **Section 02: Basic Syntax** | [**Section 03: Subroutines ➡️**](../03_Subroutines/README.md) |

</div>

---
*MiniLux0 — Learning C++ Section 02*
