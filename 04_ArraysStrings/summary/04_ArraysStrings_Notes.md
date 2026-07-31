# Section 04: Arrays & Strings — Study Notes

Personal notes from section 04 of **John Purcell's** course on Udemy (MIT 6.096 Lecture 4).
Covers contiguous memory representation of 1D/2D arrays, decay to pointers when passing to functions, `const` correctness, multidimensional array indexing, and C-style character arrays (`char[]` with `'\0'`).

---

## L27 — Array Basics

- An array reserves a contiguous block of memory for multiple elements of the same type
- Indexing calculates memory offset using `address = base + index * sizeof(type)`
- Zero-indexed indexing — `arr[0]` points directly to the start address with zero offset
- Uninitialized local arrays contain garbage values — explicit initialization is required
- Partial array initialization (`int arr[5] = {1, 2};`) automatically zeroes remaining elements
- `sizeof(arr) / sizeof(arr[0])` calculates array length in the declaration scope
- Out-of-bounds array access produces undefined behavior without compile errors

## L28 — Arrays as Function Parameters

- Array names decay to pointers — passing an array copies only the starting memory address
- Pass-by-address behavior — changes inside a function mutate the original array without needing `&`
- Using `const` in function signatures (`const int arr[]`) prevents accidental array modification
- Passing dimension sizes is mandatory — functions cannot determine raw array lengths independently
- Post-increment loops (`arr[i++]`) combine element retrieval and index advancement in one step

## L29 — Multidimensional Arrays

- 2D arrays are stored in contiguous memory in **Row-Major Order** (row by row)
- Element offset formula: `index = i * COLS + j`
- Multi-dimensional arrays are syntactic abstractions — `int m[2][4]` has the same layout as `int arr[8]`
- Secondary dimensions (`COLS`) are mandatory in function signatures (`void f(int m[][4])`)
- Partial initialization of 2D arrays fills unspecified row elements with zeros
- Row and column counts can be computed using `sizeof(m) / sizeof(m[0])` and `sizeof(m[0]) / sizeof(int)`

## L30 — C-Strings

- A C-string is a `char` array terminated by a null character `'\0'` (ASCII 0)
- String literals (`"text"`) automatically include the trailing `'\0'` character
- Un-terminated character arrays cause undefined behavior when passed to string functions
- `<cctype>` provides character inspection (`isalpha`, `isdigit`, `isalnum`) and conversion (`tolower`, `toupper`)
- `<cstring>` provides standard string utilities (`strlen`, `strcpy`, `strcat`, `strcmp`, `strchr`)
- `cin.getline(buffer, size)` reads full input lines including whitespace characters
- String algorithms — two-pointer filtering for normalization, reverse traversal for palindromes, and state-machine word counting

---

## Good practices so far

- Always initialize arrays upon declaration to prevent reading garbage memory values
- Protect read-only array parameters with `const` to ensure compile-time immutability
- Pass length arguments alongside raw arrays to prevent out-of-bounds access
- Specify secondary array dimensions explicitly when passing multidimensional matrices to functions
- Ensure space for the null terminator `'\0'` when allocating character arrays for C-strings
- Cast character values to `unsigned char` before passing them to `<cctype>` functions

---

*Last updated: L30 — C-Strings*
