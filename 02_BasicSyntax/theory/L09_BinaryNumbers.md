# Lesson 09 — Binary Numbers, Bits & Memory Layout

Computers process and store all data in **binary** (base-2), using combinations of `0` and `1`.

---

## 🔢 1. Bits vs Bytes

- **Bit**: A single memory cell containing `0` or `1`.
- **Byte**: A group of 8 bits.

### Base-2 Conversion Example:
Binary `1011` in decimal:
$$1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 = 8 + 0 + 2 + 1 = 11$$

---

## ⚙️ 2. Bitwise Operators in C++

- `&` (AND): Returns 1 if both bits are 1.
- `|` (OR): Returns 1 if at least one bit is 1.
- `^` (XOR): Returns 1 if bits are different.
- `<<` (Shift Left): Shifts bits left (multiplies by 2).
- `>>` (Shift Right): Shifts bits right (divides by 2).
