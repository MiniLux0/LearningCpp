<div align="center">

# 📂 docs/ — Build & Compilation Guides

*Technical documentation for compiling, running, and understanding the build system used in this repository.*

[![🏠 Root README](https://img.shields.io/badge/🏠_Back_to-Root_README-00599C?style=for-the-badge)](../README.md)
[![📜 Syllabus](https://img.shields.io/badge/📜_Full-Syllabus-F16822?style=for-the-badge)](../SYLLABUS.md)

</div>

---

## 📋 Guide Index

| Guide | File | When to use it |
|-------|------|----------------|
| ⚙️ **Compilation Guide** | [`COMPILATION_GUIDE.md`](COMPILATION_GUIDE.md) | **Start here** if you have never compiled C++ from a terminal. Covers manual `g++` commands and `make` basics. |
| 🛠️ **Makefile Guide** | [`MAKEFILE_GUIDE.md`](MAKEFILE_GUIDE.md) | Read this when you want to understand what each compiler flag does (`-Wall`, `-Wextra`, `-fsanitize`, etc.) or when you want to reuse the build template in your own projects. |

---

## ⚙️ Quick Command Reference

> Run these commands from inside any module's `code/` or `exercise/` directory.

```bash
make                        # Compile all .cpp files → output goes to build/
make run-L01_HelloWorld     # Compile + run a specific lesson
make asan                   # Compile with AddressSanitizer (memory leak detection)
make clean                  # Delete all compiled output
make help                   # Show available targets
```

---

## 🧭 Module Compilation — Where is each Makefile?

Every module in this repo has its own independent `Makefile` inside its `code/` and `exercise/` subdirectories:

```
01_GettingStarted/
├── code/
│   ├── makefile        ← compile lessons here
│   └── L01_HelloWorld.cpp
└── exercise/
    ├── makefile        ← compile exercises here
    └── E01_HelloWorld.cpp
```

The root `makefile` at the repository level can be **copied into any new directory** and works out-of-the-box with zero modifications.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
