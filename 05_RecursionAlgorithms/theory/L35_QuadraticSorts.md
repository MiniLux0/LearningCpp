# L35 — Algoritmos de Ordenamiento Cuadráticos: Selección, Inserción y Burbuja

> [!NOTE]
> **Fundamentación Académica:** Esta lección sintetiza los conceptos del **Capítulo 10 (*Algorithmic Analysis*, pp. 429–478)** del libro oficial de Stanford CS106B (*Programming Abstractions in C++* por Eric Roberts) y **Stanford CS106X Handouts**, cubriendo **10.1** *The sorting problem* (p. 430: Selection Sort e Insertion Sort) y **10.2** *Computational complexity* (p. 435).

---

## 🧭 Navegación Rápida

- 📄 **Lecturas Académicas Base:**
  - 🌲 [Stanford CS106B Textbook — Ch 10.1 (p. 430) & Ch 10.2 (p. 435)](../../files/cs106b/textbook/CS106BX-Reader.pdf)
  - ⚡ [Stanford CS106X — Sorting Efficiency & In-Place Algorithms](../../files/cs106x/README.md)
- 💻 **Laboratorio de Código:** [`L35_QuadraticSorts.cpp`](../code/L35_QuadraticSorts.cpp)

---

## Objetivos de Aprendizaje

- [ ] Comprender la familia de algoritmos de **ordenamiento de complejidad cuadrática ($O(N^2)$)**.
- [ ] Dominar **Selection Sort** (Ordenamiento por Selección) y su propiedad de mínimos intercambios.
- [ ] Dominar **Insertion Sort** (Ordenamiento por Inserción) y su rendimiento óptimo $O(N)$ en datos casi ordenados.
- [ ] Comprender **Bubble Sort** (Ordenamiento por Burbuja) y su optimización de parada temprana.
- [ ] Diferenciar entre **Estabilidad de Ordenamiento** (*Stability*) y **Ordenamiento In-Place**.

---

## 1. El Problema del Ordenamiento (*The Sorting Problem* — Sección 10.1)

El ordenamiento consiste en reorganizar una secuencia de $N$ elementos en un orden predeterminado (ascendente o descendente). En C++, la eficiencia del ordenamiento es vital para habilitar algoritmos rápidos como la **Búsqueda Binaria ($O(\log N)$)**.

---

## 2. Selection Sort (Ordenamiento por Selección — Sección 10.1)

### Mecánica del Algoritmo:
1. Buscar el menor elemento en el rango no ordenado de $[i \dots N-1]$.
2. Intercambiarlo (*swap*) con el elemento en la posición inicial $i$.
3. Repetir el proceso para la siguiente posición $i+1$.

```mermaid
graph TD
    A["[64, 25, 12, 22, 11]"] -->|Min en pos 4 (11)| B["[11 | 25, 12, 22, 64]"]
    B -->|Min en pos 2 (12)| C["[11, 12 | 25, 22, 64]"]
    C -->|Min en pos 3 (22)| D["[11, 12, 22 | 25, 64]"]
```

### Implementación en C++

```cpp
#include <utility> // std::swap

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            std::swap(arr[i], arr[minIdx]);
        }
    }
}
```

> [!NOTE]
> **Análisis de Complejidad de Selection Sort:**
> - **Comparaciones:** $(N-1) + (N-2) + \dots + 1 = \frac{N(N-1)}{2} = \mathbf{O(N^2)}$ en todos los casos (mejor, promedio y peor).
> - **Intercambios (*Swaps*):** Como máximo **$N-1$ intercambios** ($O(N)$). Ideal cuando escribir en memoria es costoso (ej. memoria Flash/EEPROM).
> - **Estabilidad:** **Inestable** (puede cambiar el orden relativo de elementos duplicados al intercambiar a larga distancia).

---

## 3. Insertion Sort (Ordenamiento por Inserción — Sección 10.1)

> [!TIP]
> **La Analogía de las Cartas (Eric Roberts, Sec. 10.1):**  
> Es como ordenar las cartas en tu mano. Tomas una carta nueva del mazo no ordenado e insertas la carta en su posición correcta desplazando hacia la derecha las cartas mayores.

### Mecánica del Algoritmo:
Mantiene una sub-lista izquierda ordenada. Para cada nuevo elemento `key`, desplaza los elementos mayores hacia la derecha e inserta `key` en el espacio libre.

### Implementación en C++

```cpp
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        // Desplaza los elementos de arr[0..i-1] que son mayores que key
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

> [!IMPORTANT]
> **El Comportamiento Adaptativo de Insertion Sort:**
> - **Peor Caso:** Arreglo invertido $\longrightarrow \mathbf{O(N^2)}$.
> - **Mejor Caso (Arreglo ya ordenado o casi ordenado):** $\mathbf{O(N)}$ lineal (solo realiza $1$ comparación por elemento y $0$ desplazamientos).
> - **Estabilidad:** **Estable** (preserva el orden relativo de claves idénticas).

---

## 4. Bubble Sort (Ordenamiento por Burbuja)

Recorre el arreglo comparando pares adyacentes y haciendo `swap` si están desordenados, haciendo que los elementos más grandes "floten" hacia el final del arreglo.

### Implementación Optimizada con Parada Temprana

```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break; // Si no hubo intercambios, el arreglo ya está ordenado!
    }
}
```

---

## 📊 Matriz Comparativa de Algoritmos Cuadráticos

| Algoritmo | Tiempo Mejor Caso | Tiempo Promedio | Tiempo Peor Caso | Espacio Auxiliar | Estabilidad | Intercambios (*Swaps*) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ In-Place | ❌ Inestable | $O(N)$ (Mínimo) |
| **Insertion Sort** | $\mathbf{O(N)}$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ In-Place | ✅ Estable | $O(N^2)$ desplazamientos |
| **Bubble Sort** | $\mathbf{O(N)}$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ In-Place | ✅ Estable | $O(N^2)$ swaps |

---

## ❓ Pregunta de Chequeo #1 — Selección del Algoritmo Adecuado

Tienes un arreglo de $10,000$ registros que ya está **prácticamente ordenado** (solo 5 elementos fuera de su lugar).

**¿Qué algoritmo cuadrático deberías elegir y por qué?**

<details>
<summary>🔍 <strong>Ver Explicación y Selección</strong></summary>

**Respuesta:** Deberías elegir **Insertion Sort**.

**Explicación:**
Insertion Sort es adaptativo y ejecuta en tiempo casi **lineal $O(N)$** cuando los datos están casi ordenados. En cambio, Selection Sort siempre realiza $\frac{N(N-1)}{2} \approx 50,000,000$ comparaciones sin importar si el arreglo ya está ordenado.

</details>

---

## 📝 Resumen Resumido de L35

1. **Selection Sort:** Realiza $O(N^2)$ comparaciones pero garantiza un mínimo de $O(N)$ intercambios. Inestable.
2. **Insertion Sort:** Excelente para listas pequeñas o casi ordenadas ($O(N)$ mejor caso). Estable.
3. **Bubble Sort:** Fácil de entender, optimizable con bandera `swapped`, pero ineficiente en la práctica.
4. **Estabilidad:** Un algoritmo es estable si conserva la posición relativa de elementos con claves duplicadas.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L34 — Linear & Binary Search**](L34_LinearBinarySearch.md) | [**🏠 Recursion & Algorithms**](../README.md) | [**L36 — MergeSort ➡️**](L36_MergeSort.md) |

</div>

---
*MiniLux0 — Learning C++ Section 05*
