# ⚙️ Motor Central de Animaciones (Manim Core Engine)

Este directorio contiene la arquitectura, clases base y herramientas de automatización para generar todos los diagramas y animaciones visuales de **LearningCpp**.

---

## 🏛️ 1. Clase Base: `BaseLearningScene` (`manim_base.py`)

Todos los scripts de animación del curso heredan de `BaseLearningScene`, la cual provee la paleta estándar **Cyber-Academic Dark** y constructores de componentes visuales con zonas de seguridad anti-solapamiento:

### 🎨 Paleta Cyber-Academic Dark
* `COLOR_GOLD` / `COLOR_GOLD_LIGHT`: Inmutabilidad (`const`, `constexpr`), referencias y cerrojos.
* `COLOR_CYAN` / `COLOR_CYAN_LIGHT`: Celdas de memoria RAM (Stack), tipos primitivos y flujos estándar.
* `COLOR_GREEN` / `COLOR_GREEN_LIGHT`: Optimización, *Zero-Copy*, éxito en compilación y estado `good()`.
* `COLOR_RED` / `COLOR_RED_LIGHT`: Errores de compilación, violaciones de tipos y fallos de extracción (`fail()`).
* `COLOR_PURPLE` / `COLOR_PURPLE_LIGHT`: Evaluación en tiempo de compilación y operaciones de bajo nivel.
* `COLOR_PANEL` (`#161b22`) & `COLOR_BORDER` (`#30363d`): Marcos de ventanas IDE y tarjetas de hardware.

---

### 🧩 Constructores de Componentes Visuales

```python
# 1. Encabezado estándar superior
header = self.create_header("Título de la Lección", "Subtítulo conceptual")

# 2. Ventana de código IDE (main.cpp)
win_group, code_bg = self.create_code_window(width=5.2, height=2.8, title="main.cpp")

# 3. Puntero no-invasivo de ejecución de código
ptr = self.create_code_pointer(linea_codigo)

# 4. Tarjeta de hardware (RAM / Stack / Heap)
ram_group, ram_bg = self.create_card_panel(width=5.2, height=2.8, title="Memoria RAM", subtitle="0x7FFEE4")

# 5. Grilla de bytes / arreglos contiguos (para M06 Arrays/Vectors)
grid = self.create_byte_grid([10, 20, 30, 40], base_color=self.COLOR_CYAN, show_indices=True)

# 6. Puntero láser / flecha de referencia entre celdas
arrow = self.create_pointer_arrow(mobj_origen, mobj_destino, label="[ptr]")

# 7. Insignia de rendimiento / aprendizaje (Top-Right seguro)
badge = self.create_badge("Zero-Copy: 16 bytes", width=5.8)

# 8. HUD de estado / error inferior (Garantía de NO solapamiento)
hud = self.create_hud_footer("OPTIMIZACIÓN", "Mensaje técnico explicativo.", color=self.COLOR_CYAN)
```

---

## 🛠️ 2. Administrador Central de Renderizado (`render_manager.py`)

Ubicado en `utils/scripts/render_manager.py`, permite inspeccionar, auditar y compilar animaciones por lotes:

```bash
# Listar todas las animaciones y estado de sus GIFs
python utils/scripts/render_manager.py --list

# Renderizar todas las animaciones de un módulo específico (ej: M05)
python utils/scripts/render_manager.py --module 05

# Auditar que el 100% de los GIFs incrustados en Markdown existan y no estén vacíos
python utils/scripts/render_manager.py --audit

# Renderizar absolutamente todo el curso en secuencia
python utils/scripts/render_manager.py --all
```

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
