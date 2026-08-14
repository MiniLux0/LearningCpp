# Lesson 09 — Binary Numbers, Bits & Memory Bitwise Operators

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 01** ([`Lecture01_Introduction.pdf`](../../files/mit6096/lectures/Lecture01_Introduction.pdf)) and **Stanford CS106B Textbook Appendix A** ([`CS106BX-Reader.pdf`](../../files/cs106b/textbook/CS106BX-Reader.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 01: Bitwise Memory Representation](../../files/mit6096/lectures/Lecture01_Introduction.pdf)
  - 🌲 [Stanford CS106B — Appendix A: Representation of Data in Memory](../../files/cs106b/textbook/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`L09_BinaryNumbers.cpp`](../code/L09_BinaryNumbers.cpp)

---

## Learning Objectives

- [ ] Understand the binary base-2 positional numeral system ($2^0, 2^1, 2^2, 2^3 \dots$).
- [ ] Understand bit vs. byte memory units ($1\text{ byte} = 8\text{ bits}$).
- [ ] Master bitwise operators in C++ (`&`, `|`, `^`, `~`, `<<`, `>>`).
- [ ] Calculate bitmasking operations used in low-level graphics and hardware programming.

---

## 1. Bits, Bytes & Base-2 Representation

At the physical hardware layer, computer RAM consists of microscopic transistor capacitors that store electrical charges representing binary states: **HIGH (`1`)** or **LOW (`0`)**.

- **Bit (Binary Digit):** The fundamental unit of data ($0$ or $1$).
- **Byte:** A contiguous collection of 8 bits ($2^8 = 256$ distinct combinations, $0 \dots 255$).

### Positional Binary Evaluation:
To evaluate binary `00001011` to decimal:

| Bit Position | $2^7 (128)$ | $2^6 (64)$ | $2^5 (32)$ | $2^4 (16)$ | $2^3 (8)$ | $2^2 (4)$ | $2^1 (2)$ | $2^0 (1)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Bit Value** | 0 | 0 | 0 | 0 | **1** | 0 | **1** | **1** |

$$
\text{Decimal Value} = 8 + 2 + 1 = 11
$$

---

## 2. Bitwise Operators in C++

C++ provides native operators to manipulate individual bits within integer variables:

```mermaid
graph TD
    A["a = 12 (1100)"] --- B["b = 5 (0101)"]
    A & B --> AND["a & b = 4 (0100)"]
    A | B --> OR["a | b = 13 (1101)"]
    A ^ B --> XOR["a ^ b = 9 (1001)"]
```

| Operator | Operation | Description | Example ($a=12\text{ [1100]}$, $b=5\text{ [0101]}$) | Result |
| :---: | :--- | :--- | :--- | :---: |
| **`&`** | Bitwise AND | Bit is 1 if BOTH corresponding bits are 1. | `1100 & 0101` $\rightarrow$ `0100` | `4` |
| **`\|`** | Bitwise OR | Bit is 1 if AT LEAST ONE bit is 1. | `1100 \| 0101` $\rightarrow$ `1101` | `13` |
| **`^`** | Bitwise XOR | Bit is 1 if bits ARE DIFFERENT. | `1100 ^ 0101` $\rightarrow$ `1001` | `9` |
| **`~`** | Bitwise NOT | Inverts all bits (1 $\rightarrow$ 0, 0 $\rightarrow$ 1). | `~00001100` | `-13` |
| **`<<`** | Left Shift | Shifts bits left by $N$ places (multiplies by $2^N$). | `5 << 1` (`0101` $\rightarrow$ `1010`) | `10` |
| **`>>`** | Right Shift | Shifts bits right by $N$ places (divides by $2^N$). | `12 >> 2` (`1100` $\rightarrow$ `0011`) | `3` |

---

## ❓ Self-Assessment Checkpoint #1 — Fast Power of 2 Shift

What is the decimal result of computing `1 << 4` in C++?

<details>
<summary>🔍 <strong>View Explanation & Calculation</strong></summary>

> [!TIP]
> **Calculation:** `1 << 4` $= 1 \times 2^4 = 16$.
>
> **Explanation:**
> Left shifting bit `00000001` by 4 places produces `00010000` (binary for decimal $16$). In high-performance C++ code, bit-shifting left by $N$ is used as an ultra-fast hardware replacement for exponentiation $2^N$.

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
*MiniLux0 — Learning C++ Section 02*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>