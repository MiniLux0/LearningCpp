# Lesson 18 — The `while` Loop

Loops repeat code blocks while a given condition remains `true`.

---

## 🔄 1. Syntax of `while`

```cpp
while (condition) {
    // Code block repeated as long as condition evaluates to true
    // Remember to update loop variables to prevent infinite loops!
}
```

### Example:
```cpp
int counter = 1;
while (counter <= 5) {
    cout << "Count: " << counter << "\n";
    counter++; // Increment step
}
```
