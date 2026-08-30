# 🎨 Arquitectura de Diagramas y Animaciones

Este directorio aloja toda la infraestructura programática utilizada para generar los recursos visuales personalizados (`.gif`) en el repositorio de `LearningCpp`. La infraestructura ahora está **100% basada en Manim**.

Para mantener el entorno pedagógico del repositorio lo más limpio posible, todos los scripts de este directorio son **privados** y Git los ignora (vía `.gitignore`).

## 📂 Estructura del Directorio

*   **`core/`**: El motor principal. Contiene `BaseLearningScene` (Manim). Define la estética visual global (colores estilo Catppuccin Mocha, nodos redondeados, ritmo de animaciones, etc.).
*   **`animations/`**: Scripts que generan las animaciones en GIF con Manim. Están organizados estrictamente por nombre de módulo para mantener una arquitectura escalable.

## ⚠️ Reglas para Agentes de IA
Cualquier agente de IA que modifique o cree archivos en este directorio DEBE adherirse estrictamente a las reglas establecidas en:
- `.agents/skills/manim-animations/SKILL.md`
- `.agents/skills/manim-repo-conventions/SKILL.md`

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
