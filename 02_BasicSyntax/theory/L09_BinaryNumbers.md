# Lesson 09 — Binary Numbers, Bits & Memory Bitwise Operators

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 01** ([`Lecture01_Introduction.pdf`](../../files/mit6096/lectures/Lecture01_Introduction.pdf)) and **Stanford CS106B Textbook Appendix A** ([`CS106BX-Reader.pdf`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 01: Bitwise Memory Representation](../../files/mit6096/lectures/Lecture01_Introduction.pdf)
  - 🌲 [Stanford CS106B — Appendix A: Representation of Data in Memory](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`L09_BinaryNumbers.cpp`](../code/L09_BinaryNumbers.cpp)

---

## Learning Objectives

- [ ] Understand the binary base-2 positional numeral system ( $2^0, 2^1, 2^2, 2^3 \dots$ ).
- [ ] Understand bit vs. byte memory units ( $1\text{ byte} = 8\text{ bits}$ ).
- [ ] Master bitwise operators in C++ (`&`, `|`, `^`, `~`, `<<`, `>>`).
- [ ] Calculate bitmasking operations used in low-level graphics and hardware programming.

---

## 1. Bits, Bytes & Base-2 Representation

At the physical hardware layer, computer RAM consists of microscopic transistor capacitors that store electrical charges representing binary states: **HIGH (`1`)** or **LOW (`0`)**.

- **Bit (Binary Digit):** The fundamental unit of data ( $0$ or $1$ ).
- **Byte:** A contiguous collection of 8 bits ( $2^8 = 256$ distinct combinations, $0 \dots 255$ ).

### Positional Binary Evaluation:
To evaluate binary `00001011` to decimal:

| Bit Position | $2^7 (128)$ | $2^6 (64)$ | $2^5 (32)$ | $2^4 (16)$ | $2^3 (8)$ | $2^2 (4)$ | $2^1 (2)$ | $2^0 (1)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Bit Value** | 0 | 0 | 0 | 0 | **1** | 0 | **1** | **1** |

```math
\text{Decimal Value} = 8 + 2 + 1 = 11
```

---

## 2. Bitwise Operators in C++: The Column Rule

To understand bitwise operators (`&`, `|`, `^`), the key is to **compare the numbers vertically**, as if placing one number on top of the other in primary school addition.

<div align="center">
  <img src="assets/l09_binary_numbers_manim.gif" alt="bitwise AND vertical alignment">
  <p><em><strong>Vertical Alignment:</strong> Notice how Bitwise AND (<code>&amp;</code>) operates vertically column-by-column. A result bit is <code>1</code> only if both top and bottom bits in that exact column are <code>1</code>.</em></p>
</div>

Suppose we have $12$ and $5$ in binary:
```text
12 = 1100
 5 = 0101
```

Imagine the bits are four people in a line. The operators ask a question **in each column**:

### `&` — AND ("Are BOTH bits 1?")
Output is `1` only if **BOTH** corresponding bits are `1`.
```text
  1 1 0 0
& 0 1 0 1
  --------
  0 1 0 0   (Value: 4)
```

### `|` — OR ("Is AT LEAST ONE bit 1?")
If **at least one** bit is `1`, the result is `1`.
```text
  1 1 0 0
| 0 1 0 1
  --------
  1 1 0 1   (Value: 8 + 4 + 1 = 13)
```

### `^` — XOR ("Are the bits DIFFERENT?")
Outputs `1` **only if** the top bit is different from the bottom bit.
```text
  1 1 0 0
^ 0 1 0 1
  --------
  1 0 0 1   (Value: 8 + 1 = 9)
```

### `~` — NOT ("INVERT the bit")
This operator works on a single number. It simply **flips each bit to its opposite** (`0` $\rightarrow$ `1`, `1` $\rightarrow$ `0`).
```text
~ 00001100
  --------
  11110011  (Value: -13 in Two's Complement representation)
```

### `<<` and `>>` — Shifts (Bitwise Shifts)
These operators **shift** all bits in a specific direction. It is the binary equivalent of adding or removing zeros in base 10.

- **Left Shift (`<<`)**: Shifts to the LEFT (Multiplies by 2).
  ```cpp
  5 << 1 // Shifts 1 position to the left
  ```
  ```text
    0101 (5)
  <<   1
  --------
    1010 (10)
  ```
- **Right Shift (`>>`)**: Shifts to the RIGHT (Divides by 2).
  ```cpp
  12 >> 2 // Shifts 2 positions to the right
  ```
  ```text
    1100 (12)
  >>   2
  --------
    0011 (3)
  ```

> [!TIP]
> **Mental Summary:**
> - `&` $\rightarrow$ **Both**
> - `|` $\rightarrow$ **At least one**
> - `^` $\rightarrow$ **Different**
> Do not try to memorize massive tables; practice comparing 4-bit numbers column by column.


---

## ❓ Self-Assessment Checkpoint #1 — Fast Power of 2 Shift

What is the decimal result of computing `1 << 4` in C++?

<details>
<summary>🔍 <strong>View Explanation & Calculation</strong></summary>

> [!TIP]
> **Calculation:** `1 << 4` $= 1 \times 2^4 = 16$.
>
> **Explanation:**
> Left shifting bit `00000001` by 4 places produces `00010000` (binary for decimal $16$ ). In high-performance C++ code, bit-shifting left by $N$ is used as an ultra-fast hardware replacement for exponentiation $2^N$.

</details>

---

## 📝 Summary & Key Takeaways

1. **Binary:** Base-2 system powered by $2^k$ bit positions.
2. **Byte:** 8 bits forming the basic addressable unit of memory.
3. **Shift Operators:** `<< N` multiplies by $2^N$; `>> N` divides by $2^N$.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L08 — Advanced User Input**](L08_UserInput.md) | [**🏠 Basic Syntax**](../README.md) | [**L10 — Integer Data Types ➡️**](L10_IntegerTypes.md) |

</div>


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>