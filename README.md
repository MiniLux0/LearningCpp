<div align="center">

# Learning C++

*Mi plan de aprendizaje de C++ desde cero — sigo la secuencia de MIT 6.096 Introduction to C++ (IAP 2011).*

[![C++17](https://img.shields.io/badge/C%2B%2B-17-00599C?style=flat-square&logo=cplusplus&logoColor=white)](https://en.cppreference.com/w/cpp/17)
[![GCC](https://img.shields.io/badge/GCC-15.2.0-F16822?style=flat-square&logo=gnu&logoColor=white)](https://gcc.gnu.org/)
[![Platform](https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows&logoColor=white)](https://github.com/brechtsanders/winlibs_mingw)
[![Editor](https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Progress](https://img.shields.io/badge/Progress-L30%20%2F%2060-yellow?style=flat-square)](#progress)

</div>

---

Repo personal de aprendizaje de C++ — construyendo fundamentos sólidos antes de pasar a física computacional y simulaciones numéricas.

## Progress

| # | Carpeta | Lecciones | Lectura MIT | Estado |
|---|---------|-----------|-------------|:------:|
| 01 | Getting Started | L01 – L05 | Lecture 1 — Introduction | ✅ |
| 02 | Basic Syntax | L06 – L22 | Lecture 2 — Flow of Control | 🔄 |
| 03 | Subroutines | L23 – L26 | Lecture 3 — Functions | ✅ |
| 04 | Arrays and Strings | L27 – L30 | Lecture 4 — Arrays and Strings | 🔄 |
| 05 | Pointers | L31 – L38 | Lecture 5 — Pointers | ⬜ |
| 06 | Classes | L39 – L44 | Lecture 6 — Classes | ⬜ |
| 07 | OOP | L45 – L52 | Lecture 7 — Object-Oriented Programming | ⬜ |
| 08 | Memory Management | L53 – L60 | Lecture 8 — Memory Management | ⬜ |

> 📌 Para el desglose detallado lección por lección, consulta el [TEMARIO.md](TEMARIO.md).

## Environment

| Tool | Details |
|------|---------|
| Compiler | GCC 15.2.0 via [WinLibs](https://winlibs.com/) |
| Standard | C++17 |
| Flags | `-std=c++17 -Wall -Wextra -Wshadow -Wpedantic -g` |
| Editor | VSCode |
| Build | `make` por carpeta |

## Repository Structure

```
LearningCpp/
├── .gitignore
├── GLOSSARY.md
├── README.md
├── RESOURCES.md
├── TEMARIO.md
├── makefile
│
├── 01_GettingStarted/          # L01–L05  · MIT Lecture 1
├── 02_BasicSyntax/             # L06–L22  · MIT Lecture 2 (incluye exercise/)
├── 03_Subroutines/             # L23–L26  · MIT Lecture 3 (code/, theory/, exercise/)
├── 04_ArraysStrings/           # L27–L30  · MIT Lecture 4 (code/, theory/, exercise/)
├── 05_Pointers/                # L31–L38  · MIT Lecture 5 (code/, theory/, exercise/)
├── 06_Classes/                 # L39–L44  · MIT Lecture 6 (code/, theory/, exercise/)
├── 07_OOP/                     # L45–L52  · MIT Lecture 7 (code/, theory/, exercise/)
├── 08_MemoryManagement/        # L53–L60  · MIT Lecture 8 (code/, theory/, exercise/)
└── files/                      # Materiales MIT 6.096 (lectures, assignments, project)
```

## Study Materials

| Archivo | Descripción |
|---------|-------------|
| [TEMARIO.md](TEMARIO.md) | Temario completo de 60 lecciones con detalle de temas y subtemas |
| [GLOSSARY.md](GLOSSARY.md) | Términos de C++ explicados de forma concisa |
| [RESOURCES.md](RESOURCES.md) | Documentación, herramientas y recursos |

---

*MiniLux0*