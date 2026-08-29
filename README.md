<div align="center">

# 🚀 LearningCpp

### **El Curso Interactivo y Visual de C++ Moderno**
**De Cero Absoluto a Desarrollador Profesional de la Industria (C++17 / C++20)**

[![C++17](https://img.shields.io/badge/C%2B%2B-17%2F20-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)](https://en.cppreference.com/w/cpp/17)
[![GCC](https://img.shields.io/badge/GCC-13%2B-F16822?style=for-the-badge&logo=gnu&logoColor=white)](https://gcc.gnu.org/)
[![Plataforma](https://img.shields.io/badge/Plataforma-Windows%20%7C%20Linux%20%7C%20macOS-0078D4?style=for-the-badge&logo=windows&logoColor=white)](README.md)
[![PDF Syllabus](https://img.shields.io/badge/📥_Descargar-Syllabus_PDF-dc2626?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](LearningCpp_Syllabus_Oficial.pdf)
[![Discord](https://img.shields.io/badge/Discord-Code_Lab-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/JExCwZ3YyC)

<br/>

[📜 Syllabus Completo](SYLLABUS.md) · [🏛️ Arquitectura & Filosofía](docs/ARCHITECTURE.md) · [📋 Backlog de Tareas](docs/BACKLOG.md) · [💬 Comunidad de Discord](https://discord.gg/JExCwZ3YyC)

</div>

---

## 💡 ¿Por qué existe LearningCpp?

La mayoría de los cursos de C++ tradicionales cometen uno de dos errores fatales:
1. **Enseñan C++ arcaico de hace 25 años:** Empiezan con punteros crudos obligatorios, `printf`, arreglos de C (`int arr[]`), `malloc`/`free` y `using namespace std;`, obligando al alumno a desaprender malos hábitos más adelante.
2. **Asumen que ya eres un veterano de la ingeniería:** Usan jerga académica elitista y asumen que ya entiendes cómo funciona el hardware, la memoria virtual, los enlazadores o los flujos de entrada.

**LearningCpp rompe con ambos paradigmas:**
* **C++ Moderno desde el Día 1:** Aprendes con `std::string`, inicialización uniforme `{}` segura, `std::vector`, `constexpr`, `std::unique_ptr` (RAII) y tuberías de rangos de C++20 (`|`).
* **Nivel Cero Absoluto:** Si nunca en tu vida has visto una línea de código y no sabes qué es la memoria RAM o un compilador, este curso empieza contigo en mente.

---

## 🏛️ Los 4 Pilares Pedagógicos

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 🎯 1. PRINCIPIO DE LA ESCALERA                                                         │
│    El aprendizaje es estrictamente progresivo. Cada lección se apoya ÚNICAMENTE en lo   │
│    enseñado previamente. Cero saltos mágicos de conocimiento ni "cajas negras".        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🐞 2. METODOLOGÍA "BREAK-FIRST, FIX-LATER"                                             │
│    Cada característica moderna existe porque algo en el lenguaje clásico era inseguro. │
│    El alumno primero detona un bug real en un demo intencional (Undefined Behavior,    │
│    Memory Leak, Slicing) para sentir el dolor del fallo antes de recibir la solución.  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🧠 3. MODELOS MENTALES DE MEMORIA (HARDWARE REAL)                                      │
│    No memorizamos sintaxis en abstracto: visualizamos físicamente qué ocurre en la    │
│    RAM (Stack vs Heap, direcciones hexadecimales 0x..., VTable y ciclo de vida RAII).  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 🌉 4. SCAFFOLDING & FADING ESTRICTO                                                    │
│    Usamos analogías intuitivas para romper el hielo, pero desvanecen de inmediato hacia│
│    la terminología técnica profesional que exige la industria del software.           │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🧭 El Bucle del Ciclo de Aprendizaje

Cada lección del curso forma parte de un circuito de aprendizaje estructurado en 5 pasos:

```text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   1. TEORÍA     │ ──> │  2. LABORATORIO │ ──> │   3. BUG DEMO   │ ──> │    4. RETO      │
│  Conceptos +    │     │   Exploración   │     │  Trampa real de │     │  Misión con     │
│   Modelos RAM   │     │  guiada en C++  │     │  código roto    │     │ código + tests  │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
                                                                                 │
                                                                                 ▼
                                                                        ┌─────────────────┐
                                                                        │  5. CHEATSHEET  │
                                                                        │  Hoja de repaso │
                                                                        │ técnica rápida  │
                                                                        └─────────────────┘
```

1. **Teoría (`theory/LXX_*.md`):** Explicación exhaustiva con animaciones visuales (Manim) y diagramas de hardware.
2. **Laboratorio Guiado (`lab/LXX_*.cpp`):** Código de exploración comentado paso a paso para compilar a mano en tu terminal.
3. **Demo de Bug Intencional (`lab/demos/DXX_*.cpp`):** Código roto a propósito para experimentar fallos reales en la consola.
4. **Reto Práctico (`exercise/EXX_*/`):** Reto con contexto narrativo, código con `TODOs` y su carpeta `solution/` con el código resuelto.
5. **Hoja de Repaso (`summary/ModuleXX_Cheatsheet.md`):** Resumen de consulta rápida con jerga técnica estricta.

---

## 🗺️ Mapa de Ruta del Curso (15 Módulos / 6 Fases)

| Fase | # | Módulo | Lecc. | Eje Conceptual Clave | Proyecto Integrador | Estado |
|:---:|:---:|---|:---:|---|---|:---:|
| **Fase 1: Fundamentos** | **01** | [**Getting Started**](01_GettingStarted/) | 7 | ¿Qué es programar?, compilador `g++`, `cout`/`cin`, streams | Terminal Interactiva | ✅ |
| | **02** | [**Fundamental Types**](02_FundamentalTypes/) | 7 | Tipado estático, `{}` inicialización, casting explícito | Split the Bill Calculator | ✅ |
| | **03** | [**Scope & Control Flow**](03_ScopeAndControlFlow/) | 8 | Ámbitos, `if`/`switch`, bucles, prevención de UB | Cajero / Taberna RPG | ✅ |
| **Fase 2: Funciones & Textos** | **04** | [**Functions**](04_Functions/) | 8 | Paso por valor, aislamiento, RNG moderno `<random>` | Generador Atributos RPG | ✅ |
| | **05** | [**Constants & Strings**](05_ConstantsAndStrings/) | 6 | Inmutabilidad `constexpr`, `std::string`, `string_view` | Generador de Claves | ✅ |
| **Fase 3: Colecciones** | **06** | [**Arrays & Vectors**](06_ArraysAndVectors/) | 9 | `std::vector`, límites seguros `.at()`, multi-archivo | Registro Calificaciones | 🔄 |
| | **07** | [**Compound Types**](07_CompoundTypes/) | 7 | `struct`, `enum class`, Designated Initializers C++20 | Bestiario RPG V1 | 🔄 |
| **Fase 4: Memoria Real** | **08** | [**References & Addresses**](08_ReferencesAndAddresses/) | 8 | Direcciones `&`, paso por referencia `const &`, alias | Bestiario V2 (Zero-Copy) | 🔄 |
| | **09** | [**Dynamic Memory**](09_DynamicMemory/) | 9 | Heap, punteros, `std::unique_ptr`, `std::move`, RAII | Bestiario V3 (Heap RAII) | 🔄 |
| **Fase 5: POO Moderna** | **10** | [**Classes & Encapsulation**](10_Classes/) | 10 | Encapsulamiento `m_`, `const` methods, operadores `<<`/`==` | Bestiario V4 (Multi-Archivo) | 🔄 |
| | **11** | [**Inheritance**](11_Inheritance/) | 7 | Herencia simple `: public`, cadenas de constructores, slicing | Jerarquía del Bestiario | 🔄 |
| | **12** | [**Polymorphism**](12_Polymorphism/) | 8 | `virtual`, VTable, `override`, interfaces puras, downcasting | El Coliseo (Game Loop) | 🔄 |
| **Fase 6: Profesional** | **13** | [**Error Handling**](13_ErrorHandling/) | 7 | Stack Unwinding, excepciones de dominio, `std::optional` | Motor Mazmorras Resiliente | 🔄 |
| | **14** | [**Templates & Lambdas**](14_TemplatesAndLambdas/) | 8 | Polimorfismo estático, templates en `.hpp`, NTTP, lambdas | Pipeline Genérico Eventos | 🔄 |
| | **15** | [**STL Algorithms & Ranges**](15_STLAlgorithms/) | 8 | "No Raw Loops", C++20 Ranges `\|`, asincronía, Capstone | El Motor RPG Definitivo | 🔄 |

> **Leyenda:** ✅ *Módulo completo e implementado* · 🔄 *Módulo planificado / en desarrollo activo*.

---

## ⚡ Guía Rápida: Cómo Empezar

### 1. Clona el Repositorio
```bash
git clone https://github.com/tu-usuario/LearningCpp.git
cd LearningCpp
```

### 2. Verifica tu Compilador C++
Asegúrate de contar con un compilador moderno (GCC 13+, Clang 16+ o MSVC 2022):
```bash
g++ --version
```

### 3. Entra al Primer Módulo y Compila a Mano
No usamos Makefiles ni herramientas complejas en los primeros módulos para que pierdas el miedo a la terminal:
```bash
# Entra al laboratorio del Módulo 01
cd 01_GettingStarted/lab

# Compila tu primer programa con el estándar moderno
g++ -std=c++17 L02_TuPrimerPrograma.cpp -o app

# Ejecuta tu programa
./app        # En Linux/macOS
.\app.exe    # En Windows PowerShell
```

---

## 🗂️ Arquitectura de Carpetas del Repositorio

Cada módulo sigue estrictamente una estructura modular idéntica y predecible:

```text
XX_NombreDelModulo/
├── README.md                  ← Índice general del módulo y objetivos
├── theory/                    ← Lecciones teóricas en Markdown
│   ├── LXX_Nombre.md
│   └── assets/                ← Diagramas y animaciones visuales Manim
├── lab/                       ← Laboratorios guiados en código C++
│   ├── LXX_Nombre.cpp
│   └── demos/                 ← Demos de bugs intencionales aislados
│       └── DXX_NombreBug.cpp
├── exercise/                  ← Retos prácticos con lore y desafíos
│   ├── README.md              ← Índice de retos del módulo
│   └── EXX_NombreDelReto/
│       ├── README.md          ← Misión, historia y objetivos del reto
│       ├── EXX_Nombre.cpp     ← Reto con TODOs a resolver
│       └── solution/          ← Solución oficial verificada
│           └── EXX_Nombre.cpp
└── summary/
    └── ModuleXX_Cheatsheet.md ← Hoja de repaso técnico para consulta rápida
```

---

## 💬 Comunidad & Aprendizaje en Grupo

Aprender C++ no tiene por qué ser un viaje solitario. Únete a nuestro servidor de Discord **Code Lab** para:

* 👥 **Aprender en comunidad:** Comparte tu avance con otros estudiantes en tu misma fase.
* 🆘 **Resolver dudas:** Pide ayuda cuando un ejercicio o error del compilador se resista.
* 💡 **Debatir sobre C++ Moderno:** Discute sobre patrones de diseño, optimización de hardware y mejores prácticas.

👉 [**Unirse a Code Lab en Discord**](https://discord.gg/JExCwZ3YyC)

---

## 🤝 Cómo Contribuir

Este curso es un proyecto de código abierto impulsado por la comunidad. Si encuentras una errata, deseas proponer un nuevo demo de bug o mejorar una explicación:

1. Revisa [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) y [`GEMINI.md`](GEMINI.md) para conocer las reglas de estilo y filosofía pedagógica.
2. Abre un **Issue** describiendo la mejora o problema encontrado.
3. Envía tu **Pull Request** respetando la arquitectura estandarizada de carpetas y banners de código.

---

<div align="center">
  <sub>Maintained with ❤️ by <strong>MiniLux0</strong> · 2026</sub><br>
  <sub>Un curso interactivo de C++ Moderno desde Cero Absoluto hasta Grado Profesional.</sub>
</div>
