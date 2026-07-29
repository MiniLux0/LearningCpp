# Lesson 15 — Conditionals: `if-else if-else` & Logical Operators

Handles multiple mutually exclusive branches and combined logical conditions.

---

## 🔗 Logical Operators

- `&&` (AND): True only if both expressions are true.
- `||` (OR): True if at least one expression is true.
- `!` (NOT): Inverts boolean truth value.

```cpp
if (age >= 18 && score >= 70) {
    cout << "Passed qualification!\n";
} else if (age < 18) {
    cout << "Underage applicant.\n";
} else {
    cout << "Score insufficient.\n";
}
```
