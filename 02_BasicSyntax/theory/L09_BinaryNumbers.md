# Lesson 09 — Binary Numbers, Bits & Memory Layout

Have you ever wondered how computers store numbers, text, images, and videos inside silicon chips? Underneath everything, computers only understand **electricity**: ON (`1`) or OFF (`0`).

This base-2 system is called the **Binary System**.

---

## 💡 1. Bits vs Bytes

- **Bit** (Binary Digit): The smallest unit of data. Holds a `0` or `1`.
- **Byte**: A group of 8 bits. Example: `01000001` (8 bits = 1 byte).

### How Binary Numbers Work (Base-2):
In base 10 (decimal), positions represent powers of 10 ($1, 10, 100, 1000$).
In base 2 (binary), positions represent powers of 2 ($1, 2, 4, 8, 16, 32, 64, 128$).

Let's convert binary `00001011` to decimal:
- Pos 8 ($128$): 0
- Pos 7 ($64$): 0
- Pos 6 ($32$): 0
- Pos 5 ($16$): 0
- Pos 4 ($8$): **1**
- Pos 3 ($4$): 0
- Pos 2 ($2$): **1**
- Pos 1 ($1$): **1**

$$\text{Total} = 8 + 2 + 1 = 11$$

---

## ⚡ 2. Bitwise Operators in C++

C++ allows operating directly on bits using bitwise operators:

| Operator | Name | What it does | Example (`a = 12 [1100], b = 5 [0101]`) | Result |
|:--------:|------|--------------|------------------------------------------|:------:|
| `&` | Bitwise AND | Bit is 1 only if BOTH bits are 1 | `a & b` -> `0100` | `4` |
| `\|` | Bitwise OR | Bit is 1 if AT LEAST ONE bit is 1 | `a \| b` -> `1101` | `13` |
| `^` | Bitwise XOR | Bit is 1 if bits ARE DIFFERENT | `a ^ b` -> `1001` | `9` |
| `<<` | Left Shift | Shifts bits left (multiplies by 2) | `a << 1` | `24` |
| `>>` | Right Shift | Shifts bits right (divides by 2) | `a >> 1` | `6` |

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L08 — Advanced User Input**](L08_UserInput.md) | [**Basic Syntax**](../) | [**L10 — Integer Data Types**](L10_IntegerTypes.md) |
