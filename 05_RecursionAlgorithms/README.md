<div align="center">

# 🚀 Sección 05: Recursión y Algoritmos — Pila de Llamadas, Memoización, Big-O, Ordenamiento y Backtracking

> **Lecciones**: L31 – L39  
> 🏛️ **Fuente Académica Base**: Stanford CS106B (Lectures 07–11) / MIT 6.096 (Lecture 05)  
> 📝 **Resumen Ejecutivo**: 📝 [**`summary/05_RecursionAlgorithms_Notes.md`**](summary/05_RecursionAlgorithms_Notes.md)  
> 🎯 **Enfoque Principal**: Inducción matemática, memoria en la pila de llamadas (*Call Stack*), memoización (Programación Dinámica Top-Down), análisis de complejidad Big-O, búsqueda lineal/binaria, ordenamientos cuadráticos, Divide & Vencerás $O(N \log N)$ (MergeSort, QuickSort), y Backtracking.

---

### 🧭 Navegación de Módulos

| ⬅️ Módulo Anterior | 📂 Ubicación Actual | ➡️ Siguiente Módulo |
|:------------------:|:------------------:|:------------------:|
| [**⬅️ Sección 04: Arreglos y Cadenas**](../04_ArraysStrings/README.md) | **Sección 05: Recursión y Algoritmos** | [**Sección 06: Punteros y Memoria ➡️**](../06_Pointers/) |

</div>

---

## 📌 Visión General del Módulo

Este módulo introduce el pensamiento algorítmico y la resolución recursiva de problemas: gestión de marcos en la pila de llamadas (*Call Stack*), prevención de desbordamiento de pila (*Stack Overflow*), optimización mediante Memoización Top-Down, análisis de eficiencia algorítmica con notación Big-O, búsqueda binaria, algoritmos de ordenamiento recursivo (MergeSort, QuickSort) y exploración recursiva de estados mediante Backtracking.

---

## 📋 Inventario de Lecciones, Teoría y Código

| # | Título de la Lección | 📘 Nota Teórica | 💻 Laboratorio de Código | Conceptos Técnicos Clave | Estado |
|---|----------------------|-----------------|--------------------------|--------------------------|:------:|
| **L31** | **Pensamiento Recursivo** | 📘 [`L31_ThinkingRecursively.md`](theory/L31_ThinkingRecursively.md) | 💻 [`code/L31_ThinkingRecursively.cpp`](code/L31_ThinkingRecursively.cpp) | Casos base, marcos de pila, inducción matemática, desapilado. | ✅ |
| **L32** | **Problemas Recursivos** | 📘 [`L32_RecursiveProblems.md`](theory/L32_RecursiveProblems.md) | 💻 [`code/L32_RecursiveProblems.cpp`](code/L32_RecursiveProblems.cpp) | Factoriales, serie de Fibonacci, inversión de cadenas, profundidad de llamada. | ✅ |
| **L33** | **Memoización y DP** | 📘 [`L33_Memoization.md`](theory/L33_Memoization.md) | 💻 [`code/L33_Memoization.cpp`](code/L33_Memoization.cpp) | Programación Dinámica Top-Down, eliminación de cálculo redundante $O(2^N) \to O(N)$. | ✅ |
| **L34** | **Notación Big-O** | 📘 [`L34_BigONotation.md`](theory/L34_BigONotation.md) | 💻 [`code/L34_BigONotation.cpp`](code/L34_BigONotation.cpp) | Análisis asintótico ($O(1)$, $O(\log N)$, $O(N)$, $O(N \log N)$, $O(N^2)$). | ✅ |
| **L35** | **Búsqueda Lineal y Binaria** | 📘 [`L35_LinearBinarySearch.md`](theory/L35_LinearBinarySearch.md) | 💻 [`code/L35_LinearBinarySearch.cpp`](code/L35_LinearBinarySearch.cpp) | Búsqueda secuencial $O(N)$ vs. búsqueda binaria por divide y vencerás $O(\log N)$. | ✅ |
| **L36** | **Ordenamientos Cuadráticos** | 📘 [`L36_QuadraticSorts.md`](theory/L36_QuadraticSorts.md) | 💻 [`code/L36_QuadraticSorts.cpp`](code/L36_QuadraticSorts.cpp) | Ordenamiento por Selección, Inserción y Burbuja a complejidad $O(N^2)$. | ✅ |
| **L37** | **MergeSort** | 📘 [`L37_MergeSort.md`](theory/L37_MergeSort.md) | 💻 [`code/L37_MergeSort.cpp`](code/L37_MergeSort.cpp) | Ordenamiento Divide & Vencerás $O(N \log N)$, lógica de mezcla de subarreglos. | ✅ |
| **L38** | **QuickSort** | 📘 [`L38_QuickSort.md`](theory/L38_QuickSort.md) | 💻 [`code/L38_QuickSort.cpp`](code/L38_QuickSort.cpp) | Selección de pivote, algoritmo de particionado, caso promedio vs. peor caso $O(N^2)$. | ✅ |
| **L39** | **Backtracking** | 📘 [`L39_Backtracking.md`](theory/L39_Backtracking.md) | 💻 [`code/L39_Backtracking.cpp`](code/L39_Backtracking.cpp) | Árboles de decisión, reversión de estado (*Unchoose*), N-Reinas, generación de subconjuntos. | ✅ |

---

## 🎯 Ejercicios Prácticos con Pruebas Automáticas (E01 – E08)

> 📖 **Guía de Ejercicios**: 📂 [**`exercise/README.md`**](exercise/README.md)

| # | Nombre del Ejercicio | Concepto Evaluado | 💻 Archivo de Solución | Estado |
|---|----------------------|-------------------|------------------------|:------:|
| **E01** | **Factorial** | Recursión — caso base y pila de llamadas | 💻 [`exercise/E01_Factorial.cpp`](exercise/E01_Factorial.cpp) | ✅ |
| **E02** | **Fibonacci Memoizado** | Recursión simple vs. memoizada ($O(N)$) | 💻 [`exercise/E02_Fibonacci.cpp`](exercise/E02_Fibonacci.cpp) | ✅ |
| **E03** | **Búsqueda Binaria** | Búsqueda recursiva por divide y vencerás | 💻 [`exercise/E03_BinarySearch.cpp`](exercise/E03_BinarySearch.cpp) | ✅ |
| **E04** | **MergeSort** | Ordenamiento divide y vencerás $O(N \log N)$ | 💻 [`exercise/E04_MergeSort.cpp`](exercise/E04_MergeSort.cpp) | ✅ |
| **E05** | **QuickSort** | Particionado Lomuto y posicionamiento de pivote | 💻 [`exercise/E05_QuickSort.cpp`](exercise/E05_QuickSort.cpp) | ✅ |
| **E06** | **Función Potencia** | Exponenciación rápida $O(\log \text{exp})$ | 💻 [`exercise/E06_PowerFunction.cpp`](exercise/E06_PowerFunction.cpp) | ✅ |
| **E07** | **Inversión de Cadena** | Inversión recursiva de texto sin ciclos | 💻 [`exercise/E07_StringReversal.cpp`](exercise/E07_StringReversal.cpp) | ✅ |
| **E08** | **Subconjuntos con Backtracking** | Patrón *Elegir / Explorar / Deshacer* (*Choose/Explore/Unchoose*) | 💻 [`exercise/E08_Backtracking.cpp`](exercise/E08_Backtracking.cpp) | ✅ |

---

## 🛠️ Guías de Compilación y Construcción

Tanto la carpeta `code/` como `exercise/` disponen de scripts automatizados de compilación (`makefile`):
- ⚙️ **Manual de Compilación**: [`docs/COMPILATION_GUIDE.md`](../docs/COMPILATION_GUIDE.md)
- 🛠️ **Referencia de Makefile**: [`docs/MAKEFILE_GUIDE.md`](../docs/MAKEFILE_GUIDE.md)

---
*MiniLux0 — Learning C++ Section 05*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> � 2026</sub>
</div>