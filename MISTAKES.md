# Common Mistakes and Solutions

Log of mistakes I make and how I fix them. Useful to avoid repeating them.

---

## Syntax Errors

### 1. Forgetting the semicolon `;`
```
cout << "Hello"    ← Error: expected ';' before '}' token
```
**Fix:** Always end every statement with `;`.

### 2. Using `=` instead of `==` in conditionals
```
if (x = 5)    ← Error: assignment in conditional expression
```
**Fix:** Use `==` to compare: `if (x == 5)`.

### 3. Forgetting to include `<iostream>`
```
cout was not declared in this scope
```
**Fix:** Add `#include <iostream>` at the top of the file.

---

## Variable Errors

### 4. Using a variable before initializing it
```
int x;
cout << x;    ← Warning: 'x' may be used uninitialized
```
**Fix:** Always give an initial value: `int x = 0;`.

### 5. Mixing types in operations
```
int a = 5;
double b = 2.5;
int c = a / b;    ← Warning: loss of precision
```
**Fix:** Be aware of types and use casting when needed.

---

## Memory Errors *(coming soon)*

*Will add more errors as I progress through pointers and dynamic memory.*

---

## Compilation Errors

### 6. Not having `return 0;` in `main()`
- In C++11 and later, the compiler adds it implicitly, but it is good practice to include it.

### 7. Forgetting `using namespace std;` or the `std::` prefix
```
cout was not declared in this scope
```
**Fix:** Add `using namespace std;` or use `std::cout`.

---

*Last error logged: L10 — Integer Types*
