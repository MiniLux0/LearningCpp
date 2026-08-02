<div align="center">

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L29 — Multidimensional Arrays**](L29_MultidimensionalArrays.md) | [**🏠 Arrays & Strings**](../README.md) | [**L31 — Thinking Recursively ➡️**](../../05_RecursionAlgorithms/theory/L31_ThinkingRecursively.md) |

</div>

---

# L30 — C-Strings: Character Arrays, Null Terminator and Standard Libraries (`<cstring>`, `<cctype>`, `<cstdlib>`, `<cstdio>`)

> **Core concept:** A C-string is not a special native data type, but a **contiguous array of `char`** whose end is marked by the special character **null `'\0'` (ASCII 0)**. Understanding the difference between the **array dimension** and the **string length** is the key to mastering memory and avoiding buffer overflows.

---

## Learning Objectives

- [ ] Understand the internal structure of a C-string in RAM memory and the role of the `'\0'` terminator.
- [ ] Understand why the array dimension $\neq$ string length (rule `strlen(src) + 1`).
- [ ] Use the functions of `<cstring>` (`strlen`, `strcpy`, `strcat`, `strcmp`, `strchr`) and their n-limited variants.
- [ ] Analyze and solve **Buffer Overflow**.
- [ ] Manipulate individual characters with `<cctype>` (`isalpha`, `isdigit`, `toupper`, `tolower`).
- [ ] Master the **idiomatic traversal pattern** in $O(n)$ (`str[i] != '\0'`) instead of calling `strlen()` inside the loop.
- [ ] Convert between text and numbers with `<cstdlib>` (`atoi`, `atof`) and `<cstdio>` (`sprintf`).

---

## 1. What really is a C-String?

In C++ a classic string is not a "magic" type: it is simply a contiguous `char[]` in memory where the useful content ends **before the first `'\0'`**, regardless of the total declared size.

```cpp
char greeting[20] = "Hola";
```

This reserves 20 bytes in RAM, but only the first 5 are in use: `'H'`, `'o'`, `'l'`, `'a'`, `'\0'`. The remaining 15 bytes contain unused values or zeros. No C-string function will touch those 15 bytes because they all stop immediately upon finding the `'\0'`.

```text
C-String "Hola" in memory (requires 5 useful bytes):

+-----+-----+-----+-----+------+---+---+ ... +---+
| 'H' | 'o' | 'l' | 'a' | '\0' | ? | ? | ... | ? |
+-----+-----+-----+-----+------+---+---+ ... +---+
   0     1     2     3     4     5   6       19   ← index in char greeting[20]
```

> 💡 **Fundamental Difference:**
> - **Array Dimension (`sizeof(greeting)`):** 20 bytes (total reserved capacity).
> - **String Length (`strlen(greeting)`):** 4 characters (actual length without counting the `'\0'`).
>
> ⚠️ **Danger:** Confusing the array dimension with the useful length is the #1 source of errors and security flaws in C/C++.

---

## 2. The `<cstring>` Library

Since a C-string is a raw array, **you cannot do `str1 = str2` nor `str1 == str2`** (that would compare RAM memory addresses, not the text). For this reason, the `<cstring>` library is used.

### Main Functions Table

| Function | Description | Example | Danger / Note |
|----------|-------------|---------|---------------|
| `strlen(s)` | Counts characters until `'\0'` (without counting it) | `strlen("Hola")` $\rightarrow$ `4` | None (read only). $O(n)$. |
| `strcpy(dest, src)` | Copies full `src` to `dest` (including `'\0'`) | `strcpy(buf, "Hola");` | ⚠️ **Buffer Overflow:** Does not check space in `dest`. |
| `strcat(dest, src)` | Appends `src` to the end of `dest` (replaces the `'\0'` of `dest`) | `strcat(buf, " Mundo");` | ⚠️ **Buffer Overflow:** Can overwrite contiguous memory. |
| `strcmp(s1, s2)` | Compares lexicographically | `strcmp("Ana", "Pedro")` $< 0$ | Returns `0` if they are exactly equal. |
| `strchr(s, c)` | Searches for the character `c` in `s`. Returns `char*` | `strchr("Hola", 'l')` $\rightarrow$ pointer to `'l'` | Returns `nullptr` if it does not find the character. |
| `strncpy`/`strncat` | Versions with maximum limit `n` of characters | `strncpy(dest, src, n);` | Safer, but `strncpy` does not guarantee `'\0'` if it truncates. |

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char dest[50];
    strcpy(dest, "Hola");       // dest contains "Hola\0"
    strcat(dest, " Mundo");     // dest contains "Hola Mundo\0"

    if (strcmp(dest, "Hola Mundo") == 0) {
        cout << "The strings are identical!" << endl;
    }
}
```

---

### ❓ Checkpoint Question #1 — The Danger of `strcpy`

Given the following code:
```cpp
char destination[5];
strcpy(destination, "Hola!");
```
**What happens in memory and why?**

<details>
<summary>🔍 <strong>See Explanation and Diagnosis</strong></summary>

**Answer:** It produces **Undefined Behavior and Buffer Overflow**.

**Explanation:**
The literal `"Hola!"` has 5 visible characters, but since a C-string requires the `'\0'` terminator, in memory it occupies **6 bytes**: `'H'`, `'o'`, `'l'`, `'a'`, `'!'`, `'\0'`.

Since `destination` only reserved 5 bytes (indices 0 to 4), `strcpy` will blindly write the sixth byte (`'\0'`) in the contiguous memory position outside the array. In practice this can:
1. Corrupt other neighboring variables in the *stack*.
2. Cause a Segmentation Fault.
3. Open computer security vulnerabilities.

> 🌟 **Golden Rule for Copy / Concatenation:**
> The destination array must always have a minimum capacity of:
> $$\text{Destination Capacity} \ge \text{strlen(source)} + 1$$
</details>

---

## 3. Classification and Transformation with `<cctype>`

The `<cctype>` library allows inspecting and transforming individual characters.

### Main Functions

| Function | Type | Question / Action |
|----------|------|-------------------|
| `isalpha(c)` | Inspection | Is it a letter (`'A'-'Z'`, `'a'-'z'`)? |
| `isdigit(c)` | Inspection | Is it a decimal digit (`'0'-'9'`)? |
| `isalnum(c)` | Inspection | Is it alphanumeric (letter or digit)? |
| `isspace(c)` | Inspection | Is it space, tab (`'\t'`) or newline (`'\n'`)? |
| `isupper(c)` / `islower(c)` | Inspection | Is it uppercase / lowercase? |
| `ispunct(c)` | Inspection | Is it a punctuation mark (e.g. `!`, `,`, `.`)? |
| `toupper(c)` / `tolower(c)` | Transformation | Returns the character in uppercase / lowercase. |

> ⚠️ **Key Detail 1 (Reassignment):** `toupper` and `tolower` **do not modify the original character in-place**, but return a transformed copy. To alter the original string you must reassign: `s[i] = toupper(s[i]);`.

---

### 💡 Pedagogical Note: Basic Use vs. Advanced Best Practices (`static_cast<unsigned char>`)

When you study C++ for the first time or work with the standard English alphabet (basic ASCII: `A-Z`, `a-z`, `0-9`), the direct and natural way is:

```cpp
// BASIC Form (ideal for beginners):
s[i] = toupper(s[i]);
```

However, sometimes you will see in professional code or more advanced templates the following:

```cpp
// ADVANCED / PRODUCTION Form:
s[i] = static_cast<char>(toupper(static_cast<unsigned char>(s[i])));
```

#### Why does that `static_cast<unsigned char>` conversion exist?

1. **Range of `<cctype>` functions:** The historical C/C++ functions like `toupper()` receive an `int` and the standard requires that the value be in the range of an **`unsigned char`** (`0` to `255`), or `EOF` (`-1`).
2. **The problem with signed `char`:** In many compilers and systems (like Windows or Linux x86), the `char` type is **signed** (`signed char`), with values between `-128` and `127`.
3. **Special characters / Accents:** If your text has characters outside basic ASCII (like `'á'`, `'ñ'`, etc.), their byte is interpreted as a negative number (for example, `-31`). Passing a negative number that is not `EOF` to `toupper()` causes **Undefined Behavior**.
4. **The solution:** Doing `static_cast<unsigned char>(c)` (or in C style `(unsigned char)c`) converts the byte to its positive equivalent (`0` to `255`), making the program 100% safe on any platform and language.

> 📌 **For your exercises:** You can simply write `s[i] = toupper(s[i]);`. Knowing about `static_cast<unsigned char>` will help you not to get scared when you read professional or production code.

---

### ❓ Checkpoint Question #2 — Efficiency and Idiomatic Traversal Pattern

Analyze the following two loops to traverse a C-string `s`:

```cpp
// Option A (Idiomatic Pattern):
for (int i = 0; s[i] != '\0'; i++) { ... }

// Option B:
for (int i = 0; i < strlen(s); i++) { ... }
```

**Why is Option A drastically superior to Option B?**

<details>
<summary>🔍 <strong>See Explanation and Algorithmic Complexity</strong></summary>

**Answer:** Due to time complexity ($O(n)$ vs $O(n^2)$).

**Explanation:**
- In **Option B**, `strlen(s)` is executed in **every iteration** of the loop. Since `strlen` must traverse the string from the beginning until it finds `'\0'`, each iteration takes $O(n)$ time, making the entire loop $O(n^2)$.
- In **Option A**, it takes advantage of the fact that the `'\0'` is already encoded inside the array's own memory. It is evaluated character by character and stops exactly upon reaching the end in a single traversal of $O(n)$ complexity.

> 📌 **Standard Traversal Pattern:**
> `for (int i = 0; s[i] != '\0'; i++)` or `while (*ptr != '\0')`
</details>

---

## 4. Conversion of C-Strings ↔ Numbers (`<cstdlib>`, `<cstdio>`)

All input received by keyboard or from files is read as text. To process it mathematically requires numeric conversion.

### Conversion Functions

| Function | Direction | From $\rightarrow$ To | Library | Example / Notes |
|----------|-----------|-----------------------|---------|-----------------|
| `atoi(s)` | Text $\rightarrow$ Number | C-string $\rightarrow$ `int` | `<cstdlib>` | `atoi("42")` $\rightarrow$ `42`. Returns `0` if it fails. |
| `atof(s)` | Text $\rightarrow$ Number | C-string $\rightarrow$ `double` | `<cstdlib>` | `atof("3.1416")` $\rightarrow$ `3.1416`. |
| `atol(s)` | Text $\rightarrow$ Number | C-string $\rightarrow$ `long` | `<cstdlib>` | `atol("1000000")` $\rightarrow$ `1000000L`. |
| `sprintf(dest, format, val)` | Number $\rightarrow$ Text | Value $\rightarrow$ C-string | `<cstdio>` | Writes formatted text into `dest`. |

```cpp
#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

int main() {
    // 1. Text to Number (atoi, atof)
    char numText[] = "125.75";
    double price = atof(numText);
    cout << "Price + 10: " << price + 10 << endl; // 135.75

    // 2. Number to Text (sprintf)
    char buffer[30];
    int age = 21;
    sprintf(buffer, "I am %d years old", age);
    cout << buffer << endl; // "I am 21 years old"
}
```

---

### ❓ Checkpoint Question #3 — Binary Memory vs Textual Representation

When using `sprintf(buffer, "%d", intValue);`, if `intValue` is a 32-bit integer (up to 10 decimal digits plus the negative sign `-`), **how many bytes must the `buffer` array have as a minimum?**

<details>
<summary>🔍 <strong>See Explanation: Bytes of the Type vs Digits of the Text</strong></summary>

**Answer:** Minimum **12 bytes** (`char buffer[12];`).

**Explanation and Common Confusion:**
- An `int` occupies **4 bytes** in RAM memory for its **binary representation** (which allows ranges from $-2,147,483,648$ to $2,147,483,647$).
- When converting it to **text**, each decimal digit becomes a `char` character (which occupies 1 byte each).
- For the longest case (`-2147483648`):
  - 10 bytes for the 10 digits.
  - 1 byte for the negative sign `-`.
  - 1 byte for the null terminator `'\0'`.
  - **Total:** $10 + 1 + 1 = 12\text{ bytes}$.

> 💡 **In practice:** A generous margin is usually declared (e.g. `char buffer[16];` or `char buffer[32];`) to avoid accidental overflows.
</details>

---

## 5. Reading C-Strings with Spaces (`cin.getline`)

The operator `cin >> buffer` stops upon finding the first whitespace or newline. To read complete lines:

```cpp
char fullName[50];
cout << "Enter your full name: ";
cin.getline(fullName, 50); // Reads up to 49 characters or until the '\n'
```

---

## 6. Classic Algorithms with C-Strings

### Algorithm 1: Normalization / Cleaning (In-Place)
```cpp
void cleanNormalize(char str[]) {
    // 1. Convert to lowercase
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = static_cast<char>(tolower(static_cast<unsigned char>(str[i])));
    }

    // 2. Filter non-alphanumeric characters (Read/write pointers)
    int write = 0;
    for (int read = 0; str[read] != '\0'; read++) {
        if (isalnum(static_cast<unsigned char>(str[read]))) {
            str[write++] = str[read];
        }
    }
    str[write] = '\0'; // Maintain the null terminator contract
}
```

### Algorithm 2: Palindrome Check
```cpp
bool isPalindrome(const char str[]) {
    int len = strlen(str);
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        if (str[i] != str[j]) return false;
    }
    return true;
}
```

### Algorithm 3: In-Place Reversal
```cpp
void reverse(char s[]) {
    int len = strlen(s);
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
}
```

---

## 📝 Brief Summary of L30

1. **Definition:** A C-string is a `char[]` terminated in `'\0'`. The **array dimension** $\neq$ **useful string length**.
2. **`<cstring>` Library:** `strlen`, `strcpy`, `strcat`, `strcmp` do not check bounds. The golden rule is $\text{Destination Capacity} \ge \text{strlen(source)} + 1$.
3. **`<cctype>` Library:** `isalpha`, `isdigit`, `tolower`, `toupper`. The transformation functions return a new value (they do not modify in-place).
4. **Traversal Pattern:** `for (int i = 0; s[i] != '\0'; i++)` traverses in $O(n)$ without recalculating `strlen()` in each iteration.
5. **`<cstdlib>` and `<cstdio>` Libraries:** `atoi`/`atof` convert text $\rightarrow$ number. `sprintf` converts number $\rightarrow$ text (remembering that binary type bytes $\neq$ number of printed characters).

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L29 — Multidimensional Arrays**](L29_MultidimensionalArrays.md) | [**🏠 Arrays & Strings**](../README.md) | [**L31 — Thinking Recursively ➡️**](../../05_RecursionAlgorithms/theory/L31_ThinkingRecursively.md) |

</div>
