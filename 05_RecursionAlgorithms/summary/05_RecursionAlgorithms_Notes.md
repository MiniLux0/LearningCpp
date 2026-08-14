# 📚 Resumen Ejecutivo y Notas de Estudio: Sección 05 — Recursión y Algoritmos

> **Curso**: Learning C++ (MIT 6.096 + Stanford CS106B / CS106X / CS106L)  
> **Módulo**: 05 — Recursión y Algoritmos (Lecciones L31 – L39)  
> **Directorio Teórico**: [`05_RecursionAlgorithms/theory/`](../theory/)  
> **Directorio de Código**: [`05_RecursionAlgorithms/code/`](../code/)

---

## 🎯 Resumen Ejecutivo y Competencias Clave

La Sección 05 realiza la transición desde la sintaxis básica de C++ hacia el **pensamiento algorítmico y la resolución computacional de problemas**. Explora cómo descomponer tareas complejas en subproblemas auto-similares, modelar la memoria recursiva en la Pila de Llamadas de RAM (*Call Stack*), optimizar subproblemas repetidos mediante **Memoización (Programación Dinámica Top-Down)**, analizar el crecimiento asintótico (Notación $O$), y dominar algoritmos de ordenamiento, búsqueda y exploración de estados.

---

## 📌 Desglose Técnico por Lección

### L31 — Pensamiento Recursivo
- Una función recursiva es un subprograma que se llama a sí mismo para resolver una instancia más pequeña del mismo problema.
- **Estructura Obligatoria de 2 Partes**:
  1. **Caso Base**: Condición de parada resuelta de forma trivial sin llamadas recursivas adicionales.
  2. **Paso Recursivo**: Reduce la escala del problema ($n \to n-1$) y vuelve a invocar a la función.
- **Pila de Llamadas y Marcos de Pila**: Cada llamada recursiva reserva un registro de activación en RAM que almacena parámetros locales y la dirección de retorno.
- **Desbordamiento de Pila (*Stack Overflow*)**: Ocurre cuando se omite el caso base o no se avanza hacia él.

### L32 — Problemas Recursivos Clásicos
- Las funciones matemáticas se traducen directamente a formas recursivas:
  - **Factorial**: $n! = n \times (n-1)!$ con caso base $0! = 1$.
  - **Fibonacci**: $F_n = F_{n-1} + F_{n-2}$ con casos base dobles $F_0 = 0, F_1 = 1$.
  - **Torres de Hanói**: Divide y Vencerás que requiere $2^N - 1$ movimientos.

### L33 — Memoización y Programación Dinámica Top-Down
- **Subproblemas Superpuestos (*Overlapping Subproblems*)**: La recursión simple en funciones como Fibonacci recalcula los mismos estados múltiples veces, explotando a $O(2^N)$.
- **Memoización (Top-Down DP)**: Técnica ideada por Donald Michie (1968) que almacena resultados intermedios en una tabla Caché (`vector` o `map`) para devolverlos en $O(1)$.
- **Patrón de 4 Pasos**:
  1. Consultar tabla Caché $\to$ 2. Evaluar caso base $\to$ 3. Calcular paso recursivo $\to$ 4. Almacenar resultado en Caché y retornar.
- **Impacto de Rendimiento**: Transforma Fibonacci de $O(2^N)$ a $O(N)$ lineal, y Grid Traveler de $O(2^{R+C})$ a $O(R \cdot C)$.

### L34 — Notación Big-O y Análisis Asintótico
- Mide cómo escalan el tiempo de ejecución o la memoria asignada a medida que el tamaño de entrada $N \to \infty$.
- **Reglas Asintóticas**:
  1. Ignorar constantes multiplicativas ($O(5N) \to O(N)$).
  2. Conservar únicamente el término dominante ($O(N^2 + 100N) \to O(N^2)$).
- **Jerarquía de Eficiencia**: $O(1) < O(\log N) < O(N) < O(N \log N) < O(N^2) < O(2^N)$.

### L35 — Búsqueda Lineal y Binaria
- **Búsqueda Lineal ($O(N)$)**: Inspeziona elementos secuencialmente. Funciona en arreglos no ordenados.
- **Búsqueda Binaria ($O(\log N)$)**: Utiliza Divide y Vencerás sobre **arreglos ordenados** inspeccionando el elemento central.
- **Punto Medio Seguro**: `int mid = low + (high - low) / 2` evita desbordamientos de enteros de 32 bits.

### L36 — Algoritmos de Ordenamiento Cuadráticos
- **Selection Sort ($O(N^2)$)**: Intercambios mínimos $O(N)$, inestable.
- **Insertion Sort ($O(N^2)$)**: $O(N)$ para datos casi ordenados, estable.
- **Bubble Sort ($O(N^2)$)**: Intercambia parejas adyacentes desordenadas.

### L37 — MergeSort
- **Divide y Vencerás**: Divide el arreglo en dos mitades, las ordena recursivamente y las mezcla.
- **Complejidad Temporal**: $O(N \log N)$ garantizado en todos los casos.
- **Complejidad Espacial**: Requiere memoria auxiliar $O(N)$ para la etapa de mezcla. Estable.

### L38 — QuickSort
- **Particionado de Hoare**: Selecciona un **pivote** y reordena los elementos in-place.
- **Rendimiento**: Tiempo promedio $O(N \log N)$ y espacio de pila $O(\log N)$. Peor caso $O(N^2)$ (mitigado mediante pivotes aleatorios).

### L39 — Backtracking Recursivo
- Exploración sistemática del árbol del espacio de estados.
- **Patrón Universal de 3 Pasos**:
  1. **Elegir (*Choose*)** $\to$ 2. **Explorar (*Explore*)** $\to$ 3. **Deshacer (*Unchoose*)**.

---

## ⚡ Matriz de Referencia Rápida

| Lección | Tema Principal | Complejidad Temporal | Complejidad Espacial | Fuente Académica Principal |
|---|---|:---:|:---:|---|
| **L31** | Pensamiento Recursivo | $O(N)$ | $O(N)$ Pila | Stanford CS106B Ch 7 / MIT 6.096 L5 |
| **L32** | Problemas Recursivos Clásicos | $O(N)$ a $O(2^N)$ | $O(N)$ Pila | Stanford CS106B Ch 7-8 / CS106X |
| **L33**| Memoización & Top-Down DP | $O(N)$ | $O(N)$ Caché+Pila | Stanford CS106B Ch 8.4 / CS106X |
| **L33** | Notación Big-O | $O(1) \dots O(2^N)$ | $O(1) \dots O(N)$ | Stanford CS106B Ch 10 / CS106X |
| **L34** | Búsqueda Lineal y Binaria | $O(\log N)$ | $O(1)$ | Stanford CS106B Ch 10.2 |
| **L35** | Ordenamientos Cuadráticos | $O(N^2)$ | $O(1)$ In-Place | Stanford CS106B Ch 10.3 |
| **L36** | MergeSort | $O(N \log N)$ | $O(N)$ | Stanford CS106B Ch 10.3 / CS106X |
| **L37** | QuickSort | $O(N \log N)$ prom | $O(\log N)$ In-Place | Stanford CS106B Ch 10.3 / CS106X |
| **L38** | Backtracking Recursivo | $O(b^d)$ Árbol Decisión | $O(d)$ Pila | Stanford CS106B Ch 9 / CS106X |

---

*MiniLux0 — Resumen Ejecutivo de la Sección 05*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> � 2026</sub>
</div>