<div align="center">

# 🚀 Learning C++ & Computer Science

*A structured learning journey in C++, Modern C++ Standards, Algorithms, and Data Structures — unifying the curricula of **MIT 6.096**, **Stanford CS106B**, **Stanford CS106X**, and **Stanford CS106L**.*

[![C++17](https://img.shields.io/badge/C%2B%2B-17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)](https://en.cppreference.com/w/cpp/17)
[![Compiler](https://img.shields.io/badge/GCC-15.2.0-F16822?style=for-the-badge&logo=gnu&logoColor=white)](https://gcc.gnu.org/)
[![Platform](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/brechtsanders/winlibs_mingw)
[![Progress](https://img.shields.io/badge/Progress-L30%20%2F%2075-yellow?style=for-the-badge)](#-modules-map--progress)

</div>

---

> ### ⚡ Quick Start & Repository Navigation
> 
> * 📜 **Complete 75-Lesson Syllabus**: [**`SYLLABUS.md`**](SYLLABUS.md) — Step-by-step lesson breakdown (L01 to L75).
> * 🌐 **Academic Guide & PDF Catalog**: [**`files/Master_Academic_Guide.md`**](files/Master_Academic_Guide.md) — MIT & Stanford lecture slides, assignments, and textbooks.
> * 📖 **Theory Notes**: Located inside each module's `theory/` directory (e.g., [`01_GettingStarted/theory/`](01_GettingStarted/theory/)).
> * 💻 **Executable Code Labs**: Located inside each module's `code/` directory with automated `makefile` compilation.

---

## 📊 Modules Map & Progress

| # | Module Name | Lessons | Academic Source | Key Core Topics | Module Hub | Status |
|---|-------------|---------|-----------------|-----------------|:----------:|:------:|
| **01** | **Getting Started** | L01 – L05 | MIT L1 / CS106L L1 | Anatomy, GCC compilation, formatting, `cin` & `cout` | 🚀 [`01_GettingStarted/`](01_GettingStarted/README.md) | ✅ |
| **02** | **Basic Syntax** | L06 – L22 | MIT L2 / CS106L L2–3 | Types, Uniform Init `{}`, IEEE float $\epsilon$, loops | 🚀 [`02_BasicSyntax/`](02_BasicSyntax/README.md) | ✅ |
| **03** | **Subroutines** | L23 – L26 | MIT L3 / CS106L L3–4 | Functions, pass-by-ref (`&`, `const &`), header files | 🚀 [`03_Subroutines/`](03_Subroutines/README.md) | ✅ |
| **04** | **Arrays & Strings** | L27 – L30 | MIT L4 / CS106L L4–5 | 1D/2D arrays, array decay, C-strings, `stringstream` | 🚀 [`04_ArraysStrings/`](04_ArraysStrings/README.md) | ✅ |
| **05** | **Recursion & Algorithms** | L31 – L38 | CS106B / CS106X | Recursion, Big-O, MergeSort, QuickSort, Backtracking | 🚀 [`05_RecursionAlgorithms/`](05_RecursionAlgorithms/README.md) | ⬜ |
| **06** | **Pointers** | L39 – L46 | MIT L5 / CS106L L3,11 | Pointers, arithmetic, references, Const-Correctness | 🚀 [`06_Pointers/`](06_Pointers/) | ⬜ |
| **07** | **Classes** | L47 – L52 | MIT L6 / CS106L L2,10 | Structs vs Classes, encapsulation, Operator Overloading | 🚀 [`07_Classes/`](07_Classes/) | ⬜ |
| **08** | **OOP & Polymorphism** | L53 – L58 | MIT L7 / CS106L L10 | Inheritance, dynamic dispatch, `virtual`, destructors | 🚀 [`08_OOP/`](08_OOP/) | ⬜ |
| **09** | **Memory Management** | L59 – L63 | MIT L8 / CS106L L13-15 | Stack vs Heap, `new`/`delete`, RAII, Rule of 0/3/5, Move | 🚀 [`09_MemoryManagement/`](09_MemoryManagement/) | ⬜ |
| **10** | **Data Structures** | L64 – L68 | CS106B / CS106L | Linked Lists, BST Trees, Custom Iterators, HashMaps | 🚀 [`10_DataStructures/`](10_DataStructures/) | ⬜ |
| **11** | **File I/O & Streams** | L69 – L72 | MIT L10 / CS106L L4 | Stream states, Text (`.txt`) and Binary (`.bin`) Files | 🚀 [`11_FileIO/`](11_FileIO/) | ⬜ |
| **12** | **Advanced C++ & STL** | L73 – L75 | MIT L9-10 / CS106L L5-9 | Templates, STL Containers, Lambdas, Huffman & WikiRacer | 🚀 [`12_AdvancedCPP/`](12_AdvancedCPP/) | ⬜ |

---

## 📁 Repository Organization

```
LearningCpp/
├── 01_GettingStarted/          # L01–L05  (README.md, theory/, code/, exercise/)
├── 02_BasicSyntax/             # L06–L22  (README.md, theory/, code/, exercise/)
├── 03_Subroutines/              # L23–L26  (README.md, theory/, code/, exercise/)
├── 04_ArraysStrings/            # L27–L30  (README.md, theory/, code/, exercise/)
├── 05_RecursionAlgorithms/      # L31–L38  (README.md, theory/, code/, exercise/)
├── 06_Pointers/ ... 12_AdvancedCPP/
│
├── files/                       # Academic materials, lecture PDFs & course guides
│   ├── Master_Academic_Guide.md # 🌐 Complete course comparison & academic guide
│   ├── mit6096/                 # MIT 6.096 original materials (lectures, assignments)
│   ├── cs106b/                  # Stanford CS106B textbook, assignments & libraries
│   ├── cs106x/                  # Stanford CS106X handouts & capstone projects
│   └── cs106l/                  # Stanford CS106L modern C++ lecture PDFs & projects
│
├── SYLLABUS.md                   # Full 75-lesson syllabus map
├── RESOURCES.md                 # Academic handout catalog
└── makefile                     # Root build script
```

---

## 🛠️ How to Build & Run Code

Each module contains an independent `makefile` in its `code/` subdirectory:

```bash
# 1. Navigate to the desired module's code directory
cd 01_GettingStarted/code

# 2. Compile all lessons in the module
make

# 3. Run the compiled executable
.\L01_HelloWorld.exe
```

---

## 📚 Essential Links & Resources

- 🌐 [**Master Academic Guide**](files/Master_Academic_Guide.md): Detailed comparison matrix between MIT 6.096, Stanford CS106B, CS106X, and CS106L.
- 📄 [**Academic Materials Archive (`files/`)**](files/README.md): Hub for local PDF slides, problem sets, and starter code.
- ⚙️ [**Compilation Guide**](docs/COMPILATION_GUIDE.md): Beginner step-by-step tutorial on manual GCC compilation.
- 🛠️ [**Makefile Guide**](docs/MAKEFILE_GUIDE.md): Technical guide to compiler flags (`-Wall -Wextra -std=c++17`) and sanitizer usage.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>