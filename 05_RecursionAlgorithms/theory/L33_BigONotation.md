# L33 — Notación Big-O: Análisis Asintótico de Complejidad Temporal y Espacial

> [!NOTE]
> **Fundamentación Académica:** Esta lección sintetiza los conceptos del **Capítulo 10 (*Algorithmic Analysis*)** del libro oficial de Stanford CS106B ([`CS106BX-Reader.pdf`](../../files/cs106b/textbook/CS106BX-Reader.pdf)) y **Stanford CS106X Handouts**.

---

## 🧭 Navegación Rápida

- 📄 **Lecturas Académicas Base:**
  - 🌲 [Stanford CS106B Textbook (Ch 10, pp. 433–470)](../../files/cs106b/textbook/CS106BX-Reader.pdf)
  - ⚡ [Stanford CS106X — Asymptotic Algorithmic Analysis](../../files/cs106x/README.md)
- 💻 **Laboratorio de Código:** [`L33_BigONotation.cpp`](../code/L33_BigONotation.cpp)

---

## Objetivos de Aprendizaje

- [ ] Comprender qué mide la **Notación Big-O ($O$)** y por qué es independiente del hardware/reloj de la CPU.
- [ ] Diferenciar entre **Complejidad Temporal** (*Time Complexity*) y **Complejidad Espacial** (*Space Complexity*).
- [ ] Clasificar las funciones de crecimiento estándar: $O(1)$, $O(\log N)$, $O(N)$, $O(N \log N)$, $O(N^2)$, $O(2^N)$.
- [ ] Aplicar las reglas de simplificación asintótica (descartar constantes y términos no dominantes).

---

## 1. ¿Por qué necesitamos la Notación Big-O?

No podemos medir la eficiencia de un algoritmo simplemente usando un cronómetro (`std::chrono`), porque el tiempo en segundos depende de:
- La potencia del procesador (CPU).
- El compilador y sus optimizaciones (`-O3`).
- Otros programas abiertos en el sistema operativo.

> [!IMPORTANT]
> **La Notación Big-O** mide cómo **crece el número de operaciones requeridas** a medida que el tamaño de los datos de entrada ($N$) tiende al infinito ($N \to \infty$).

---

## 2. Jerarquía de Complejidades Comunes

A continuación se muestra el ranking de eficiencias ordenadas de más rápida a más lenta:

| Notación Big-O | Nombre Complejidad | Ejemplo Algorítmico típico | Evaluación para $N = 1000$ |
| :---: | :--- | :--- | :--- |
| **$O(1)$** | **Constante** | Acceso a un elemento de un arreglo `arr[i]` o push en pila. | $1$ operación |
| **$O(\log N)$** | **Logarítmica** | Búsqueda Binaria (*Binary Search*). | $\approx 10$ operaciones |
| **$O(N)$** | **Lineal** | Búsqueda Lineal (*Linear Search*) o recorrer un arreglo de inicio a fin. | $1000$ operaciones |
| **$O(N \log N)$** | **Lineal-Logarítmica** | Algoritmos de ordenamiento eficientes: **MergeSort**, **QuickSort**. | $\approx 10,000$ operaciones |
| **$O(N^2)$** | **Cuadrática** | Bucles anidados simples: **Bubble Sort**, **Selection Sort**, **Insertion Sort**. | $1,000,000$ operaciones |
| **$O(2^N)$** | **Exponencial** | Fibonacci recursivo ingenuo o generación de todos los subconjuntos. | $1.07 \times 10^{301}$ op. 💥 |

---

## 3. Reglas de Simplificación Asintótica

Para calcular el Big-O de cualquier bloque de código C++:

### Regla 1: Descartar Constantes Multiplicativas
Si un algoritmo realiza $5N$ operaciones, constantes como el $5$ no cambian la tasa de crecimiento para $N$ grande:
$$O(5N) \implies O(N)$$

### Regla 2: Mantener únicamente el Término Dominante
Si un algoritmo realiza $N^2 + 100N + 500$ operaciones, cuando $N = 1,000,000$, el término $N^2 = 10^{12}$ domina por completo sobre $100N = 10^8$:
$$O(N^2 + 100N + 500) \implies O(N^2)$$

---

## 4. Ejemplos Prácticos de Código C++

### Ejemplo A: Complejidad Constante $O(1)$
```cpp
bool esPrimerElementoPar(const int arr[], int size) {
    if (size == 0) return false;
    return arr[0] % 2 == 0; // Se ejecuta en 1 sola operación independientemente de si N es 10 o 1,000,000
}
```

### Ejemplo B: Complejidad Lineal $O(N)$
```cpp
int sumarElementos(const int arr[], int n) {
    int suma = 0;
    for (int i = 0; i < n; i++) { // Se ejecuta exactamente N veces
        suma += arr[i];
    }
    return suma;
}
```

### Ejemplo C: Complejidad Cuadrática $O(N^2)$
```cpp
void imprimirMatrizBucleAnidado(int n) {
    for (int i = 0; i < n; i++) {         // N iteraciones exteriores
        for (int j = 0; j < n; j++) {     // N iteraciones interiores
            cout << "(" << i << "," << j << ") ";
        }
    }
} // Total: N * N = N^2 operaciones -> O(N^2)
```

---

## 5. Complejidad Espacial (*Space Complexity*)

No solo medimos el tiempo, sino también la **memoria adicional** que consume el programa:
- **$O(1)$ Espacial:** Si solo usamos un par de variables simples (`int i`, `double temp`).
- **$O(N)$ Espacial:** Si creamos un arreglo secundario de tamaño $N$, o si realizamos $N$ llamadas recursivas en el *Call Stack*.

---

## ❓ Pregunta de Chequeo #1 — Cálculo de Complejidad

Calcula el Big-O del siguiente código C++:

```cpp
void algoritmoMisterioso(int n) {
    for (int i = 0; i < n; i++) {
        cout << i << endl;
    }
    for (int j = 0; j < n; j++) {
        for (int k = 0; j < n; j++) { // Atención aquí
            // Operaciones O(1)
        }
    }
}
```

**¿Cuál es la complejidad temporal asintótica en notación Big-O?**

<details>
<summary>🔍 <strong>Ver Explicación y Respuesta</strong></summary>

> [!TIP]
> **Respuesta:** **$O(N^2)$**
>
> **Explicación:**
> El primer bucle realiza $N$ operaciones $\to O(N)$.
> El segundo bloque contiene dos bucles anidados que realizan $N \times N = N^2$ operaciones $\to O(N^2)$.
> Sumando ambos bloques: $O(N + N^2)$.
> Aplicando la **Regla del Término Dominante**, ignoramos $N$ y nos quedamos con la potencia mayor: **$O(N^2)$**.

</details>

---

## 📝 Resumen Resumido de L33

1. **Big-O** describe el límite superior del crecimiento del tiempo o espacio en función del tamaño de entrada $N$.
2. **Ignorar constantes:** $O(2N)$ es $O(N)$.
3. **Quedarse con el término dominante:** $O(N^2 + N)$ es $O(N^2)$.
4. **Ranking de eficiencia:** $O(1) < O(\log N) < O(N) < O(N \log N) < O(N^2) < O(2^N)$.

---

<div align="center">

### 🧭 Navigation & Progression

| ⬅️ Previous Lesson | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:--------------:|:--------------:|
| [**⬅️ L32 — Recursive Problems**](L32_RecursiveProblems.md) | [**🏠 Recursion & Algorithms**](../README.md) | [**L34 — Linear & Binary Search ➡️**](L34_LinearBinarySearch.md) |

</div>

---
*MiniLux0 — Learning C++ Section 05*
