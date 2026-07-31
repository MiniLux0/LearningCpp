# 🚀 Section 04: Arrays & Strings — Fixed Arrays, C-Strings & Streams

> **Lessons**: L27 – L30  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 04) / Stanford CS106L (Lecture 04 & 05) / Stanford CS106B (Assignment 1)  
> 🎯 **Primary Focus**: Fixed-size 1D and 2D arrays, array decay to pointer, passing arrays to functions, null-terminated C-strings (`char[]`), `<cstring>` functions, and `std::string` stream processing.

---

## 📌 Module Overview

This module explores sequential memory layouts in C++. It starts with contiguous fixed-size 1D static arrays, zero-initialization, out-of-bounds safety risks, 2D matrix representations, and how arrays decay into raw pointers when passed to subroutines. It then covers null-terminated C-style strings (`char[]`), `<cstring>` manipulation functions (`strlen`, `strcpy`, `strcmp`), transitioning into modern `std::string` and stringstream processing (`std::stringstream`).

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L27–L28** | 📄 [`MIT 6.096 Lecture 04`](../files/mit6096/lectures/Lecture04_ArraysAndStrings.pdf) | Contiguous memory allocation, element indexing, size calculation (`sizeof(arr)/sizeof(arr[0])`), array decay to raw pointer `T*`, passing array length explicitly to functions. |
| **L29** | 📄 [`MIT 6.096 Lecture 04`](../files/mit6096/lectures/Lecture04_ArraysAndStrings.pdf) \| [`CS106B Assignment 1`](../files/cs106b/assignments/Assignment%201/) | Multi-dimensional arrays, Row-Major Order memory storage, 2D matrix traversal, Grid simulation logic (*Game of Life*). |
| **L30** | 📄 [`MIT 6.096 Lecture 04`](../files/mit6096/lectures/Lecture04_ArraysAndStrings.pdf) \| [`CS106L Lecture 04`](../files/cs106l/lectures/WL4_Streams.pdf) | Null terminator character `'\0'`, C-string manipulation functions (`strlen`, `strcpy`, `strcat`, `strcmp`), `std::string` stream conversions. |

---

## 💻 Lessons & Code Inventory (`04_ArraysStrings/code/`)

| # | Lesson | Code File | Key Technical Concepts | Status |
|---|--------|-----------|------------------------|:------:|
| **L27** | **Array Basics** | [`L27_ArrayBasics.cpp`](code/L27_ArrayBasics.cpp) | 1D fixed static arrays, element access, bounds risks, array initialization lists `{}`. | ✅ |
| **L28** | **Arrays as Parameters** | [`L28_ArraysAsParameters.cpp`](code/L28_ArraysAsParameters.cpp) | Array decay to pointer (`int arr[]` $\rightarrow$ `int*`), passing array size, modifying elements in-place. | ✅ |
| **L29** | **Multidimensional Arrays** | [`L29_MultidimensionalArrays.cpp`](code/L29_MultidimensionalArrays.cpp) | 2D matrices, nested loops, Row-Major indexing, 2D grid operations. | ✅ |
| **L30** | **C-Strings** | [`L30_CStrings.cpp`](code/L30_CStrings.cpp) | Null-terminated `char[]` arrays, `'\0'` marker, `<cstring>` library functions, string streams. | ✅ |

---

## 🛠️ How to Compile & Run

To compile and run the code files in this module:

```bash
# Navigate to the code directory
cd 04_ArraysStrings/code

# Compile all lessons using Makefile
make

# Run a specific lesson executable
.\L27_ArrayBasics.exe
.\L30_CStrings.exe
```

---

## 📁 Directory Structure

```
04_ArraysStrings/
├── README.md               # 📄 Module guide (this file)
├── code/                   # C++ source files (L27–L30) & Makefile
│   ├── L27_ArrayBasics.cpp
│   ├── L28_ArraysAsParameters.cpp
│   ├── L29_MultidimensionalArrays.cpp
│   ├── L30_CStrings.cpp
│   └── makefile
├── theory/                 # Detailed Markdown notes & theory docs
├── summary/                # Detailed section summary notes
├── exercise/               # Practical exercises and array challenges
└── ejercicios_arrays_strings.md
```

---

## 🔗 Navigation & Quick Links

- ⬅️ [Previous Module: Section 03 — Subroutines](../03_Subroutines/README.md)
- 📋 [Master Syllabus (`TEMARIO.md`)](../TEMARIO.md)
- 🌐 [Academic Files Hub (`files/README.md`)](../files/README.md)
- ➡️ [Next Module: Section 05 — Recursion & Algorithms](../05_RecursionAlgorithms/README.md)

---
*MiniLux0 — Learning C++ Section 04*
