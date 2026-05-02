# Learning C++

Personal repository to document my C++ learning journey.  
Organized by topic, following a self-paced syllabus alongside my university course (CC112 — UNI).

---

## Topics

| # | Topic | Status |
|---|-------|--------|
| 01 | Basics (variables, types, control flow) | ✅ |
| 02 | Functions and recursion | ✅ |
| 03 | Arrays and sorting algorithms | ✅ |
| 04 | Pointers and strings | 🔄 In progress |
| 05 | Structs and user-defined types | ⏳ |
| 06 | Dynamic memory | ⏳ |
| 07 | File I/O | ⏳ |
| 08 | OOP — Classes and objects | ⏳ |

---

## Folder structure

```
LearningCpp/
├── 01-basics/
├── 02-functions/
├── 03-arrays/
├── 04-pointers/
├── 05-structs/
├── 06-dynamic-memory/
├── 07-file-io/
└── 08-oop/
```

---

## How to compile

Uses a custom `Makefile` per folder. Available commands:

```bash
make                      # build everything (normal)
make asan                 # build everything (with AddressSanitizer)
make run-<name>           # build and run <name>.cpp
make run-asan-<name>      # same, with ASan (catches memory bugs)
make clean                # remove build artifacts
```

Builds land in `build/` (normal) or `buildasan/` (ASan).  
Flags: `-std=c++17 -Wall -Wextra -Wshadow -Wpedantic -g`

Environment: MSYS2 + g++ + VSCode on Windows.