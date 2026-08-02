<div align="center">

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L28: Arrays as Parameters**](L28_ArraysAsParameters.md) | [**Section 04: Arrays & Strings**](../README.md) | [**L30: C-Strings ➡️**](L30_CStrings.md) |

</div>

---

# L29 — Multidimensional Arrays: Matrices, Memory Layout and Functions

> **Core concept:** C++ does not have "real" matrices in hardware. A 2D array `int m[3][4]` is a **syntactic abstraction** stored as a **1D contiguous block in memory** following Row-Major Order.

---

## Learning Objectives

- [ ] Understand how 2D and 3D matrices are represented in RAM memory (Row-Major Order)
- [ ] Master the syntax of declaration, explicit, partial and zero initialization
- [ ] Apply the rule of mandatory dimensions in function parameters (`int m[][COLS]`)
- [ ] Dynamically calculate rows and columns using `sizeof`
- [ ] Manipulate 2D arrays of characters (arrays of C-style strings)

---

## 1. The core idea: Row-Major Order

A 2D matrix of `3 rows x 4 columns` (`int m[3][4]`) in C++ is not a physical grid. In RAM memory, the rows are placed **consecutively one after another**:

```
Conceptually (3x4 Grid):

        Col 0   Col 1   Col 2   Col 3
Row 0  [  1  ] [  2  ] [  3  ] [  4  ]
Row 1  [  5  ] [  6  ] [  7  ] [  8  ]
Row 2  [  9  ] [ 10  ] [ 11  ] [ 12  ]

In RAM Memory (Contiguous block of 12 ints = 48 bytes):
+----+----+----+----+----+----+----+----+----+----+----+----+
|  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 | 11 | 12 |
+----+----+----+----+----+----+----+----+----+----+----+----+
 <---- Row 0 ---->   <---- Row 1 ---->   <---- Row 2 ---->
```

### Address calculation by the compiler

To access `m[i][j]`, the compiler performs the offset addressing formula:

$$\text{Address}(m[i][j]) = \text{Base Address} + (i \times \text{COLS} + j) \times \text{sizeof(type)}$$

- `m[0][0]` → $(0 \times 4 + 0) = 0$
- `m[1][2]` → $(1 \times 4 + 2) = 6$ → offset position 6 (element `7`)
- **Conclusion:** `int m[2][4]` and `int m[8]` occupy exactly the same bytes in memory.

---

## 2. Declaration and Initialization

### A. Direct assignment by indices
```cpp
int m[2][3];
m[0][0] = 1; m[0][1] = 2; m[0][2] = 3;
m[1][0] = 4; m[1][1] = 5; m[1][2] = 6;
```

### B. Initialization with nested braces (Recommended for clarity)
```cpp
int m[3][4] = {
    {1, 2, 3, 4},   // Row 0
    {5, 6, 7, 8},   // Row 1
    {9, 10, 11, 12} // Row 2
};
```

### C. Flattened initialization (Takes advantage of row-major order)
```cpp
int m[2][4] = {6, 0, 9, 6, 2, 0, 1, 1};
// Row 0: 6, 0, 9, 6
// Row 1: 2, 0, 1, 1
```

### D. Partial initialization (Implicit zeros)
If you do not specify all the elements, the missing ones are automatically filled with `0`:
```cpp
int partial[2][3] = {{1, 2}, {3}};
// Results in:
// {1, 2, 0}
// {3, 0, 0}

int zeros[3][4] = {0}; // Fills all 12 elements with 0 (also equivalent to = {})
```

### E. Precaution: Uninitialized variables (Garbage values vs. Zeros)

> ⚠️ **Attention!** Declaring `int matrix[2][2];` inside a function (like `main()`) **does NOT guarantee that its elements are `0`**.
>
> - **Inside a function (Local):** `int m[2][2];` contains **garbage values** from RAM memory. You must use `= {}` or `= {0}` to initialize it to zeros.
> - **Outside functions (Global) or with `static`:** C++ guarantees automatic zero initialization (*zero-initialization*).

---

## 3. Rule of Dimensions: Why is the second dimension MANDATORY?

When declaring and initializing in a single step, the **first dimension (rows)** can be omitted and the compiler deduces it:

```cpp
int m[][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}}; // Correct: deduces 2 rows
```

However, the **secondary dimensions (columns) can NEVER be omitted**:
```cpp
// int m[2][] = {{1, 2}, {3, 4}}; // ❌ COMPILATION ERROR
```

> **Why?** To calculate `m[i][j]`, the formula requires knowing $\text{COLS}$ ($i \times \text{COLS} + j$). Without the number of columns, the compiler does not know how many elements to skip to advance to the next row.

---

## 4. Passing Multidimensional Arrays to Functions

Due to pointer decay, when passing a matrix to a function, the **first dimension is optional**, but **all other dimensions must be fixed**:

```cpp
// Function definition (COLS = 4 mandatory)
void print2D(const int m[][4], int rows) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < 4; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}

// Call in main:
int matrix[3][4] = {...};
print2D(matrix, 3);
```

---

## 5. Calculation of Rows and Columns with `sizeof`

When the matrix is in the same scope as its declaration:

```cpp
int matrix[3][4];

int totalBytes = sizeof(matrix);        // 3 * 4 * 4 = 48 bytes
int rowBytes   = sizeof(matrix[0]);     // 4 * 4 = 16 bytes
int elemBytes  = sizeof(matrix[0][0]);  // 4 bytes

int rows = sizeof(matrix) / sizeof(matrix[0]);       // 48 / 16 = 3
int cols = sizeof(matrix[0]) / sizeof(matrix[0][0]); // 16 / 4  = 4
```

---

## 6. Three-Dimensional Arrays (3D)

A 3D array can be visualized as a volume (layers $\times$ rows $\times$ columns):

```cpp
int cube[2][3][4] = {0}; // 2 matrices of 3x4 (total 24 integers)
cube[1][2][3] = 99;      // Layer 1, Row 2, Column 3

// Triple nested traversal:
for (int c = 0; c < 2; c++) {
    for (int r = 0; r < 3; r++) {
        for (int col = 0; col < 4; col++) {
            // process cube[c][r][col]
        }
    }
}
```

---

## 7. Arrays of C-Strings (2D `char` Matrix)

A matrix `char names[ROWS][LENGTH]` behaves as a list of C-style text strings:

```cpp
char names[3][20] = {"Ana", "Carlos", "Beatriz"};

// names[0] is a C-string "Ana\0"
// names[1] is "Carlos\0"
// names[2] is "Beatriz\0"

for (int i = 0; i < 3; i++) {
    cout << "Person " << i + 1 << ": " << names[i] << endl;
}
```

---

## 8. Checkpoint Questions

<details>
<summary><strong>1. Why are <code>int arr[2][4]</code> and <code>int arr[8]</code> identical in RAM memory?</strong></summary>

Because both reserve 8 consecutive integers in memory (32 bytes). The 2D notation `[2][4]` is just an abstraction that uses the formula `i * 4 + j` to access the indices.
</details>

<details>
<summary><strong>2. Why does the signature <code>void f(int m[][])</code> cause a compilation error?</strong></summary>

Because without specifying the number of columns (`COLS`), the function cannot calculate the jump between rows `i * COLS + j`. The first dimension can be omitted, but the columns must be fixed.
</details>

<details>
<summary><strong>3. If I declare <code>int m[2][2];</code> inside <code>main()</code>, are all its elements 0?</strong></summary>

No. Being a local variable without an explicit initializer, its elements will contain **garbage values** from RAM memory. To force them all to zero you must write `int m[2][2] = {};`.
</details>

---

## 9. Proposed Exercise

> **Transpose of a square matrix in-place (3x3):**
> Write a function `void transpose(int m[3][3])` that swaps `m[i][j]` with `m[j][i]` for all $i < j$.

```cpp
void transpose(int m[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            int temp = m[i][j];
            m[i][j] = m[j][i];
            m[j][i] = temp;
        }
    }
}
```

---

## Related files

- [`L29_MultidimensionalArrays.cpp`](../code/L29_MultidimensionalArrays.cpp) — Demonstration of 2D, 3D matrices, functions and arrays of strings

## Navigation

| ← Previous | Next → |
|------------|--------|
| [L28 — Arrays as Parameters](L28_ArraysAsParameters.md) | [L30 — C-Strings](L30_CStrings.md) |
