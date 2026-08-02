<div align="center">

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L27: Array Basics**](L27_ArrayBasics.md) | [**Section 04: Arrays & Strings**](../README.md) | [**L29: Multidimensional Arrays ➡️**](L29_MultidimensionalArrays.md) |

</div>

---

# L28 — Arrays as Parameters: Pass by Address and `const`

> **Core concept:** When you pass an array to a function, the elements are not copied — only the **start address** is copied. The function accesses the **same memory** as `main()`. That is why you do not need `&` as with normal variables.

## Learning Objectives

- [ ] Understand why arrays are passed "by address" automatically
- [ ] Contrast with pass by value of a normal `int` (Lesson 3)
- [ ] Use `const` to protect an array from accidental writing
- [ ] Read the compact `for` loop with `i++` in the index (post-increment)
- [ ] Write a function that modifies an array in-place (without `const`)

---

## 1. The array name is the start address

When you declare `int arr[] = {1, 2, 3, 4, 5, 6, 7};`, the name `arr` is not "the 7 values" — it is the **address** of the first house in memory:

```
arr → start address (e.g. house 2000)
       [1] [2] [3] [4] [5] [6] [7]
        ↑
   arr points here
```

When you call `sum(arr, 7)`:
- The 7 elements are **not** copied one by one
- **Only that address** is copied — a single number (4 or 8 bytes)
- The function receives that address and "walks" through the **same houses** as `main()`

---

## 2. Contrast with normal `int` (without `&`)

This is what makes arrays special compared to what we saw in L29 (Pass by Value):

```cpp
// Normal variable — the value is COPIED
void attemptToModify(int x) {
    x = 999;  // only modifies the local copy
}

int main() {
    int myVariable = 42;
    attemptToModify(myVariable);
    // myVariable is still 42 — the value was copied
    // They are two different memory houses
}
```

| What is passed | What is copied? | Does it modify the original? |
|----------------|-----------------|------------------------------|
| `int x` (without `&`) | The full **value** | ❌ No — they are two distinct houses |
| `int arr[]` | Only the **address** | ✅ Yes — same memory house |
| `int &x` (with `&`) | **Alias** (reference) | ✅ Yes — as we saw in L29 |

> **Important:** With arrays there is no copy of content, only copy of the **address**. That is why it behaves "as if" it were pass by reference, without needing `&`.

---

## 3. `const` — "read only, do not modify"

Since the array is passed by address, **without `const` the function could modify your original array** without you noticing. `const` is a safeguard:

```cpp
int sum(const int array[], const int length) {
    // array[0] = 999;  ← ❌ Compilation ERROR: array is const
    long sum = 0;
    for (int i = 0; i < length; i++) {
        sum += array[i];
    }
    return sum;
}
```

- ✅ `const int array[]` = promise to the compiler: **"this function can only read, not write"**
- ❌ If you try to break the promise → **compilation error** — it protects you
- Without `const`, doing `array[0] = 999;` inside `sum()` **would** modify `arr` in `main()`

---

## 4. The compact `for` with `i++` in the index

In the reading, `sum` uses a compact style that compresses everything into one line:

```cpp
for(int i = 0; i < length; sum += array[i++]);
```

Breakdown:
```
for (initialization;  condition;      update)                 body;
     int i = 0;       i < length;     sum += array[i++]      ;  ← EMPTY
```

**The body of the loop is the empty `;`.** All the work happens in the "update".

### `i++` (post-increment) inside `array[i++]`

It does **two things** in one step:
1. **Uses** the current value of `i` to read → `array[i]`
2. **Afterwards**, increments `i` by 1

It is equivalent to:
```cpp
sum += array[i];  // uses i as it is
i++;              // then increments i
```

### Step-by-step traversal with `{1, 2, 3, 4, 5, 6, 7}`

| Turn | `i` on entry | `array[i]` | `sum` after | `i` on exit |
|------|--------------|------------|-------------|-------------|
| 1    | 0            | 1          | 0 + 1 = 1   | 1           |
| 2    | 1            | 2          | 1 + 2 = 3   | 2           |
| 3    | 2            | 3          | 3 + 3 = 6   | 3           |
| 4    | 3            | 4          | 6 + 4 = 10  | 4           |
| 5    | 4            | 5          | 10 + 5 = 15 | 5           |
| 6    | 5            | 6          | 15 + 6 = 21 | 6           |
| 7    | 6            | 7          | 21 + 7 = 28 | 7           |
| —    | 7            | —          | — (exits)   | —           |

`i` reaches 7 (`length`) → false condition → loop ends → `return 28`.

> **Note:** The compact style is valid but hard to read. In readable code it is written like this:
> ```cpp
> for (int i = 0; i < length; i++) {
>     sum += array[i];
> }
> ```

---

## 5. Checkpoint question

<details>
<summary><strong>If you remove the <code>const</code> from <code>array[]</code> in <code>sum</code>, and inside you do <code>array[0] = 999;</code>, what happens to <code>arr</code> in <code>main()</code>?</strong></summary>

The first element of `arr` in `main()` **is modified to 999**. The function is writing directly to the same memory that `main()` uses, because the array was passed by address — it is not a copy.

</details>

<details>
<summary><strong>And why is it different from an <code>int</code> passed without <code>&</code>?</strong></summary>

With `void func(int x) { x = 999; }` the **value is copied** to `x` — they are two distinct houses. Modifying `x` does not touch the original variable. With arrays there is no copy of content, only copy of the **address** — that is why the original is modified without needing `&`.

</details>

---

## 6. Exercise: `duplicate` — in-place modification

> Write `void duplicate(int arr[], int length)` that multiplies each element by 2, modifying the original (**without** `const`). Then in `main()`, show the array before and after to verify that it did change.

```cpp
void duplicate(int arr[], int length) {
    for (int i = 0; i < length; i++) {
        arr[i] *= 2;
    }
}
```

- **Without `const`** because the function needs to **write** to the array
- The change is reflected in `main()` because the address was passed, not a copy

---

## Key Summary L28

| Concept | Detail |
|---------|--------|
| Array name | It is the **start address** of the block in memory |
| When passed to function | Only the **address** is copied, not the elements |
| Without `const` | The function **can modify** the original array |
| With `const` | The function **can only read** — the compiler forbids writing |
| `i++` post-increment | First **uses** `i`, **then** increments |
| Contrast with `int` | Normal `int` is **copied** (value) — array is passed by **address** |

---

## Related files

- [`L28_ArraysAsParameters.cpp`](../code/L28_ArraysAsParameters.cpp) — Executable code with `sum()`, `duplicate()` and `int` contrast

## Navigation

| ← Previous | Next → |
|------------|--------|
| [L27 — Array Basics](L27_ArrayBasics.md) | [L29 — Multidimensional Arrays](L29_MultidimensionalArrays.md) |
