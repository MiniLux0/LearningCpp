# ⚙️ Stanford CS106L: Standard C++ Programming (Modern C++)

> **Stanford University — Department of Computer Science**  
> 🎓 **Level**: Advanced / Modern Engineering  
> 👨‍🏫 **Course Directors**: Avery Wang, Fabian Boemer, Sathya Chitturi, Chloe Barreau  
> 📖 **Official Source**: [Stanford CS106L Course Site](http://web.stanford.edu/class/cs106l/)  
> 🎯 **Primary Focus**: Modern C++ standards (C++11/17/20), memory safety, template container design, move semantics, RAII, and smart pointers.

---

## 1. 🎯 Course Overview & Educational Vision

Stanford CS106L is Stanford's advanced companion course dedicated exclusively to **Modern Standard C++**. While traditional C++ courses focus on C-style constructs, CS106L teaches modern C++ engineering: type safety, compile-time abstractions, zero-cost abstractions, automated resource management, and move semantics.

In this repository, Stanford CS106L serves as the **Modern C++ engineering standard**, updating all classic algorithms and object concepts to C++11/17/20 standards.

---

## 2. 🧠 Key Technical Competencies & Learning Outcomes

1. **Modern Type System**: Uniform Initialization `{}`, brace initialization, type inference (`auto`), structured bindings (`auto [k, v]`).
2. **Streams & Error States**: `std::stringstream`, file streams (`ifstream`, `ofstream`), stream flags (`good`, `fail`, `eof`), safe `getline` loops.
3. **STL Containers & Iterators**: Custom iterator design (`begin()`, `end()`, `operator++`, `operator*`), range-based loops, iterator categories.
4. **Functional Programming**: Lambda expressions (`[capture](params) { body }`), functors, predicates, `<algorithm>` library (`std::find_if`, `std::transform`, `std::accumulate`).
5. **Class Lifecycle & Resource Management**: Const-Correctness, Operator Overloading, Special Member Functions (Rule of 0 / 3 / 5), Move Semantics (`std::move`, `T&&`), RAII, Smart Pointers (`unique_ptr`, `shared_ptr`, `weak_ptr`).

---

## 3. 📚 Comprehensive 17-Lecture PDF Syllabus

Extracted directly from all 17 PDF lectures in [`files/cs106l/lectures/`](lectures/):

| # | Lecture PDF | Core Technical Topics Extracted | Repository Module |
|---|-------------|---------------------------------|-------------------|
| **L01** | [`Welcome to C++!.pdf`](lectures/Welcome%20to%20C++!.pdf) | Evolution of standards (C++98 $\rightarrow$ C++11 $\rightarrow$ C++17 $\rightarrow$ C++20), why C++ dominates high-performance systems. | [`01_GettingStarted`](../../01_GettingStarted/) |
| **L02** | [`WLecture1_intro.pdf`](lectures/WLecture1_intro.pdf) | Zero-cost abstractions, compilation pipeline, static type system, header files, `std::` scope. | [`01_GettingStarted`](../../01_GettingStarted/) |
| **L03** | [`WL2-Structures.pdf`](lectures/WL2-Structures.pdf) | Struct memory alignment, `std::pair`, `std::tuple`, structured bindings (C++17 `auto [x, y] = pair`). | [`02_BasicSyntax`](../../02_BasicSyntax/) |
| **L04** | [`WLecture_3_Init_and_Ref.pdf`](lectures/WLecture_3_Init_and_Ref.pdf) | Uniform Initialization `{}` (brace initialization), prevention of narrowing conversions, Lvalues vs Rvalues, references (`&`, `const &`). | [`02_BasicSyntax`](../../02_BasicSyntax/) / [`03_Subroutines`](../../03_Subroutines/) |
| **L05** | [`WL4_Streams.pdf`](lectures/WL4_Streams.pdf) | Stream hierarchy, buffer flushing (`std::endl` vs `\n`), `std::stringstream`, file I/O (`ifstream`, `ofstream`), state flags (`good`, `fail`, `eof`), `getline`. | [`11_FileIO`](../../11_FileIO/) |
| **L06** | [`WL5_Containers.pdf`](lectures/WL5_Containers.pdf) | Sequence containers (`vector`, `deque`, `list`), associative containers (`map`, `set`, `unordered_map`), performance trade-offs. | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **L07** | [`WL6_Iterators.pdf`](lectures/WL6_Iterators.pdf) | Iterator abstraction pattern, sentinel bounds (`begin()`, `end()`), range-based `for` loops, iterator categories, iterator invalidation. | [`10_DataStructures`](../../10_DataStructures/) / [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **L08** | [`WL7_Templates.pdf`](lectures/WL7_Templates.pdf) | Generic programming, function templates (`template <typename T>`), template argument deduction, specialization. | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **L09** | [`WL8_Functions.pdf`](lectures/WL8_Functions.pdf) | Function pointers, Functors (`operator()`), Lambda expressions (`[capture](params) { body }`), STL algorithms (`<algorithm>`). | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **L10** | [`WL9-STL-Summary.pdf`](lectures/WL9-STL-Summary.pdf) | Deep-dive summary of STL architecture, container trade-offs, cache friendliness of contiguous memory. | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **L11** | [`WL10_Temp_classes.pdf`](lectures/WL10_Temp_classes.pdf) | Class templates (`template <typename T> class Container`), template header organization (`.h` / `.tpp` pattern). | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |
| **L12** | [`WL11_Const.pdf`](lectures/WL11_Const.pdf) | Const-Correctness engineering, `const` member functions, `const` iterators (`cbegin()`), `const_cast` hazards, `mutable` keyword. | [`06_Pointers`](../../06_Pointers/) / [`07_Classes`](../../07_Classes/) |
| **L13** | [`WL12_Operators.pdf`](lectures/WL12_Operators.pdf) | Overloading operators (`operator+`, `operator+=`, `operator<<`, `operator>>`, `operator==`, `operator[]`), member vs non-member operators. | [`07_Classes`](../../07_Classes/) |
| **L14** | [`WL13_SMF.pdf`](lectures/WL13_SMF.pdf) | Object lifecycle: Default Constructor, Destructor, Copy Constructor, Copy Assignment Operator, Rule of 0 / 3. | [`09_MemoryManagement`](../../09_MemoryManagement/) |
| **L15** | [`WL14-Move.pdf`](lectures/WL14-Move.pdf) | Lvalues vs Rvalues, Rvalue References (`T&&`), `std::move`, Move Constructor, Move Assignment Operator, Rule of 5, zero-copy transfers. | [`09_MemoryManagement`](../../09_MemoryManagement/) |
| **L16** | [`WL15_RAII.pdf`](lectures/WL15_RAII.pdf) | Resource Acquisition Is Initialization (RAII), exception safety, smart pointers (`unique_ptr`, `shared_ptr`, `weak_ptr`), `make_unique`, `make_shared`. | [`09_MemoryManagement`](../../09_MemoryManagement/) |
| **L17** | [`WL16-Wrapup.pdf`](lectures/WL16-Wrapup.pdf) | Modern C++ wrap-up, preview of C++17/20 features (`std::optional`, `std::variant`, Concepts, Ranges, Coroutines). | [`12_AdvancedCPP`](../../12_AdvancedCPP/) |

---

## 4. 💻 Assignments & Practical Projects Catalog

Projects located in [`files/cs106l/assignments/`](assignments/):

| Project Folder | Primary Technical Concepts | Practical Engineering Goals |
|----------------|----------------------------|-----------------------------|
| 🔗 [`linked-list-starter`](assignments/linked-list-starter/) | Custom Iterators, Special Member Functions, Template Container | Implement custom `begin()` and `end()` iterators for a singly linked list supporting range-based `for` loops. |
| 🗂️ [`HashMap`](assignments/HashMap/) | Template Class `HashMap<K,V>`, Separate Chaining, Operator Overloading (`[]`) | Build a generic template hash map container from scratch with custom bucket iterators and `const` correctness. |
| 🌐 [`WikiRacer`](assignments/WikiRacer/) | Priority Queues, Web String Parsing, Streams, `unordered_set` | Implement an algorithmic Wikipedia ladder finder game using BFS with Priority Queues to find shortest link paths. |

---

## 5. 👥 Discussion Sections & Practice Exercises

CS106L includes interactive code exercises focusing on:
- Writing custom lambda predicates for `<algorithm>` functions (`std::find_if`, `std::transform`).
- Refactoring raw pointer management into `std::unique_ptr` and RAII wrappers.
- Writing custom template container iterators with `begin()` and `end()`.

---

## 6. 🗺️ Repository Alignment & Module Mapping

| Repository Module | CS106L Lectures & Projects Alignment |
|-------------------|--------------------------------------|
| [`02_BasicSyntax`](../../02_BasicSyntax/) | Lectures 3–4 (Structures, Uniform Initialization `{}`) |
| [`06_Pointers`](../../06_Pointers/) | Lecture 12 (Const-Correctness Engineering) |
| [`07_Classes`](../../07_Classes/) | Lecture 13 (Operator Overloading) & HashMap Project |
| [`09_MemoryManagement`](../../09_MemoryManagement/) | Lectures 14–16 (SMF, Rule of 0/3/5, Move Semantics, RAII, Smart Pointers) |
| [`10_DataStructures`](../../10_DataStructures/) | Lecture 7 (Iterators) & linked-list-starter Project |
| [`11_FileIO`](../../11_FileIO/) | Lecture 5 (Stream Processing & State Flags) |
| [`12_AdvancedCPP`](../../12_AdvancedCPP/) | Lectures 6, 8, 9, 10, 11, 17 & WikiRacer Project |

---

## 7. 🔗 Navigation & Quick Links

- 🌐 [Master Academic Guide](../Master_Academic_Guide.md)
- 🏛️ [MIT 6.096 Syllabus](../mit6096/README.md)
- 🌲 [Stanford CS106B Syllabus](../cs106b/README.md)
- ⚡ [Stanford CS106X Syllabus](../cs106x/README.md)
- 📋 [Master Repository Syllabus (`SYLLABUS.md`)](../../SYLLABUS.md)

---
*MiniLux0 — Stanford CS106L Syllabus Documentation*
