# L37 — MergeSort: Ordenamiento por Mezcla `O(N \log N)`

> [!NOTE]
> **Fundamentación Académica:** Esta lección sintetiza los conceptos del **Capítulo 10 (*Algorithmic Analysis*, pp. 429–478)** del libro oficial de Stanford CS106B (*Programming Abstractions in C++* por Eric Roberts), cubriendo **10.3** *Recursion to the rescue* (p. 443) y **10.4** *Standard complexity classes* (p. 449).

---

## 🧭 Navegación Rápida

- 📄 **Lecturas Académicas Base:**
  - 🌲 [Stanford CS106B Textbook — Ch 10.3 (p. 443) & Ch 10.4 (p. 449)](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Laboratorio de Código:** [`L37_MergeSort.cpp`](../code/L37_MergeSort.cpp)

---

## Objetivos de Aprendizaje

- [ ] Entender por qué los algoritmos cuadráticos $O(N^2)$ son insuficientes para entradas grandes (Sección 10.3).
- [ ] Dominar la estrategia **Divide y Vencerás** aplicada al ordenamiento.
- [ ] Implementar el algoritmo **MergeSort** con sus dos funciones clave: `sort` y `merge`.
- [ ] Derivar matemáticamente la complejidad $O(N \log N)$ a partir del árbol de recursión.
- [ ] Interpretar la tabla comparativa $N^2$ vs $N \log N$ de la Figura 10-5 del texto (p. 447–448).

---

## 1. La Necesidad de un Mejor Algoritmo (Sección 10.3)

Los algoritmos cuadráticos como Selection Sort e Insertion Sort requieren $\frac{N(N-1)}{2}$ comparaciones. Para $N = 100,000$ eso son **5,000,000,000 operaciones** — inaceptable en la práctica.

> *"To develop a better sorting algorithm, you need to adopt a qualitatively different approach."*
> — CS106B, Sec. 10.3

### La Idea Clave: Explotar la Relación Inversa

> [!TIP]
> **La Propiedad Clave de los Algoritmos Cuadráticos (Sec. 10.3):**  
> Si el tamaño del problema se **duplica**, el tiempo cuadrático se **cuadruplica** ( $\times 4$ ).  
> Inversamente, si divides el problema a la **mitad**, el tiempo se **cuarteriza** ( $\div 4$ ).  
>
> Esto sugiere que dividir el arreglo en mitades y resolver recursivamente puede reducir el tiempo total de forma drástica.

---

## 2. Estrategia Divide y Vencerás: MergeSort

El algoritmo **MergeSort** (*Ordenamiento por Mezcla*) descrito en la Sección 10.3 usando la siguiente estrategia de 5 pasos:

![Animation](assets/merge_sort.gif)

---

## 3. El Paso de Mezcla (`merge`) — El Corazón del Algoritmo

La operación de **mezcla** reconstruye un vector ordenado combinando dos sub-vectores *ya ordenados*. Su lógica se basa en una observación clave: el primer elemento del vector final **siempre** es el menor de los primeros elementos de `v1` y `v2`.

### Visualización del Paso Merge

Partiendo de estas dos mitades ya ordenadas:

```
v1: [25, 30, 40, 70]
v2: [19, 35, 55, 80]
```

El proceso de mezcla compara cabezas y elige siempre el menor:

| Paso | v1 (p1) | v2 (p2) | Elegido | Resultado acumulado |
| :---: | :---: | :---: | :---: | :--- |
| 1 | **25** | **19** | 19 (de v2) | `[19]` |
| 2 | **25** | **35** | 25 (de v1) | `[19, 25]` |
| 3 | **30** | **35** | 30 (de v1) | `[19, 25, 30]` |
| 4 | **40** | **35** | 35 (de v2) | `[19, 25, 30, 35]` |
| 5 | **40** | **55** | 40 (de v1) | `[19, 25, 30, 35, 40]` |
| 6 | **70** | **55** | 55 (de v2) | `[19, 25, 30, 35, 40, 55]` |
| 7 | **70** | **80** | 70 (de v1) | `[19, 25, 30, 35, 40, 55, 70]` |
| 8 | *(vacío)* | **80** | 80 (de## 4. Implementación en C++

> [!NOTE]
> MergeSort necesita un **arreglo auxiliar temporal** para almacenar los elementos durante la mezcla — es el mismo concepto del `memo[]` de L33: un arreglo extra que usamos como herramienta de apoyo.

```cpp
#include <iostream>
using namespace std;

const int MAX_N = 10000; // Tamaño máximo del arreglo auxiliar

// ── MEZCLA de dos mitades ya ordenadas dentro del mismo arreglo ───────────────
// Recibe: arr[], los índices low, mid, high
// Usa: un arreglo temporal para reordenar
void merge(int arr[], int low, int mid, int high) {
    int temp[MAX_N]; // Arreglo temporal — igual a memo[] en L33

    int p1 = low;       // Puntero a la mitad izquierda [low..mid]
    int p2 = mid + 1;   // Puntero a la mitad derecha  [mid+1..high]
    int k  = low;       // Puntero al arreglo temporal

    // Comparar cabezas y elegir siempre el menor
    while (p1 <= mid && p2 <= high) {
        if (arr[p1] <= arr[p2]) temp[k++] = arr[p1++];
        else                    temp[k++] = arr[p2++];
    }

    // Copiar el resto de la mitad que no se agotó
    while (p1 <= mid)  temp[k++] = arr[p1++];
    while (p2 <= high) temp[k++] = arr[p2++];

    // Copiar el resultado de vuelta al arreglo original
    for (int i = low; i <= high; i++)
        arr[i] = temp[i];
}

// ── MERGESORT recursivo ───────────────────────────────────────────────────────
void mergeSort(int arr[], int low, int high) {
    if (low >= high) return;  // Caso Base: subarreglo de 1 elemento ya está ordenado

    int mid = low + (high - low) / 2; // Seguro contra overflow (igual que búsqueda binaria)

    mergeSort(arr, low, mid);          // Conquista izquierda
    mergeSort(arr, mid + 1, high);     // Conquista derecha
    merge(arr, low, mid, high);        // Combinar
}

int main() {
    int datos[] = {38, 27, 43, 3, 9, 82, 10};
    int n = 7;

    mergeSort(datos, 0, n - 1);

    for (int i = 0; i < n; i++) cout << datos[i] << " ";
    // Salida: 3 9 10 27 38 43 82

    return 0;
}
```

---

## 5. Árbol de Recursión y Derivación de `O(N log N)`

### Árbol para `N = 8`

![Animation](assets/l37_merge_tree.gif)

### ¿Cuántos Niveles Hay?

Cada nivel divide $N$ por 2. El número de niveles $k$ es aquel tal que $2^k = N$:

```math
k = \log_2 N
```

### Trabajo en Cada Nivel

En cada nivel se realiza una mezcla completa. La mezcla de todos los sub-arreglos de un nivel cuesta exactamente **$N$ operaciones** en total (cada elemento se mueve exactamente una vez por nivel).

### Total de Trabajo

```math
\text{Niveles} \times \text{Trabajo por nivel} = \log_2 N \times N = O(N \log N)
```

---

## 6. Comparativa `N² vs N log N` (Figura 10-5, p. 447)

| $N$ | Selection Sort $O(N^2)$ | MergeSort $O(N \log N)$ | Factor de Mejora |
| :---: | :---: | :---: | :---: |
| 10 | 100 | ~33 | $\times 3$ |
| 100 | 10,000 | ~664 | $\times 15$ |
| 1,000 | 1,000,000 | ~9,965 | $\times 100$ |
| 10,000 | 100,000,000 | ~132,877 | $\times 753$ |
| 100,000 | **10,000,000,000** | ~1,660,964 | **$\times 6{,}021$** |

> *"For large vectors, merge sort clearly represents a significant improvement."*
> — CS106B, Sec. 10.3

---

## 7. Clases de Complejidad Estándar (Sección 10.4)

MergeSort introdujo la importancia de la clase $O(N \log N)$. El texto de Sección 10.4 presenta la jerarquía completa:

| Clase | Nombre | Ejemplo |
| :---: | :--- | :--- |
| $O(1)$ | Constante | Acceso a un índice de arreglo |
| $O(\log N)$ | Logarítmica | Búsqueda Binaria (L35) |
| $O(N)$ | Lineal | Búsqueda Lineal (L35) |
| $O(N \log N)$ | **Lineal-logarítmica** | **MergeSort** |
| $O(N^2)$ | Cuadrática | Selection Sort (L36) |
| $O(2^N)$ | Exponencial | Backtracking sin poda (L39) |

![Animation](assets/l37_complexity.gif)

> [!IMPORTANT]
> **Tractable vs Intractable (Sec. 10.4):**
> Los problemas solubles en tiempo **polinomial** ( $O(N^k)$ ) se consideran **tractables** (computacionalmente viables).
> Los que solo tienen soluciones **exponenciales** ( $O(2^N)$ ) son **intratables** — por ejemplo, el Subset-Sum Problem y el Travelling Salesman Problem.

---

## ❓ Pregunta de Chequeo #1 — Árbol de Recursión

Para un arreglo de $N = 16$ elementos, ¿cuántos **niveles** tendrá el árbol de recursión de MergeSort y cuántas llamadas habrá en el último nivel antes de los casos base?

<details>
<summary>🔍 <strong>Ver Solución</strong></summary>

**Niveles:** $\log_2(16) = 4$ niveles de recursión (sin contar el nivel base).

**Llamadas en el último nivel:** $2^4 = 16$ llamadas, cada una con un sub-arreglo de **2 elementos** que se mezclan en arreglos de **1 elemento**.

</details>

---

## ❓ Pregunta de Chequeo #2 — Estabilidad

¿Es MergeSort un algoritmo **estable**?

<details>
<summary>🔍 <strong>Ver Respuesta</strong></summary>

**Sí, MergeSort es estable.** En el paso de mezcla, cuando `arr[p1] <= arr[p2]`, elegimos el de la izquierda primero. Esto preserva el orden relativo de elementos con claves iguales que estaban originalmente en la mitad izquierda antes que los de la derecha.

</details>

---

## 📝 Resumen de L37

1. **MergeSort** aplica la estrategia **Divide y Vencerás** recursivamente para alcanzar $O(N \log N)$.
2. El paso `merge` combina dos mitades **ya ordenadas** usando un arreglo auxiliar temporal en $O(N)$ comparaciones.
3. El **árbol de recursión** tiene $\log_2 N$ niveles, con $N$ trabajo total por nivel → $O(N \log N)$.
4. Para $N = 100{,}000$: Selection Sort tarda **>2.5 minutos**; MergeSort **<0.5 segundos** (Sec. 10.3).
5. MergeSort es **estable** y **no in-place** — requiere $O(N)$ memoria auxiliar para el arreglo temporal.

---

<div align="center">

### 🧭 Navegación y Progresión

| ⬅️ Lección Anterior | 🏠 Inicio de Sección | ➡️ Siguiente Lección |
|:------------------:|:-------------------:|:------------------:|
| [**⬅️ L35 — Ordenamientos Cuadráticos**](L36_QuadraticSorts.md) | [**🏠 Recursión y Algoritmos**](../README.md) | [**L38 — QuickSort ➡️**](L38_QuickSort.md) |

</div>

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>