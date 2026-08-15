---
name: diagramas-toolkit
description: >-
  Standard protocol for generating architectural, algorithmic, and memory diagrams in LearningCpp.
  Enforces Mermaid-free, 100% vector SVGs using Graphviz or Native SVG with CSS animations.
---

# LearningCpp Diagrams Toolkit

This repository enforces a strict "No Mermaid, No Matplotlib" policy for diagrams due to poor text rendering, font inconsistencies, and lack of visual polish. All diagrams must be generated as crisp, scalable SVG files using specific Python methodologies.

## Core Directives

1. **NEVER USE MERMAID:** Do not write ````mermaid```` blocks in Markdown files. All diagrams must be external `![Image](assets/diagram.svg)` links.
2. **NEVER USE MATPLOTLIB:** Matplotlib generates fuzzy, polygon-based text that looks terrible in web browsers. Do not use it for drawing arrays, stacks, or memory blocks.
3. **WHITE BACKGROUNDS ONLY:** All SVGs must explicitly declare a white background (e.g., `<rect width="100%" height="100%" fill="#ffffff"/>` or Graphviz `bgcolor='white'`).
4. **SANS-SERIF FONT:** Always enforce `font-family: sans-serif` natively.

## Authorized Technologies

### 1. Graphviz (for Flowcharts, Trees, and State Machines)
Use the `graphviz` Python package for logical flows, recursion trees, and general graphs.
- Enforce modern colors (e.g., `#e1f5fe` for nodes, `#0288d1` for borders).
- Use `node(shape='box', style='rounded,filled', fontname='sans-serif')`.

### 2. Graphviz HTML-Like Nodes (for Memory Layouts and Call Stacks)
For memory addresses, C-style arrays, and call stacks, use Graphviz `shape='none'` nodes containing HTML tables.
```python
dot.node('struct', '''<
  <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
    <TR><TD BGCOLOR="#ffcdd2">Stack Top</TD></TR>
    <TR><TD>main()</TD></TR>
  </TABLE>>''', shape='none')
```

### 3. Native Animated SVGs (for Sorting, Searching, and Algorithms)
For step-by-step algorithm visualizations (e.g., Bubble Sort, Binary Search, Hanoi), generate **Native SVGs** directly via Python string manipulation.
- **Why?** It allows for pixel-perfect geometric shapes and native CSS `@keyframes` animations.
- **How?** Write a python script that outputs `<svg>` tags, `<rect>` elements, and `<style>` blocks.
- Inject CSS animations like `@keyframes` to move elements dynamically inside the markdown without needing external JavaScript.

## Execution Workflow
1. Create a python generator script in `utils/diagrams/` (e.g., `build_s06.py`).
2. Generate the `.svg` files into the appropriate `theory/assets/` directory.
3. Replace any existing Mermaid code in the `.md` file with a standard markdown image link.
4. Run `git add .` and commit the changes. Avoid committing `__pycache__` directories.
