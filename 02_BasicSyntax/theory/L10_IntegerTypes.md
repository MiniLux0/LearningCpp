# Lesson 10 — Integer Types, Memory Sizes & Overflow

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 01** ([`Lecture01_Introduction.pdf`](../../files/mit6096/lectures/Lecture01_Introduction.pdf)) and **Stanford CS106B Textbook Appendix A** ([`CS106BX-Reader.pdf`](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 01: Integer Types & Fixed Width Allocation](../../files/mit6096/lectures/Lecture01_Introduction.pdf)
  - 🌲 [Stanford CS106B — Appendix A: Representation of Integers & Limits](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`L10_IntegerTypes.cpp`](../code/L10_IntegerTypes.cpp)

---

## Learning Objectives

- [ ] Select appropriate integer types (`short`, `int`, `long long`) based on memory bounds.
- [ ] Understand signed vs. unsigned binary representation (Two's Complement).
- [ ] Inspect platform limits using `#include <climits>` (`INT_MAX`, `INT_MIN`, `LLONG_MAX`).
- [ ] Recognize and prevent **Integer Overflow** and Undefined Behavior.

---

## 1. Integer Data Types & Memory Bounds

| Data Type | Standard Memory | Minimum Value ( $2^{k-1}$ ) | Maximum Value ( $2^{k-1}-1$ ) | Typical Application |
| :--- | :---: | :---: | :---: | :--- |
| **`short`** | 2 Bytes (16 bits) | $-32,768$ | $+32,767$ | Memory-constrained embedded sensors. |
| **`int`** | 4 Bytes (32 bits) | $-2,147,483,648$ | $+2,147,483,647$ | Default choice for general loop counters and quantities. |
| **`long long`** | 8 Bytes (64 bits) | $\approx -9.22 \times 10^{18}$ | $\approx +9.22 \times 10^{18}$ | Financial balances, timestamps, planetary distances. |

> [!TIP]
> **Checking Machine Limits at Runtime:**
> You can query exact hardware size limits using `<climits>`:
> ```cpp
> #include <iostream>
> #include <climits>
> 
> cout << "Max int: " << INT_MAX << "\n"; // 2147483647
> ```

---

## 2. Signed vs. Unsigned Integers (Two's Complement)

By default, integers are **signed** (the most significant bit MSB acts as a negative sign flag in Two's Complement representation).

When a variable is declared `unsigned`, the sign bit is re-purposed as a magnitude bit, **doubling the positive maximum range**:

<div align="center">
  <img src="assets/l10_integer_types_manim.gif" alt="integer overflow and sign bit flipping">
  <p><em><strong>Integer Overflow:</strong> When you add 1 to the maximum positive limit, the binary carries over entirely to the MSB (Most Significant Bit). Since this bit represents the sign in Two's Complement, the value wraps around to the lowest possible negative number!</em></p>
</div>

```cpp
unsigned int score = 4000000000U; // Valid! Fits within 4.2 billion unsigned limit
```

---

## 3. Integer Overflow: The "Odometer" Effect

To understand **Overflow**, imagine the mechanical odometer of an old car that only has 4 digits. What happens when you reach `9999` kilometers and drive 1 more kilometer? 

The counter clicks over, it has no room for the `1`, and it **rolls all the way back to `0000`**.

Integers in computer memory do exactly the same thing because they have a fixed maximum size limit.

### Overflow in Unsigned Numbers (`unsigned`)
If you have an `unsigned short` with a maximum limit of `65535` and you add `1`, the counter simply wraps around to `0`.

### Overflow in Signed Numbers (`signed`)
Here, the infamous negative wrap-around occurs. C++ uses **Two's Complement** representation, where the most significant bit (MSB) acts as a sign indicator.

If you reach the maximum positive limit (e.g., `2,147,483,647` for a 32-bit `int`), all magnitude bits are set to `1`. When you add `1` more, the arithmetic carry propagates to the left, **accidentally flipping the sign bit to 1**.

As a result, your maximum positive number instantly turns into the most extreme negative number (`-2,147,483,648`)!

```cpp
int maxVal = INT_MAX; // 2,147,483,647 (The odometer is at its maximum)
maxVal = maxVal + 1;  // OVERFLOW! The sign bit flips: -2,147,483,648
```

> [!CAUTION]
> **Undefined Behavior (UB):**
> In C++, signed integer overflow is officially **Undefined Behavior (UB)** under the ISO C++ standard. Modern compilers with optimization enabled (`-O2` or `-O3`) can assume that signed overflow "never happens" and optimize away safety boundary checks in your code. Handle type limits carefully!

---

## ❓ Self-Assessment Checkpoint #1 — Overflow Behavior

If `short count = 32767;` and you execute `count++;`, what value will `count` contain on a standard 16-bit short system?

<details>
<summary>🔍 <strong>View Explanation & Answer</strong></summary>

> [!NOTE]
> **Result:** `-32768`.
>
> **Explanation:**
> `32767` in 16-bit binary is `0111 1111 1111 1111`. Adding `1` yields `1000 0000 0000 0000`, which represents `-32768` in Two's Complement signed representation.

</details>

---

## 📝 Summary & Key Takeaways

1. **Selection:** Use `int` for general calculations; use `long long` for values exceeding 2 billion.
2. **Unsigned:** Doubles positive range, but cannot store negative numbers.
3. **Overflow:** Exceeding type limits wraps around and causes undefined behavior in signed types.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L09 — Binary & Bit Layouts**](L09_BinaryNumbers.md) | [**🏠 Basic Syntax**](../README.md) | [**L11 — Floating-Point Types ➡️**](L11_FloatingPointTypes.md) |

</div>


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>