# Lesson 06 — Variables, Primitive Types & Initialization

> [!NOTE]
> **Academic Foundation:** This lesson synthesizes core concepts from **MIT 6.096 Lecture 02** ([`Lecture02_FlowOfControl.pdf`](../../files/mit6096/lectures/Lecture02_FlowOfControl.pdf)) and **Stanford CS106L Lecture 02** ([`WL2-Structures.pdf`](../../files/cs106l/lectures/WL2-Structures.pdf)).

---

## 🧭 Quick Navigation

- 📄 **Base Academic Lectures:**
  - 🏛️ [MIT 6.096 — Lecture 02: Primitive Data Types & Allocation](../../files/mit6096/lectures/Lecture02_FlowOfControl.pdf)
  - ⚙️ [Stanford CS106L — Lecture 02: Uniform Brace Initialization `{}`](../../files/cs106l/lectures/WL2-Structures.pdf)
- 💻 **Code Lab:** [`l06_variables.cpp`](../code/l06_variables.cpp)

---

## Learning Objectives

- [ ] Understand how C++ allocates memory cells in RAM for primitive data types.
- [ ] Differentiate between C-style assignment (`=`), direct initialization `()`, and **Modern Uniform Brace Initialization `{}`** (C++11).
- [ ] Identify illegal variable identifier names and reserved keyword collisions.
- [ ] Prevent uninitialized variable bugs and Undefined Behavior (UB).

---

## 1. Variables & RAM Memory Allocation

In C++, a **variable** is a named, typed memory location reserved in RAM.

![l06_variables](assets/l06_variables.svg)

> [!TIP]
> **The Type Contract:**
> Before using any variable, C++ requires specifying its **data type**. The type dictates:
> 1. Exactly how many **bytes of RAM** to reserve (e.g., `int` = 4 bytes, `double` = 8 bytes).
> 2. How the binary bit pattern is interpreted by CPU instructions.

---

## 2. Modern Initialization Styles in C++

C++ supports three distinct initialization syntaxes:

```cpp
// 1. C-style Assignment (Legacy)
int a = 10;

// 2. Direct Constructor-Style (C++98)
int b(20);

// 3. Modern Uniform Brace Initialization (C++11 — Best Practice)
int c{30};
```

> [!IMPORTANT]
> **Why Uniform Brace Initialization `{}` is Superior:**
> Brace initialization `{}` prevents **Narrowing Conversions** at compile time.
> ```cpp
> double pi = 3.14159;
> int x = pi;   // Compiles silently! Truncates 3.14159 to 3 (data loss).
> int y{pi};  // COMPILER ERROR! Disallows narrowing conversion double -> int.
> ```

---

## 3. The Danger of Uninitialized Variables

> [!CAUTION]
> **Garbage Value Trap:**
> Declaring a local variable without an explicit initial value (`int count;`) leaves whatever random binary junk was previously stored at that RAM address intact. Reading from an uninitialized local variable results in **Undefined Behavior (UB)**.

---

## ❓ Self-Assessment Checkpoint #1 — Narrowing Conversions

Predict the compiler's response to the following line in modern C++17:

```cpp
int temperature{72.8};
```

<details>
<summary>🔍 <strong>View Explanation & Answer</strong></summary>

> [!NOTE]
> **Result:** **Compile-Time Error**.
>
> **Explanation:**
> Because brace initialization `{}` is used, the C++ compiler strictly forbids narrowing conversions from floating-point (`double`) to integer (`int`). To compile, you must either explicitly cast (`static_cast<int>(72.8)`) or use `double temperature{72.8};`.

</details>

---

## 📝 Summary & Key Takeaways

1. **Variables:** Named memory locations reserved in RAM.
2. **Type Contract:** Specifies byte size and CPU interpretation.
3. **Modern Practice:** Prefer `{}` uniform brace initialization to eliminate narrowing conversions.
4. **Safety:** Always initialize variables immediately upon declaration.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ Section 01 Capstone**](../../01_GettingStarted/theory/L05_InteractiveProfileApp.md) | [**🏠 Basic Syntax**](../README.md) | [**L07 — Strings & Text ➡️**](l07_strings.md) |

</div>


---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>