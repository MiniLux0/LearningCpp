# 🗺️ LearningCpp — Project Roadmap & TODOs

## 📌 Pending Tasks

### 🎨 Visual & Manim Standardization
- [ ] **Estandarizar animaciones en Secciones 01, 02, 03 y 04:**
  - Auditar todas las lecciones de los módulos 01 a 04.
  - Asegurar que cualquier visualización o diagrama animado se genere mediante **Manim** siguiendo estrictamente el protocolo definido en `.agents/skills/manim-animations/SKILL.md`.
  - Exportar inicialmente a `.mp4` para las pruebas y luego convertir a `.gif` ultra-comprimido (usando la misma configuración de `ffmpeg` con algoritmo Lanczos a 15fps que usamos en la Sección 05).
  - Validar que la nomenclatura de los archivos siga el prefijo de la lección (ej. `l04_variables.gif`).
  - Asegurarse de que las referencias en los archivos Markdown utilicen `<div align="center"> <img src="..." alt="..."> </div>` para compatibilidad nativa con GitHub Markdown.

### 📚 Arquitectura de Documentación
- [ ] **Implementar Estrategia de Documentación de 3 Capas:**
  - Desplegar la estructura propuesta en el artefacto `repo_documentation_strategy.md`.
  - Crear/Actualizar la capa académica (READMEs y lecciones).
  - Crear/Actualizar la capa técnica (Guías de compilación).
  - Documentar el ecosistema de IA/Agentes en `.agents/`.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
