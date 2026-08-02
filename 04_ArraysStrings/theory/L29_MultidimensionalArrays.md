# Lesson 29 — Multidimensional Arrays: Matrices & Row-Major Layout

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **Stanford CS106B Textbook Chapter 11** ([`CS106BX-Reader.pdf`](../../files/cs106b/textbook/CS106BX-Reader.pdf)) and **MIT 6.096 Lecture 04** ([`Lecture04_Arrays.pdf`](../../files/mit6096/lectures/Lecture04_Arrays.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🌲 [Stanford CS106B — Chapter 11: Multidimensional Grid Allocation](../../files/cs106b/textbook/CS106BX-Reader.pdf)
  - 🏛️ [MIT 6.096 — Lecture 04: Row-Major Order Memory Layout](../../files/mit6096/lectures/Lecture04_Arrays.pdf)
- 💻 **Code Lab:** [`L29_MultidimensionalArrays.cpp`](../code/L29_MultidimensionalArrays.cpp)

---

## Learning Objectives

- [ ] Understand **Row-Major Order** mapping of 2D grids into 1D RAM memory.
- [ ] Calculate 2D-to-1D index offset formulas: $\text{flat index} = i \times \text{COLS} + j$.
- [ ] Traverse 2D matrices using nested `for` loops.
- [ ] Pass 2D arrays to functions (why column dimensions `COLS` are mandatory in parameters).

---

## 1. Row-Major Memory Mapping

Computer RAM hardware is strictly 1-dimensional. A 2D matrix `int matrix[2][3]` is stored as a 1D sequence of rows placed end-to-end:

```mermaid
graph LR
    SubGraph1["Row 0: matrix[0][0], matrix[0][1], matrix[0][2]"] --- SubGraph2["Row 1: matrix[1][0], matrix[1][1], matrix[1][2]"]
```

$$\text{Flat Index}(i, j) = i \times \text{COLS} + j$$

> [!IMPORTANT]
> **Why Column Bounds are Mandatory in Function Parameters:**
> To calculate element address `matrix[i][j]`, the compiler must know the exact number of columns `COLS` to skip past full rows. This is why functions taking 2D arrays MUST specify column dimensions in parameter definitions:
> ```cpp
> void printMatrix(int m[][3], int rows); // COLS (3) is MANDATORY!
> ```

---

## 2. Matrix Traversal & Initialization

```cpp
#include <iostream>

const int ROWS = 2;
const int COLS = 3;

void display(const int grid[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            std::cout << grid[i][j] << "\t";
        }
        std::cout << "\n";
    }
}

int main() {
    int matrix[ROWS][COLS]{
        {1, 2, 3}, // Row 0
        {4, 5, 6}  // Row 1
    };
    display(matrix);
    return 0;
}
```

---

## ❓ Self-Assessment Checkpoint #1 — Flat Offset Calculation

Given a matrix `int grid[4][5]`, what is the 1D flat memory index of element `grid[2][3]`?

<details>
<summary>🔍 <strong>View Explanation & Calculation</strong></summary>

> [!NOTE]
> **Calculation:** $\text{flat index} = (2 \times 5) + 3 = 13$.
>
> **Explanation:**
> Row $2$ skips past $2$ full rows of $5$ columns each ($10$ elements). Adding column index $3$ offsets $13$ positions from the array base address.

</details>

---

## 📝 Summary & Key Takeaways

1. **Row-Major Order:** Rows are laid out contiguously in 1D RAM memory.
2. **Indexing:** Computed as $i \times \text{COLS} + j$.
3. **Parameters:** Column bounds `COLS` must be specified in function parameter signatures.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L28 — Arrays as Parameters**](L28_ArraysAsParameters.md) | [**🏠 Arrays & Strings**](../README.md) | [**L30 — C-Strings ➡️**](L30_CStrings.md) |

</div>

---
*MiniLux0 — Learning C++ Section 04*
