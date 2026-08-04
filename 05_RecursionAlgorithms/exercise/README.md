# 05_RecursionAlgorithms — Exercises (L31-L38)

Integrative practice covering recursion fundamentals, Big-O complexity analysis, binary search, divide-and-conquer sorting, and recursive backtracking.
Progression: each exercise builds on the previous one. Solve it, share your attempt, and we will review it before moving on.

Error patterns to watch for in all exercises:
- Always define a base case — recursion without a base case causes infinite stack growth and a crash.
- Ensure recursive calls move toward the base case (smaller input, narrower range, reduced state).
- In sorting: distinguish between dividing the problem and merging/combining the results.
- In backtracking: remember to undo your choice before exploring the next branch (rollback).

---

## L31-L32 — Thinking Recursively & Recursive Problems

### Exercise 1 — Factorial
```cpp
long long factorial(int n);
```
Compute `n!` recursively. What is the base case? What happens if `n == 0`? Verify your function does not recurse infinitely for negative inputs.

### Exercise 2 — Fibonacci
```cpp
long long fibonacci(int n);
```
Return the nth Fibonacci number (0-indexed: `fib(0)=0`, `fib(1)=1`). After it works, observe how many redundant calls are made for `fib(10)` — this is the motivation for memoization.

---

## L33 — Big-O Notation

*(No standalone coding exercise — complexity analysis is embedded in exercises E03–E08. For each solution you write, annotate its Big-O time and space complexity in a comment.)*

---

## L34 — Linear & Binary Search

### Exercise 3 — Binary Search
```cpp
int binarySearch(const int arr[], int size, int target);
```
Returns the index of `target` in the sorted array, or `-1` if not found. Implement it **recursively** using `low` and `high` bounds. What is the Big-O time complexity vs linear search?

---

## L35-L36 — MergeSort

### Exercise 4 — MergeSort
```cpp
void mergeSort(int arr[], int low, int high);
void merge(int arr[], int low, int mid, int high);
```
Implement the classic divide-and-conquer merge sort. The `merge` helper must combine two already-sorted halves into a sorted result. What is the space complexity and why does MergeSort need auxiliary memory?

---

## L37 — QuickSort

### Exercise 5 — QuickSort
```cpp
void quickSort(int arr[], int low, int high);
int partition(int arr[], int low, int high);
```
Use the last element as the pivot. `partition` must rearrange the array so elements less than pivot come before it and greater elements after. What is the worst-case scenario and when does it occur?

---

## L31-L32 — Advanced Recursive Problems

### Exercise 6 — Power Function
```cpp
double power(double base, int exp);
```
Compute `base^exp` recursively. First implement the naïve O(exp) version, then optimize to O(log exp) using the fact that `base^exp = base^(exp/2) * base^(exp/2)` when `exp` is even.

### Exercise 7 — String Reversal
```cpp
string reverseString(const string& s);
```
Return a reversed copy of the string using recursion — no loops allowed. What is the base case? What is the recursive case in terms of the first character and the rest of the string?

---

## L38 — Backtracking

### Exercise 8 — Backtracking: Subsets
```cpp
void generateSubsets(const vector<int>& nums, int idx,
                     vector<int>& current, vector<vector<int>>& result);
```
Generate all subsets of `nums` using recursive backtracking. At each index, make two choices: include `nums[idx]` or skip it. Undo your choice before the next branch. How many subsets does a set of N elements produce?

---

## 🛠️ How to Build and Run Exercises

```bash
cd 05_RecursionAlgorithms/exercise
make
.\build\E01_Factorial.exe
```
