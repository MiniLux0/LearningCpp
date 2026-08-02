# 04_ArraysStrings — Exercises (L27-L30)

Integrative review of Array Basics, Arrays as Parameters, Multidimensional Arrays, and CStrings.
Progression: each exercise builds on the previous one. Solve it, share your attempt, and we will review it before moving on.

Error patterns to watch for in all exercises:
- Do not hardcode sizes — always receive them as a parameter.
- Check the direction of your comparisons (`>` vs `<=`, etc.) before assuming they are correct.
- In C-strings: distinguish between array dimension vs actual content length (the `'\0'` dictates this).

---

## L27 — Array Basics

### Exercise 1 — Maximum
```cpp
int maximo(const int arr[], int size);
```
Returns the maximum value of the array. What initial value do you set for "maximum so far" to make it safe regardless of the array's content?

### Exercise 2 — Average
```cpp
double promedio(const int arr[], int size);
```
Calculates the average of the elements. Beware of integer division — at what point in the calculation do you need to force a `double` type?

### Exercise 3 — In-place Reversal
```cpp
void invertir(int arr[], int size);
```
Reverses the order of the array elements, modifying it directly (without creating a new array). Hint: think of two indices advancing from the ends towards the center — what is the stopping condition so they don't "cross over" or fall short?

---

## L28 — Arrays as Parameters (Pass by Reference)

### Exercise 4 — Increment All
```cpp
void incrementarTodo(int arr[], int size, int delta);
```
Adds `delta` to each element of the array. After calling this function in `main`, is the original array modified? Explain why, in terms of how arrays are passed to functions in C++.

### Exercise 5 — Linear Search
```cpp
int buscar(const int arr[], int size, int objetivo);
```
Returns the index of the first occurrence of `objetivo` (target), or `-1` if it is not found. Double-check your `for` loop condition: are you iterating up to `size - 1` or are you off by one?

---

## L29 — Multidimensional Arrays

### Exercise 6 — Matrix Sum
```cpp
int sumaMatriz(const int mat[][10], int filas, int columnasReales);
```
Sums all the elements of a matrix with up to 10 columns, but where only the first `columnasReales` (actual columns) of each row have valid data. Why can you only leave the first dimension unspecified when declaring the parameter in C++, but not the second?

### Exercise 7 — Transpose Square Matrix
```cpp
void transponer(int mat[][10], int n);
```
Transposes an `n x n` square matrix in-place (without an auxiliary matrix). Hint: if you swap `mat[i][j]` with `mat[j][i]` for all `i,j`, you will undo your own work. What range of `(i,j)` avoids that?

---

## L30 — CStrings

### Exercise 8 — `miStrlen`
```cpp
int miStrlen(const char s[]);
```
Implement your own version of `strlen` from scratch (without using `<cstring>`). What is your loop condition?

### Exercise 9 — Safe `miStrcpy`
```cpp
bool miStrcpy(char dest[], int destSize, const char src[]);
```
Copies `src` to `dest` only if it fits (using `destSize` to verify before writing), and returns `true`/`false` depending on whether the copy was possible. This is exactly what `strcpy` from `<cstring>` *does not* do — how many bytes minimum need to fit, counting the terminator?

### Exercise 10 — Count Vowels
```cpp
int contarVocales(const char s[]);
```
Counts how many vowels (uppercase or lowercase) the string has, using `<cctype>` functions instead of manually comparing `s[i] == 'a' || s[i] == 'A' || ...`.

### Exercise 11 — In-place C-string Reversal
```cpp
void invertirString(char s[]);
```
Same as Exercise 3, but for a C-string. Key difference: how do you get the "size" here, if it is not passed as a parameter?

### Exercise 12 — Uppercase without `std::string`
```cpp
void aMayusculas(char s[]);
```
Converts the string to uppercase in-place using `<cctype>`. Quick reminder: `toupper` returns the result, it doesn't modify its argument — how do you apply that here?
