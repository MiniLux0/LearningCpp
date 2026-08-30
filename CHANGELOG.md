# Changelog — LearningCpp

Todos los cambios notables de este proyecto se documentan en este archivo.  
El formato sigue estrictamente el estándar de [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [Unreleased]

### Completado
- **Blindaje de Rigor Técnico & Lema Formativo**:
  - Adopción del lema pedagógico oficial: **"Entiende primero. Abstrae después."**
  - Clarificación en teoría y web sobre `std::mt19937` como PRNG determinista de alto rendimiento (no criptográfico).
  - Sustitución de afirmaciones absolutas por terminología técnica rigurosa: *gestión determinista de recursos con RAII* y *prevención sistemática de lecturas de valores residuales indeterminados (UB)*.
  - Explicación fundamentada de `std::endl` basada en la eliminación de vaciados síncronos forzados de buffer.
- **Pipeline de Integración Continua (CI Matrix)**:
  - Creación de `.github/workflows/ci.yml` con compilación estricta C++17 (`-Wall -Wextra -Wpedantic`) y auditoría de estándares en Linux (Ubuntu) y Windows (MinGW).
- **Alineación a C++17 Base con Evolución a C++20**:
  - Estandarización oficial de todo el código ejecutable, laboratorios, retos y comandos en **C++17 puro (`-std=c++17`)**.
  - Incorporación en la teoría de bloques pedagógicos comparativos de *Evolución a C++20* (Designated Initializers en M07, `std::erase_if` en M06/M15, Concepts en M14 y Ranges en M15).
  - Promesa formativa ajustada a: *"De Cero Absoluto a C++ Moderno — Fundamentos de Grado Profesional"*.
  - Modelo pedagógico formalizado de **Ownership (`std::unique_ptr`) vs. Observación (`T*` / `T&`)**.
  - Filosofía de bucles refinada a *"Claridad ante todo: Algoritmos STL para transformaciones y range-for para secuencias directas"*.
- **Enriquecimiento del Syllabus (`SYLLABUS.md`)**:
  - Incorporación del diagrama del **Bucle de Aprendizaje** en 5 pasos (*Teoría & RAM ➔ Laboratorio ➔ Bug Demo ➔ Reto Práctico ➔ Cheatsheet*).
  - Creación de la **Matriz Ejecutiva** de 15 módulos detallando lecciones, ejes conceptuales y proyectos integradores.
  - Estimación de **Carga Horaria (Workload)** (16 semanas regular / 8 semanas intensiva).
  - Integración del **Grafo Visual de Dependencias de Conocimiento (Mermaid)** conectando las 6 fases formativas hasta el Capstone.
  - Definición de las **Rúbricas de Dominio por Niveles** (Nivel Aprendiz, Intermedio y Avanzado).
  - Redacción exhaustiva y estandarizada de las **117 lecciones** del temario oficial.
- **Compilación del PDF Oficial (`LearningCpp_Syllabus_Oficial.pdf`)**:
  - Maquetación y diseño de publicación ejecutiva en PDF multi-página con degradados oscuros, tarjetas de fase, matriz dashboard en una sola página, insignias codificadas por color y paginación profesional.
- **Nuevo README Principal (`README.md`)**:
  - Reescritura total con narrativa de grado profesional: manifiesto "¿Por qué existe LearningCpp?", los 4 pilares pedagógicos, guía de inicio rápido en terminal, insignia de autor **MiniLux0**, licencia MIT y enlaces oficiales.
- **Mejora Canónica de Licencia (`LICENSE`)**:
  - Actualización formal de la **Licencia MIT (Copyright © 2026 MiniLux0)** con 100% de compatibilidad para detectores SPDX de GitHub.
  - Clarificación explícita de cobertura para código fuente (`.cpp`/`.hpp`), material educativo (`.md`/`SYLLABUS.md`) y plataforma web/animaciones (`web/`, `utils/`).
- **Indexación Global & Metadatos Sociales (WhatsApp, Instagram, Facebook, Twitter/X, Discord, Google)**:
  - Creación de `web/CITATION.cff` y `web/package.json` para atribución canónica de autoría (**MiniLux0**) y palabras clave de búsqueda.
  - Generación de imagen de vista previa HD [`web/assets/images/og-preview.png`](web/assets/images/og-preview.png) (1200×630 px, optimizada a 55 KB) e iconos de aplicación [`web/assets/images/apple-touch-icon.png`](web/assets/images/apple-touch-icon.png).
  - Metadatos OpenGraph completos con dimensiones, tipos MIME y URLs canónicas seguras.
  - Esquema estructurado Schema.org JSON-LD en grafo (`@graph`) vinculando la entidad `Person (MiniLux0)` con el curso (`Course`) y el repositorio (`SoftwareSourceCode`).
  - Actualización de `web/sitemap.xml` y `web/robots.txt` orientados a `https://minilux0.github.io/LearningCpp/`.
- **Nueva Animación Hero Cinematográfica (`assets/hero_learningcpp.gif`)**:
  - Programación con ManimCE en [`utils/diagrams/animations/hero_readme_showcase.py`](utils/diagrams/animations/hero_readme_showcase.py) estructurada en **3 Actos independientes (cero solapes visuales)**:
    - *Acto 1:* Bienvenida oficial con logotipo neón `C++`, título del curso e insignia de autor `MiniLux0`.
    - *Acto 2:* Vistazo panorámico al plan de estudios en 6 fases y 15 módulos.
    - *Acto 3:* El Circuito de Aprendizaje en 5 pasos conectados y tarjeta de bienvenida final.
  - Erradicación de cajas blancas ("tofu" missing glyphs) asegurando compatibilidad tipográfica nativa.
  - Compresión Lanczos + doble pasada de paleta optimizada en FFmpeg (2.4 MB).
- **Rediseño, Depuración y Optimización de la Plataforma Web (`web/`)**:
  - **Redirección Directa 1:1 a Lecciones en GitHub**: Vinculación de cada tarjeta de lección dentro del modal directamente a su archivo Markdown específico (`blob/main/.../theory/LXX_Nombre.md`), eliminando enlaces intermedios o redundantes para una experiencia de lectura fluida con un solo clic.
  - **Corrección del Salto Involuntario de Scroll**: Eliminación de `body.style.overflow = 'hidden'` que reiniciaba el scroll a 0 en dispositivos móviles al abrir el menú/modales, y retiro de `scrollIntoView()` forzado en el cambio de fases.
  - **Rediseño de Pestañas de Fases (`.phase-tabs`)**: Contenedor envolvente (`flex-wrap: wrap`) con badge numérico independiente (`.tab-btn-count`), resolviendo el bloqueo de navegación en PC y adaptándose fluidamente a pantallas móviles.
  - **Soporte Móvil Integral**:
    - Bloqueo de desplazamiento horizontal en celulares mediante `overflow-x: hidden` raíz en `html`/`body`, reseteo universal `min-width: 0` y contenedores fluidos.
    - Botones con áreas táctiles ergonómicas de **44px a 48px** (WCAG AAA).
  - **Optimización de Rendimiento (`app.js`)**: Reducción masiva de peso de **110 KB a ~20 KB**, conservando búsqueda en tiempo real (Ctrl+K), modal de lecciones, lightbox Manim y conmutador de tema oscuro/claro.
  - **Autosuficiencia de Recursos Multimedia (`web/assets/animations/`)**: Sincronización local de todas las animaciones Manim dentro de la plataforma web, garantizando carga 100% libre de errores 404 en GitHub Pages tanto online como en modo offline local.
- **Módulos 01 a 05 Finalizados al 100%**:
  - **M01 — Getting Started**: 7 lecciones, laboratorios, demos, 6 retos y 6 animaciones Manim (`l00` a `l06`).
  - **M02 — Fundamental Types**: 7 lecciones, 7 laboratorios, 4 demos de bugs, 7 retos y 7 animaciones Manim (`l01` a `l07`).
  - **M03 — Scope & Control Flow**: 8 lecciones, 8 laboratorios, 9 demos de bugs, 8 retos y 7 animaciones Manim (`l01` a `l07`).
  - **M04 — Functions**: 8 lecciones, 8 laboratorios, 6 demos de bugs, 8 retos y 7 animaciones Manim (`l01` a `l07`).
  - **M05 — Constants & Strings**: 6 lecciones, 6 laboratorios, 4 demos de bugs, 6 retos y 5 animaciones Manim (`l01` a `l05`).
- **Auditoría Técnica y Pedagógica Integral (Módulos 01 a 05)**:
  - 100% de conformidad en 756 pruebas automatizadas de compilación limpia con `g++ -std=c++17 -Wall -Wextra`.
  - Cero emojis en código fuente (`.cpp` y `.h`).
  - Estandarización de avisos de autochequeo interactivo `<details>` en todas las lecciones teóricas.
- **Higiene del Repositorio y Raíz Limpia**:
  - Reubicación de archivos de soporte (`package.json`, `CITATION.cff`) dentro de `web/` para mantener la raíz con únicamente archivos esenciales de C++ y documentación oficial.
  - Consolidación limpia de `docs/` en únicamente [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) y [`docs/BACKLOG.md`](docs/BACKLOG.md).
  - Eliminación de scripts muertos en `web/assets/js/` (`code-viewer.js`, `modules-explorer.js`, `ram-visualizer.js`, `terminal-simulator.js`).
  - Eliminación de archivos temporales de análisis, caché de Manim (`media/`), respaldos obsoletos y archivos de compilación de Python (`__pycache__`/`.pyc`).
  - Purgado absoluto de referencias internas no estudiantiles en toda la documentación pública del curso.

### En progreso
- **Implementación de Módulo 06 (Arrays & Vectors)**: Desarrollo activo de la Fase 3 (Colecciones) con sus 9 lecciones teóricas, laboratorios, demos de Buffer Overflow (`D02`), límites seguros `.at()` y arquitectura multi-archivo.

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
