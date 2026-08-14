# 🎯 Section 04: Practical Exercises & Solutions — Arrays & Strings

> **Module**: Section 04 (`04_ArraysStrings`)  
> 🎯 **Focus**: Practice on 1D/2D arrays, pointer decay, C-strings (`<cstring>`), character inspection (`<cctype>`), and `string`.

---

## 🧭 Exercise Inventory (E01 – E12)

| # | Exercise Name | Evaluated Concept | 💻 Code File | Status |
|---|---------------|-------------------|--------------|:------:|
| **E01** | **Maximum of an Array** | 1D array traversal & comparison | 💻 [`E01_Maximum.cpp`](E01_Maximum.cpp) | ✅ |
| **E02** | **Average Calculation** | 1D array accumulation & floating-point casting | 💻 [`E02_Average.cpp`](E02_Average.cpp) | ✅ |
| **E03** | **In-Place Array Reversal** | Frontier pointers (`low`/`high`) & element swap | 💻 [`E03_ReverseArray.cpp`](E03_ReverseArray.cpp) | ✅ |
| **E04** | **Increment All** | Array parameter modification in-place | 💻 [`E04_IncrementAll.cpp`](E04_IncrementAll.cpp) | ✅ |
| **E05** | **Linear Search** | Searching algorithm & index return | 💻 [`E05_LinearSearch.cpp`](E05_LinearSearch.cpp) | ✅ |
| **E06** | **2D Matrix Sum** | Row-Major nested loop matrix accumulation | 💻 [`E06_MatrixSum.cpp`](E06_MatrixSum.cpp) | ✅ |
| **E07** | **Transpose Square Matrix** | In-place `mat[i][j]` element swapping | 💻 [`E07_TransposeMatrix.cpp`](E07_TransposeMatrix.cpp) | ✅ |
| **E08** | **Reimplementing `strlen`** | Manual character count until `'\0'` sentinel | 💻 [`E08_CustomStrlen.cpp`](E08_CustomStrlen.cpp) | ✅ |
| **E09** | **Safe `miStrcpy` Copy** | Buffer overflow prevention in C-strings | 💻 [`E09_SafeStrcpy.cpp`](E09_SafeStrcpy.cpp) | ✅ |
| **E10** | **Count Vowels** | Character classification with `<cctype>` | 💻 [`E10_CountVowels.cpp`](E10_CountVowels.cpp) | ✅ |
| **E11** | **In-Place C-String Reversal** | Modifying C-style character arrays | 💻 [`E11_ReverseString.cpp`](E11_ReverseString.cpp) | ✅ |
| **E12** | **Convert to Uppercase** | Case transformation using `toupper()` | 💻 [`E12_ToUppercase.cpp`](E12_ToUppercase.cpp) | ✅ |

---

## 💡 Implementation Details per Exercise

### E01 — Maximum of an Array (`E01_Maximum.cpp`)
- **Signature:** `int maximo(const int arr[], int size);`
- **Technique:** Takes `arr[0]` as the initial reference value and iterates through the remaining elements.

### E02 — Average Calculation (`E02_Average.cpp`)
- **Signature:** `double promedio(const int arr[], int size);`
- **Technique:** Accumulates integer sum and performs explicit casting `static_cast<double>(sum) / size` to avoid integer division.

### E03 — In-Place Array Reversal (`E03_ReverseArray.cpp`)
- **Signature:** `void invertir(int arr[], int size);`
- **Technique:** Uses two frontier indices (`low = 0`, `high = size - 1`) and performs `swap(arr[low], arr[high])` until `low >= high`.

### E04 — Increment All (`E04_IncrementAll.cpp`)
- **Signature:** `void incrementarTodo(int arr[], int size, int delta);`
- **Technique:** Leverages array pointer decay to modify the original array memory in-place.

### E05 — Linear Search (`E05_LinearSearch.cpp`)
- **Signature:** `int buscar(const int arr[], int size, int target);`
- **Technique:** Returns the index of the first matching occurrence or `-1` if not found.

### E06 — 2D Matrix Sum (`E06_MatrixSum.cpp`)
- **Signature:** `int sumaMatriz(const int mat[][10], int rows, int cols);`
- **Technique:** Traverses in Row-Major order (outer loop `i` for rows, inner loop `j` for columns).

### E07 — Transpose Matrix (`E07_TransposeMatrix.cpp`)
- **Signature:** `void transponer(int mat[][10], int n);`
- **Technique:** Swaps `mat[i][j]` with `mat[j][i]` iterating only over the upper triangle (`j > i`).

### E08 — Reimplementing `strlen` (`E08_CustomStrlen.cpp`)
- **Signature:** `int miStrlen(const char s[]);`
- **Technique:** Counts characters in a `char[]` array until reaching the null sentinel `'\0'`.

### E09 — Safe `miStrcpy` Copy (`E09_SafeStrcpy.cpp`)
- **Signature:** `bool miStrcpy(char dest[], int destSize, const char src[]);`
- **Technique:** Checks if `strlen(src) + 1 <= destSize` before copying to prevent Buffer Overflows.

### E10 — Count Vowels (`E10_CountVowels.cpp`)
- **Signature:** `int contarVocales(const char s[]);`
- **Technique:** Uses `tolower()` from `<cctype>` to count both uppercase and lowercase vowels uniformly.

### E11 — In-Place C-String Reversal (`E11_ReverseString.cpp`)
- **Signature:** `void invertirString(char s[]);`
- **Technique:** Measures length with `strlen` and reverses characters in-place while keeping the final `'\0'` in its position.

### E12 — Convert to Uppercase (`E12_ToUppercase.cpp`)
- **Signature:** `void aMayusculas(char s[]);`
- **Technique:** Traverses the array and applies `s[i] = static_cast<char>(toupper(static_cast<unsigned char>(s[i])))`.

---


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>