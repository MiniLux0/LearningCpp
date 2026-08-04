<div align="center">

# ⚙️ Stanford CS106L — Standard C++ Programming

*Stanford University · Department of Computer Science*

[![🏠 Root README](https://img.shields.io/badge/🏠_Back_to-Root_README-00599C?style=for-the-badge)](../../README.md)
[![📂 Files Hub](https://img.shields.io/badge/📂_Back_to-Files_Hub-555555?style=for-the-badge)](../README.md)

</div>

---

## What is CS106L?

CS106L teaches you **modern C++** — the way professional engineers actually write it today. While MIT 6.096 teaches classic C++ syntax, CS106L teaches the features introduced in C++11, C++17, and C++20 that make code safer, faster, and cleaner.

- 🎓 **Level**: Advanced (take after Module 05 or alongside Modules 06–12)
- 🔗 **Official page**: [Stanford CS106L](http://web.stanford.edu/class/cs106l/)

> **When to open this folder:** Start reading CS106L lectures when you reach Module 06 (Pointers). The modern C++ perspective will complement and deepen every module from there onward.

---

## 📚 What You Learn

| Topic | What it means in plain English |
|-------|-------------------------------|
| **Uniform Initialization `{}`** | A safer, consistent way to initialize any variable |
| **`auto` & structured bindings** | Let the compiler figure out the type so you don't have to repeat it |
| **STL containers** | `vector`, `map`, `set`, `unordered_map` — when to use each |
| **Iterators** | Pointers that work on any container (used in range-based `for` loops) |
| **Lambdas** | Anonymous functions you can pass around like values |
| **Const-Correctness** | Protecting data from accidental changes — a professional habit |
| **Operator Overloading** | Making your classes work with `+`, `<<`, `==` etc. |
| **Rule of 0 / 3 / 5** | How to manage object copying and moving correctly |
| **Move Semantics** | Transferring resources without copying — huge for performance |
| **RAII & Smart Pointers** | Never manually `delete` again — `unique_ptr` / `shared_ptr` do it for you |

---

## 📋 Lecture PDF Map

17 lecture PDFs in [`lectures/`](lectures/):

| # | PDF | Topics | Module |
|:-:|-----|--------|--------|
| L01 | [`Welcome to C++!.pdf`](lectures/Welcome%20to%20C++!.pdf) | Why modern C++? Evolution from C++98 to C++20 | [`01_GettingStarted`](../../01_GettingStarted/) |
| L02 | [`WLecture1_intro.pdf`](lectures/WLecture1_intro.pdf) | Compilation pipeline, static types, header files | [`01_GettingStarted`](../../01_GettingStarted/) |
| L03 | [`WL2-Structures.pdf`](lectures/WL2-Structures.pdf) | Structs, `std::pair`, structured bindings (C++17) | [`02_BasicSyntax`](../../02_BasicSyntax/) |
| L04 | [`WLecture_3_Init_and_Ref.pdf`](lectures/WLecture_3_Init_and_Ref.pdf) | Uniform init `{}`, narrowing prevention, references | [`02_BasicSyntax`](../../02_BasicSyntax/) |
| L05 | [`WL4_Streams.pdf`](lectures/WL4_Streams.pdf) | Streams, file I/O, state flags, `getline` | [`11_FileIO`](../../11_FileIO/) |
| L06 | [`WL5_Containers.pdf`](lectures/WL5_Containers.pdf) | `vector`, `map`, `set`, `unordered_map` — trade-offs | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| L07 | [`WL6_Iterators.pdf`](lectures/WL6_Iterators.pdf) | Iterators, `begin()`/`end()`, range-based `for` | [`10_DataStructures`](../../10_DataStructures/) |
| L08 | [`WL7_Templates.pdf`](lectures/WL7_Templates.pdf) | Function & class templates, type deduction | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| L09 | [`WL8_Functions.pdf`](lectures/WL8_Functions.pdf) | Lambdas, functors, `std::find_if`, `std::transform` | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| L10 | [`WL9-STL-Summary.pdf`](lectures/WL9-STL-Summary.pdf) | Full STL summary & best practices | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| L11 | [`WL10_Temp_classes.pdf`](lectures/WL10_Temp_classes.pdf) | Template classes, `.tpp` pattern | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| L12 | [`WL11_Const.pdf`](lectures/WL11_Const.pdf) | Const-correctness, `const` methods, `cbegin()` | [`06_Pointers`](../../06_Pointers/) |
| L13 | [`WL12_Operators.pdf`](lectures/WL12_Operators.pdf) | Operator overloading: `+`, `<<`, `==`, `[]` | [`07_Classes`](../../07_Classes/) |
| L14 | [`WL13_SMF.pdf`](lectures/WL13_SMF.pdf) | Copy constructor, copy assignment, Rule of 0/3 | [`09_MemoryManagement`](../../09_MemoryManagement/) |
| L15 | [`WL14-Move.pdf`](lectures/WL14-Move.pdf) | `std::move`, rvalue references `T&&`, Rule of 5 | [`09_MemoryManagement`](../../09_MemoryManagement/) |
| L16 | [`WL15_RAII.pdf`](lectures/WL15_RAII.pdf) | RAII, `unique_ptr`, `shared_ptr`, `weak_ptr` | [`09_MemoryManagement`](../../09_MemoryManagement/) |
| L17 | [`WL16-Wrapup.pdf`](lectures/WL16-Wrapup.pdf) | C++17/20 preview: `optional`, `variant`, Concepts | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |

---

## 💻 Projects

3 hands-on projects in [`assignments/`](assignments/):

| Project | What you build | Key skills |
|---------|----------------|------------|
| [`linked-list-starter/`](assignments/linked-list-starter/) | A linked list with custom iterators for range-based `for` | Iterators, Special Member Functions |
| [`HashMap/`](assignments/HashMap/) | A generic `HashMap<K, V>` container from scratch | Templates, operator overloading, const-correctness |
| [`WikiRacer/`](assignments/WikiRacer/) | Shortest path finder between Wikipedia articles | Priority queues, streams, `unordered_set`, BFS |

> These projects are **advanced** — tackle them after completing Modules 09–12.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
