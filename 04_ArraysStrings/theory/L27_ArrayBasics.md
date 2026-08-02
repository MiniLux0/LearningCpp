# L27: Array Basics — Declaration, Initialization, and Index Access

## 1. The core idea: contiguous memory

A normal variable (`int x;`) reserves **one space** for **one value**.

An **array** (`int arr[4];`) reserves **a contiguous block** of memory for **multiple values of the same type**, all placed one after another.

```
memory:  [house 2000] [house 2001] [house 2002] [house 2003]  ← 4 bytes = 1 int
         [house 2004] [house 2005] [house 2006] [house 2007]  ← 2nd int
         [house 2008] [house 2009] [house 2010] [house 2011]  ← 3rd int
         [house 2012] [house 2013] [house 2014] [house 2015]  ← 4th int
         ↑ start address (arr[0])
```

**The index does not "search" — it calculates an address:**
```
arr_address[i] = start_address + i × sizeof(type)
```

- `arr[0]` → offset 0 → start_address
- `arr[1]` → offset 1 × 4 = 4 bytes → start_address + 4
- `arr[2]` → offset 2 × 4 = 8 bytes → start_address + 8

That is why the first index is **0**: you don't move, you are already at the beginning.

---

## 2. Three ways to initialize

### Way 1: Declare and assign later
```cpp
int arr[4];
arr[0] = 6;
arr[1] = 0;
arr[2] = 9;
arr[3] = 6;
```

### Way 2: Initialize in the declaration (explicit size)
```cpp
int arr[4] = {6, 0, 9, 6};
```

### Way 3: Size inferred by the compiler
```cpp
int arr[] = {6, 0, 9, 6, 2, 0, 1, 1};  // size = 8
```
The compiler **counts the elements** and sets the dimension. Advantage: there is no risk of the size and the value list getting out of sync.

---

## 3. Partial initialization → the rest are zeros

```cpp
int arr[5] = {1, 2};  // arr = {1, 2, 0, 0, 0}
int zeros[10] = {0};  // all zeros
```

Rule: **unspecified elements are initialized to 0** (value-initialization).

---

## 4. Index access

```cpp
int data[5] = {10, 20, 30, 40, 50};

cout << data[0];   // 10
cout << data[4];   // 50

int i = 2;
cout << data[i];        // 30  (variable as index)
cout << data[i + 1];    // 40  (expression as index)
```

**Valid range:** `0` to `n-1` (where `n` = dimension).
- `data[5]` → **undefined behavior** (reads/writes outside the block)
- There is no guaranteed compilation or execution error — it corrupts memory silently.

---

## 5. Array size at runtime

```cpp
int arr[5] = {10, 20, 30, 40, 50};
int n = sizeof(arr) / sizeof(arr[0]);  // 5 (C++98 compatible)

// C++17: std::size (requires <iterator>)
#include <iterator>
int n17 = std::size(arr);  // 5 — clearer, works with any container
```

> **Watch out:** `sizeof(arr) / sizeof(arr[0])` only works in the **scope where the array was declared**. If you pass the array to a function, it "decays" to a pointer and `sizeof` returns the size of the pointer (8 bytes on 64 bits), not the array. `std::size` has the same limitation.

---

## 6. Typical traversal

```cpp
// classic for with index
for (int i = 0; i < n; i++) {
    cout << arr[i] << ' ';
}

// range-based for (C++11) — read-only or modification by reference
for (int x : arr) {
    cout << x << ' ';
}

for (int &x : arr) {
    x *= 2;  // modifies the original
}

// C++17: structured bindings do not apply to native arrays directly
// but std::array does support them
```

---

## 7. Checkpoint question

> **If you write `int data[5];` without initializing and then do `cout << data[2];` — what does it print?**

**Answer:** **Garbage (indeterminate value)**.
- The declaration reserves the contiguous block, but **does not clean it**.
- Those bytes contain whatever was in that memory before.
- It is not 0, it is not an error — it is "whatever happens to be there".

---

## 8. Proposed exercise

> **Write a program that:**
>
> - Declares an integer array of size 6 (use a constant or variable for the size, don't repeat it as a magic number in the loop — this is where I watch for your "fixed numbers" pattern)
> - Asks the user for the 6 values one by one with `cin`
> - Prints them all again, separated by space

```cpp
#include <iostream>
using namespace std;

int main() {
    const int SIZE = 6;           // constant for the size — without hardcoding 6 in the loop
    int values[SIZE];

    for (int i = 0; i < SIZE; i++) {
        cout << "value[" << i << "]: ";
        cin >> values[i];
    }

    cout << "\nRead values: ";
    for (int i = 0; i < SIZE; i++) {
        cout << values[i] << ' ';
    }
    cout << endl;
    return 0;
}
```

> **C++17 Note:** In modern code, for sizes decided at runtime, `std::vector<int>` (header `<vector>`) is preferred. It manages memory automatically and knows its size with `.size()`. Native fixed-size arrays are for when the dimension is known at compile time.

---

## Related files

- [`L27_ArrayBasics.cpp`](../code/L27_ArrayBasics.cpp) — Executable code with array declaration, initialization, and traversal

### 🧭 Navigation & Progression
| ⬅️ Previous Module | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L26 — Headers & Prototypes**](../../03_Subroutines/theory/L26_HeadersAndPrototypes.md) | [**Arrays & Strings**](../) | [**L28 — Arrays as Parameters**](L28_ArraysAsParameters.md) |