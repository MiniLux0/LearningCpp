<div align="center">

# 🚀 Section 04: Arrays & Strings — Fixed Arrays, C-Strings & Streams

> **Lessons**: L27 – L30  
> 🏛️ **Academic Base Source**: MIT 6.096 (Lecture 04) / Stanford CS106L (Lectures 04 & 05) / Stanford CS106B (Assignment 1)  
> 📖 **Theory Directory**: 📂 [**`04_ArraysStrings/theory/`**](theory/)  
> 📝 **Executive Summary**: 📝 [**`summary/04_ArraysStrings_Notes.md`**](summary/04_ArraysStrings_Notes.md)  
> 🎯 **Primary Focus**: Fixed-size 1D/2D arrays, array decay to pointer, passing arrays to functions, null-terminated C-strings (`char[]`), `<cstring>` functions, and `std::string` stream processing.

---

### 🧭 Module Navigation Hub

[![Root README](https://img.shields.io/badge/🏠_Root-README-00599C?style=for-the-badge)](../README.md)
[![Master Syllabus](https://img.shields.io/badge/📜_Master-SYLLABUS-F16822?style=for-the-badge)](../SYLLABUS.md)
[![Academic Guide](https://img.shields.io/badge/🌐_Academic-Guide-007ACC?style=for-the-badge)](../files/Master_Academic_Guide.md)
[![Resources](https://img.shields.io/badge/📚_Resources-Catalog-2ea44f?style=for-the-badge)](../RESOURCES.md)

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| [**⬅️ Section 03: Subroutines**](../03_Subroutines/README.md) | **Section 04: Arrays & Strings** | [**Section 05: Recursion & Algorithms ➡️**](../05_RecursionAlgorithms/README.md) |

</div>

---

## 📌 Module Overview

This module explores sequential memory layouts in C++: contiguous fixed 1D arrays, out-of-bounds safety risks, 2D matrix representations, array decay to raw pointers in subroutines, null-terminated C-strings (`char[]`), `<cstring>` manipulation functions (`strlen`, `strcpy`, `strcmp`), and modern `std::string` stream processing (`std::stringstream`).

---

## 📋 Lessons, Theory & Code Inventory

| # | Lesson Name | 📘 Theory Note | 💻 Code Lab | Key Technical Concepts | Status |
|---|-------------|----------------|-------------|------------------------|:------:|
| **L27** | **Array Basics** | 📘 [`theory/L27_ArrayBasics.md`](theory/L27_ArrayBasics.md) | 💻 [`code/L27_ArrayBasics.cpp`](code/L27_ArrayBasics.cpp) | 1D fixed static arrays, element indexing, bounds risks, initialization lists. | ✅ |
| **L28** | **Arrays as Parameters** | 📘 [`theory/L28_ArraysAsParameters.md`](theory/L28_ArraysAsParameters.md) | 💻 [`code/L28_ArraysAsParameters.cpp`](code/L28_ArraysAsParameters.cpp) | Array decay (`int arr[]` $\rightarrow$ `int*`), passing size, in-place modification. | ✅ |
| **L29** | **Multidimensional Arrays** | 📘 [`theory/L29_MultidimensionalArrays.md`](theory/L29_MultidimensionalArrays.md) | 💻 [`code/L29_MultidimensionalArrays.cpp`](code/L29_MultidimensionalArrays.cpp) | 2D matrices, nested loops, Row-Major Order indexing, grid operations. | ✅ |
| **L30** | **C-Strings** | 📘 [`theory/L30_CStrings.md`](theory/L30_CStrings.md) | 💻 [`code/L30_CStrings.cpp`](code/L30_CStrings.cpp) | Null-terminated `char[]`, `'\0'` marker, `<cstring>` functions, string streams. | ✅ |

---

## 🎯 Practical Exercises (E01 – E12)

> 📖 **Exercise Guide**: 📂 [**`exercise/README.md`**](exercise/README.md)

| # | Exercise Name | Topic | 💻 Solution File | Status |
|---|---------------|-------|------------------|:------:|
| **E01** | **Maximum** | Array Basics | 💻 [`exercise/E01_Maximo.cpp`](exercise/E01_Maximo.cpp) | ✅ |
| **E02** | **Average** | Array Basics | 💻 [`exercise/E02_Promedio.cpp`](exercise/E02_Promedio.cpp) | ✅ |
| **E03** | **Reverse Array** | Array Basics | 💻 [`exercise/E03_InvertirArreglo.cpp`](exercise/E03_InvertirArreglo.cpp) | ✅ |
| **E04** | **Increment All** | Arrays as Parameters | 💻 [`exercise/E04_IncrementarTodo.cpp`](exercise/E04_IncrementarTodo.cpp) | ✅ |
| **E05** | **Linear Search** | Arrays as Parameters | 💻 [`exercise/E05_BusquedaLineal.cpp`](exercise/E05_BusquedaLineal.cpp) | ✅ |
| **E06** | **Matrix Sum** | Multidimensional Arrays | 💻 [`exercise/E06_SumaMatriz.cpp`](exercise/E06_SumaMatriz.cpp) | ✅ |
| **E07** | **Transpose Matrix** | Multidimensional Arrays | 💻 [`exercise/E07_TransponerMatriz.cpp`](exercise/E07_TransponerMatriz.cpp) | ✅ |
| **E08** | **My Strlen** | C-Strings | 💻 [`exercise/E08_MiStrlen.cpp`](exercise/E08_MiStrlen.cpp) | ✅ |
| **E09** | **My Safe Strcpy** | C-Strings | 💻 [`exercise/E09_MiStrcpySeguro.cpp`](exercise/E09_MiStrcpySeguro.cpp) | ✅ |
| **E10** | **Count Vowels** | C-Strings & `<cctype>` | 💻 [`exercise/E10_ContarVocales.cpp`](exercise/E10_ContarVocales.cpp) | ✅ |
| **E11** | **Reverse String** | C-Strings & `strlen` | 💻 [`exercise/E11_InvertirString.cpp`](exercise/E11_InvertirString.cpp) | ✅ |
| **E12** | **To Uppercase** | C-Strings & `toupper` | 💻 [`exercise/E12_AMayusculas.cpp`](exercise/E12_AMayusculas.cpp) | ✅ |

---

## 📚 Academic Source & PDF Alignment

| Lessons | Academic PDF Source | Key Theoretical Topics Covered |
|---------|---------------------|--------------------------------|
| **L27–L28** | 📄 [`MIT 6.096 Lecture 04`](../files/mit6096/lectures/Lecture04_ArraysAndStrings.pdf) | Contiguous memory allocation, element indexing, `sizeof(arr)/sizeof(arr[0])`, array decay to raw pointer `T*`. |
| **L29** | 📄 [`MIT 6.096 Lecture 04`](../files/mit6096/lectures/Lecture04_ArraysAndStrings.pdf) \| [`CS106B Assignment 1`](../files/cs106b/assignments/Assignment%201/) | Multi-dimensional arrays, Row-Major Order memory storage, 2D matrix traversal, Grid simulation logic. |
| **L30** | 📄 [`MIT 6.096 Lecture 04`](../files/mit6096/lectures/Lecture04_ArraysAndStrings.pdf) \| [`CS106L Lecture 04`](../files/cs106l/lectures/WL4_Streams.pdf) | Null terminator `'\0'`, C-string manipulation functions (`strlen`, `strcpy`, `strcmp`), `std::string` stream conversions. |

## 🛠️ Build & Compilation Guides

Both `code/` and `exercise/` subdirectories contain automated `makefile` scripts:
- ⚙️ **Compilation Tutorial**: [`docs/COMPILATION_GUIDE.md`](../docs/COMPILATION_GUIDE.md)
- 🛠️ **Makefile & Sanitizer Reference**: [`docs/MAKEFILE_GUIDE.md`](../docs/MAKEFILE_GUIDE.md)

---

<div align="center">

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| [**⬅️ Section 03: Subroutines**](../03_Subroutines/README.md) | **Section 04: Arrays & Strings** | [**Section 05: Recursion & Algorithms ➡️**](../05_RecursionAlgorithms/README.md) |

</div>

---
*MiniLux0 — Learning C++ Section 04*
