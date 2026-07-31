# ⚡ Stanford CS106X: Programming Abstractions in C++ (Honors Track)

> **Stanford University — Department of Computer Science**  
> 🎓 **Level**: Accelerated / Honors Computer Science Core  
> 👨‍🏫 **Instructors**: Jerry Cain & Garrick Fernandez  
> 📖 **Official Course Links**: [Main Page](https://web.stanford.edu/class/cs106x/) \| [Handouts Catalog](https://web.stanford.edu/class/cs106x/handouts.html) \| [Assignments Catalog](https://web.stanford.edu/class/cs106x/assignments.html)  
> 🎯 **Primary Focus**: High-performance ADT engineering, 4-Way Priority Queues, Top-Down Memoization, Sparse String Arrays, Tries & Lexicons, and Spreadsheet Engines.

---

## 1. 🎯 Course Overview & Educational Vision

CS106X is Stanford's honors/accelerated version of Programming Abstractions in C++. Designed for students with strong programming foundations, it covers the CS106B curriculum at an accelerated pace, delving into advanced algorithm analysis, dynamic programming, sparse data structures, and capstone software architecture.

In this repository, Stanford CS106X serves as the **accelerated & honors benchmark**, pushing algorithmic efficiency and complex system design.

---

## 2. 🧠 Key Technical Competencies & Learning Outcomes

1. **4-Way Priority Queues**: Building multi-way binary heaps and pointer-based priority queues.
2. **Memoization & Top-Down DP**: Caching recursive state spaces to reduce exponential $O(2^n)$ time complexities to polynomial time.
3. **Sparse Memory Abstractions**: Designing sparse string arrays and memory-efficient data structures.
4. **Tries & Prefix Trees**: Implementing Trie structures for $O(L)$ dictionary and prefix lookups.
5. **Full System Architecture**: Building `Stanford 1-2-3`, a complete Excel-style spreadsheet calculation engine supporting formula evaluation, cell dependency DAGs, and grid layout.

---

## 3. 📚 Comprehensive 34-Handout Curriculum Map

Extracted from the [Official Stanford CS106X Handouts Page](https://web.stanford.edu/class/cs106x/handouts.html):

| # | Handout Title | Key Topics & Code Materials Extracted | Repository Module |
|---|---------------|---------------------------------------|-------------------|
| **1** | [Course Information](https://web.stanford.edu/class/cs106x/handouts.html) | CS106X course administration, environment setup | [`01_GettingStarted`](../../01_GettingStarted/) |
| **2** | [Course Syllabus](https://web.stanford.edu/class/cs106x/handouts.html) | Accelerated learning plan & topic schedule | [`01_GettingStarted`](../../01_GettingStarted/) |
| **3** | Queen Safety | 2D Grid safety checks, N-Queens logic `[01-intro-code.zip]` | [`02_BasicSyntax`](../../02_BasicSyntax/) |
| **4** | C++ Strings | String manipulation, memory allocation, `<string>` | [`04_ArraysStrings`](../../04_ArraysStrings/) |
| **5** | **Assignment 1: Life** | 2D cellular automaton matrix simulation (*Game of Life*) | [`04_ArraysStrings`](../../04_ArraysStrings/) |
| **6** | Stacks and Queues | Linear ADTs: LIFO vs FIFO stack and queue mechanics | [`10_DataStructures`](../../10_DataStructures/) |
| **7** | Maps and Sets | Associative containers: key-value pairs, hash sets | [`10_DataStructures`](../../10_DataStructures/) |
| **8** | Section Handout 1 | ADT practice exercises & solution `[08S-Solution.pdf]` | [`10_DataStructures`](../../10_DataStructures/) |
| **9** | Recursion | Recursive thinking, base cases, call stack mechanics | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **10** | **Assignment 2: ADTs** | Practical container applications & custom ADT logic | [`10_DataStructures`](../../10_DataStructures/) |
| **11** | Recursive Backtracking I | Exhaustive recursive search, decision trees, subsets | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **12** | Section Handout 2 | Recursion & backtracking section exercises & solution | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **13** | Recursive Backtracking II | Advanced backtracking, N-Queens, pruning optimization | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **14** | Memoization | Top-down dynamic programming & recursive caching | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **15** | **Assignment 3: Boggle** | Word-finding game on a letter grid with lexicon lookup | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **16** | Sparse String Array | Memory-efficient sparse array data structures | [`06_Pointers`](../../06_Pointers/) |
| **17** | Section Handout 3 | Pointer & array section exercises & solution | [`06_Pointers`](../../06_Pointers/) |
| **18** | **Assignment 4: ADTs & Recursion** | Combining data structures and recursion | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) / [`10_DataStructures`](../../10_DataStructures/) |
| **19** | All About Linked Lists | Pointer manipulation, node creation, linked list reversal | [`10_DataStructures`](../../10_DataStructures/) |
| **20** | Final Project Specifications | CS106X capstone project roadmap and requirements | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **21** | CS106X Practice Midterm | Midterm examination review & full solution | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **22** | Hashing & HashMaps | Hash functions, collision resolution, hash maps | [`10_DataStructures`](../../10_DataStructures/) |
| **23** | Section Handout 4 | Hash table section exercises, solution & addendum | [`10_DataStructures`](../../10_DataStructures/) |
| **24** | CS106X Midterm Exam | Official midterm exam questions, solution & starter code | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) / [`10_DataStructures`](../../10_DataStructures/) |
| **25** | **Assignment 5: PQueue** | 4-Way Priority Queue (Array, Pointer, List, Heap) | [`10_DataStructures`](../../10_DataStructures/) |
| **26** | Trees & TreeMaps | Binary Search Trees (BST) & self-balancing tree concepts | [`10_DataStructures`](../../10_DataStructures/) |
| **27** | Tries & Lexicons | Prefix trees (Tries) for fast dictionary lookup | [`10_DataStructures`](../../10_DataStructures/) |
| **28** | Section Handout 5 | Tree & trie section exercises & solution | [`10_DataStructures`](../../10_DataStructures/) |
| **29** | **Assignment 6: Huffman** | Bitwise file compression engine using Huffman trees | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **30** | Section Handout 6 | Compression section exercises & solution | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **31** | Introduction to Graphs | Graph nodes, edges, adjacency lists, BFS & DFS | [`10_DataStructures`](../../10_DataStructures/) |
| **32** | **Assignment 7: Stanford 1-2-3** | Capstone: Excel-style spreadsheet calculation engine | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **33** | CS106X Practice Final | Final examination practice & solution | [`10_DataStructures`](../../10_DataStructures/) |
| **34** | Section Handout 7 | Final graph & algorithm section exercises & solution | [`10_DataStructures`](../../10_DataStructures/) |

---

## 4. 💻 Assignments & Practical Projects Catalog (Assignments 1–7)

Extracted from the [Official Stanford CS106X Assignments Page](https://web.stanford.edu/class/cs106x/assignments.html):

| # | Assignment | Due Date | Handout Document | Starter Code & Materials | Demo Binaries |
|---|------------|----------|------------------|--------------------------|---------------|
| **1** | **Game of Life** | 10/02 | `05-Assignment-1-Life.pdf` | `assign-1-game-of-life.zip` | Mac Demo / PC Demo |
| **2** | **ADTs** | 10/09 | `10-Assignment-2-ADTs.pdf` | `assign-2-adts.zip` | Mac Demo / PC Demo |
| **3** | **Boggle** | 10/16 | `15-Assignment-3-Boggle.pdf` | `assign-3-boggle.zip` | Mac Demo / PC Demo |
| **4** | **Recursion and ADTs** | 10/23 | `18-Assignment-4-ADTs-and-Recursion.pdf` | `assign-4-recursion-and-adts.zip` | No demo apps |
| **5** | **PQueue** | 11/04 | `25-Assignment-5-PQueue.pdf` | `assign-5-pqueue.zip` | No demo apps |
| **6** | **Huffman** | 11/11 | `29-Assignment-6-Huffman.pdf` | `assign-6-huffman.zip` | No demo apps |
| **7** | **Stanford 123** | 11/19 | `32-Assignment-7-Stanford-1-2-3.pdf` | `assign-7-stanford-123.zip` | Mac Demo / PC Demo |

---

## 5. 👥 Discussion Sections & Practice Exercises

The CS106X curriculum includes 7 intensive discussion section handouts (Handouts 8, 12, 17, 23, 28, 30, 34) focusing on:
- High-performance memory management and pointer safety.
- Memoization table design for dynamic programming.
- Advanced graph traversal optimizations and trie dictionary lookups.

---

## 6. 🗺️ Repository Alignment & Module Mapping

| Repository Module | CS106X Handouts & Assignments Alignment |
|-------------------|-----------------------------------------|
| [`04_ArraysStrings`](../../04_ArraysStrings/) | Handouts 4–5 (C++ Strings & Assignment 1: Game of Life) |
| [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) | Handouts 9, 11–15, 18, 21, 24 & Assignments 3 (Boggle) & 4 |
| [`06_Pointers`](../../06_Pointers/) | Handouts 16, 17, 19 (Sparse Arrays & Linked Lists) |
| [`10_DataStructures`](../../10_DataStructures/) | Handouts 6–7, 22, 25–28, 31 & Assignment 5 (4-Way PQueue) |
| [`12_AdvancedCPP`](../../12_AdvancedCPP/) | Handouts 29, 32 & Assignments 6 (Huffman) & 7 (Stanford 123) |

---

## 7. 🔗 Navigation & Quick Links

- 🌐 [Master Academic Guide](../Master_Academic_Guide.md)
- 🏛️ [MIT 6.096 Syllabus](../mit6096/README.md)
- 🌲 [Stanford CS106B Syllabus](../cs106b/README.md)
- ⚙️ [Stanford CS106L Syllabus](../cs106l/README.md)
- 📋 [Master Repository Syllabus (`TEMARIO.md`)](../../TEMARIO.md)

---
*MiniLux0 — Stanford CS106X Syllabus Documentation*
