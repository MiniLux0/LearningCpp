<div align="center">

# 🚀 Section 04: Static Arrays, C-Strings & Modern Strings

> **Lessons**: L27 – L30D  
> 🏛️ **Academic Base Source**: Stanford CS106B (Chapters 3 & 11) / MIT 6.096 (Lecture 04) / Stanford CS106L (Lectures 04 & 05)  
> 📝 **Executive Summary**: 📝 [**`summary/04_ArraysStrings_Notes.md`**](summary/04_ArraysStrings_Notes.md)  
> 🎯 **Primary Focus**: 1D/2D static arrays, RAM memory layout, Row-Major Order, array decay to pointers (`int*`), C-strings (`<cstring>`), modern dynamic strings (`<string>`), character inspection (`<cctype>`), and string algorithms ($O(N)$ Palindromes, Pig Latin, Caesar Cipher).

---

### 🧭 Module Navigation Hub

| ⬅️ Previous Module | 📂 Current Location | ➡️ Next Module |
|:------------------:|:-------------------:|:--------------:|
| [**⬅️ Section 03: Subroutines**](../03_Subroutines/README.md) | **Section 04: Arrays & Strings** | [**Section 05: Recursion & Algorithms ➡️**](../05_RecursionAlgorithms/README.md) |

</div>

---

## 📌 Module Overview

This module covers sequential data structures in contiguous memory: from 1D and 2D static arrays to C-style character arrays (`char[]` from `<cstring>`), the modern `string` object from `<string>`, the independent character inspection library `<cctype>`, and high-level string processing algorithms.

---

## 📋 Lessons, Theory & Code Inventory

| # | Lesson Title | 📘 Theory Note | 💻 Code Lab | Key Technical Concepts | Status |
|---|--------------|----------------|-------------|------------------------|:------:|
| **L27** | **1D Static Arrays** | 📘 [`theory/L27_ArrayBasics.md`](theory/L27_ArrayBasics.md) | 💻 [`code/L27_ArrayBasics.cpp`](code/L27_ArrayBasics.cpp) | Contiguous memory, offset formula, zero-indexing, `{}` initialization, memory boundaries. | ✅ |
| **L28** | **Arrays as Parameters** | 📘 [`theory/L28_ArraysAsParameters.md`](theory/L28_ArraysAsParameters.md) | 💻 [`code/L28_ArraysAsParameters.cpp`](code/L28_ArraysAsParameters.cpp) | Pointer decay (`int*`), loss of `sizeof`, `size` parameter, `const` array parameters. | ✅ |
| **L29** | **Multidimensional Arrays** | 📘 [`theory/L29_MultidimensionalArrays.md`](theory/L29_MultidimensionalArrays.md) | 💻 [`code/L29_MultidimensionalArrays.cpp`](code/L29_MultidimensionalArrays.cpp) | 2D matrices, Row-Major Order, $(i \times C) + j$ flat index formula, mandatory column dimension in parameters. | ✅ |
| **L30A** | **`<cstring>` Library** | 📘 [`theory/L30A_CStrings.md`](theory/L30A_CStrings.md) | 💻 [`code/L30A_CStrings.cpp`](code/L30A_CStrings.cpp) | Traditional C-strings (`char[]`), null terminator `'\0'`, `strlen`, `strcpy`, `strcat`, `strcmp`, `strchr`. | ✅ |
| **L30B** | **`<string>` Library** | 📘 [`theory/L30B_StdString.md`](theory/L30B_StdString.md) | 💻 [`code/L30B_StdString.cpp`](code/L30B_StdString.cpp) | `string` object, `length`, `substr`, `find`, `rfind`, `insert`, `erase`, `replace`, `.at(i)` vs `[]`, `const string&`. | ✅ |
| **L30C** | **`<cctype>` Library** | 📘 [`theory/L30C_CCtype.md`](theory/L30C_CCtype.md) | 💻 [`code/L30C_CCtype.cpp`](code/L30C_CCtype.cpp) | Character inspection (`isalpha`, `isdigit`, `isalnum`, `islower`, `isupper`, `isspace`, `ispunct`, `tolower`, `toupper`). | ✅ |
| **L30D** | **String Algorithms** | 📘 [`theory/L30D_StringApplications.md`](theory/L30D_StringApplications.md) | 💻 [`code/L30D_StringApplications.cpp`](code/L30D_StringApplications.cpp) | Palindrome complexity $O(N)$ vs $O(N^2)$, Pig Latin, Caesar Cipher, Stanford `strlib.h` abstractions. | ✅ |

---

## 🎯 Practical Exercises (E01 – E12)

> 📖 **Exercise Guide**: 📂 [**`exercise/README.md`**](exercise/README.md)

| # | Exercise Name | Topic | 💻 Solution File | Status |
|---|---------------|-------|------------------|:------:|
| **E01** | **Find Maximum** | 1D arrays & traversal | 💻 [`exercise/E01_Maximum.cpp`](exercise/E01_Maximum.cpp) | ✅ |
| **E02** | **Average Calculation** | 1D arrays & accumulation | 💻 [`exercise/E02_Average.cpp`](exercise/E02_Average.cpp) | ✅ |
| **E03** | **In-Place Array Reversal** | Frontier pointers (`low`/`high`) & swap | 💻 [`exercise/E03_ReverseArray.cpp`](exercise/E03_ReverseArray.cpp) | ✅ |
| **E04** | **Increment All** | In-place array parameter modification | 💻 [`exercise/E04_IncrementAll.cpp`](exercise/E04_IncrementAll.cpp) | ✅ |
| **E05** | **Linear Search** | Array searching & index return | 💻 [`exercise/E05_LinearSearch.cpp`](exercise/E05_LinearSearch.cpp) | ✅ |
| **E06** | **2D Matrix Sum** | Row-Major nested loop accumulation | 💻 [`exercise/E06_MatrixSum.cpp`](exercise/E06_MatrixSum.cpp) | ✅ |
| **E07** | **Transpose Square Matrix** | In-place `mat[i][j]` element swapping | 💻 [`exercise/E07_TransposeMatrix.cpp`](exercise/E07_TransposeMatrix.cpp) | ✅ |
| **E08** | **Custom `strlen` Implementation** | Manual character count until `'\0'` sentinel | 💻 [`exercise/E08_CustomStrlen.cpp`](exercise/E08_CustomStrlen.cpp) | ✅ |
| **E09** | **Safe `miStrcpy` Copy** | Buffer overflow prevention in C-strings | 💻 [`exercise/E09_SafeStrcpy.cpp`](exercise/E09_SafeStrcpy.cpp) | ✅ |
| **E10** | **Count Vowels** | Character classification with `<cctype>` | 💻 [`exercise/E10_CountVowels.cpp`](exercise/E10_CountVowels.cpp) | ✅ |
| **E11** | **In-Place C-String Reversal** | Modifying C-style character arrays | 💻 [`exercise/E11_ReverseString.cpp`](exercise/E11_ReverseString.cpp) | ✅ |
| **E12** | **Convert to Uppercase** | Case transformation using `toupper()` | 💻 [`exercise/E12_ToUppercase.cpp`](exercise/E12_ToUppercase.cpp) | ✅ |

---

## 📚 Academic Source Alignment

| Lessons | Academic Source PDF | Key Theoretical Topics |
|---------|---------------------|------------------------|
| **L27–L29** | 📄 [`MIT 6.096 Lecture 04`](../files/mit6096/lectures/Lecture04_ArraysAndStrings.pdf) \| [`CS106B Textbook Ch 11`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf) | 1D/2D static arrays, contiguous memory, Row-Major Order, pointer decay. |
| **L30A** | 📄 [`CS106B Textbook Ch 3.5`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf) \| [`MIT 6.096 Lecture 04`](../files/mit6096/lectures/Lecture04_ArraysAndStrings.pdf) | `<cstring>` library, C-strings, `'\0'` null sentinel, buffer overflows. |
| **L30B** | 📄 [`CS106B Textbook Ch 3.1-3.4`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf) | `<string>` library, `string` object, substrings, searching, `const string&` passing. |
| **L30C** | 📄 [`CS106B Textbook Ch 3.3`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf) | `<cctype>` library, predicates (`isalpha`, `isdigit`), transformations (`tolower`, `toupper`). |
| **L30D** | 📄 [`CS106B Textbook Ch 3.6-3.7`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf) | Palindromes $O(N)$ vs $O(N^2)$, Pig Latin, Caesar Cipher, `strlib.h` abstractions. |

---

## 🛠️ Build & Compilation Guides

Subdirectories `code/` and `exercise/` include automated `makefile`s:
- ⚙️ **Compilation Tutorial**: [`docs/COMPILATION_GUIDE.md`](../docs/COMPILATION_GUIDE.md)
- 🛠️ **Makefile & Sanitizer Reference**: [`docs/MAKEFILE_GUIDE.md`](../docs/MAKEFILE_GUIDE.md)

> [!TIP]
> **New to C++ compilation?**
> If you don't know how to compile or run C++ code from your terminal, refer to the documentation hub in 📂 [**`docs/README.md`**](../docs/README.md).


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>