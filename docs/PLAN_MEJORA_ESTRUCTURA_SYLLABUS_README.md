# 🚀 Plan Maestro de Mejoras y Auditoría — LearningCpp
### *Optimizaciones para la Estructura, Syllabus, README y Experiencia del Alumno*

---

## 📌 1. Resumen Ejecutivo y Diagnóstico

Este documento consolida el análisis integral de **LearningCpp**, identificando brechas operativas, inconsistencias de navegación y oportunidades de mejora en la **estructura de carpetas**, el **`SYLLABUS.md`**, el **`README.md`** y las herramientas del repositorio, incorporando además las lecciones aprendidas tras la comparativa con el curso universitario **`cc112A`**.

---

## 🗂️ 2. Mejoras para la Estructura del Repositorio

### 2.1. Creación de Carpetas "Stub" para Módulos 06 al 15 (Eliminación de Errores 404)
* **Diagnóstico actual:** Al clonar el repositorio o navegar en GitHub, las carpetas de los módulos `06_ArraysAndVectors/` a `15_STLAlgorithms/` no existen, rompiendo los enlaces de las tablas del `README.md` y `SYLLABUS.md`.
* **Solución propuesta:** Crear la estructura de directorios mínima para cada módulo pendiente con un archivo `README.md` informativo.
  ```text
  06_ArraysAndVectors/
  └── README.md   ← "🚧 Módulo en desarrollo activo (Fase 3). Consulta docs/BACKLOG.md"
  ```

### 2.2. Incorporación de Licencia de Código Abierto (`LICENSE`)
* **Diagnóstico actual:** Falta un archivo de licencia en la raíz.
* **Solución propuesta:** Agregar una licencia permisiva estándar de la industria (ej. **MIT** o **Apache 2.0**) o de documentación abierta (**CC-BY-4.0**) para clarificar derechos de uso, contribución y distribución.

### 2.3. Separación de Guías de Contribución: Humanos vs Agentes IA
* **Diagnóstico actual:** El README apunta a `GEMINI.md`, el cual es un protocolo estricto para agentes de IA.
* **Solución propuesta:**
  * Mantener `GEMINI.md` para asistentes inteligentes.
  * Crear `CONTRIBUTING.md` con lenguaje claro para humanos (cómo clonar, compilar, reportar erratas y hacer Pull Requests).
  * Crear `docs/STYLE_GUIDE.md` extrayendo los estándares de codificación C++17/20 para estudiantes.

### 2.4. Infraestructura de Integración Continua (`.github/`)
* **Diagnóstico actual:** No hay validación automática de que el código siga compilando ante modificaciones.
* **Solución propuesta:**
  * `.github/workflows/ci.yml`: GitHub Action que ejecute `g++ -std=c++17 -Wall -Wextra -Wpedantic` en Ubuntu y Windows sobre todos los `.cpp` de `lab/`, `demos/` y `exercise/**/solution/`.
  * `.github/ISSUE_TEMPLATE/`: Plantillas para reporte de erratas (`errata.md`) y propuesta de nuevos demos de bugs (`new_bug_demo.md`).
  * `.github/PULL_REQUEST_TEMPLATE.md`: Checklist de verificación previa (cero emojis en `.cpp`, banners estándar, sin `using namespace std;`).

### 2.5. Completitud del Entorno VSCode (`.vscode/`)
* **Diagnóstico actual:** Solo existe `tasks.json`.
* **Solución propuesta:**
  * `.vscode/settings.json`: Configurar encoding UTF-8 sin BOM, standard C++17/20, formateador `clang-format` y linters.
  * `.vscode/launch.json`: Preconfigurar perfiles de depuración paso a paso con GDB/LLDB para Windows y Linux.

### 2.6. Script de Verificación Global (`verify_all.py` / `verify_all.ps1`)
* **Solución propuesta:** Crear un script en `utils/scripts/verify_all.py` que:
  1. Compile todos los laboratorios y soluciones.
  2. Verifique la ausencia de emojis dentro de archivos `.cpp` y `.h`.
  3. Verifique que no existan enlaces relativos rotos en los archivos `.md`.

---

## 📜 3. Mejoras para el `SYLLABUS.md`

### 3.1. Estimación de Tiempos y Carga Horaria (Workload)
* **Propuesta:** Incorporar una estimación de dedicación temporal sugerida:
  * **Ruta Estándar:** 16 semanas (6 a 8 horas por semana).
  * **Ruta Intensiva:** 8 semanas (12 a 15 horas por semana).
  * Desglose de horas estimadas por Fase (ej. *Fase 1: 15h, Fase 2: 12h, Fase 3: 18h, Fase 4: 20h, Fase 5: 25h, Fase 6: 30h*).

### 3.2. Criterios de Evaluación y Rúbricas de Autochequeo
* **Propuesta:** Agregar una sección de *Métricas de Dominio*:
  * **Nivel Aprendiz (Fases 1–2):** Capacidad de manipular flujos I/O, control de tipos seguros y modularización de funciones sin UB.
  * **Nivel Intermedio (Fases 3–4):** Dominio de `std::vector`, paso por referencia `const &` y gestión del Heap mediante `std::unique_ptr` con cero memory leaks.
  * **Nivel Avanzado (Fases 5–6):** Arquitectura POO idiomática con polimorfismo dinámico (VTable), excepciones de dominio, templates y pipelines C++20 Ranges.
  * **Rúbrica del Capstone Project:** Criterios de evaluación para *"El Motor RPG Definitivo"*.

### 3.3. Mapa / Grafo de Dependencias de Conocimiento
* **Propuesta:** Incluir un diagrama Mermaid que muestre el flujo de aprendizaje:
  ```mermaid
  graph TD
      F1[Fase 1: Fundamentos] --> F2[Fase 2: Funciones & Strings]
      F2 --> F3[Fase 3: Colecciones & Structs]
      F3 --> F4[Fase 4: Memoria & Punteros Inteligentes]
      F4 --> F5[Fase 5: POO & Polimorfismo]
      F5 --> F6[Fase 6: Nivel Profesional & Capstone]
  ```

### 3.4. Bibliografía y Recursos de Referencia Recomendados
* **Propuesta:** Incluir un catálogo de lecturas de apoyo:
  * *A Tour of C++ (3rd Edition)* — Bjarne Stroustrup (C++20).
  * *Effective Modern C++* — Scott Meyers.
  * *C++ Primer (5th Edition)* — Lippman, Lajoie, Moo.
  * *cppreference.com* y *LearnCpp.com*.

---

## 📄 4. Mejoras para el `README.md`

### 4.1. Corrección de Placeholders en Comandos
* **Diagnóstico actual:** Línea 114 contiene `https://github.com/tu-usuario/LearningCpp.git`.
* **Solución propuesta:** Reemplazar por la URL real del repositorio o documentar claramente la sustitución con variables.

### 4.2. Dashboard Visual de Progreso del Curso
* **Propuesta:** Agregar un widget de estado en el encabezado:
  ```text
  Progreso del Temario: [████████░░░░░░░░░░░░] 33% (5/15 Módulos Implementados)
  ```
  Complementado con insignias dinámicas de Shields.io indicando el estado de cada fase.

### 4.3. Guía de Instalación del Compilador por Plataforma (Cero Absoluto)
* **Propuesta:** Incluir instrucciones de 1 comando para configurar el entorno:
  * **Windows:** MinGW-w64 vía MSYS2 (`pacman -S mingw-w64-ucrt-x86_64-gcc`) o instalador WinLibs.
  * **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install build-essential gdb`.
  * **macOS:** `xcode-select --install` o `brew install gcc`.

### 4.4. Sección de Preguntas Frecuentes (FAQ)
* **Propuesta:** Añadir un acordeón interactivo `<details>` con respuestas a dudas recurrentes:
  1. *¿Por qué C++17/20 y no C clásico?* → Explicar seguridad de memoria y estándares modernos de la industria.
  2. *¿Por qué está prohibido `using namespace std;`?* → Evitar colisión de nombres y enseñar visibilidad explícita.
  3. *¿Por qué se usa `\n` en lugar de `std::endl`?* → Rendimiento y prevención de flushes forzados.
  4. *¿Necesito conocimientos previos de matemáticas o informática?* → No, el curso parte desde cero absoluto.

### 4.5. Insignias de Compiler Explorer (Godbolt)
* **Propuesta:** Añadir enlaces directos a Godbolt en los demos de bugs (`demos/DXX_`) para que el estudiante pueda probar el código en el navegador sin instalar nada.

---

## 🔄 5. Lecciones y Sinergias Aprendidas de `cc112A`

Al contrastar con el repositorio universitario **`cc112A`**, se identifican dos áreas clave para enriquecer **`LearningCpp`**:

1. **Profundización en Persistencia y Streams de Archivos:**
   * En `cc112A`, el módulo 07 cubre exhaustivamente archivos de texto y binarios (`<fstream>`, `seekg`, `seekp`, serialización de registros).
   * *Recomendación:* Enriquecer el Módulo 13 de `LearningCpp` (o una subsección en M06/M07) para que el estudiante aprenda a guardar y cargar datos del juego en disco de forma segura y moderna.
2. **Puente Algorítmico (Pensamiento Recursivo):**
   * `cc112A` entrena fuertemente el pensamiento recursivo (Divide y Vencerás, MergeSort, QuickSort).
   * *Recomendación:* En el Módulo 15 de algoritmos, incluir una lección conceptual que explique cómo los algoritmos estándar de la STL resuelven internamente estos problemas de forma óptima.

---

## 🎯 6. Matriz de Priorización y Roadmap de Ejecución

| Nivel | Acción | Archivos Impactados | Estado |
| :---: | :--- | :--- | :---: |
| 🔴 **P1** | Crear carpetas stub para M06–M15 con `README.md` provisionales | `06_ArraysAndVectors/` a `15_STLAlgorithms/` | ⏳ Pendiente |
| 🔴 **P1** | Implementar Módulo 06 (`06_ArraysAndVectors`) | `06_ArraysAndVectors/` (9 lecciones) | ⏳ Pendiente |
| 🔴 **P1** | Corregir placeholder `git clone` y añadir barra de progreso en `README.md` | `README.md` | ⏳ Pendiente |
| 🟡 **P2** | Generar assets visuales Manim para Módulo 05 | `05_ConstantsAndStrings/theory/assets/` | ⏳ Pendiente |
| 🟡 **P2** | Agregar archivo `LICENSE` y `CONTRIBUTING.md` para humanos | `LICENSE`, `CONTRIBUTING.md` | ⏳ Pendiente |
| 🟡 **P2** | Enriquecer `SYLLABUS.md` con carga horaria, rúbricas y bibliografía | `SYLLABUS.md` | ⏳ Pendiente |
| 🟢 **P3** | Configurar GitHub Actions (`.github/workflows/ci.yml`) | `.github/` | ⏳ Pendiente |
| 🟢 **P3** | Crear script de verificación y compilación global `verify_all.py` | `utils/scripts/verify_all.py` | ⏳ Pendiente |
| 🟢 **P3** | Completar configuración de VSCode (`settings.json`, `launch.json`) | `.vscode/` | ⏳ Pendiente |

---

<div align="center">
  <sub>Documento generado como guía técnica y estratégica para el ecosistema <strong>LearningCpp</strong> · 2026</sub>
</div>
