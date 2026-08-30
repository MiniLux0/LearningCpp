<div align="center">

# 🚀 LearningCpp

### **El Curso Interactivo y Visual de C++ Moderno**
**De Cero Absoluto a C++ Moderno — Fundamentos de Grado Profesional (C++17 Base · Evolución C++20)**

[![Autor](https://img.shields.io/badge/Autor-Jesus%20Vera%20V.%20(MiniLux0)-10b981?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MiniLux0)
[![C++17 Base](https://img.shields.io/badge/C%2B%2B-17_Base-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)](https://en.cppreference.com/w/cpp/17)
[![GCC](https://img.shields.io/badge/GCC-13%2B-F16822?style=for-the-badge&logo=gnu&logoColor=white)](https://gcc.gnu.org/)
[![Plataforma](https://img.shields.io/badge/Plataforma-Windows%20%7C%20Linux%20%7C%20macOS-0078D4?style=for-the-badge&logo=windows&logoColor=white)](README.md)
[![Web Oficial](https://img.shields.io/badge/🌐_Portal_Web-Online_Live-2563eb?style=for-the-badge)](https://minilux0.github.io/LearningCpp/)
[![PDF Syllabus](https://img.shields.io/badge/📥_Descargar-Syllabus_PDF-dc2626?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](LearningCpp_Syllabus_Oficial.pdf)
[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-059669?style=for-the-badge&logo=open-source-initiative&logoColor=white)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Code_Lab-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/JExCwZ3YyC)

<br/>

[📜 Syllabus Completo](SYLLABUS.md) · [🌐 Portal Web Online](https://minilux0.github.io/LearningCpp/) · [🏛️ Arquitectura](docs/ARCHITECTURE.md) · [📋 Backlog](docs/BACKLOG.md) · [💬 Discord](https://discord.gg/JExCwZ3YyC)

<br/><br/>

<img src="assets/hero_learningcpp.gif" alt="LearningCpp — C++ Moderno Visual e Interactivo" width="90%">

</div>

---

## 💡 ¿Por qué existe LearningCpp?

La mayoría de cursos tradicionales de C++ cometen dos errores formativos: enseñan **C++ arcaico de hace 25 años** (punteros crudos obligatorios para todo, `printf`, arreglos estilo C y `using namespace std;`) o **asumen experiencia previa avanzada** en hardware y compiladores.

**LearningCpp rompe ambos paradigmas:**
* 🛡️ **C++ Moderno desde el Día 1:** Sintaxis segura con `std::string`, `{}` inicialización uniforme, `std::vector`, `constexpr`, `std::unique_ptr` (RAII) y algoritmos estándar de la STL.
* 🪜 **Nivel Cero Absoluto:** Diseñado para estudiantes sin conocimientos previos de memoria RAM ni compilación.

---

## 🏛️ Los 4 Pilares Pedagógicos

| Pilar | Principio Técnico | Beneficio Formativo |
|:---|:---|:---|
| 🎯 **1. Principio de la Escalera** | Progresión estrictamente incremental | Cada lección se construye **únicamente** sobre lo enseñado antes. Cero cajas negras. |
| 🐞 **2. Metodología Break-First** | Diagnóstico intencional de fallos | Experimenta el fallo real (*Buffer Overflow*, *Undefined Behavior*, *Slicing*) antes de aprender la solución. |
| 🧠 **3. Modelos Mentales de RAM** | Arquitectura y hardware real | Visualiza exactamente qué ocurre en la memoria física (*Stack vs Heap*, direcciones `0x...`, *VTable* y *RAII*). |
| 🌉 **4. Scaffolding & Fading** | De la intuición a la industria | Analogías físicas iniciales que se desvanecen de inmediato hacia la terminología profesional de ingeniería. |

---

## 🧭 El Circuito de Aprendizaje (5 Pasos por Lección)

```text
📖 1. Teoría & Hardware  ➔  🧪 2. Laboratorio Guiado  ➔  🐞 3. Demo de Bug  ➔  🏋️ 4. Reto Práctico  ➔  📝 5. Cheatsheet
```

1. **Teoría (`theory/LXX_*.md`):** Explicación exhaustiva con animaciones visuales Manim y modelos de memoria física.
2. **Laboratorio Guiado (`lab/LXX_*.cpp`):** Código de exploración comentado paso a paso para compilar a mano en consola.
3. **Demo de Bug (`lab/demos/DXX_*.cpp`):** Trampas reales del lenguaje aisladas para experimentar fallos en vivo.
4. **Reto Práctico (`exercise/EXX_*/`):** Reto con historia (lore), código con `TODOs` y su carpeta `solution/`.
5. **Hoja de Repaso (`summary/ModuleXX_Cheatsheet.md`):** Resumen de consulta técnica ultra-resumido.

---

## 🌐 Plataforma Web Interactiva

Accede a la plataforma web interactiva del curso online o de manera offline:

* 🚀 **Sitio Web Oficial en Vivo:** 👉 [**minilux0.github.io/LearningCpp**](https://minilux0.github.io/LearningCpp/)
* 📖 **Explorador Interactivo del Temario:** Navega entre las 6 fases y 117 lecciones con búsqueda instantánea (Ctrl+K).
* 🎬 **Galería de Animaciones Manim:** Visualiza los modelos de memoria RAM física (Stack vs Heap, VTable, RAII).
* 💻 **Showcase de C++17 Idiomático:** Ejemplos directos de inicialización uniforme, `std::vector` y `std::unique_ptr`.
* 💡 **Uso Offline:** Haz doble clic en [`web/index.html`](web/index.html) desde tu explorador de archivos.

---

## 🗺️ Mapa de Ruta del Curso (15 Módulos / 6 Fases)

| Fase | # | Módulo | Lecc. | Eje Conceptual Clave | Proyecto Integrador | Estado |
|:---:|:---:|---|:---:|---|---|:---:|
| **Fase 1: Fundamentos** | **01** | [**Getting Started**](01_GettingStarted/) | 7 | Compilación `g++`, `cout`/`cin`, streams, namespaces | Terminal Interactiva | ✅ |
| | **02** | [**Fundamental Types**](02_FundamentalTypes/) | 7 | Tipado estático, `{}` inicialización, casting explícito | Split the Bill Calculator | ✅ |
| | **03** | [**Scope & Control Flow**](03_ScopeAndControlFlow/) | 8 | Ámbitos en Stack, `if`/`switch`, bucles, prevención UB | Cajero / Taberna RPG | ✅ |
| **Fase 2: Funciones & Textos** | **04** | [**Functions**](04_Functions/) | 8 | Paso por valor, aislamiento, RNG moderno `<random>` | Generador Atributos RPG | ✅ |
| | **05** | [**Constants & Strings**](05_ConstantsAndStrings/) | 6 | Inmutabilidad `constexpr`, `std::string`, `string_view` | Generador de Claves | ✅ |
| **Fase 3: Colecciones** | **06** | [**Arrays & Vectors**](06_ArraysAndVectors/) | 9 | `std::vector`, límites seguros `.at()`, multi-archivo | Registro Calificaciones | 🔄 |
| | **07** | [**Compound Types**](07_CompoundTypes/) | 7 | `struct`, `enum class`, Agregados C++17 (Mirada C++20) | Bestiario RPG V1 | 🔄 |
| **Fase 4: Memoria Real** | **08** | [**References & Addresses**](08_ReferencesAndAddresses/) | 8 | Direcciones `&`, paso por referencia `const &`, alias | Bestiario V2 (Zero-Copy) | 🔄 |
| | **09** | [**Dynamic Memory**](09_DynamicMemory/) | 9 | Heap, punteros observadores, `unique_ptr`, `move`, RAII | Bestiario V3 (Heap RAII) | 🔄 |
| **Fase 5: POO Moderna** | **10** | [**Classes & Encapsulation**](10_Classes/) | 10 | Encapsulamiento `m_`, constructores, operadores `<<`/`==` | Bestiario V4 (Modular) | 🔄 |
| | **11** | [**Inheritance**](11_Inheritance/) | 7 | Herencia `: public`, constructores derivados, slicing | Jerarquía del Bestiario | 🔄 |
| | **12** | [**Polymorphism**](12_Polymorphism/) | 8 | `virtual`, VTable, `override`, interfaces puras | El Coliseo (Game Loop) | 🔄 |
| **Fase 6: Resiliencia & Especialización** | **13** | [**Error Handling**](13_ErrorHandling/) | 7 | Stack Unwinding, excepciones de dominio, `std::optional` | Motor Mazmorras Resiliente | 🔄 |
| | **14** | [**Templates & Lambdas**](14_TemplatesAndLambdas/) | 8 | Polimorfismo estático, templates `.hpp`, `if constexpr` | Pipeline Genérico Eventos | 🔄 |
| | **15** | [**STL Algorithms & Pipelines**](15_STLAlgorithms/) | 8 | Algoritmos STL, Erase-Remove, iteradores, Capstone Final | El Motor RPG Definitivo | 🔄 |

> **Leyenda:** ✅ *Módulo completo e implementado* · 🔄 *Módulo en desarrollo activo*.

---

## ⚡ Guía Rápida: Cómo Empezar

### 1. Clona el Repositorio
```bash
git clone https://github.com/MiniLux0/LearningCpp.git
cd LearningCpp
```

### 2. Verifica tu Compilador C++
Asegúrate de contar con un compilador moderno (GCC 13+, Clang 16+ o MSVC 2022):
```bash
g++ --version
```

### 3. Entra al Primer Módulo y Compila
```bash
# Entra al laboratorio del Módulo 01
cd 01_GettingStarted/lab

# Compila con el estándar moderno
g++ -std=c++17 L02_TuPrimerPrograma.cpp -o app

# Ejecuta tu binario
./app        # En Linux/macOS
.\app.exe    # En Windows
```

---

## 🗂️ Arquitectura de Carpetas del Repositorio

Cada módulo sigue estrictamente una estructura predecible y uniforme:

```text
XX_NombreDelModulo/
├── README.md                  ← Índice general del módulo y objetivos
├── theory/                    ← Lecciones teóricas en Markdown
│   ├── LXX_Nombre.md
│   └── assets/                ← Animaciones visuales Manim optimizadas (GIFs)
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

## 💬 Comunidad & Contribución

* 👥 **Comunidad en Discord:** Resuelve dudas, comparte tu progreso y debate sobre C++ Moderno en [**Discord Code Lab**](https://discord.gg/JExCwZ3YyC).
* 🤝 **Contribuciones:** Si encuentras una errata o deseas proponer un nuevo ejercicio, consulta [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) y abre un Pull Request.

---

<div align="center">
  <sub>Maintained with ❤️ by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub><br>
  <sub>Un curso interactivo de C++ Moderno desde Cero Absoluto hasta Fundamentos de Grado Profesional.</sub>
</div>
