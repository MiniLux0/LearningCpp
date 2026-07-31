<div align="center">

# 🚀 Learning C++ & Computer Science

*A structured learning journey in C++, Modern C++ Standards, Algorithms, and Data Structures — unifying the curricula of **MIT 6.096**, **Stanford CS106B**, **Stanford CS106X**, and **Stanford CS106L**.*

[![C++17](https://img.shields.io/badge/C%2B%2B-17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)](https://en.cppreference.com/w/cpp/17)
[![Compiler](https://img.shields.io/badge/GCC-15.2.0-F16822?style=for-the-badge&logo=gnu&logoColor=white)](https://gcc.gnu.org/)
[![Platform](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/brechtsanders/winlibs_mingw)
[![Editor](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Progress](https://img.shields.io/badge/Progress-L30%20%2F%2075-yellow?style=for-the-badge)](#-modules-map--progress)

</div>

---

## 📌 About the Repository

This repository serves as a personal log and hands-on laboratory for learning **Modern C++ (C++17/20)**, **Algorithms**, and **Data Structures**. The study plan merges the technical rigor of four landmark Computer Science courses:

- 🏛️ **MIT 6.096** (*Introduction to C++*): Syntax, compilation pipeline, pointers, manual memory management (`new`/`delete`), and Object-Oriented Programming (OOP).
- 🌲 **Stanford CS106B** (*Programming Abstractions*): Recursion, Backtracking, Big-O Notation, Linked Lists, BST Trees, Hash Tables, and Graph Algorithms.
- ⚡ **Stanford CS106X** (*Accelerated Programming Abstractions*): High-performance challenges, 4-way Priority Queue implementations, Huffman compression, and capstone projects.
- ⚙️ **Stanford CS106L** (*Standard C++ Programming*): Modern C++ standards (C++11/17/20), Uniform Initialization, Streams, Containers, Custom Iterators, Lambdas, Const-Correctness, Operator Overloading, Special Member Functions (Rule of 0/3/5), Move Semantics (`std::move`), RAII, and Smart Pointers (`std::unique_ptr`, `std::shared_ptr`).

### 📁 Academic Materials Archive (`files/`)
All original academic resources supporting this study plan—lecture PDFs, problem sets, solutions, starter code, textbooks, and specialized course syllabi—are housed in the [`files/`](files/) directory. 

For a complete breakdown of course difficulty levels, pedagogical differences, and open-source learning roadmaps, consult the 🌐 [**Master Academic Guide**](files/Master_Academic_Guide.md).

---

## 📊 Modules Map & Progress

| # | Module | Lessons | Base Source | Key Topics | Theory Notes | Code Lab | Status |
|---|--------|---------|-------------|------------|:------------:|:--------:|:------:|
| **01** | [`01_GettingStarted`](01_GettingStarted/) | L01 – L05 | MIT L1 / CS106L | First program, text output, comments, `std::cin` & `std::cout` | 📘 [`theory/`](01_GettingStarted/theory/) | 💻 [`code/`](01_GettingStarted/code/) | ✅ |
| **02** | [`02_BasicSyntax`](02_BasicSyntax/) | L06 – L22 | MIT L2 / CS106L | Primitive types, Uniform Initialization `{}` , conditionals, loops | 📘 [`theory/`](02_BasicSyntax/theory/) | 💻 [`code/`](02_BasicSyntax/code/) | 🔄 |
| **03** | [`03_Subroutines`](03_Subroutines/) | L23 – L26 | MIT L3 / CS106L | Functions, pass-by-reference (`&`, `const &`), `.h` headers | 📘 [`theory/`](03_Subroutines/theory/) | 💻 [`code/`](03_Subroutines/code/) | ✅ |
| **04** | [`04_ArraysStrings`](04_ArraysStrings/) | L27 – L30 | MIT L4 / CS106L | 1D/2D arrays, C-strings, `std::string`, stringstreams | 📘 [`theory/`](04_ArraysStrings/theory/) | 💻 [`code/`](04_ArraysStrings/code/) | 🔄 |
| **05** | [`05_RecursionAlgorithms`](05_RecursionAlgorithms/) | L31 – L38 | Stanford CS106B/X | Recursion, Big-O Notation, MergeSort, QuickSort | 📘 `theory/` | 💻 `code/` | ⬜ |
| **06** | [`06_Pointers`](06_Pointers/) | L39 – L46 | MIT L5 / CS106L | Pointers, references, Const-Correctness, callbacks, 2D matrices | 📘 `theory/` | 💻 `code/` | ⬜ |
| **07** | [`07_Classes`](07_Classes/) | L47 – L52 | MIT L6 / CS106L | Structs, classes, encapsulation, Operator Overloading | 📘 `theory/` | 💻 `code/` | ⬜ |
| **08** | [`08_OOP`](08_OOP/) | L53 – L58 | MIT L7 / CS106L | Inheritance, polymorphism, `virtual`, destructors | 📘 `theory/` | 💻 `code/` | ⬜ |
| **09** | [`09_MemoryManagement`](09_MemoryManagement/) | L59 – L63 | MIT L8 / CS106L | Stack vs Heap, `new`/`delete`, RAII, Rule of 0/3/5, Move Semantics | 📘 `theory/` | 💻 `code/` | ⬜ |
| **10** | [`10_DataStructures`](10_DataStructures/) | L64 – L68 | Stanford / CS106L | Linked Lists, BST Trees, Custom Iterators, HashMaps, Graphs | 📘 `theory/` | 💻 `code/` | ⬜ |
| **11** | [`11_FileIO`](11_FileIO/) | L69 – L72 | MIT L10 / CS106L | Stream states, Text (`.txt`) and Binary (`.bin`) Files | 📘 `theory/` | 💻 `code/` | ⬜ |
| **12** | [`12_AdvancedCPP`](12_AdvancedCPP/) | L73 – L75 | MIT L9-10 / CS106L | Templates, STL Containers, Lambdas, Huffman & WikiRacer | 📘 `theory/` | 💻 `code/` | ⬜ |

> 📜 For a detailed step-by-step lesson breakdown, check [**TEMARIO.md**](TEMARIO.md).

---

## 📁 Repository Structure

Each module is consistently structured with modular subdirectories:

```
LearningCpp/
├── 01_GettingStarted/          # L01–L05  · MIT L1 (code/, theory/, exercise/)
├── 02_BasicSyntax/             # L06–L22  · MIT L2 (incluye exercise/) (E01-E10)
├── 03_Subroutines/              # Functions (code/, theory/, exercise/)
├── 04_ArraysStrings/            # Arrays & Strings (code/, theory/, exercise/)
├── 05_RecursionAlgorithms/      # Recursion, Big-O & Sorting (code/, theory/, exercise/)
├── 06_Pointers/                 # Pointers & Memory (code/, theory/, exercise/)
├── 07_Classes/                  # Classes & Encapsulation (code/, theory/, exercise/)
├── 08_OOP/                      # Inheritance & Polymorphism (code/, theory/, exercise/)
├── 09_MemoryManagement/         # Stack vs Heap, RAII, Deep Copy, Rule of 0/3/5 (code/, theory/, exercise/)
├── 10_DataStructures/           # Linked Lists, Custom Iterators, Trees & HashMaps (code/, theory/, exercise/)
├── 11_FileIO/                   # Text Files, Streams & Binary Records (code/, theory/, exercise/)
├── 12_AdvancedCPP/              # Templates, STL, Lambdas & Advanced Projects (code/, theory/, exercise/)
│
├── files/                       # Academic materials, textbooks & syllabi
│   ├── Master_Academic_Guide.md # 🌐 Master guide & course comparison matrix
│   ├── README.md                # Academic files entry hub
│   ├── mit6096/                 # MIT 6.096 (README.md, lectures/, assignments/, solutions/, project/)
│   ├── cs106b/                  # Stanford CS106B (README.md, textbook/, assignments/, sections/, libraries/)
│   ├── cs106x/                  # Stanford CS106X (README.md, 34 handouts & 7 assignments catalog)
│   └── cs106l/                  # Stanford CS106L (README.md, 17 lecture PDFs, 3 projects)
│
├── TEMARIO.md                   # Full 75-lesson syllabus
├── RESOURCES.md                 # Stanford & MIT handouts, lectures, and assignments catalog
└── makefile                     # Root build script
```

---

## 🛠️ Requirements & Installation

### Compiler and Tools

- **Compiler**: GCC 15.2.0 (installable on Windows via [WinLibs](https://winlibs.com/)).
- **C++ Standard**: C++17 (`-std=c++17`).
- **Recommended Compilation Flags**:
  ```bash
  g++ -std=c++17 -Wall -Wextra -Wshadow -Wpedantic -g
  ```

### How to Build & Run

Each code directory contains its own `makefile`. To compile and run any lesson:

```bash
# Navigate to the desired module directory (e.g., 03_Subroutines/code)
cd 03_Subroutines/code

# Build all programs in the module
make

# Run a specific executable (e.g., on Windows)
.\L23_Functions.exe
```

---

## 📚 Documentation & Resources

- 🌐 [**Master Academic Guide (`files/Master_Academic_Guide.md`)**](files/Master_Academic_Guide.md): Complete matrix comparison, course levels, learning roadmap, and syllabus alignment for MIT 6.096, Stanford CS106B, CS106X, and CS106L.
- 📄 [**Academic Materials Archive (`files/README.md`)**](files/README.md): Central hub for local PDF lectures, problem sets, starter code, solutions, and course syllabi.
- 📜 [**TEMARIO.md**](TEMARIO.md): Detailed 75-lesson syllabus map.
- 🔗 [**RESOURCES.md**](RESOURCES.md): Detailed catalog of textbooks, handouts, MIT lectures, and Stanford assignments.
- ⚙️ [**COMPILATION_GUIDE.md**](docs/COMPILATION_GUIDE.md): Beginner step-by-step tutorial on compiling C++ manually with GCC and Makefiles.
- 🛠️ [**MAKEFILE_GUIDE.md**](docs/MAKEFILE_GUIDE.md): Complete technical guide to the build system, compiler flags, AddressSanitizer, and Makefile reuse.

---

<div align="center">
  <sub>Developed by <strong>MiniLux0</strong> · 2026</sub>
</div>