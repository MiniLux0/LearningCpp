# Changelog — LearningCpp

Todos los cambios notables de este proyecto se documentan aquí.  
El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [Unreleased]

### Completado
- **Diseño Curricular Completo (15 Módulos / 6 Fases)**: Se finalizó la planificación arquitectónica y pedagógica de todo el curso (M01 a M15). Se fijaron las 20 decisiones de diseño fundamentales, garantizando la progresión desde Cero Absoluto hasta Nivel Profesional con C++20 Ranges, Programación Genérica y Capstone Integrador.
- **Enriquecimiento del Syllabus (`SYLLABUS.md`)**:
  - Incorporación del diagrama del **Bucle de Aprendizaje** en 5 pasos (*Teoría & RAM ➔ Laboratorio ➔ Bug Demo ➔ Reto Práctico ➔ Cheatsheet*).
  - Creación de la **Matriz Ejecutiva** de 15 módulos detallando lecciones, ejes conceptuales y proyectos integradores.
  - Redacción exhaustiva y estandarizada de las **117 lecciones** del temario oficial.
- **Compilación del PDF Oficial (`LearningCpp_Syllabus_Oficial.pdf`)**:
  - Maquetación y diseño de publicación ejecutiva en PDF multi-página con degradados oscuros, tarjetas de fase, matriz dashboard en una sola página, insignias codificadas por color y paginación profesional.
- **Nuevo README Principal (`README.md`)**:
  - Reescritura total con estética y narrativa de grado profesional: manifiesto "¿Por qué existe LearningCpp?", los 4 pilares pedagógicos, guía de inicio rápido en terminal y enlaces oficiales.
- **Refactorización y Limpieza de Documentación**: 
  - Se consolidaron `CRITICAL_REVISION.md` y `COURSE_PLAN.md` en un único documento maestro de ingeniería: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).
  - Se migró y renombró `PENDING.md` a [`docs/BACKLOG.md`](docs/BACKLOG.md) con el checklist completo de lecciones, demos de bugs y retos.
  - Se trasladó la referencia de LearnCpp a [`docs/learncpp_reference.txt`](docs/learncpp_reference.txt).
  - Se respaldó toda la documentación original en [`_backup_docs/`](_backup_docs/).
  - Se limpió la raíz del repositorio dejando únicamente los archivos esenciales para el alumno y agentes (`README.md`, `SYLLABUS.md`, `CHANGELOG.md`, `GEMINI.md`, `LearningCpp_Syllabus_Oficial.pdf`).
- **Estandarización y Protocolo Maestro (`GEMINI.md`)**: Reescritura integral del reglamento para agentes de IA. Se incluyó el pipeline paso a paso para la creación de módulos, el mapa de referencia de los 15 módulos, los vetos absolutos (`using namespace std;` y `std::endl`), las reglas de scaffolding/fading, estándares de C++17/C++20 y los protocolos de validación pre-entrega.
- **Módulo 01 — Getting Started**: Finalizado al 100% con 7 lecciones teóricas, laboratorios, demos, 6 retos y sus 6 animaciones Manim (`l00` a `l06`) bajo la paleta Cyber-Academic Dark.
- **Módulo 02 — Fundamental Types**: Finalizado al 100% con 7 lecciones, 7 laboratorios, 4 demos de bugs, 7 retos y sus **7 animaciones Manim modernizadas** (`l01` a `l07`) con celdas estructuradas de memoria RAM Stack, diagnóstico de narrowing y pipeline de ALU.
- **Módulo 03 — Scope & Control Flow**: Finalizado al 100% con 8 lecciones teóricas, 8 laboratorios guiados, 8 demos de bugs intencionales (`D01`–`D07b`), 8 retos prácticos con lore inmersivo (`E01`–`E08`), cheatsheet técnico y sus **7 animaciones Manim modernizadas** (`l01` a `l07`) con evaluación de bifurcaciones, jump tables, mutación en RAM y shadowing.
- **Módulo 04 — Functions**: Finalizado al 100% con 8 lecciones teóricas, 8 laboratorios guiados, 6 demos de bugs, 8 retos y sus **7 animaciones Manim modernizadas** (`l01` a `l07`) con tipografía `MarkupText` a 20pt, sangría de 4 espacios (tab), puntero de depuración (`▶`), celdas estructuradas de Stack RAM y tarjetas de error de compilador de alto contraste.
- **Módulo 05 — Constants & Strings**: Finalizado al 100% con 6 lecciones teóricas, 6 laboratorios, 4 demos de bugs, 6 retos prácticos y sus **5 animaciones Manim de alta fidelidad** (`l01` a `l05`) bajo la paleta Cyber-Academic Dark y sistema de no-solapamiento.
- **Motor Central de Animaciones (`utils/`)**: Implementación del CLI de renderizado y auditoría `render_manager.py` y expansión de `BaseLearningScene` con primitivas UI estandarizadas.
- **Estandarización Total Módulos 01 a 05**: Homologación absoluta de banners, cero emojis en código `.cpp`, prohibición estricta de `using namespace std;` y `std::endl`, 100% de enlaces Markdown validados y pausas pedagógicas ampliadas (3.0s / 5.0s).

### En progreso
- **Implementación de Módulo 06 (Arrays & Vectors)**: Desarrollo activo de la Fase 3 (Colecciones) con sus 9 lecciones teóricas, laboratorios, demos de Buffer Overflow (`D02`), límites seguros `.at()` y arquitectura multi-archivo.

---

## [2.0.0] — 2026-08-25 · Refactorización completa

### Identidad y filosofía
- Curso redefinido como **independiente** — sin atribución a MIT/Stanford.
- Público objetivo declarado: **cero absoluto → profesional**.
- Filosofía: C++ moderno (C++17/20) desde la lección 1, sin sintaxis legada como base.

### Nueva estructura de módulos (13 módulos, 6 fases)
- **Fase 1 — Fundamentos:** `01_GettingStarted`, `02_FundamentalTypes`, `03_ScopeAndControlFlow`
- **Fase 2 — Funciones y STL básica:** `04_Functions`, `05_StringsAndVectors`
- **Fase 3 — POO Moderna:** `06_CompoundTypes`, `07_Classes`, `08_Inheritance`, `09_Polymorphism`
- **Fase 4 — Memoria:** `10_MemoryManagement`
- **Fase 5 — Estructuras de Datos:** `11_RecursionAlgorithms`, `12_DataStructures`
- **Fase 6 — Nivel Profesional:** `13_AdvancedCPP`

### Módulo 01 — Getting Started
- Nueva lección **L00 ¿Qué es programar?** — conceptual, sin código ni instalación.
- Renumeración completa: L00–L05 (viejo) → L01–L06 (nuevo).
- Estructura `exercise/` migrada a subcarpetas individuales `E0X_Nombre/`.
- Archivos de `theory/` y `code/` renombrados al nuevo esquema.
- `summary/` renombrado a `Module01_Cheatsheet.md`.

### Documentación raíz
- `README.md` — reescrito con nueva identidad, comunidad Discord, guía de contribución.
- `SYLLABUS.md` — reescrito desde cero; 13 módulos, voz propia, sin tags MIT/CS106.
- `COURSE_PLAN.md` — nuevo documento maestro del plan de refactorización.
- `.gitignore` — reescrito moderno (`build/`, `*.o`, `*.exe`, `__pycache__/`).

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
