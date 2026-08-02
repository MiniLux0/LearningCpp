# L34 — Búsqueda Lineal y Binaria: Algoritmos, Complejidad e Implementación

> [!NOTE]
> **Fundamentación Académica:** Esta lección sintetiza los conceptos del **Capítulo 7 (*Introduction to Recursion*, pp. 315–348)** y **Capítulo 10 (*Algorithmic Analysis*, pp. 429–478)** del libro oficial de Stanford CS106B (*Programming Abstractions in C++* por Eric Roberts) y **Stanford CS106X Handouts**, cubriendo **7.5** *The binary search algorithm* (p. 335) y **10.2** *Computational complexity* (p. 435).

---

## 🧭 Navegación Rápida

- 📄 **Lecturas Académicas Base:**
  - 🌲 [Stanford CS106B Textbook — Ch 7.5 (p. 335) & Ch 10.2 (p. 435)](../../files/cs106b/textbook/CS106BX-Reader.pdf)
  - ⚡ [Stanford CS106X — Searching & Algorithm Complexity](../../files/cs106x/README.md)
- 💻 **Laboratorio de Código:** [`L34_LinearBinarySearch.cpp`](../code/L34_LinearBinarySearch.cpp)

---

## Objetivos de Aprendizaje

- [ ] Entender el funcionamiento y limitaciones de la **Búsqueda Lineal ($O(N)$)** en arreglos desordenados (Sección 10.2).
- [ ] Dominar la **Búsqueda Binaria ($O(\log N)$)** en arreglos previamente **ordenados** (Sección 7.5).
- [ ] Implementar versiones **iterativas** y **recursivas** de la Búsqueda Binaria.
- [ ] Prevenir el error clásico de desbordamiento entero en el cálculo del punto medio: `mid = low + (high - low) / 2`.
- [ ] Analizar por qué $\log_2(1,000,000) \approx 20$ comparaciones frente a $1,000,000$ comparaciones lineales.

---

## 1. Búsqueda Lineal (*Linear Search* — Sección 10.2)

La **Búsqueda Lineal** o secuencial examina cada elemento del arreglo uno por uno desde el índice `0` hasta encontrar el elemento buscado o agotar la secuencia.

- **Requisito:** Ninguno. Funciona en arreglos tanto **desordenados** como ordenados.
- **Complejidad Temporal:**
  - **Mejor Caso:** $O(1)$ (el elemento está en la primera posición `arr[0]`).
  - **Peor Caso:** $O(N)$ (el elemento está al final o no existe en el arreglo).
  - **Caso Promedio:** $O(N)$ ($\approx N/2$ comparaciones).

```cpp
int busquedaLineal(const int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) return i; // Encontrado
    }
    return -1; // No encontrado
}
```

---

## 2. Búsqueda Binaria (*Binary Search* — Sección 7.5)

> [!TIP]
> **La Analogía del Diccionario (Eric Roberts, Sec. 7.5):**  
> Cuando buscas una palabra en un diccionario de 1,000 páginas, no hojeas página por página desde la primera. Abres el libro justo en la mitad. Si la palabra buscada es alfabéticamente menor, descartas toda la mitad derecha y repites el proceso en la mitad izquierda.

### Prerrequisito Fundamental:
La Búsqueda Binaria **REQUIERE obligatoriamente que el arreglo esté estrictamente ORDENADO**.

```mermaid
graph TD
    Subgraph Array ["Arreglo Ordenado: [5, 12, 19, 27, 33, 45, 58, 64, 72, 89, 93]"]
    end
    Step1["Comparar Target=45 con Mid=45 (Índice 5)"] -->|¡Coincidencia!| Found["Retornar Índice 5"]
```

### Estrategia Divide y Vencerás:
1. Calcular el punto medio `mid`.
2. Si `arr[mid] == target`, se ha encontrado el elemento.
3. Si `target < arr[mid]`, buscar recursivamente en la mitad izquierda (`low` a `mid - 1`).
4. Si `target > arr[mid]`, buscar recursivamente en la mitad derecha (`mid + 1` a `high`).

---

## 3. Implementación Recursiva e Iterativa en C++

### 🛠️ Implementación Recursiva (Sección 7.5)

```cpp
int busquedaBinariaRecursiva(const int arr[], int low, int high, int target) {
    // 1. CASO BASE 1: Rango exhausto sin encontrar el elemento
    if (low > high) return -1;

    // Prevención de overflow entero
    int mid = low + (high - low) / 2;

    // 2. CASO BASE 2: Elemento encontrado
    if (arr[mid] == target) return mid;

    // 3. PASO RECURSIVO: Reducir búsqueda a la mitad correspondiente
    if (arr[mid] > target)
        return busquedaBinariaRecursiva(arr, low, mid - 1, target);
    else
        return busquedaBinariaRecursiva(arr, mid + 1, high, target);
}
```

### 🛠️ Implementación Iterativa ($O(1)$ Espacio)

```cpp
int busquedaBinariaIterativa(const int arr[], int size, int target) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2; // Seguro contra overflow

        if (arr[mid] == target) return mid;
        if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1; // No encontrado
}
```

---

## ⚠️ Detalle Crítico de Ingeniería: Prevención de Integer Overflow

> [!CAUTION]
> **El Bug de Josh Bloch (2006):**  
> La fórmula tradicional `int mid = (low + high) / 2;` contiene un error sutil. En arreglos masivos donde `low + high > 2,147,483,647` (límite de 32-bit signed `int`), la suma sufre un **Overflow Entero** produciendo un número negativo y causando un *Segmentation Fault*.
>
> **La Solución Segura:**
> $$\text{mid} = \text{low} + \frac{\text{high} - \text{low}}{2}$$

---

## 📊 Comparativa de Escalamiento Asintótico

| Tamaño del Arreglo ($N$) | Búsqueda Lineal $O(N)$ (Peor Caso) | Búsqueda Binaria $O(\log_2 N)$ (Peor Caso) |
| :---: | :---: | :---: |
| **10** | $10$ comparaciones | $4$ comparaciones |
| **100** | $100$ comparaciones | $7$ comparaciones |
| **1,000** | $1,000$ comparaciones | $10$ comparaciones |
| **1,000,000** | $1,000,000$ comparaciones | **$\mathbf{20}$ comparaciones** |
| **1,000,000,000** | $1,000,000,000$ comparaciones | **$\mathbf{30}$ comparaciones** |

---

## ❓ Pregunta de Chequeo #1 — Máximo Número de Comparaciones

Para un arreglo ordenado de **$8,000,000$ elementos**, ¿cuál es el número máximo de comparaciones que realizará la Búsqueda Binaria para encontrar un elemento o determinar que no existe?

<details>
<summary>🔍 <strong>Ver Explicación y Cálculo Logarítmico</strong></summary>

**Respuesta:** Realizará como máximo **23 comparaciones**.

**Cálculo:**
$$\lceil \log_2(8,000,000) \rceil = \lceil 22.93 \rceil = 23$$

Esto demuestra el poder del crecimiento logarítmico frente a los $8,000,000$ de pasos que requeriría la búsqueda lineal.

</details>

---

## 📝 Resumen Resumido de L34

1. **Búsqueda Lineal:** $O(N)$ en el peor caso. Funciona sobre datos desordenados.
2. **Búsqueda Binaria:** $O(\log N)$ en el peor caso. **Exige datos estrictamente ordenados**.
3. **Punto Medio Seguro:** Usar siempre `mid = low + (high - low) / 2` para evitar desbordamiento de 32 bits.
4. **Paradigma:** Divide y Vencerás reduce el problema a la mitad en cada paso logarítmico.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L33 — Big-O Notation**](L33_BigONotation.md) | [**🏠 Recursion & Algorithms**](../README.md) | [**L35 — Quadratic Sorts ➡️**](L35_QuadraticSorts.md) |

</div>

---
*MiniLux0 — Learning C++ Section 05*
