<div align="center">

# 🚀 Learning C++ & Computer Science

**A meticulously structured, 75-lesson journey through C++ — from Hello World to Advanced STL.**  
Unifying the rigorous curricula of *MIT 6.096*, *Stanford CS106B*, *Stanford CS106X*, and *Stanford CS106L*.

[![C++17](https://img.shields.io/badge/C%2B%2B-17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)](https://en.cppreference.com/w/cpp/17)
[![Compiler](https://img.shields.io/badge/GCC-15.2.0-F16822?style=for-the-badge&logo=gnu&logoColor=white)](https://gcc.gnu.org/)
[![Platform](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/brechtsanders/winlibs_mingw)
[![Progress](https://img.shields.io/badge/Progress-Modules_01–05_✓-4caf50?style=for-the-badge)](#-modules-map--progress)

</div>

---

## 🚦 New Here? Start Here

| 👋 If you are… | 📍 Go to | Why |
|:---|:---|:---|
| Seeing this repo for the **first time** | 📜 [`SYLLABUS.md`](SYLLABUS.md) | Full 75-lesson roadmap — understand the learning path first |
| Ready to **write your first line of C++** | 🚀 [`01_GettingStarted/`](01_GettingStarted/README.md) | Lesson 1 — Hello World, GCC compilation, `cout` |
| Need to **compile and run** a lesson | ⚙️ [`docs/COMPILATION_GUIDE.md`](docs/COMPILATION_GUIDE.md) | Step-by-step GCC & Makefile tutorial for beginners |
| Looking for **theory notes** for a specific lesson | 📖 `XX_ModuleName/theory/LXX_*.md` | Every module has a `theory/` folder with detailed notes |
| Looking for **MIT / Stanford lecture PDFs** | 🌐 [`files/Master_Academic_Guide.md`](files/Master_Academic_Guide.md) | Academic materials archive: lectures, assignments, textbooks |

> **`RESOURCES.md`** is a reference catalog for academic sources — useful as a bookmark, but **not required reading** to follow the course.

---

## 📖 About This Repository

This is a personal C++ mastery project built around four top-tier university curricula, merged into a single coherent path:

| Course | Institution | Focus Area |
|--------|-------------|----------------|
| **MIT 6.096** | MIT OpenCourseWare | C++ syntax, compilation pipeline, pointers, classes, OOP, dynamic memory |
| **CS106B** | Stanford | Recursion, Big-O, ADTs, sorting algorithms, linked lists, BST trees |
| **CS106X** | Stanford (Honors) | Accelerated pace, backtracking, Huffman compression, graph algorithms |
| **CS106L** | Stanford | Modern C++ (C++11/17): iterators, lambdas, RAII, move semantics, smart pointers |

### 🧠 Pedagogical Philosophy & Standards
1. **Strict Progressive Disclosure:** The curriculum is strictly progressive. To force mastery of memory fundamentals, **no dynamic STL containers (`std::vector`, `std::array`) or smart pointers are used before Module 06.** Early modules rely exclusively on C-style static arrays and manual logic.
2. **Standardized Structure:** Every module follows the exact same internal directory structure:
   - `theory/` — Markdown notes with custom, programmatic `manim` animations and SVGs.
   - `code/` — Runnable C++ implementations of the theory.
   - `exercise/` — Practice problems, test cases, and solutions.
   - `summary/` — Cheat-sheets for quick revision.
3. **Automated Builds:** Every `code/` and `exercise/` folder features a plug-and-play `Makefile`.

---

## 📊 Modules Map & Progress

| # | Module | Lessons | Academic Source | Key Topics | Status |
|:-:|--------|:-------:|-----------------|------------|:------:|
| **01** | [**Getting Started**](01_GettingStarted/README.md) | L01–L05 | MIT L1 · CS106L L1 | Program anatomy, GCC pipeline, `cout` / `cin`, namespaces | ✅ |
| **02** | [**Basic Syntax**](02_BasicSyntax/README.md) | L06–L22 | MIT L2 · CS106L L2–3 | Primitive types, uniform init `{}`, IEEE float epsilon, loops | ✅ |
| **03** | [**Subroutines**](03_Subroutines/README.md) | L23–L26 | MIT L3 · CS106L L3–4 | Functions, pass-by-ref (`&`, `const &`), `.h` header files | ✅ |
| **04** | [**Arrays & Strings**](04_ArraysStrings/README.md) | L27–L30D | CS106B Ch 3,11 · MIT L4 | 1D/2D arrays, array decay, C-strings, `std::string`, `<cctype>`, string algorithms | ✅ |
| **05** | [**Recursion & Algorithms**](05_RecursionAlgorithms/README.md) | L31–L39 | CS106B · CS106X | Recursion, Memoization (DP), Big-O, MergeSort, QuickSort, Backtracking | ✅ |
| **06** | [**Pointers**](06_Pointers/) | L40–L47 | MIT L5 · CS106L L3, L11 | Pointers, arithmetic, references, const-correctness, callbacks | ⬜ |
| **07** | [**Classes**](07_Classes/) | L47–L52 | MIT L6 · CS106L L2, L10 | Structs vs classes, encapsulation, operator overloading | ⬜ |
| **08** | [**OOP & Polymorphism**](08_OOP/) | L53–L58 | MIT L7 · CS106L L10 | Inheritance, `virtual` functions, dynamic dispatch, abstract classes | ⬜ |
| **09** | [**Memory Management**](09_MemoryManagement/) | L59–L63 | MIT L8 · CS106L L13–15 | Stack vs heap, `new`/`delete`, RAII, Rule of 0/3/5, move semantics | ⬜ |
| **10** | [**Data Structures**](10_DataStructures/) | L64–L68 | CS106B · CS106L | Linked lists, BST, custom iterators, hash maps, priority queues | ⬜ |
| **11** | [**File I/O & Streams**](11_FileIO/) | L69–L72 | MIT L10 · CS106L L4 | Stream states, `ifstream` / `ofstream`, text & binary file I/O | ⬜ |
| **12** | [**Advanced C++ & STL**](12_AdvancedCPP/) | L73–L75 | MIT L9–10 · CS106L L5–9 | Templates, STL containers, lambdas, Huffman, WikiRacer | ⬜ |

---

## 🛠️ How to Build & Run Code

Every `code/` and `exercise/` subdirectory contains an automated `Makefile`. No long `g++` commands needed.

```bash
# 1. Navigate to any module's code directory
cd 01_GettingStarted/code

# 2. Compile all lessons → output goes to build/
make

# 3. Compile + run a specific lesson immediately
make run-L01_HelloWorld

# 4. Compile with memory sanitizers (detects leaks & undefined behavior)
make asan

# 5. Delete all compiled output
make clean
```

> 💡 **New to compilation?** → ⚙️ [`docs/COMPILATION_GUIDE.md`](docs/COMPILATION_GUIDE.md) — beginner-friendly GCC walkthrough.  
> 💡 **Want to understand the flags?** → 🛠️ [`docs/MAKEFILE_GUIDE.md`](docs/MAKEFILE_GUIDE.md) — deep-dive on `-Wall`, `-Wextra`, `-fsanitize`, and more.

---

## 📚 Reference Links

| | Resource | Description |
|---|----------|-------------|
| 🌐 | [**Master Academic Guide**](files/Master_Academic_Guide.md) | Full curricula comparison & PDF index for all 4 courses |
| 📄 | [**Academic Materials (`files/`)**](files/) | Local lecture slides, problem sets, assignments & starter code |
| ⚙️ | [**Compilation Guide**](docs/COMPILATION_GUIDE.md) | Beginner step-by-step GCC & Makefile tutorial |
| 🛠️ | [**Makefile Guide**](docs/MAKEFILE_GUIDE.md) | Compiler flags, sanitizers & build system deep-dive |
| 📖 | [cppreference.com](https://cppreference.com/) | Official C++ language & standard library reference |
| 📘 | [LearnCpp.com](https://www.learncpp.com/) | Comprehensive free C++ tutorial |

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>