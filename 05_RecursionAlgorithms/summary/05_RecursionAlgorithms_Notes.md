# 📚 Section 05 Summary & Executive Study Notes: Recursion & Algorithms

> **Course**: Learning C++ (MIT 6.096 + Stanford CS106B / CS106X / CS106L)  
> **Module**: 05 — Recursion & Algorithms (Lessons L31 – L38)  
> **Theory Directory**: [`05_RecursionAlgorithms/theory/`](../theory/)  
> **Code Directory**: [`05_RecursionAlgorithms/code/`](../code/)

---

## 🎯 Executive Summary & Core Competencies

Section 05 transitions from basic C++ syntax to **algorithmic thinking and computer science problem solving**. It explores how to decompose complex tasks into self-similar subproblems, model recursive memory execution on the RAM Call Stack, analyze asymptotic growth ($O$-Notation), and master sorting, searching, and state-space exploration algorithms.

---

## 📌 Lesson-by-Lesson Technical Breakdown

### L31 — Thinking Recursively
- A recursive function is a subprogram that calls itself to solve a smaller instance of the same problem.
- **Mandatory 2-part structure**:
  1. **Base Case**: Halting condition resolved trivially without recursive calls.
  2. **Recursive Step**: Reduces the problem scale ($n \to n-1$) and calls the function again.
- **Call Stack & Stack Frames**: Each recursive call allocates an activation record in RAM storing local parameters and the return address.
- **Stack Overflow**: Occurs when missing a base case or failing to advance towards it, exhausting available stack space.

### L32 — Classic Recursive Problems
- Mathematical functions translate directly to recursive forms:
  - **Factorial**: $n! = n \times (n-1)!$ with base case $0! = 1$.
  - **Fibonacci**: $F_n = F_{n-1} + F_{n-2}$ with dual base cases $F_0 = 0, F_1 = 1$.
  - **Power**: $a^b = a \times a^{b-1}$.
- **Call Tree Redundancy**: Naive recursive Fibonacci generates a binary call tree with $O(2^N)$ redundant calls.
- **C-String Reversal**: Leveraging the LIFO (*Last-In, First-Out*) call stack unwinding phase to process string characters in reverse order.

### L33 — Big-O Notation & Asymptotic Analysis
- Measures how an algorithm's execution time or memory requirements scale as input size $N \to \infty$.
- **Asymptotic Rules**:
  1. Ignore multiplicative constants ($O(5N) \to O(N)$).
  2. Retain only the dominant term ($O(N^2 + 100N) \to O(N^2)$).
- **Efficiency Hierarchy**: $O(1) < O(\log N) < O(N) < O(N \log N) < O(N^2) < O(2^N)$.

### L34 — Linear & Binary Search
- **Linear Search ($O(N)$)**: Checks elements sequentially. Works on unsorted arrays.
- **Binary Search ($O(\log N)$)**: Employs Divide & Conquer on **sorted arrays** by inspecting the middle element.
- **Logarithmic Growth**: Reduces search space by half at each step ($\log_2(8 \times 10^9) \approx 33$ comparisons).
- **Safe Midpoint**: `int mid = low + (high - low) / 2` avoids 32-bit integer overflow.

### L35 — Quadratic Sorting Algorithms
- **Selection Sort ($O(N^2)$)**: Repeatedly selects the minimum element from the unsorted region. Unstable.
- **Insertion Sort ($O(N^2)$)**: Shifts elements to insert each item into its sorted position. Runs in $O(N)$ for nearly-sorted data. Stable.
- **Bubble Sort ($O(N^2)$)**: Swaps adjacent out-of-order pairs. Early-exit optimization halts when no swaps occur.

### L36 — MergeSort
- **Divide & Conquer**: Splits array into two halves, recursively sorts both, and merges them.
- **Time Complexity**: Guaranteed $O(N \log N)$ in all cases (worst, average, best).
- **Space Complexity**: Requires $O(N)$ auxiliary memory for merging. Stable.

### L37 — QuickSort
- **Partitioning**: Selects a **pivot** and rearranges elements so items $\le \text{pivot}$ are left and items $> \text{pivot}$ are right.
- **Performance**: Average $O(N \log N)$ time and $O(\log N)$ stack space. Worst case $O(N^2)$ (avoided via randomized pivots or median-of-three).
- **In-Place**: Highly cache-efficient for RAM arrays (`std::sort`).

### L38 — Recursive Backtracking
- Systematic state space tree exploration.
- **Universal 3-Step Pattern**:
  1. **Choose**: Make a tentative decision.
  2. **Explore**: Recurse to solve the remaining decisions.
  3. **Unchoose**: Revert the decision (backtrack) to try alternative branches.
- **Pruning**: Early branch truncation to eliminate invalid search paths.

---

## ⚡ Quick Reference Matrix

| Lesson | Core Topic | Time Complexity | Space Complexity | Primary Academic Source |
|---|---|:---:|:---:|---|
| **L31** | Thinking Recursively | $O(N)$ | $O(N)$ Stack | Stanford CS106B Ch 7 / MIT 6.096 L5 |
| **L32** | Classic Recursive Problems | $O(N)$ to $O(2^N)$ | $O(N)$ Stack | Stanford CS106B Ch 8 / CS106X |
| **L33** | Big-O Notation | $O(1) \dots O(2^N)$ | $O(1) \dots O(N)$ | Stanford CS106B Ch 10 / CS106X |
| **L34** | Linear & Binary Search | $O(\log N)$ | $O(1)$ | Stanford CS106B Ch 10.2 |
| **L35** | Quadratic Sorts | $O(N^2)$ | $O(1)$ In-Place | Stanford CS106B Ch 10.3 |
| **L36** | MergeSort | $O(N \log N)$ | $O(N)$ | Stanford CS106B Ch 10.3 / CS106X |
| **L37** | QuickSort | $O(N \log N)$ avg | $O(\log N)$ In-Place | Stanford CS106B Ch 10.3 / CS106X |
| **L38** | Recursive Backtracking | $O(b^d)$ Decision Tree | $O(d)$ Stack | Stanford CS106B Ch 9 / CS106X |

---
*MiniLux0 — Learning C++ Section 05 Executive Summary*
