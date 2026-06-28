<div align="center">

# Learning C++

*C++ course exercises and notes — John Purcell (Udemy). Tracking my progress lesson by lesson.*

[![C++17](https://img.shields.io/badge/C%2B%2B-17-00599C?style=flat-square&logo=cplusplus&logoColor=white)](https://en.cppreference.com/w/cpp/17)
[![GCC](https://img.shields.io/badge/GCC-15.2.0-F16822?style=flat-square&logo=gnu&logoColor=white)](https://gcc.gnu.org/)
[![Platform](https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows&logoColor=white)](https://github.com/brechtsanders/winlibs_mingw)
[![Editor](https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Progress](https://img.shields.io/badge/Progress-L16%20%2F%2082-yellow?style=flat-square)](#progress)

</div>

---

Personal learning repo for C++ — going from zero, building solid fundamentals before moving into computational physics and numerical simulations. Each lesson lives in its own `.cpp` file; each section has its own `makefile`.

## Progress

| # | Section | Lessons | Status |
|---|---------|---------|:------:|
| 01 | Getting Started | L01 – L05 | ✅ |
| 02 | Basic Syntax | L06 – L26 | 🔄 `L16` |
| 03 | Subroutines | L27 – L30 | ⬜ |
| 04 | Object Oriented Coding | L31 – L38 | ⬜ |
| 05 | Pointers and Memory | L39 – L52 | ⬜ |
| 06 | Inheritance | L53 – L55 | ⬜ |
| 07 | Odds and Ends | L56 – L57 | ⬜ |
| 08 | Particle Fire Simulation | L58 – L75 | ⬜ |
| 09 | Conclusion | L76 – L77 | ⬜ |
| 10 | Bonus | L78 – L81 | ⬜ |
| 11 | Advanced C++ | L82 | ⬜ |

## Environment

| Tool | Details |
|------|---------|
| Compiler | GCC 15.2.0 via [WinLibs](https://winlibs.com/) |
| Standard | C++17 |
| Flags | `-std=c++17 -Wall -Wextra -Wshadow -Wpedantic -g` |
| Editor | VSCode |
| Build | `make` per folder |

### Build a lesson

```bash
# From inside any section folder:
make        # compile
make run    # compile and run
```

> [!NOTE]
> Each section folder has its own `makefile`. No global build — compile only what you're working on.

## Exercises

Practice problems to reinforce what I have learned. Each exercise has only the instructions — I write the code myself.

```bash
cd exercises
make run-E01_VariableTypes   # compile and run
```

| # | Exercise | Topic | Difficulty |
|---|----------|-------|------------|
| E01 | Variable Types | int, double, char, bool | Easy |
| E02 | Name and Age | cin, string concatenation | Easy |
| E03 | Sizeof Types | sizeof for all basic types | Easy |
| E04 | Float Precision | float vs double, setprecision | Medium |
| E05 | Integer Division | Integer division trap | Medium |
| E06 | Char ASCII | char, casting, ASCII arithmetic | Easy |
| E07 | Grade Check | if / else | Easy |
| E08 | Age Classifier | if / else if / else chain | Medium |
| E09 | Compare Numbers | Comparing two numbers | Easy |
| E10 | Simple Calculator | Operators, division by zero | Hard |

## Repository Structure

```
LearningCpp/
├── 01_GettingStarted/      # L01–L05  · First program, text output
│   └── summary/
│       └── GettingStarted_Notes.md
├── 02_BasicSyntax/         # L06–L26  · Variables, types, loops, arrays
│   └── summary/
│       ├── BasicSyntax_Notes.md
│       └── LearningProgress.md
├── 03_Subroutines/         # L27–L30  · Functions, headers, prototypes
├── 04_ObjectOriented/      # L31–L38  · Classes, constructors, OOP
├── 05_PointersMemory/      # L39–L52  · Pointers, dynamic memory, references
├── 06_Inheritance/         # L53–L55  · Inheritance, encapsulation
├── 07_OddsAndEnds/         # L56–L57  · Two's complement, static keyword
├── 08_ParticleFire/        # L58–L75  · SDL2 particle fire project
├── 09_Conclusion/          # L76–L77  · Next steps
├── 10_Bonus/               # L78–L81  · Polymorphism, static libraries
├── 11_Advanced/            # L82      · Advanced C++
├── exercises/              # Practice exercises for L06–L15
│   ├── 01_variables/       # E01–E03  · Types, sizeof
│   ├── 02_operations/      # E04–E06  · Precision, ASCII
│   ├── 03_conditionals/    # E07–E09  · if, if-else, if-else if
│   └── 04_combined/        # E10      · Calculator
├── GLOSSARY.md             # C++ terms defined in simple language
├── MISTAKES.md             # Common errors and how to fix them
├── RESOURCES.md            # Useful links, tools, and references
└── CHANGELOG.md            # Progress log with dates
```

## Study Materials

| File | Description |
|------|-------------|
| `GLOSSARY.md` | C++ terms explained in simple language — growing as I learn |
| `MISTAKES.md` | Errors I have made and how I fixed them — so I do not repeat them |
| `RESOURCES.md` | Useful links: documentation, tools, practice sites, YouTube channels |
| `CHANGELOG.md` | When I completed each section — tracks my timeline |
| `*/summary/*_Notes.md` | Personal study notes per section with key concepts |

## Lesson Index

<details>
<summary><strong>01 — Getting Started</strong> · L01–L05 · ✅ Done</summary>

- L01 · Introducing C++
- L02 · Screen Resolution
- L03 · Setup and Installation
- L04 · Hello World
- L05 · Outputting Text

</details>

<details>
<summary><strong>02 — Basic Syntax</strong> · L06–L26 · 🔄 In progress</summary>

- L06 · Variables
- L07 · Strings
- L08 · User Input
- L09 · Binary Numbers and Computer Memory
- L10 · Integer Types
- L11 · Floating Point Types
- L12 · Char and Bool
- L13 · If
- L14 · If-Else
- L15 · If-Else If-Else
- **L16 · Comparing Floats** ← current
- L17 · Conditions
- L18 · While Loops
- L19 · Do-While Loops
- L20 · For Loops
- L21 · Break and Continue
- L22 · Arrays
- L23 · Multidimensional Arrays
- L24 · Sizeof and Arrays
- L25 · Sizeof Multidimensional Arrays
- L26 · Switch

</details>

<details>
<summary><strong>03 — Subroutines</strong> · L27–L30</summary>

- L27 · Functions
- L28 · Return Values
- L29 · Function Parameters
- L30 · Headers and Prototypes

</details>

<details>
<summary><strong>04 — Object Oriented Coding</strong> · L31–L38</summary>

- L31 · Classes
- L32 · Data Members
- L33 · Constructors and Destructors
- L34 · Getters and Setters
- L35 · String Streams
- L36 · Overloading Constructors
- L37 · The `this` Keyword
- L38 · Constructor Initialization Lists

</details>

<details>
<summary><strong>05 — Pointers and Memory</strong> · L39–L52</summary>

- L39 · Pointers
- L40 · Arithmetic
- L41 · Pointers and Arrays
- L42 · Pointer Arithmetic
- L43 · Char Arrays
- L44 · Reversing a String
- L45 · References
- L46 · The `const` Keyword
- L47 · Copy Constructors
- L48 · The `new` Operator
- L49 · Returning Objects from Functions
- L50 · Allocating Memory
- L51 · Arrays and Functions
- L52 · Namespaces

</details>

<details>
<summary><strong>06 — Inheritance</strong> · L53–L55</summary>

- L53 · Inheritance
- L54 · Encapsulation
- L55 · Constructor Inheritance

</details>

<details>
<summary><strong>07 — Odds and Ends</strong> · L56–L57</summary>

- L56 · Two's Complement
- L57 · Static Keyword

</details>

<details>
<summary><strong>08 — Particle Fire Simulation</strong> · L58–L75</summary>

- L58 · Particle Fire Explosion
- L59 · Using C++ Libraries
- L60 · Acquiring SDL
- L61 · A Basic SDL Program
- L62 · Creating an SDL Window
- L63 · Textures, Renderers and Buffers
- L64 · Setting Pixel Colors
- L65 · Creating the Screen Class
- L66 · Bit Shifting and Colors
- L67 · Adding a Set Pixel Method
- L68 · Animating Colors
- L69 · Creating Particles
- L70 · Animating Particles
- L71 · Creating an Explosion
- L72 · Ensuring Constant Speed
- L73 · Bitwise AND
- L74 · Implementing Box Blur
- L75 · Tweaking Particle Motion

</details>

<details>
<summary><strong>09 — Conclusion</strong> · L76–L77</summary>

- L76 · Languages Overview
- L77 · What Next

</details>

<details>
<summary><strong>10 — Bonus</strong> · L78–L81</summary>

- L78 · OOP Design Considerations
- L79 · Postfix and Prefix
- L80 · Polymorphism
- L81 · Creating Static Libraries

</details>

<details>
<summary><strong>11 — Advanced C++</strong> · L82</summary>

- L82 · Advanced C++ Course

</details>

---

*MiniLux0 · Physics @ Universidad Nacional de Ingeniería (UNI) · Lima, Perú*