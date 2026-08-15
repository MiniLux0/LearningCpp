# Lesson 11 — Floating-Point Types, IEEE 754 & Precision

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 01** ([`Lecture01_Introduction.pdf`](../../files/mit6096/lectures/Lecture01_Introduction.pdf)) and **Stanford CS106B Textbook Appendix A** ([`CS106BX-Reader.pdf`](../../files/cs106b/textbook/CS106BX-Reader.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 01: Floating-Point Allocation & IEEE 754](../../files/mit6096/lectures/Lecture01_Introduction.pdf)
  - 🌲 [Stanford CS106B — Appendix A: Representation of Real Numbers](../../files/cs106b/textbook/CS106BX-Reader.pdf)
- 💻 **Code Lab:** [`L11_FloatingPointTypes.cpp`](../code/L11_FloatingPointTypes.cpp)

---

## Learning Objectives

- [ ] Differentiate single-precision (`float`) vs. double-precision (`double`) types under the IEEE 754 standard.
- [ ] Control output stream formatting with `<iomanip>` (`fixed`, `setprecision()`).
- [ ] Understand why floating-point numbers incur binary representation rounding errors ($`0.1 + 0.2 \neq 0.3`$).

---

## 1. IEEE 754 Floating-Point Types (`float` vs. `double`)

Real numbers with fractional decimals are represented using floating-point scientific notation under the IEEE 754 binary standard:

```math
\text{Value} = (-1)^{\text{sign}} \times \text{mantissa} \times 2^{\text{exponent}}
```

| Data Type | Memory Size | Mantissa Bits | Decimal Precision | Standard Usage |
| :--- | :---: | :---: | :---: | :--- |
| **`float`** | 4 Bytes (32 bits) | 23 bits | $`\approx 7`$ significant digits | GPU graphics, games, embedded audio buffers. |
| **`double`** | 8 Bytes (64 bits) | 52 bits | $`\approx 15-17`$ significant digits | **Standard default** for engineering, math, and physics. |

```cpp
float  fVal = 3.14159265f; // 'f' suffix specifies float literal
double dVal = 3.141592653589793; // Default floating literal is double
```

---

## 2. Formatting Output Precision (`<iomanip>`)

By default, `cout` truncates floating-point output to 6 significant digits. Use `fixed` and `setprecision(N)` from `<iomanip>` for precise control:

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double pi = 3.141592653589793;

    cout << "Default cout : " << pi << "\n";
    cout << "Fixed 2 Decimals  : " << fixed << setprecision(2) << pi << "\n";
    cout << "Fixed 10 Decimals : " << fixed << setprecision(10) << pi << "\n";

    return 0;
}
```

> [!WARNING]
> **Binary Rounding Representation Errors:**
> Numbers like $`0.1`$ ($`1/10`$) cannot be represented exactly in binary powers of 2. In binary floating-point representation, $`0.1`$ is an infinitely repeating fraction:
> ```text
> 0.1 (decimal) = 0.00011001100110011... (binary)
> ```
> Consequently, computing `0.1 + 0.2` in `double` yields `0.30000000000000004`!

---

## ❓ Self-Assessment Checkpoint #1 — Literal Suffixes

What is the type of the literal `3.14` versus `3.14f` in C++?

<details>
<summary>🔍 <strong>View Explanation & Answer</strong></summary>

> [!NOTE]
> **Answer:** `3.14` is a `double` literal; `3.14f` is a `float` literal.
>
> **Explanation:**
> Writing `float x = 3.14;` without the `f` suffix causes the compiler to generate a `double` literal first, and then convert it to `float`, potentially triggering compiler warnings for precision truncation.

</details>

---

## 📝 Summary & Key Takeaways

1. **Default Type:** Always use `double` for general floating-point math.
2. **Formatting:** Use `#include <iomanip>` with `fixed` and `setprecision()`.
3. **Imprecision:** Binary floating-point cannot store fractions like $`1/10`$ with 100% exactness.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L10 — Integer Types & Limits**](L10_IntegerTypes.md) | [**🏠 Basic Syntax**](../README.md) | [**L12 — Char & Bool Types ➡️**](L12_CharAndBool.md) |

</div>


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>