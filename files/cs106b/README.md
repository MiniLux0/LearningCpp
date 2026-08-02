# 🌲 Stanford CS106B: Programming Abstractions in C++ (Standard Track)

> **Stanford University — Department of Computer Science**  
> 🎓 **Level**: Intermediate Computer Science Core  
> 👨‍🏫 **Instructors**: Keith Schwarz, Julie Zelenski, Chris Gregg  
> 📖 **Official Textbook**: *Programming Abstractions in C++* by Eric S. Roberts ([PDF Reader](textbook/CS106BX-Reader.pdf))  
> 🎯 **Primary Focus**: Abstract Data Types (ADTs), Recursion, Backtracking, Big-O Notation, Linked Lists, Binary Trees, Priority Queues, Huffman Compression, and Graph Theory.

---

## 1. 🎯 Course Overview & Educational Vision

Stanford CS106B is one of the most celebrated Computer Science courses in academia. It teaches students how to model and solve complex computational problems using **abstractions**, **data structures**, **recursion**, and **algorithm design**.

In this repository, Stanford CS106B serves as the **algorithmic & data structures core**, bridging low-level C++ syntax with high-level software engineering and algorithm analysis.

---

## 2. 🧠 Key Technical Competencies & Learning Outcomes

1. **Abstract Data Types (ADTs)**: Mastering custom collection classes (`Vector`, `Grid`, `Stack`, `Queue`, `Map`, `Set`, `PriorityQueue`, `Lexicon`) and memory layouts.
2. **Recursive Problem Solving**: Thinking recursively, mastering base cases vs recursive steps, call stack visualization, and exhaustive backtracking search.
3. **Algorithmic Analysis**: Evaluating time complexity ($O(1), O(\log n), O(n), O(n \log n), O(n^2)$) and space complexity of search and sort algorithms.
4. **Pointer Memory & Custom Data Structures**: Building low-level data structures from scratch (Singly/Doubly Linked Lists, Binary Search Trees, Min/Max Heaps, Hash Tables).
5. **Graph Theory & Traversals**: Graph modeling (Adjacency Matrix/List), Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra's shortest path, Kruskal's Minimum Spanning Tree (MST).

---

## 3. 📚 Comprehensive Curriculum & Textbook Syllabus

Extracted from the official textbook *Programming Abstractions in C++* ([`textbook/CS106BX-Reader.pdf`](textbook/CS106BX-Reader.pdf)):

| Chapter | Title | Core Computer Science Concepts Extracted | Repository Module |
|---------|-------|------------------------------------------|-------------------|
| **Ch 1** | Overview of C++ | Basic C++ syntax, control flow, functions, type conversions. | [`01_GettingStarted`](../../01_GettingStarted/) / [`02_BasicSyntax`](../../02_BasicSyntax/) |
| **Ch 2** | Functions & Libraries | Scope, function overloading, standard libraries, interface `.h` vs implementation `.cpp`. | [`03_Subroutines`](../../03_Subroutines/) |
| **Ch 3** | Strings | Character mechanics, C-strings vs `std::string`, string manipulation. | [`04_ArraysStrings`](../../04_ArraysStrings/) |
| **Ch 4** | Streams | Input/output streams, stringstreams, file streams, stream formatting. | [`11_FileIO`](../../11_FileIO/) |
| **Ch 5** | Collections | ADTs: `Vector`, `Grid`, `Stack`, `Queue`, `Map`, `Set`, `Lexicon`. | [`04_ArraysStrings`](../../04_ArraysStrings/) / [`10_DataStructures`](../../10_DataStructures/) |
| **Ch 6** | Designing Classes | Encapsulation, class layout, constructors, destructors, operator overloading. | [`07_Classes`](../../07_Classes/) |
| **Ch 7** | Introduction to Recursion | Thinking recursively, base case, call stack activation frames, fractals. | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **Ch 8** | Recursive Procedures | Recursive string/math algorithms, permutations, subsets. | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **Ch 9** | Recursive Backtracking | Decision trees, state space exploration, N-Queens, Boggle, maze solving. | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **Ch 10** | Algorithmic Analysis | Asymptotic analysis, Big-O notation, Linear/Binary Search, Merge Sort, Quick Sort. | [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) |
| **Ch 11** | Pointers and Arrays | Addresses, dereferencing, pointer arithmetic, dynamic memory allocation. | [`06_Pointers`](../../06_Pointers/) |
| **Ch 12** | Dynamic Memory | Stack vs Heap, `new`/`delete`, dynamic array expansion, destructors. | [`09_MemoryManagement`](../../09_MemoryManagement/) |
| **Ch 13** | Efficiency and ADTs | Linked list implementations of stacks and queues, pointer manipulation. | [`10_DataStructures`](../../10_DataStructures/) |
| **Ch 14** | Linear Structures | Singly linked lists, doubly linked lists, sentinel nodes, list reversal. | [`10_DataStructures`](../../10_DataStructures/) |
| **Ch 15** | Maps & Search Trees | Binary Search Trees (BST), tree invariants, recursive traversals. | [`10_DataStructures`](../../10_DataStructures/) |
| **Ch 16** | Trees & Heaps | Binary heaps, Min/Max heaps, Priority Queue implementations. | [`10_DataStructures`](../../10_DataStructures/) |
| **Ch 17** | Sets & Hash Tables | Hash functions, bucket hashing, collision resolution (chaining vs open addressing). | [`10_DataStructures`](../../10_DataStructures/) |
| **Ch 18** | Graphs | Graph nodes, edges, adjacency matrices/lists, BFS, DFS, Dijkstra, Kruskal. | [`10_DataStructures`](../../10_DataStructures/) |

---

## 4. 💻 Assignments & Practical Projects Catalog

Catalog of assignments located in [`files/cs106b/assignments/`](assignments/):

| # | Assignment Folder | Projects & Applied Computer Science Problems | Key Algorithms & Structures |
|---|-------------------|----------------------------------------------|-----------------------------|
| **0** | [`starter-assign0/`](assignments/starter-assign0/) | Environment setup, Qt Debugger step-through tutorial, `NameHash` hashing algorithm. | Hash functions, Qt configuration |
| **1** | [`Assignment 1/`](assignments/Assignment%201/) | **Welcome to C++**: `OnlyConnect` consonant string filter, `PlayingFair` Thue-Morse sequence, `Plotter` canvas graphics, `Sandpiles` avalanche simulation, recursive `StackOverflow`. | String processing, recursion, grid simulation |
| **2** | [`Assignment 2/`](assignments/Assignment%202/) | **Fun with Collections**: `RisingTides` 2D terrain grid flood simulation, `RosettaStone` language identification with frequency `Map` & `Set`. | 2D Grids, `Map`, `Set`, Frequency matching |
| **3** | [`Assignment 3/`](assignments/Assignment%203/) | **Recursion & Backtracking**: Recursive maze solver, subset generation, `Boggle` 4x4 matrix word search solver. | Exhaustive backtracking, Lexicon pruning |
| **4** | [`Assignment 4/`](assignments/Assignment%204/) | **Priority Queue & Linked Lists**: Linked list node manipulation, heap allocation, binary heap `PriorityQueue` container. | Singly/Doubly Linked Lists, Min/Max Binary Heaps |
| **5** | [`Assignment 5/`](assignments/Assignment%205/) | **Trees & File Compression**: Binary Search Tree traversal, frequency tree construction, bitwise file compression & decompression using **Huffman Coding**. | BST, Frequency trees, Bitwise I/O streams |
| **6** | [`Assignment 6/`](assignments/Assignment%206/) | **Graph Algorithms**: Graph data structures, Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra's Shortest Path, Kruskal's Minimum Spanning Tree. | Graph nodes/edges, BFS, DFS, Dijkstra, Kruskal |
| **7–9** | [`assignments/`](assignments/) | **Capstones & Advanced ADTs**: Custom memory allocators, spreadsheet engines, high-performance ADT benchmarks. | Advanced pointers, allocators |

---

## 5. 👥 Discussion Sections & Practice Exercises

Weekly discussion section starter code in [`files/cs106b/sections/`](sections/):
- **Section 1–2**: Collections (`Grid`, `Map`, `Set`) & Stream processing exercises.
- **Section 3–4**: Advanced recursion & recursive backtracking practice.
- **Section 5–6**: Linked List node manipulation, tail pointers, memory safety.
- **Section 7–8**: Binary Search Trees, Graph traversals, Big-O asymptotic analysis.

---

## 6. 🗺️ Repository Alignment & Module Mapping

| Repository Module | CS106B Textbook & Assignments Alignment |
|-------------------|-----------------------------------------|
| [`04_ArraysStrings`](../../04_ArraysStrings/) | Chapters 3, 5 & Assignment 1–2 (Collections) |
| [`05_RecursionAlgorithms`](../../05_RecursionAlgorithms/) | Chapters 7–10 & Assignment 3 (Recursion, Backtracking, Big-O) |
| [`06_Pointers`](../../06_Pointers/) | Chapter 11 (Pointers & Address Arithmetic) |
| [`07_Classes`](../../07_Classes/) | Chapter 6 (Designing Classes & Encapsulation) |
| [`09_MemoryManagement`](../../09_MemoryManagement/) | Chapter 12 (Dynamic Memory & Heap Allocation) |
| [`10_DataStructures`](../../10_DataStructures/) | Chapters 13–18 & Assignments 4, 5, 6 (Linked Lists, BST, Heaps, Graphs) |
| [`11_FileIO`](../../11_FileIO/) | Chapter 4 (Streams & File Processing) |
| [`12_AdvancedCPP`](../../12_AdvancedCPP/) | Assignment 5 (Huffman Coding Compression) |

---

## 7. 🔗 Navigation & Quick Links

- 🌐 [Master Academic Guide](../Master_Academic_Guide.md)
- 🏛️ [MIT 6.096 Syllabus](../mit6096/README.md)
- ⚡ [Stanford CS106X Syllabus](../cs106x/README.md)
- ⚙️ [Stanford CS106L Syllabus](../cs106l/README.md)
- 📋 [Master Repository Syllabus (`SYLLABUS.md`)](../../SYLLABUS.md)

---
*MiniLux0 — Stanford CS106B Syllabus Documentation*