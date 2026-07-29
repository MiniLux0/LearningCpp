<div align="center">

# 🚀 Learning C++ & Computer Science

*A structured learning journey in C++, Algorithms, and Data Structures — unifying the curricula of **MIT 6.096**, **Stanford CS106B**, and **Stanford CS106X**.*

[![C++17](https://img.shields.io/badge/C%2B%2B-17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)](https://en.cppreference.com/w/cpp/17)
[![Compiler](https://img.shields.io/badge/GCC-15.2.0-F16822?style=for-the-badge&logo=gnu&logoColor=white)](https://gcc.gnu.org/)
[![Platform](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/brechtsanders/winlibs_mingw)
[![Editor](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Progress](https://img.shields.io/badge/Progress-L30%20%2F%2075-yellow?style=for-the-badge)](#-modules-map--progress)

</div>

---

## 📌 About the Repository

This repository serves as a personal log and hands-on laboratory for learning **Modern C++ (C++17)**, **Algorithms**, and **Data Structures**. The study plan merges the technical rigor of three landmark Computer Science courses:

- 🏛️ **MIT 6.096** (*Introduction to C++*): Syntax, compilation pipeline, pointers, manual memory management (`new`/`delete`), and Object-Oriented Programming (OOP).
- 🌲 **Stanford CS106B** (*Programming Abstractions*): Recursion, Backtracking, Big-O Notation, Linked Lists, BST Trees, and Hash Tables.
- ⚡ **Stanford CS106X** (*Accelerated Programming Abstractions*): High-performance challenges, 4-way Priority Queue implementations, Huffman compression, and capstone projects.

---

## 📊 Modules Map & Progress

| # | Module | Lessons | Base Source | Key Topics | Status |
|---|--------|---------|-------------|------------|:------:|
| **01** | [`01_GettingStarted`](01_GettingStarted/) | L01 – L05 | MIT L1 | First program, text output, comments, `std::cin` & `std::cout` | ✅ |
| **02** | [`02_BasicSyntax`](02_BasicSyntax/) | L06 – L22 | MIT L2 | Syntax, conditionals, loops, and exercises | 🔄 |
| **03** | [`03_Subroutines`](03_Subroutines/) | L23 – L26 | MIT L3 | Functions, pass-by-reference, `.h` headers | ✅ |
| **04** | [`04_ArraysStrings`](04_ArraysStrings/) | L27 – L30 | MIT L4 | 1D/2D arrays, C-strings, `std::string` | 🔄 |
| **05** | [`05_RecursionAlgorithms`](05_RecursionAlgorithms/) | L31 – L38 | Stanford CS106B | Recursion, Big-O Notation, MergeSort, QuickSort | ⬜ |
| **06** | [`06_Pointers`](06_Pointers/) | L39 – L46 | MIT L5 / Stanford | Pointers, references, callbacks, 2D matrices | ⬜ |
| **07** | [`07_Classes`](07_Classes/) | L47 – L52 | MIT L6 | Structs, classes, encapsulation, constructors | ⬜ |
| **08** | [`08_OOP`](08_OOP/) | L53 – L58 | MIT L7 | Inheritance, polymorphism, `virtual`, destructors | ⬜ |
| **09** | [`09_MemoryManagement`](09_MemoryManagement/) | L59 – L63 | MIT L8 | Stack vs Heap, `new`/`delete`, RAII, Deep Copy | ⬜ |
| **10** | [`10_DataStructures`](10_DataStructures/) | L64 – L68 | Stanford CS106B/X | Linked Lists, BST Trees, Heaps | ⬜ |
| **11** | [`11_FileIO`](11_FileIO/) | L69 – L72 | MIT L10 / Stanford | Persistence: Text (`.txt`) and Binary (`.bin`) Files | ⬜ |
| **12** | [`12_AdvancedCPP`](12_AdvancedCPP/) | L73 – L75 | MIT L9-10 / Stanford X | Templates, STL, Exceptions, Huffman Compression | ⬜ |

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
├── 09_MemoryManagement/         # Stack vs Heap, RAII, Deep Copy (code/, theory/, exercise/)
├── 10_DataStructures/           # Linked Lists, Trees & Heaps (code/, theory/, exercise/)
├── 11_FileIO/                   # Text Files & Binary Records (code/, theory/, exercise/)
├── 12_AdvancedCPP/              # Templates, STL & Advanced Projects (code/, theory/, exercise/)
│
├── files/                       # Academic materials & textbooks
│   ├── CS106BX-Reader.pdf       # Official Stanford textbook (Eric Roberts)
│   ├── lectures/                # MIT 6.096 lecture PDFs
│   └── assignments/             # MIT official assignments & solutions
│
├── TEMARIO.md                   # Full 75-lesson syllabus
├── RESOURCES.md                 # Stanford handouts & assignments catalog
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

- 📜 [**TEMARIO.md**](TEMARIO.md): Detailed lesson syllabus.
- 🛠️ [**MAKEFILE_GUIDE.md**](docs/MAKEFILE_GUIDE.md): Complete guide to the C++ build system, flags, AddressSanitizer, and Makefile reuse.
- 🔗 [**RESOURCES.md**](RESOURCES.md): Catalog of books, handouts, and official Stanford CS106X assignments.

---

<div align="center">
  <sub>Developed by <strong>MiniLux0</strong> · 2026</sub>
</div>