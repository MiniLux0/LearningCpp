# 📝 Section 04: Arrays, C-Strings & Modern `string` — Study Summary and Notes

Study notes and executive summary of **Section 04: Arrays, C-Strings, and Modern `string`** from the C++ course (Stanford CS106B Chapter 3 / MIT 6.096 Lecture 04).
It covers contiguous memory representation of 1D/2D arrays, array decay to pointers (`T*`), traditional C-strings (`<cstring>`), modern `string` operations (`<string>`), character predicates (`<cctype>`), and algorithmic string processing (palindromes $O(N^2)$ vs $O(N)$, Pig Latin, ciphers).

---

## 🧭 Table of Contents

1. [Lessons and Theory](#-lessons-and-theory)
2. [Practical Exercises (E01 – E12)](#-practical-exercises-e01--e12)
3. [Summary by Lesson](#-summary-by-lesson)
   - [L27 — Array Basics](#l27--array-basics)
   - [L28 — Arrays as Parameters](#l28--arrays-as-parameters)
   - [L29 — Multidimensional Arrays](#l29--multidimensional-arrays)
   - [L30A — `<cstring>` Library](#l30a--cstring-library)
   - [L30B — `<string>` Library](#l30b--string-library)
   - [L30C — `<cctype>` Library](#l30c--cctype-library)
   - [L30D — String Applications](#l30d--string-applications)
4. [Best Practices and Key Patterns](#-best-practices-and-key-patterns)

---

## 📘 Lessons and Theory

| Lesson | Title | Theory Note | Code Lab |
| :--- | :--- | :--- | :--- |
| **L27** | Array Basics | 📘 [`L27_ArrayBasics.md`](../theory/L27_ArrayBasics.md) | 💻 [`L27_ArrayBasics.cpp`](../code/L27_ArrayBasics.cpp) |
| **L28** | Arrays as Parameters | 📘 [`L28_ArraysAsParameters.md`](../theory/L28_ArraysAsParameters.md) | 💻 [`L28_ArraysAsParameters.cpp`](../code/L28_ArraysAsParameters.cpp) |
| **L29** | Multidimensional Arrays | 📘 [`L29_MultidimensionalArrays.md`](../theory/L29_MultidimensionalArrays.md) | 💻 [`L29_MultidimensionalArrays.cpp`](../code/L29_MultidimensionalArrays.cpp) |
| **L30A** | `<cstring>` Library | 📘 [`L30A_CStrings.md`](../theory/L30A_CStrings.md) | 💻 [`L30A_CStrings.cpp`](../code/L30A_CStrings.cpp) |
| **L30B** | `<string>` Library | 📘 [`L30B_StdString.md`](../theory/L30B_StdString.md) | 💻 [`L30B_StdString.cpp`](../code/L30B_StdString.cpp) |
| **L30C** | `<cctype>` Library | 📘 [`L30C_CCtype.md`](../theory/L30C_CCtype.md) | 💻 [`L30C_CCtype.cpp`](../code/L30C_CCtype.cpp) |
| **L30D** | String Applications | 📘 [`L30D_StringApplications.md`](../theory/L30D_StringApplications.md) | 💻 [`L30D_StringApplications.cpp`](../code/L30D_StringApplications.cpp) |

---

## 🎯 Practical Exercises (E01 – E12)

| # | Exercise | Topic | Code File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **E01** | Maximum of an array | Array Basics | 💻 [`E01_Maximum.cpp`](../exercise/E01_Maximum.cpp) | ✅ |
| **E02** | Average calculation | Array Basics | 💻 [`E02_Average.cpp`](../exercise/E02_Average.cpp) | ✅ |
| **E03** | Reverse array in-place | Array Basics | 💻 [`E03_ReverseArray.cpp`](../exercise/E03_ReverseArray.cpp) | ✅ |
| **E04** | Increment all | Arrays as parameters | 💻 [`E04_IncrementAll.cpp`](../exercise/E04_IncrementAll.cpp) | ✅ |
| **E05** | Linear search | Arrays as parameters | 💻 [`E05_LinearSearch.cpp`](../exercise/E05_LinearSearch.cpp) | ✅ |
| **E06** | Matrix sum | Multidimensional Arrays | 💻 [`E06_MatrixSum.cpp`](../exercise/E06_MatrixSum.cpp) | ✅ |
| **E07** | Transpose matrix | Multidimensional Arrays | 💻 [`E07_TransposeMatrix.cpp`](../exercise/E07_TransposeMatrix.cpp) | ✅ |
| **E08** | Custom `strlen` | C-Strings | 💻 [`E08_CustomStrlen.cpp`](../exercise/E08_CustomStrlen.cpp) | ✅ |
| **E09** | Custom safe `strcpy` | C-Strings | 💻 [`E09_SafeStrcpy.cpp`](../exercise/E09_SafeStrcpy.cpp) | ✅ |
| **E10** | Count vowels | C-Strings & `<cctype>` | 💻 [`E10_CountVowels.cpp`](../exercise/E10_CountVowels.cpp) | ✅ |
| **E11** | Reverse C-String in-place | C-Strings & `strlen` | 💻 [`E11_ReverseString.cpp`](../exercise/E11_ReverseString.cpp) | ✅ |
| **E12** | Convert to uppercase | C-Strings & `toupper` | 💻 [`E12_ToUppercase.cpp`](../exercise/E12_ToUppercase.cpp) | ✅ |

---

## 💡 Summary by Lesson

### L27 — Array Basics
- An array reserves a contiguous block of RAM memory to store multiple elements of the same type.
- Address calculation: $\text{address} = \text{start} + \text{index} \times \text{sizeof(type)}$.
- Indexing starts at `0`. Uninitialized local arrays contain garbage values.
- `sizeof(arr) / sizeof(arr[0])` calculates the number of elements only within the scope of array definition.

### L28 — Arrays as Parameters
- When an array is passed to a function, it decays into a raw pointer (*array decay*): `int arr[]` $\rightarrow$ `int*`.
- Modifying elements inside the function alters the original array in `main`.
- Use `const int arr[]` for read-only parameters. Always pass `size` as an explicit parameter.

### L29 — Multidimensional Arrays
- 2D arrays are stored in contiguous memory in **Row-Major Order** (row by row).
- Offset formula: $\text{flat index} = i \times \text{COLS} + j$.
- Column dimension must be explicitly specified in function signatures: `void func(int mat[][10], int rows)`.

### L30A — `<cstring>` Library
- A C-string is a `char` array ending with the null character sentinel **`'\0'`** (ASCII 0).
- Array capacity must be at least $\text{length} + 1$ bytes.
- `#include <cstring>` provides `strlen`, `strcpy`, `strcat`, `strcmp`, `strchr`.

### L30B — `<string>` Library
- `string` (from `#include <string>`) is an abstract object managing its dynamic memory automatically on the heap.
- Always pass strings as `const string&` to avoid $O(N)$ string copying overhead.
- Essential operations: `.length()`, `.empty()`, `.substr(pos, len)`, `.find(target, pos)`, `.rfind()`, `.insert()`, `.erase()`, `.replace()`.
- Access bounds: `str[i]` is fast and unchecked, while `str.at(i)` performs bounds checking and throws `out_of_range`.

### L30C — `<cctype>` Library
- `#include <cctype>` is an independent C++ standard header specifically for inspecting and classifying individual `char` elements.
- Functions include `isalpha`, `isdigit`, `isalnum`, `islower`, `isupper`, `isspace`, `ispunct`, `tolower`, `toupper`.
- Always use `static_cast<unsigned char>(ch)` for character safety.

### L30D — String Applications
- **Palindrome Complexity:**
  - Naïve recursive `substr(1, len-2)` creates heap string copies at every step $\rightarrow O(N^2)$ time & space!
  - Optimized Frontier Indices (or Two-Pointer `low`/`high`) operates in $O(N)$ time and $O(1)$ extra space.
- **Pig Latin Translation:** Checks vowel rules (`"apple"` $\rightarrow$ `"appleway"`) and splits consonant clusters (`"trash"` $\rightarrow$ `"ashtray"`).
- **Ciphers:** Caesar cipher rotates letters modulo 26 preserving case; Letter-substitution cipher maps alphabet bijectively.
- **Stanford `strlib` Helpers:** Functions like `startsWith`, `endsWith`, `trim`, and `split`.

---

## 🛡️ Best Practices and Key Patterns

1. **Implicit initialization:** Always initialize arrays to avoid reading garbage from RAM (`int arr[10] = {};`).
2. **Use of `const`:** Protect arrays and strings in function signatures when read-only (`const int arr[]`, `const string& str`).
3. **Passing dimensions:** Explicitly pass array dimensions along with raw C arrays.
4. **Respect the `'\0'`:** Ensure space for the null character when declaring C-strings ($\text{capacity} \ge \text{strlen} + 1$).
5. **Frontier Pointers ($O(N)$):** Use two indices (`low` and `high`) for string reversal and palindrome verification to avoid $O(N^2)$ substring copies.

---

*Section 04 completed at 100% — CS106B Chapter 3 alignment complete*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> � 2026</sub>
</div>