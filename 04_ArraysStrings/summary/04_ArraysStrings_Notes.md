# 📝 Section 04: Arrays & Strings — Study Summary and Notes

Study notes and executive summary of **Section 04: Arrays and C-Strings** from the C++ course.
It covers contiguous memory representation of 1D/2D arrays, decay to pointers when passed to functions (*array decay*), correctness with `const`, indexing of multidimensional matrices, and handling of C-strings (null-terminated `char[]` with `'\0'`) using `<cstring>` and `<cctype>`.

---

## 🧭 Table of Contents

1. [Lessons and Theory](#-lessons-and-theory)
2. [Practical Exercises (E01 – E12)](#-practical-exercises-e01--e12)
3. [Summary by Lesson](#-summary-by-lesson)
   - [L27 — Array Basics](#l27--array-basics)
   - [L28 — Arrays as Parameters](#l28--arrays-as-parameters)
   - [L29 — Multidimensional Arrays](#l29--multidimensional-arrays)
   - [L30 — C-Strings](#l30--c-strings)
4. [Best Practices and Key Patterns](#-best-practices-and-key-patterns)

---

## 📘 Lessons and Theory

| Lesson | Title | Theory Note | Code Lab |
| :--- | :--- | :--- | :--- |
| **L27** | Array Basics | 📘 [`L27_ArrayBasics.md`](../theory/L27_ArrayBasics.md) | 💻 [`L27_ArrayBasics.cpp`](../code/L27_ArrayBasics.cpp) |
| **L28** | Arrays as Parameters | 📘 [`L28_ArraysAsParameters.md`](../theory/L28_ArraysAsParameters.md) | 💻 [`L28_ArraysAsParameters.cpp`](../code/L28_ArraysAsParameters.cpp) |
| **L29** | Multidimensional Arrays | 📘 [`L29_MultidimensionalArrays.md`](../theory/L29_MultidimensionalArrays.md) | 💻 [`L29_MultidimensionalArrays.cpp`](../code/L29_MultidimensionalArrays.cpp) |
| **L30** | C-Strings | 📘 [`L30_CStrings.md`](../theory/L30_CStrings.md) | 💻 [`L30_CStrings.cpp`](../code/L30_CStrings.cpp) |

---

## 🎯 Practical Exercises (E01 – E12)

| # | Exercise | Topic | Code File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **E01** | Maximum of an array | Array Basics | 💻 [`E01_Maximo.cpp`](../exercise/E01_Maximo.cpp) | ✅ |
| **E02** | Average | Array Basics | 💻 [`E02_Promedio.cpp`](../exercise/E02_Promedio.cpp) | ✅ |
| **E03** | Reverse array in-place | Array Basics | 💻 [`E03_InvertirArreglo.cpp`](../exercise/E03_InvertirArreglo.cpp) | ✅ |
| **E04** | Increment all | Arrays as parameters | 💻 [`E04_IncrementarTodo.cpp`](../exercise/E04_IncrementarTodo.cpp) | ✅ |
| **E05** | Linear search | Arrays as parameters | 💻 [`E05_BusquedaLineal.cpp`](../exercise/E05_BusquedaLineal.cpp) | ✅ |
| **E06** | Matrix sum | Multidimensional Arrays | 💻 [`E06_SumaMatriz.cpp`](../exercise/E06_SumaMatriz.cpp) | ✅ |
| **E07** | Transpose matrix | Multidimensional Arrays | 💻 [`E07_TransponerMatriz.cpp`](../exercise/E07_TransponerMatriz.cpp) | ✅ |
| **E08** | Custom `strlen` | C-Strings | 💻 [`E08_MiStrlen.cpp`](../exercise/E08_MiStrlen.cpp) | ✅ |
| **E09** | Custom safe `strcpy` | C-Strings | 💻 [`E09_MiStrcpySeguro.cpp`](../exercise/E09_MiStrcpySeguro.cpp) | ✅ |
| **E10** | Count vowels | C-Strings & `<cctype>` | 💻 [`E10_ContarVocales.cpp`](../exercise/E10_ContarVocales.cpp) | ✅ |
| **E11** | Reverse C-String in-place | C-Strings & `strlen` | 💻 [`E11_InvertirString.cpp`](../exercise/E11_InvertirString.cpp) | ✅ |
| **E12** | Convert to uppercase | C-Strings & `toupper` | 💻 [`E12_AMayusculas.cpp`](../exercise/E12_AMayusculas.cpp) | ✅ |

---

## 💡 Summary by Lesson

### L27 — Array Basics
- An array reserves a contiguous block of RAM memory to store multiple elements of the same type.
- The memory address is calculated as: $\text{address} = \text{start} + \text{index} \times \text{sizeof(type)}$.
- Indexing starts at `0` (`arr[0]` points directly to the start without offset).
- Uninitialized local arrays contain garbage values; partial initialization (`int arr[5] = {1, 2};`) fills the remaining elements with zeros.
- `sizeof(arr) / sizeof(arr[0])` calculates the number of elements **only within the declaration scope**.

### L28 — Arrays as Parameters
- When an array is passed to a function, it decays into a pointer (*array decay*): only the starting memory address is copied.
- Since it is passed by address, any modification within the function alters the original array in `main`.
- Using `const int arr[]` prevents accidental modifications in read-only functions.
- **It is mandatory to pass the size of the array as a separate parameter**, as the function cannot independently calculate the array's length.

### L29 — Multidimensional Arrays
- 2D arrays are stored in contiguous memory in **Row-Major Order** (row by row).
- Offset formula: $\text{flat\_index} = i \times \text{COLS} + j$.
- When declaring function parameters with multidimensional arrays, it is **mandatory** to specify the secondary dimensions (columns), for example: `void function(int mat[][10], int rows)`.

### L30 — C-Strings
- A C-string is an array of `char` whose useful content must end with the null character **`'\0'`** (ASCII 0).
- The array's capacity must be at least $\text{useful length} + 1$ to include the null terminator `'\0'`.
- The `<cstring>` library includes utilities like `strlen`, `strcpy`, `strcat`, `strcmp`, and `strchr`.
- The `<cctype>` library offers functions to classify and convert characters such as `isalpha`, `isdigit`, `tolower`, `toupper`.
- **Performance:** Avoid calling `strlen(s)` in the loop condition (`i < strlen(s)`). It is better to store the length beforehand in a variable (`int len = strlen(s);`) or use the traversal pattern `s[i] != '\0'`.
- **Basic vs advanced form in `<cctype>`:** For beginners, `s[i] = toupper(s[i]);` is enough. In production code, `static_cast<unsigned char>` is used to prevent undefined behaviors with special characters outside of ASCII.

---

## 🛡️ Best Practices and Key Patterns

1. **Implicit initialization:** Always initialize arrays to avoid reading garbage from RAM.
2. **Use of `const`:** Protect arrays in function signatures when they shouldn't be modified (`const int arr[]`).
3. **Passing dimensions:** Explicitly pass the array `size` along with one-dimensional arrays.
4. **Respect the `'\0'`:** Ensure space for the null character when declaring and manipulating C-strings.
5. **Two pointers (Ends to center):** Use two indices `i = 0` and `j = len - 1` with the condition `i < j` for reversal and palindrome inspection algorithms in $O(n)$.

---

*Last update: Section 04 completed at 100%*
