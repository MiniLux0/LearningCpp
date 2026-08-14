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
| **04** | [`04_ArraysStrings`](04_ArraysStrings/) | CS106B Ch 3,11 / MIT L4 | Static 1D/2D arrays, C-strings (`char[]`), `std::string`, `<cctype>`, string algorithms | 📘 [`theory/`](04_ArraysStrings/theory/) | 💻 [`code/`](04_ArraysStrings/code/) | ✅ |
| **05** | [`05_RecursionAlgorithms`](05_RecursionAlgorithms/) | Stanford CS106B/X | Recursion, Memoization (DP), Big-O Notation, Search & Sorting, Backtracking | 📘 [`theory/`](05_RecursionAlgorithms/theory/) | 💻 [`code/`](05_RecursionAlgorithms/code/) | ✅ |
| **06** | [`06_Pointers`](06_Pointers/) | MIT L5 / CS106L L3,11 | Pointers, pointer arithmetic, references, Const-Correctness, callbacks | 📘 [`theory/`](06_Pointers/theory/) | 💻 [`code/`](06_Pointers/code/) | ⬜ |
| **07** | [`07_Classes`](07_Classes/) | MIT L6 / CS106L L2,10,12 | Structs vs Classes, encapsulation, constructors, Operator Overloading | 📘 [`theory/`](07_Classes/theory/) | 💻 [`code/`](07_Classes/code/) | ⬜ |
| **08** | [`08_OOP`](08_OOP/) | MIT L7 / CS106L L10 | Inheritance, dynamic dispatch, virtual functions, abstract classes | 📘 [`theory/`](08_OOP/theory/) | 💻 [`code/`](08_OOP/code/) | ⬜ |
| **09** | [`09_MemoryManagement`](09_MemoryManagement/) | MIT L8 / CS106L L13-15 | Stack vs Heap, RAII, Rule of 0/3/5, Move Semantics (`std::move`), Smart Pointers | 📘 [`theory/`](09_MemoryManagement/theory/) | 💻 [`code/`](09_MemoryManagement/code/) | ⬜ |
| **10** | [`10_DataStructures`](10_DataStructures/) | Stanford / CS106L | Linked Lists, BST Trees, Custom Iterators, HashMaps, Priority Queues | 📘 [`theory/`](10_DataStructures/theory/) | 💻 [`code/`](10_DataStructures/code/) | ⬜ |
| **11** | [`11_FileIO`](11_FileIO/) | MIT L10 / CS106L L4 | Stream States (`stringstream`, `ifstream`), Text & Binary File I/O | 📘 [`theory/`](11_FileIO/theory/) | 💻 [`code/`](11_FileIO/code/) | ⬜ |
| **12** | [`12_AdvancedCPP`](12_AdvancedCPP/) | MIT L9-10 / CS106L L5-9 | Templates, STL Containers & Iterators, Lambdas, Exceptions, Huffman Compression | 📘 [`theory/`](12_AdvancedCPP/theory/) | 💻 [`code/`](12_AdvancedCPP/code/) | ⬜ |

---

## 📘 Detailed Syllabus by Module

---

### 🔹 Section 01 — Getting Started: C++ Fundamentals for Beginners (L01–L05) · MIT L1 / CS106L L1 ✅
- **L01**: Hello World & C++ Program Anatomy (`#include <iostream>`, `int main()`, `cout`, and `return 0`).
- **L02**: Namespaces & `using namespace std;` (Understanding the `std::` scope, naming collisions, and best practices).
- **L03**: Comments, Newlines & Code Formatting (Single-line `//` and multi-line `/* */` comments, `\n` vs `endl`, tab `\t`, quotes `\"`).
- **L04**: Interactive User Input (`cin` for reading user keyboard input, combining `cin` and `cout`).
- **L05**: Mini-Project: Interactive Profile Generator (A complete beginner project combining user input, formatting, and namespaces).

---

### 🔹 Section 02 — Basic Syntax (L06–L22) · MIT L2 / CS106L L2–L3 ✅
- **L06–L12**: Variables, primitive types (`int`, `double`, `float`, `char`, `bool`), `sizeof`, binary representation, overflow, numeric casting.
- **L13–L17**: Conditionals (`if`, `else`, `else if`), relational and logical operators, safe float comparison with epsilon.
- **L18–L22**: Loops (`while`, `do-while`, `for`), nested loops, `break`, `continue`, `switch-case`, Uniform Initialization `{}` (CS106L).

---

### 🔹 Section 03 — Subroutines (L23–L26) · MIT L3 / CS106L L3 ✅
- **L23**: Anatomy of Functions (Return types, parameters, `void`, `return`).
- **L24**: Return Values & Data Flow (Non-void return types, `return` statement, early return).
- **L25**: Parameters & References (Pass by value vs pass by reference `&`, `const &` efficiency).
- **L26**: Headers & Prototypes (Function prototypes, `.h` / `.cpp` separation, `#pragma once` include guards).

---

### 🔹 Section 04 — Arrays and Strings (L27–L30D) · CS106B Ch 3 & 11 / MIT L4 ✅
- **L27**: Array Basics (Contiguous memory, initialization, `for` loop traversal, bounds checking).
- **L28**: Arrays as Function Parameters (Pointer decay `int*`, passing size, read-only `const int arr[]`).
- **L29**: Multidimensional Arrays (2D matrix, Row-Major Order storage, flat index formula $(i \times C) + j$).
- **L30A**: Traditional C-Strings (`char[]` terminated with `'\0'`, `<cstring>` functions).
- **L30B**: Modern `std::string` (`<string>` initialization forms, methods `substr`, `find`, `replace`, `.at(i)` vs `[]`, `const string&`).
- **L30C**: `<cctype>` Character Inspection & Transformation (`isalpha`, `isdigit`, `isspace`, `tolower`, `toupper`, `static_cast<unsigned char>`).
- **L30D**: String Processing & Applications (Palindrome complexity $O(N)$ vs $O(N^2)$, Pig Latin, Caesar Cipher, Stanford `strlib.h`).

---

### 🔹 Section 05 — Recursion & Algorithms (L31–L39) · Stanford CS106B / CS106X ✅
- **L31**: Thinking Recursively (Base case, recursive step, call stack, mutual recursion, induction).
- **L32**: Classic Recursive Problems (Factorial, Fibonacci, Towers of Hanoi).
- **L33**: Memoization & Top-Down Dynamic Programming (Eliminating $O(2^N)$ redundancy, lookup caching with `vector` and `unordered_map`, Grid Traveler).
- **L34**: Algorithmic Complexity & Big-O Notation (Time and space complexity: $O(1), O(\log N), O(N), O(N \log N), O(N^2)$).
- **L35**: Linear & Binary Search (Linear search on unsorted arrays vs binary search on sorted arrays, safe midpoint calculation).
- **L36**: Quadratic Sorting Algorithms (Bubble Sort, Selection Sort, Insertion Sort — analysis & stability).
- **L37**: Divide & Conquer Sorting (Merge Sort — $O(N \log N)$ recursion & subarray merging).
- **L38**: Fast Sorting (Quick Sort — pivot selection, Hoare & Lomuto partitioning, randomized pivots).
- **L39**: Recursive Backtracking (Choose-Explore-Unchoose pattern, Mazes, Nim Game, subset generation).

---

### 🔹 Section 06 — Pointers & Advanced Memory (L40–L47) · MIT L5 / CS106L L3, L11 ⬜
- **L40**: Pointer Fundamentals (Address-of operator `&`, dereference operator `*`, primitive pointers).
- **L41**: Pointer Arithmetic (Type-dependent step size, `ptr++`, offset notation `*(arr + i)` vs `arr[i]`).
- **L42**: Pointers & Arrays (Equivalence between array name and constant pointer).
- **L43**: References vs Pointers (Key differences: alias vs address, reassignment, nullability).
- **L44**: Const-Correctness (`const int* p`, `int* const p`, `const int* const p`, CS106L Const Rules).
- **L45**: Double Pointers (`int**`) & Dynamic 2D Arrays (Dynamic matrices on the heap).
- **L46**: Function Pointers & Callbacks (`int (*funcPtr)(int, int)`, generic pointers `void*`).
- **L47**: Dangerous Pointers (Null pointers `nullptr`, dangling pointers, uninitialized pointers, use-after-free).

---

### 🔹 Section 07 — Classes & Encapsulation (L48–L53) · MIT L6 / CS106L L2, L10, L12 ⬜
- **L48**: Structs in C/C++ (C `struct` vs C++ `struct`, struct arrays, dot operator access).
- **L49**: Introduction to Classes (`class` vs `struct`, access modifiers `public`, `private`, `protected`).
- **L50**: Constructors & Destructors (Default, parameterized, overloading, destructor `~Class()`).
- **L51**: Encapsulation & Invariants (Getters and Setters, internal state protection).
- **L52**: Member Initializer Lists (`Class() : member(val) {}`, initializing `const` members and references).
- **L53**: Const Methods & Operator Overloading (`const` methods, `operator+`, `operator<<`, `operator==`, `operator[]`).

---

### 🔹 Section 08 — Object-Oriented Programming (L54–L59) · MIT L7 / CS106L L10 ⬜
- **L54**: Inheritance Concepts (Base class vs derived class, syntax `class Derived : public Base`).
- **L55**: Constructor/Destructor Chains in Inheritance (Invocation order in inheritance hierarchies).
- **L56**: Method Overriding & Redefinition (Redefining base methods in derived classes).
- **L57**: Polymorphism & Virtual Functions (Dynamic dispatch, `virtual` keyword, virtual table `vtable`).
- **L58**: Abstract Classes & Pure Virtual Functions (`= 0` functions, interface classes).
- **L59**: Virtual Destructors (Why destructors MUST be `virtual` in polymorphic hierarchies).

---

### 🔹 Section 09 — Dynamic Memory & Modern Resource Management (L60–L64) · MIT L8 / CS106L L13–L15 ⬜
- **L60**: Stack vs Heap Allocation (Lifetime and performance tradeoffs).
- **L61**: Dynamic Operators (`new`, `delete`, `new[]`, `delete[]`, double-free prevention).
- **L62**: Special Member Functions & The Rule of 0 / 3 / 5 (Copy Constructor, Copy Assignment, Move Constructor, Move Assignment).
- **L63**: Move Semantics & Rvalue References (`std::move`, `T&&`, efficient resource transfers).
- **L64**: RAII & Smart Pointers (Resource Acquisition Is Initialization, `std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`).

---

### 🔹 Section 10 — Data Structures (L65–L69) · Stanford CS106B / CS106X / CS106L ⬜
- **L65**: Linked Lists I — Nodes & Dynamic Allocation (`Node` definition with `struct`, heap allocation).
- **L66**: Linked Lists II & Custom Iterators (Insertion/deletion, creating custom iterators with `begin()` and `end()`).
- **L67**: Doubly Linked Lists & Template Linked Lists (Doubly linked lists, templated container nodes).
- **L68**: Binary Search Trees (BST) & Traversals (Search property $L < N < R$, recursive traversals).
- **L69**: Hash Tables & HashMap Implementation (Bucket hashing, collision resolution, CS106L HashMap project).

---

### 🔹 Section 11 — File I/O & Streams (L70–L73) · MIT L10 / CS106L L4 ⬜
- **L70**: Stream Abstractions & Stringstreams (`std::stringstream`, parsing strings, `std::ifstream`, `std::ofstream`).
- **L71**: Stream State & Formatting (File check `is_open()`, state flags `fail()`, `eof()`, `getline()`).
- **L72**: Binary File I/O (`ios::binary` mode, `.write()` and `.read()` methods, saving/loading `struct` records directly).
- **L73**: Random File Access (File position pointers `seekg` (get), `seekp` (put), `tellg`, `tellp`, record offset edits).

---

### 🔹 Section 12 — Advanced C++ & Standard Template Library (L74–L75) · MIT L9–10 / CS106L L5–L9 / Stanford X ⬜
- **L74**: Function & Class Templates (`template <typename T>`, generic containers and algorithms).
- **L75**: STL Containers, Iterators & Lambdas (`std::vector`, `std::map`, `std::set`, STL algorithms, lambda functions `[&]`).

---

*MiniLux0 — Master Syllabus (MIT 6.096 + Stanford CS106B / CS106X / CS106L)*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> � 2026</sub>
</div>