<div align="center">

# 🚀 Section 05: Recursion & Algorithms — Call Stack, Big-O, Sorting & Backtracking

> **Lessons**: L31 – L38  
> 🏛️ **Academic Base Source**: Stanford CS106B (Lectures 07–11) / MIT 6.096 (Lecture 05)  
> 📝 **Executive Summary**: 📝 [**`summary/05_RecursionAlgorithms_Notes.md`**](summary/05_RecursionAlgorithms_Notes.md)  
> 🎯 **Primary Focus**: Mathematical induction, call stack memory, base cases vs recursive steps, Big-O complexity Analysis, linear/binary search, quadratic sorts (Selection, Insertion), $O(N \log N)$ Divide & Conquer (MergeSort, QuickSort), and Recursive Backtracking.

---

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:------------------:|:--------------:|
| [**⬅️ Section 04: Arrays & Strings**](../04_ArraysStrings/README.md) | **Section 05: Recursion & Algorithms** | [**Section 06: Pointers & Memory ➡️**](../06_Pointers/) |

</div>

---

## 📌 Module Overview

This module introduces algorithmic thinking and recursive problem solving: managing call stack frames, avoiding stack overflow, analyzing algorithmic efficiency with Big-O notation, binary search, recursive sorting algorithms (MergeSort, QuickSort), and recursive backtracking state exploration.

---

## 📋 Lessons, Theory & Code Inventory

| # | Lesson Name | 📘 Theory Note | 💻 Code Lab | Key Technical Concepts | Status |
|---|-------------|----------------|-------------|------------------------|:------:|
| **L31** | **Thinking Recursively** | 📘 [`L31_ThinkingRecursively.md`](theory/L31_ThinkingRecursively.md) | 💻 [`code/L31_ThinkingRecursively.cpp`](code/L31_ThinkingRecursively.cpp) | Base cases, call stack frames, induction, call stack unwind. | ✅ |
| **L32** | **Recursive Problems** | 📘 [`L32_RecursiveProblems.md`](theory/L32_RecursiveProblems.md) | 💻 [`code/L32_RecursiveProblems.cpp`](code/L32_RecursiveProblems.cpp) | Factorials, Fibonacci sequence, string reversal, call depth. | ✅ |
| **L33** | **Big-O Notation** | 📘 [`L33_BigONotation.md`](theory/L33_BigONotation.md) | 💻 [`code/L33_BigONotation.cpp`](code/L33_BigONotation.cpp) | Asymptotic analysis ($O(1)$, $O(\log N)$, $O(N)$, $O(N \log N)$, $O(N^2)$). | ✅ |
| **L34** | **Linear & Binary Search** | 📘 [`L34_LinearBinarySearch.md`](theory/L34_LinearBinarySearch.md) | 💻 [`code/L34_LinearBinarySearch.cpp`](code/L34_LinearBinarySearch.cpp) | Sequential search $O(N)$ vs divide-and-conquer binary search $O(\log N)$. | ✅ |
| **L35** | **Quadratic Sorts** | 📘 [`L35_QuadraticSorts.md`](theory/L35_QuadraticSorts.md) | 💻 [`code/L35_QuadraticSorts.cpp`](code/L35_QuadraticSorts.cpp) | Selection Sort, Insertion Sort, Bubble Sort $O(N^2)$ performance. | ✅ |
| **L36** | **MergeSort** | 📘 [`L36_MergeSort.md`](theory/L36_MergeSort.md) | 💻 [`code/L36_MergeSort.cpp`](code/L36_MergeSort.cpp) | Divide & Conquer $O(N \log N)$ sorting, array merging logic. | ✅ |
| **L37** | **QuickSort** | 📘 [`L37_QuickSort.md`](theory/L37_QuickSort.md) | 💻 [`code/L37_QuickSort.cpp`](code/L37_QuickSort.cpp) | Pivot selection, partitioning algorithm, average vs worst case $O(N^2)$. | ✅ |
| **L38** | **Backtracking** | 📘 [`L38_Backtracking.md`](theory/L38_Backtracking.md) | 💻 [`code/L38_Backtracking.cpp`](code/L38_Backtracking.cpp) | Decision trees, state rollback, N-Queens, subset generation. | ✅ |

---

## 🎯 Practical Exercises (E01 – E08)

> 📖 **Exercise Guide**: 📂 [**`exercise/README.md`**](exercise/README.md)

| # | Exercise Name | Topic | 💻 Solution File | Status |
|---|---------------|-------|------------------|:------:|
| **E01** | **Factorial** | Recursion — base case & call stack | 💻 [`exercise/E01_Factorial.cpp`](exercise/E01_Factorial.cpp) | ✅ |
| **E02** | **Fibonacci** | Naive vs memoized recursion | 💻 [`exercise/E02_Fibonacci.cpp`](exercise/E02_Fibonacci.cpp) | ✅ |
| **E03** | **Binary Search** | Recursive divide & conquer search | 💻 [`exercise/E03_BinarySearch.cpp`](exercise/E03_BinarySearch.cpp) | ✅ |
| **E04** | **MergeSort** | Divide & conquer O(n log n) sort | 💻 [`exercise/E04_MergeSort.cpp`](exercise/E04_MergeSort.cpp) | ✅ |
| **E05** | **QuickSort** | Lomuto partition & pivot placement | 💻 [`exercise/E05_QuickSort.cpp`](exercise/E05_QuickSort.cpp) | ✅ |
| **E06** | **Power Function** | Naive vs fast exponentiation | 💻 [`exercise/E06_PowerFunction.cpp`](exercise/E06_PowerFunction.cpp) | ✅ |
| **E07** | **String Reversal** | Recursive reversal without loops | 💻 [`exercise/E07_StringReversal.cpp`](exercise/E07_StringReversal.cpp) | ✅ |
| **E08** | **Backtracking Subsets** | Choose / Explore / Unchoose pattern | 💻 [`exercise/E08_Backtracking.cpp`](exercise/E08_Backtracking.cpp) | ✅ |

---

## 🛠️ Build & Compilation Guides

Both `code/` and `exercise/` subdirectories contain automated `makefile` scripts:
- ⚙️ **Compilation Tutorial**: [`docs/COMPILATION_GUIDE.md`](../docs/COMPILATION_GUIDE.md)
- 🛠️ **Makefile & Sanitizer Reference**: [`docs/MAKEFILE_GUIDE.md`](../docs/MAKEFILE_GUIDE.md)

> [!TIP]
> **New to C++ compilation?**
> If you don't know how to compile or run C++ code from your terminal, refer to the documentation hub in 📂 [**`docs/README.md`**](../docs/README.md).

---
*MiniLux0 — Learning C++ Section 05*
