# 🏛️ MIT 6.096: Introduction to C++

> **Massachusetts Institute of Technology — Independent Activities Period (IAP 2011)**  
> 🎓 **Level**: Beginner to Intermediate  
> 👨‍🏫 **Course Director**: Geza Kovacs  
> 📖 **Official Source**: [MIT OpenCourseWare (6.096)](https://ocw.mit.edu/courses/6-096-introduction-to-c-january-iap-2011/)  
> 🎯 **Primary Focus**: Low-level C++ syntax, GCC compilation model, raw pointers, manual heap allocation (`new`/`delete`), Object-Oriented Programming (OOP), and templates.

---

## 1. 🎯 Course Overview & Educational Vision

MIT 6.096 is a fast-paced, intensive C++ course developed at MIT to transition programmers into low-level systems programming. The course builds a strong foundation in hardware-software interaction, memory management, compile-time vs runtime behavior, and clean object-oriented class design.

In this repository, MIT 6.096 serves as the **low-level systems foundation**, teaching students how raw memory operates before introducing high-level data structure abstractions.

---

## 2. 🧠 Key Technical Competencies & Learning Outcomes

1. **Compilation Pipeline**: Understanding source code transformation through the preprocessor (`#include`, `#define`), compiler (`g++`), assembler, and linker.
2. **Pointers & Memory Control**: Mastering address arithmetic (`&`, `*`), `nullptr`, pointer decay, stack frames, and heap allocation.
3. **Manual Memory Management**: Allocating and freeing dynamic memory (`new`, `delete`, `new[]`, `delete[]`) while preventing memory leaks and dangling pointers.
4. **Object-Oriented Design**: Designing encapsulated classes, constructor initializer lists, inheritance hierarchies, virtual method tables (`vtable`), and pure virtual abstract interfaces.
5. **Generic Programming**: Writing type-independent utilities using function and class templates.

---

## 3. 📚 Comprehensive Curriculum & Syllabus

Below is the detailed 10-lecture syllabus extracted directly from the official MIT 6.096 PDF lecture notes ([`files/mit6096/lectures/`](lectures/)):

| # | Lecture PDF | Core Technical Topics Extracted | Repository Module |
|---|-------------|---------------------------------|-------------------|
| **L01** | [`Lecture01_Introduction.pdf`](lectures/Lecture01_Introduction.pdf) | Compiled vs interpreted languages, C++ compilation steps, `main()` signature, primitive types (`int`, `double`, `char`, `bool`), `const` qualifier, operator precedence, `std::` scope. | [`01_GettingStarted`](../../01_GettingStarted/) |
| **L02** | [`Lecture02_FlowOfControl.pdf`](lectures/Lecture02_FlowOfControl.pdf) | Conditionals (`if`, `else`, `switch`), relational & logical operators, loops (`while`, `do-while`, `for`), `break`, `continue`, ternary operator (`? :`). | [`02_BasicSyntax`](../../02_BasicSyntax/) |
| **L03** | [`Lecture03_Functions.pdf`](lectures/Lecture03_Functions.pdf) | Subroutine signature, return types, pass-by-value vs pass-by-reference (`T&`) vs `const` reference (`const T&`), function overloading, default parameters, inline functions, header guard `#ifndef`. | [`03_Subroutines`](../../03_Subroutines/) |
| **L04** | [`Lecture04_ArraysAndStrings.pdf`](lectures/Lecture04_ArraysAndStrings.pdf) | Fixed 1D/2D static arrays, array decay to pointer, C-strings (`char[]` terminated with `'\0'`), `<cstring>` (`strlen`, `strcpy`, `strcmp`), introduction to `std::string`. | [`04_ArraysStrings`](../../04_ArraysStrings/) |
| **L05** | [`Lecture05_Pointers.pdf`](lectures/Lecture05_Pointers.pdf) | Memory addresses, `&` and `*` operators, pointer arithmetic (`ptr + i`), `const int*` vs `int* const`, references vs pointers, double pointers (`int**`). | [`06_Pointers`](../../06_Pointers/) |
| **L06** | [`Lecture06_Classes.pdf`](lectures/Lecture06_Classes.pdf) | Structs vs classes, access specifiers (`public`, `private`), constructors, destructors (`~Class`), member initializer lists (`Class() : val(0) {}`), `this` pointer. | [`07_Classes`](../../07_Classes/) |
| **L07** | [`Lecture07_OOP.pdf`](lectures/Lecture07_OOP.pdf) | Inheritance (`class Derived : public Base`), access modes (`protected`), constructor order, method overriding, `virtual` functions, `vtable`, pure virtual (`= 0`), abstract classes, virtual destructors. | [`08_OOP`](../../08_OOP/) |
| **L08** | [`Lecture08_MemoryManagement.pdf`](lectures/Lecture08_MemoryManagement.pdf) | Stack vs Heap, `new`/`delete` and `new[]`/`delete[]`, dynamic array resizing (`PointArray`), memory leaks, dangling pointers, double-free bugs. | [`09_MemoryManagement`](../../09_MemoryManagement/) |
| **L09** | [`Lecture09_AdvancedTopicsI.pdf`](lectures/Lecture09_AdvancedTopicsI.pdf) | Generic programming, function templates (`template <typename T>`), class templates, template deduction, preprocessor macros vs inline templates. | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **L10** | [`Lecture10_AdvancedTopicsII.pdf`](lectures/Lecture10_AdvancedTopicsII.pdf) | Standard streams (`cin`, `cout`), file I/O (`ifstream`, `ofstream`), `stringstream`, stream flags (`good`, `fail`, `eof`), exception handling (`try`/`catch`/`throw`), basic STL. | [`11_FileIO`](../../11_FileIO/) / [`12_AdvancedCPP`](../../12_AdvancedCPP/) |

---

## 4. 💻 Assignments & Practical Projects Catalog

| # | Assignment PDF | Solution PDF | Key Practical Exercises & Applied Code |
|---|----------------|--------------|----------------------------------------|
| **Assignment 1** | [`Assignment01.pdf`](assignments/Assignment01.pdf) | [`Solution01.pdf`](solutions/Solution01.pdf) | Scope debugging, prime generation with trial division, Leibniz Pi approximation, control flow edge cases. |
| **Assignment 2** | [`Assignment02.pdf`](assignments/Assignment02.pdf) | [`Solution02.pdf`](solutions/Solution02.pdf) | Pass-by-reference array modification, matrix transpositions, C-string reversal using pointer arithmetic. |
| **Assignment 3** | [`Assignment03.pdf`](assignments/Assignment03.pdf) | [`Solution03.pdf`](solutions/Solution03.pdf) | Designing `Point` geometry class, implementing dynamic container `PointArray` with automatic buffer reallocation, deep copy vs shallow copy. |
| **Assignment 4** | [`Assignment04.pdf`](assignments/Assignment04.pdf) | [`Solution04.pdf`](solutions/Solution04.pdf) | Polymorphic banking system (`Account`, `CheckingAccount`, `SavingsAccount`), virtual interest calculation, generic template swap/min functions. |
| **Final Project** | [`FinalProject.pdf`](project/FinalProject.pdf) | N/A | Standalone capstone C++ project combining OOP, dynamic memory, file I/O, and templates. |

---

## 5. 👥 Discussion Sections & Practice Exercises

The MIT 6.096 curriculum includes integrated lab problem sets focusing on:
- Hands-on pointer manipulation and memory debugging.
- Class encapsulation and invariant checking.
- Refactoring procedural code into clean polymorphic C++ class structures.

---

## 6. 🗺️ Repository Alignment & Module Mapping

| Repository Module | MIT 6.096 Lectures & Assignments Alignment |
|-------------------|--------------------------------------------|
| [`01_GettingStarted`](../../01_GettingStarted/) | Lecture 1 (Hello World, Compilation, Types) |
| [`02_BasicSyntax`](../../02_BasicSyntax/) | Lecture 2 (Flow of Control, Loops, Switch) & Assignment 1 |
| [`03_Subroutines`](../../03_Subroutines/) | Lecture 3 (Functions, Pass-by-reference) & Assignment 2 |
| [`04_ArraysStrings`](../../04_ArraysStrings/) | Lecture 4 (1D/2D Arrays, C-Strings) & Assignment 2 |
| [`06_Pointers`](../../06_Pointers/) | Lecture 5 (Pointers, Address Arithmetic, References) |
| [`07_Classes`](../../07_Classes/) | Lecture 6 (Classes, Encapsulation, Constructors) & Assignment 3 |
| [`08_OOP`](../../08_OOP/) | Lecture 7 (Inheritance, Virtual Functions, Polymorphism) & Assignment 4 |
| [`09_MemoryManagement`](../../09_MemoryManagement/) | Lecture 8 (Stack vs Heap, `new`/`delete`, Dynamic Arrays) & Assignment 3 |
| [`11_FileIO`](../../11_FileIO/) | Lecture 10 (File Streams, `stringstream`, Exceptions) |
| [`12_AdvancedCPP`](../../12_AdvancedCPP/) | Lecture 9 (Templates) & Final Project |

---

## 7. 🔗 Navigation & Quick Links

- 🌐 [Master Academic Guide](../Master_Academic_Guide.md)
- 🌲 [Stanford CS106B Syllabus](../cs106b/README.md)
- ⚡ [Stanford CS106X Syllabus](../cs106x/README.md)
- ⚙️ [Stanford CS106L Syllabus](../cs106l/README.md)
- 📋 [Master Repository Syllabus (`TEMARIO.md`)](../../TEMARIO.md)

---
*MiniLux0 — MIT 6.096 Syllabus Documentation*
