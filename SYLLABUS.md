# Master Syllabus — Learning C++ (MIT 6.096 + Stanford CS106B / CS106X / CS106L)

<div align="center">

[![🏠 Root README](https://img.shields.io/badge/🏠_Back_to-Root_README-00599C?style=for-the-badge)](README.md)
[![📚 Resources Catalog](https://img.shields.io/badge/📚_Resources-Catalog-2ea44f?style=for-the-badge)](RESOURCES.md)
[![📂 Docs & Build Guides](https://img.shields.io/badge/📂_Docs-Build_Guides-555555?style=for-the-badge)](docs/README.md)

</div>

> **🗺️ This is your course roadmap.** Read it to understand the full learning path (L01–L75) and which lesson comes next.
> Follow the modules **in numerical order** — each section builds directly on the previous one.
> You do **not** need to read `RESOURCES.md` to follow this syllabus.

> **Unified Study Plan for Modern C++, Algorithms, Data Structures, and Software Engineering**
> Designed to master C++ from scratch to advanced level, combining technical syntax rigor, modern standards (C++11/17/20), algorithm analysis, and software design principles.

---


## 🏛️ Academic Sources Quadtrilogy

| Source | Primary Focus | Syllabus & Materials |
|--------|--------------|----------------------|
| **MIT 6.096** | C++ Syntax, Pointers, Classes, OOP, Dynamic Memory (`new`/`delete`), Templates | 📄 [`files/mit6096/README.md`](files/mit6096/README.md) (10 Lectures, 4 Assignments, Solutions, Final Project) |
| **Stanford CS106B** | Recursion, Backtracking, Big-O Notation, ADTs (Stack, Queue, Map, Set), Linked Lists, BST Trees | 📄 [`files/cs106b/README.md`](files/cs106b/README.md) (Textbook *Eric Roberts*, Assignments 0–9, Sections 1–8) |
| **Stanford CS106X** | Accelerated/Honors Version: High-performance challenges, 4-way Priority Queues, Memoization, Boggle, Huffman, Stanford 1-2-3 | 📄 [`files/cs106x/README.md`](files/cs106x/README.md) (34 Handouts, 7 Capstone Assignments) |
| **Stanford CS106L** | Modern Standard C++ (C++11/17/20): Uniform Initialization, Stream States, Custom Iterators, Lambdas, Const-Correctness, Operator Overloading, SMFs, Move Semantics, RAII, Smart Pointers | 📄 [`files/cs106l/README.md`](files/cs106l/README.md) (17 Lecture PDFs, 3 Projects: `HashMap`, `WikiRacer`, `linked-list`) |

---

## 📊 Complete Modules Map (Lessons L01 – L75)

| # | Section | Base Source | Key Content | Theory Notes | Code Lab | Status |
|---|---------|-------------|-------------|:------------:|:--------:|:------:|
| **01** | [`01_GettingStarted`](01_GettingStarted/) | MIT L1 / CS106L L1 | First program, compilation pipeline, tokens, `cout`/`cin` | 📘 [`theory/`](01_GettingStarted/theory/) | 💻 [`code/`](01_GettingStarted/code/) | ✅ |
| **02** | [`02_BasicSyntax`](02_BasicSyntax/) | MIT L2 / CS106L L2-3 | Primitive types, Uniform Initialization `{}` , conditionals, loops | 📘 [`theory/`](02_BasicSyntax/theory/) | 💻 [`code/`](02_BasicSyntax/code/) | ✅ |
| **03** | [`03_Subroutines`](03_Subroutines/) | MIT L3 / CS106L L3 | Functions, pass-by-value/reference (`&`, `const &`), `.h` headers | 📘 [`theory/`](03_Subroutines/theory/) | 💻 [`code/`](03_Subroutines/code/) | ✅ |
| **04** | [`04_ArraysStrings`](04_ArraysStrings/) | MIT L4 / CS106L L4 | Static 1D/2D arrays, C-strings (`<cstring>`), Streams & `std::string` | 📘 [`theory/`](04_ArraysStrings/theory/) | 💻 [`code/`](04_ArraysStrings/code/) | ✅ |
| **05** | [`05_RecursionAlgorithms`](05_RecursionAlgorithms/) | Stanford CS106B/X | Recursion vs. Iteration, Backtracking, Big-O Notation, Search & Sorting | 📘 [`theory/`](05_RecursionAlgorithms/theory/) | 💻 [`code/`](05_RecursionAlgorithms/code/) | ✅ |
| **06** | [`06_Pointers`](06_Pointers/) | MIT L5 / CS106L L3,11 | Pointers, pointer arithmetic, references, Const-Correctness, callbacks | 📘 `theory/` | 💻 `code/` | ⬜ |
| **07** | [`07_Classes`](07_Classes/) | MIT L6 / CS106L L2,10,12 | Structs vs Classes, encapsulation, constructors, Operator Overloading | 📘 `theory/` | 💻 `code/` | ⬜ |
| **08** | [`08_OOP`](08_OOP/) | MIT L7 / CS106L L10 | Inheritance, dynamic dispatch, virtual functions, abstract classes | 📘 `theory/` | 💻 `code/` | ⬜ |
| **09** | [`09_MemoryManagement`](09_MemoryManagement/) | MIT L8 / CS106L L13-15 | Stack vs Heap, RAII, Rule of 0/3/5, Move Semantics (`std::move`), Smart Pointers | 📘 `theory/` | 💻 `code/` | ⬜ |
| **10** | [`10_DataStructures`](10_DataStructures/) | Stanford / CS106L | Linked Lists, BST Trees, Custom Iterators, HashMaps, Priority Queues | 📘 `theory/` | 💻 `code/` | ⬜ |
| **11** | [`11_FileIO`](11_FileIO/) | MIT L10 / CS106L L4 | Stream States (`stringstream`, `ifstream`), Text & Binary File I/O | 📘 `theory/` | 💻 `code/` | ⬜ |
| **12** | [`12_AdvancedCPP`](12_AdvancedCPP/) | MIT L9-10 / CS106L L5-9 | Templates, STL Containers & Iterators, Lambdas, Exceptions, Huffman Compression | 📘 `theory/` | 💻 `code/` | ⬜ |

---

## 📘 Detailed Syllabus by Module

---

### 🔹 Section 01 — Getting Started: C++ Fundamentals for Beginners (L01–L05) · MIT L1 / CS106L L1 ✅
- **L01**: Hello World & C++ Program Anatomy (`#include <iostream>`, `int main()`, `std::cout`, and `return 0`).
- **L02**: Namespaces & `using namespace std;` (Understanding the `std::` scope, naming collisions, and best practices).
- **L03**: Comments, Newlines & Code Formatting (Single-line `//` and multi-line `/* */` comments, `\n` vs `std::endl`, tab `\t`, quotes `\"`).
- **L04**: Interactive User Input (`std::cin` for reading user keyboard input, combining `cin` and `cout`).
- **L05**: Mini-Project: Interactive Profile Generator (A complete beginner project combining user input, formatting, and namespaces).

---

### 🔹 Section 02 — Basic Syntax (L06–L22) · MIT L2 / CS106L L2–L3 ✅
- **L06–L12**: Variables, primitive types (`int`, `double`, `float`, `char`, `bool`), `sizeof`, binary representation, overflow, numeric casting.
- **L13–L17**: Conditionals (`if`, `else`, `else if`), relational and logical operators, safe float comparison with epsilon.
- **L18–L22**: Loops (`while`, `do-while`, `for`), nested loops, `break`, `continue`, `switch-case`, Uniform Initialization `{}` (CS106L).

---

### 🔹 Section 03 — Subroutines (L23–L26) · MIT L3 / CS106L L3 ✅
- **L23**: Anatomy of Functions (Return types, parameters, `void`, `return`).
- **L24**: Pass by Value vs Pass by Reference (`&`, `const &`), signatures and function overloading.
- **L25**: Headers and Prototypes (`.h` / `.cpp` separation, preprocessor directives `#ifndef`).
- **L26**: Function Scope & Lifetime (Local, global, and static variables).

---

### 🔹 Section 04 — Arrays and Strings (L27–L30) · MIT L4 / CS106L L4 ✅
- **L27**: Array Basics (Contiguous memory, initialization, `for` loop traversal).
- **L28**: Arrays as Function Parameters (Decay to pointer, passing dimensions).
- **L29**: Multidimensional Arrays (2D matrix, row/column traversal, nested initialization).
- **L30**: C-Strings vs `std::string` (`char[]` terminated with `'\0'`, `<cstring>` functions, `<cctype>`, stream string manipulation).

---

### 🔹 Section 05 — Recursion & Algorithms (L31–L38) · Stanford CS106B / CS106X ⬜
- **L31**: Thinking Recursively (Base case, recursive step, call stack).
- **L32**: Classic Recursive Problems (Factorial, Fibonacci, Power, String reversal).
- **L33**: Algorithmic Complexity & Big-O Notation (Time and space complexity: $O(1), O(\log n), O(n), O(n^2)$).
- **L34**: Linear & Binary Search (Linear search on unsorted arrays vs binary search on sorted arrays).
- **L35**: Quadratic Sorting Algorithms (Bubble Sort, Selection Sort, Insertion Sort — analysis & implementation).
- **L36**: Divide & Conquer Sorting (Merge Sort — recursion & subarray merging).
- **L37**: Fast Sorting (Quick Sort — pivot selection, `partition` step, Quickselect).
- **L38**: Recursive Backtracking & Memoization (Mazes, N-Queens, Boggle, subsets).

---

### 🔹 Section 06 — Pointers & Advanced Memory (L39–L46) · MIT L5 / CS106L L3, L11 ⬜
- **L39**: Pointer Fundamentals (Address-of operator `&`, dereference operator `*`, primitive pointers).
- **L40**: Pointer Arithmetic (Type-dependent step size, `ptr++`, offset notation `*(arr + i)` vs `arr[i]`).
- **L41**: Pointers & Arrays (Equivalence between array name and constant pointer).
- **L42**: References vs Pointers (Key differences: alias vs address, reassignment, nullability).
- **L43**: Const-Correctness (`const int* p`, `int* const p`, `const int* const p`, CS106L Const Rules).
- **L44**: Double Pointers (`int**`) & Dynamic 2D Arrays (Dynamic matrices on the heap).
- **L45**: Function Pointers & Callbacks (`int (*funcPtr)(int, int)`, generic pointers `void*`).
- **L46**: Dangerous Pointers (Null pointers `nullptr`, dangling pointers, uninitialized pointers, use-after-free).

---

### 🔹 Section 07 — Classes & Encapsulation (L47–L52) · MIT L6 / CS106L L2, L10, L12 ⬜
- **L47**: Structs in C/C++ (C `struct` vs C++ `struct`, struct arrays, dot operator access).
- **L48**: Introduction to Classes (`class` vs `struct`, access modifiers `public`, `private`, `protected`).
- **L49**: Constructors & Destructors (Default, parameterized, overloading, destructor `~Class()`).
- **L50**: Encapsulation & Invariants (Getters and Setters, internal state protection).
- **L51**: Member Initializer Lists (`Class() : member(val) {}`, initializing `const` members and references).
- **L52**: Const Methods & Operator Overloading (`const` methods, `operator+`, `operator<<`, `operator==`, `operator[]`).

---

### 🔹 Section 08 — Object-Oriented Programming (L53–L58) · MIT L7 / CS106L L10 ⬜
- **L53**: Inheritance Concepts (Base class vs derived class, syntax `class Derived : public Base`).
- **L54**: Constructor/Destructor Chains in Inheritance (Invocation order in inheritance hierarchies).
- **L55**: Method Overriding & Redefinition (Redefining base methods in derived classes).
- **L56**: Polymorphism & Virtual Functions (Dynamic dispatch, `virtual` keyword, virtual table `vtable`).
- **L57**: Abstract Classes & Pure Virtual Functions (`= 0` functions, interface classes).
- **L58**: Virtual Destructors (Why destructors MUST be `virtual` in polymorphic hierarchies).

---

### 🔹 Section 09 — Dynamic Memory & Modern Resource Management (L59–L63) · MIT L8 / CS106L L13–L15 ⬜
- **L59**: Stack vs Heap Allocation (Lifetime and performance tradeoffs).
- **L60**: Dynamic Operators (`new`, `delete`, `new[]`, `delete[]`, double-free prevention).
- **L61**: Special Member Functions & The Rule of 0 / 3 / 5 (Copy Constructor, Copy Assignment, Move Constructor, Move Assignment).
- **L62**: Move Semantics & Rvalue References (`std::move`, `T&&`, efficient resource transfers).
- **L63**: RAII & Smart Pointers (Resource Acquisition Is Initialization, `std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`).

---

### 🔹 Section 10 — Data Structures (L64–L68) · Stanford CS106B / CS106X / CS106L ⬜
- **L64**: Linked Lists I — Nodes & Dynamic Allocation (`Node` definition with `struct`, heap allocation).
- **L65**: Linked Lists II & Custom Iterators (Insertion/deletion, creating custom iterators with `begin()` and `end()`).
- **L66**: Doubly Linked Lists & Template Linked Lists (Doubly linked lists, templated container nodes).
- **L67**: Binary Search Trees (BST) & Traversals (Search property $L < N < R$, recursive traversals).
- **L68**: Hash Tables & HashMap Implementation (Bucket hashing, collision resolution, CS106L HashMap project).

---

### 🔹 Section 11 — File I/O & Streams (L69–L72) · MIT L10 / CS106L L4 ⬜
- **L69**: Stream Abstractions & Stringstreams (`std::stringstream`, parsing strings, `std::ifstream`, `std::ofstream`).
- **L70**: Stream State & Formatting (File check `is_open()`, state flags `fail()`, `eof()`, `getline()`).
- **L71**: Binary File I/O (`ios::binary` mode, `.write()` and `.read()` methods, saving/loading `struct` records directly).
- **L72**: Random File Access (File position pointers `seekg` (get), `seekp` (put), `tellg`, `tellp`, record offset edits).

---

### 🔹 Section 12 — Advanced C++ & Standard Template Library (L73–L75) · MIT L9–10 / CS106L L5–L9 / Stanford X ⬜
- **L73**: Function & Class Templates (`template <typename T>`, generic containers and algorithms).
- **L74**: STL Containers, Iterators & Lambdas (`std::vector`, `std::map`, `std::set`, STL algorithms, lambda functions `[&]`).
- **L75**: Advanced Projects & Compression (Huffman compression, WikiRacer project, exceptions `try`/`catch`, `static_cast`).

---

*MiniLux0 — Master Syllabus (MIT 6.096 + Stanford CS106B / CS106X / CS106L)*
