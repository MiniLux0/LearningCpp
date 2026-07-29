# Lesson 10 — Integer Data Types & Range Limits

C++ provides multiple integer types to balance memory consumption and numeric range.

---

## 📊 Integer Types Comparison

| Type | Typical Size | Minimum Value | Maximum Value |
|------|--------------|---------------|---------------|
| `short` | 2 Bytes (16 bits) | -32,768 | 32,767 |
| `int` | 4 Bytes (32 bits) | -2,147,483,648 | 2,147,483,647 |
| `long long` | 8 Bytes (64 bits) | $\approx -9 \times 10^{18}$ | $\approx 9 \times 10^{18}$ |

### Unsigned Integers:
Adding `unsigned` eliminates negative numbers, doubling the positive range (e.g., `unsigned int` ranges from `0` to `4,294,967,295`).

### Integer Overflow:
Exceeding the maximum limit wraps around to negative values (Two's Complement overflow behavior).

---

### 🧭 Navigation & Progression
| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L09 — Binary & Memory Layout**](L09_BinaryNumbers.md) | [**Basic Syntax**](../) | [**L11 — Floating-Point Types**](L11_FloatingPointTypes.md) |

