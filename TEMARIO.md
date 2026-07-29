# Master Syllabus — Learning C++ (MIT 6.096 + Stanford CS106B / CS106X)

> **Unified Study Plan for C++, Algorithms, and Data Structures**
> Designed to master C++ from scratch and build solid foundations in Algorithms, Data Structures, and Software Engineering.

---

## 🏛️ Academic Sources Trilogy

| Source | Primary Focus | Materials |
|--------|--------------|-----------|
| **MIT 6.096** | C++ Syntax, Pointers, Classes, OOP, Dynamic Memory (`new`/`delete`), Templates | 10 Lecture PDFs, 4 Assignments, Solutions, Final Project |
| **Stanford CS106B** | Recursion, Backtracking, Big-O Notation, ADTs (Stack, Queue, Map, Set), Linked Lists, BST Trees | Textbook *Programming Abstractions in C++* (Eric Roberts), Slides, Exercises |
| **Stanford CS106X** | Accelerated/Honors Version: High-performance challenges, 4-way Priority Queues, Memoization, Boggle, Huffman, Stanford 1-2-3 | 34 Handouts, 7 Assignments (Life, ADTs, Boggle, PQueue, Huffman, Stanford 123) |

---

## 📊 Complete Modules Map (Lessons L01 – L75)

| # | Section | Base Source | Key Content | Status |
|---|---------|-------------|-------------|:------:|
| **01** | `01_GettingStarted` | MIT L1 | First program, compilation pipeline, tokens, `cout`/`cin` | ✅ |
| **02** | `02_BasicSyntax` | MIT L2 | Primitive types, conditionals (`if`/`switch`), loops (`while`/`for`) | 🔄 |
| **03** | `03_Subroutines` | MIT L3 | Functions, pass-by-value/reference, prototypes, `.h` headers | ✅ |
| **04** | `04_ArraysStrings` | MIT L4 | Static 1D/2D arrays, C-strings (`<cstring>`), `std::string` | 🔄 |
| **05** | `05_RecursionAlgorithms` | Stanford | Recursion vs. Iteration, Backtracking, Big-O Notation ($O(1), O(n), O(n \log n)$), Linear/Binary Search, Sorting (Bubble, Selection, Insertion, Merge, QuickSort) | ⬜ |
| **06** | `06_Pointers` | MIT L5 / Stanford | Pointers, pointer arithmetic, references, `const`, function pointers, callbacks, dynamic 2D matrices (`int**`) | ⬜ |
| **07** | `07_Classes` | MIT L6 | `class` vs `struct`, member fields, constructors/destructors, encapsulation, getters/setters, `this` | ⬜ |
| **08** | `08_OOP` | MIT L7 | Inheritance (`public`/`protected`), overriding, polymorphism, virtual functions (`virtual`), abstract classes (`=0`) | ⬜ |
| **09** | `09_MemoryManagement` | MIT L8 | Stack vs Heap, `new`/`delete`, `new[]`/`delete[]`, memory leaks, RAII, deep copy vs shallow copy, Rule of Three | ⬜ |
| **10** | `10_DataStructures` | Stanford | Structs, Singly/Doubly Linked Lists (`Node* head`), `next`/`prev` pointers, Binary Search Trees (BST), InOrder/PreOrder/PostOrder traversals, Priority Queues, Heaps | ⬜ |
| **11** | `11_FileIO` | MIT L10 / Stanford | File Streams `<fstream>`, text files (`.txt`), binary files (`.bin`), struct records, random access (`seekg`, `seekp`) | ⬜ |
| **12** | `12_AdvancedCPP` | MIT L9-10 / Stanford X | Templates (functions/classes), STL (`std::vector`, `std::map`, `std::set`), Exceptions (`try`/`catch`), Type Casting (`static_cast`), Huffman Compression | ⬜ |

---

## 📘 Detailed Syllabus by Module

---

### 🔹 Section 01 — Getting Started: C++ Fundamentals for Beginners (L01–L05) · MIT L1 ✅
- **L01**: Hello World & C++ Program Anatomy (`#include <iostream>`, `int main()`, `std::cout`, and `return 0`).
- **L02**: Namespaces & `using namespace std;` (Understanding the `std::` scope, naming collisions, and best practices).
- **L03**: Comments, Newlines & Code Formatting (Single-line `//` and multi-line `/* */` comments, `\n` vs `std::endl`, tab `\t`, quotes `\"`).
- **L04**: Interactive User Input (`std::cin` for reading user keyboard input, combining `cin` and `cout`).
- **L05**: Mini-Project: Interactive Profile Generator (A complete beginner project combining user input, formatting, and namespaces).

---

### 🔹 Section 02 — Basic Syntax (L06–L22) · MIT Lecture 2 🔄
- **L06–L12**: Variables, primitive types (`int`, `double`, `float`, `char`, `bool`), `sizeof`, binary representation, overflow, numeric casting.
- **L13–L17**: Conditionals (`if`, `else`, `else if`), relational and logical operators, safe float comparison with epsilon.
- **L18–L22**: Loops (`while`, `do-while`, `for`), nested loops, `break`, `continue`, `switch-case`.

---

### 🔹 Section 03 — Subroutines (L23–L26) · MIT Lecture 3 ✅
- **L23**: Anatomy of Functions (Return types, parameters, `void`, `return`).
- **L24**: Pass by Value vs Pass by Reference (`&`), signatures and function overloading.
- **L25**: Headers and Prototypes (`.h` / `.cpp` separation, preprocessor directives `#ifndef`).
- **L26**: Function Scope & Lifetime (Local, global, and static variables).

---

### 🔹 Section 04 — Arrays and Strings (L27–L30) · MIT Lecture 4 🔄
- **L27**: Array Basics (Contiguous memory, initialization, `for` loop traversal).
- **L28**: Arrays as Function Parameters (Decay to pointer, passing dimensions).
- **L29**: Multidimensional Arrays (2D matrix, row/column traversal, nested initialization).
- **L30**: C-Strings vs `std::string` (`char[]` terminated with `'\0'`, `<cstring>` functions: `strlen`, `strcpy`, `strcat`, `strcmp`, `cin.getline()`).

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

### 🔹 Section 06 — Pointers & Advanced Memory (L39–L46) · MIT Lecture 5 / Stanford ⬜
- **L39**: Pointer Fundamentals (Address-of operator `&`, dereference operator `*`, primitive pointers).
- **L40**: Pointer Arithmetic (Type-dependent step size, `ptr++`, offset notation `*(arr + i)` vs `arr[i]`).
- **L41**: Pointers & Arrays (Equivalence between array name and constant pointer).
- **L42**: References vs Pointers (Key differences: alias vs address, reassignment, nullability).
- **L43**: Const Correctness with Pointers (`const int* p`, `int* const p`, `const int* const p`).
- **L44**: Double Pointers (`int**`) & Dynamic 2D Arrays (Dynamic matrices on the heap).
- **L45**: Function Pointers & Callbacks (`int (*funcPtr)(int, int)`, generic pointers `void*`).
- **L46**: Dangerous Pointers (Null pointers `nullptr`, dangling pointers, uninitialized pointers, use-after-free).

---

### 🔹 Section 07 — Classes & Encapsulation (L47–L52) · MIT Lecture 6 / Stanford ⬜
- **L47**: Structs in C/C++ (C `struct` vs C++ `struct`, struct arrays, dot operator access).
- **L48**: Introduction to Classes (`class` vs `struct`, access modifiers `public`, `private`, `protected`).
- **L49**: Constructors & Destructors (Default, parameterized, overloading, destructor `~Class()`).
- **L50**: Encapsulation & Invariants (Getters and Setters, internal state protection).
- **L51**: Member Initializer Lists (`Class() : member(val) {}`, initializing `const` members and references).
- **L52**: The `this` Pointer & Const Methods (`this->member`, `const` methods that preserve state).

---

### 🔹 Section 08 — Object-Oriented Programming (L53–L58) · MIT Lecture 7 / Stanford ⬜
- **L53**: Inheritance Concepts (Base class vs derived class, syntax `class Derived : public Base`).
- **L54**: Constructor/Destructor Chains in Inheritance (Invocation order in inheritance hierarchies).
- **L55**: Method Overriding & Redefinition (Redefining base methods in derived classes).
- **L56**: Polymorphism & Virtual Functions (Dynamic dispatch, `virtual` keyword, virtual table `vtable`).
- **L57**: Abstract Classes & Pure Virtual Functions (`= 0` functions, interface classes).
- **L58**: Virtual Destructors (Why destructors MUST be `virtual` in polymorphic hierarchies).

---

### 🔹 Section 09 — Dynamic Memory & Resource Management (L59–L63) · MIT Lecture 8 ⬜
- **L59**: Stack vs Heap Allocation (Lifetime and performance tradeoffs).
- **L60**: Dynamic Operators (`new`, `delete`, `new[]`, `delete[]`, double-free prevention).
- **L61**: Memory Leaks & Debugging Tools (Identifying memory leaks).
- **L62**: Deep Copy vs Shallow Copy (Shallow copy pointer issues, implementing Copy Constructors).
- **L63**: The Rule of Three / RAII (Resource Acquisition Is Initialization: Destructor, Copy Constructor, Copy Assignment `operator=`).

---

### 🔹 Section 10 — Data Structures (L64–L68) · Stanford CS106B / CS106X ⬜
- **L64**: Linked Lists I — Nodes & Dynamic Allocation (`Node` definition with `struct`, creating the first node on the heap).
- **L65**: Linked Lists II — Basic Operations (Insertion at front/end, searching, node deletion, freeing entire list).
- **L66**: Doubly Linked Lists (Doubly linked lists with `prev` and `next` pointers).
- **L67**: Binary Trees I — Structure & Traversal (`TreeNode` with `left` and `right`, recursive traversals: InOrder, PreOrder, PostOrder).
- **L68**: Binary Search Trees & Priority Queues (Search property $L < N < R$, BST insertion/deletion, Heaps).

---

### 🔹 Section 11 — File I/O & Persistence (L69–L72) · MIT Lecture 10 / Stanford ⬜
- **L69**: Text File Streams (`#include <fstream>`, `ifstream` for reading, `ofstream` for writing, `ofstream::app`).
- **L70**: Stream State & Formatting (File open check `is_open()`, end-of-file `eof()`, line-by-line reading `getline()`).
- **L71**: Binary File I/O (`ios::binary` mode, `.write()` and `.read()` methods, saving/loading `struct` records directly).
- **L72**: Random File Access (File position pointers `seekg` (get), `seekp` (put), `tellg`, `tellp`, record modification at offset).

---

### 🔹 Section 12 — Advanced C++ Topics & Projects (L73–L75) · MIT L9–10 / Stanford CS106X ⬜
- **L73**: Function & Class Templates (`template <typename T>`, generic functions and classes).
- **L74**: Standard Template Library (STL) (Practical usage of `std::vector`, `std::map`, `std::set`, iterators).
- **L75**: Exceptions, Type Casting & Compression (Huffman compression, `try`/`catch`/`throw`, `static_cast`).

---

*MiniLux0 — Master Syllabus (MIT 6.096 + Stanford CS106B / CS106X)*
