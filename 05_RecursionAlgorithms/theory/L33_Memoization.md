# L33 — Memoización y Programación Dinámica Top-Down

> [!NOTE]
> **Fundamentación Académica:** Esta lección cubre la **Sección 8.4 (*Memoization*, pp. 365–370)** del libro oficial de Stanford CS106B (*Programming Abstractions in C++* por Eric Roberts).

---

## 🧭 Navegación Rápida

- 📄 **Lectura Académica Base:**
  - 🌲 [Stanford CS106B Textbook — Ch 8.4: Memoization (pp. 365–370)](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Laboratorio de Código:** [`L33_Memoization.cpp`](../code/L33_Memoization.cpp)

---

## Objetivos de Aprendizaje

- [ ] Identificar el fenómeno de **Subproblemas Superpuestos**: cuándo una función recursiva recalcula el mismo valor múltiples veces.
- [ ] Entender qué es la **Memoización** y cómo actúa como un "cuaderno de apuntes" para la función.
- [ ] Implementar memoización usando **arreglos estáticos** — la misma herramienta que ya conoces de la Sección 04.
- [ ] Transformar la función `fibonacciNaive` de $O(2^N)$ a $O(N)$ aplicando el patrón de 4 pasos.

> [!NOTE]
> **Herramientas que usamos en esta lección:**
> Solo necesitas lo que ya viste: arreglos (`int arr[]`, **Sección 04**), funciones con parámetros por referencia (`&`, **Sección 03**), y `for`/`if` (**Sección 02**). No se introduce nada nuevo del lenguaje — solo una nueva *técnica de diseño*.

---

## 1. El Problema — ¿Por qué la Recursión Simple es Lenta?

En **L32** implementamos `fibonacciNaive`. Funciona, pero es desesperadamente lento para valores grandes. Observa el árbol de llamadas para `fib(4)`:

<div align="center">
  <video autoplay loop muted playsinline src="assets/fib_memo_tree.mp4"></video>
</div>

¿Lo ves? `fib(2)` se calcula **dos veces**. `fib(1)` se calcula **tres veces**. Cada vez, la función **repite exactamente el mismo trabajo** desde cero, sin recordar que ya lo hizo.

Esto se llama **Subproblemas Superpuestos (*Overlapping Subproblems*)**. La consecuencia matemática es brutal: el número total de llamadas crece a $O(2^N)$.

| Llamada | Sin Memoización | Con Memoización |
| :--- | :--- | :--- |
| `fib(10)` | 177 llamadas | 10 llamadas |
| `fib(30)` | 2,692,537 llamadas | 30 llamadas |
| `fib(50)` | ≈ $10^{15}$ llamadas (minutos) | 50 llamadas (< 1 ms) |

> [!TIP]
> **Analogía del Cuaderno de Apuntes:**
> Imagina que cada vez que alguien te pregunta *"¿Cuánto es 237 × 48?"* lo calculas de cero.
> Una persona inteligente lo calcula **una sola vez**, lo anota en un cuaderno y la próxima vez **lee la respuesta directamente**. Eso es exactamente la **Memoización**.

---

## 2. La Solución — El Patrón de 4 Pasos

La **Memoización** consiste en darle a la función un **arreglo auxiliar (`memo[]`)** que actúa como cuaderno. Antes de calcular algo, la función consulta el cuaderno. Si ya está anotado, retorna inmediatamente.

<div align="center">
  <video autoplay loop muted playsinline src="assets/l33_overlapping.mp4"></video>
</div>

Los 4 pasos son siempre los mismos, en ese orden exacto:

```
PASO 1 → ¿Ya calculé este valor antes? (consultar el cuaderno)
PASO 2 → ¿Es un caso base trivial?
PASO 3 → Llamada recursiva para calcularlo
PASO 4 → Anotar el resultado en el cuaderno antes de retornar
```

---

## 3. Implementación — Fibonacci Memoizado con Array

Usamos un arreglo estático como cuaderno. El valor centinela `-1` significa *"aún no calculado"*:

```cpp
#include <iostream>
using namespace std;

// MAX_N define el tamaño máximo del cuaderno de apuntes (arreglo memo)
const int MAX_N = 100;

// El arreglo 'memo' es el cuaderno: memo[n] guarda el resultado de fib(n)
// Inicializado con -1 (centinela = "no calculado todavía")
long long memo[MAX_N];

void inicializarMemo() {
    for (int i = 0; i < MAX_N; i++) {
        memo[i] = -1; // -1 significa "aún no calculado"
    }
}

long long fibMemo(int n) {
    // ─── PASO 1: Consultar el cuaderno ───────────────────────────────────────
    // Si memo[n] != -1, ya existe la respuesta. Retornar directamente en O(1).
    if (memo[n] != -1) return memo[n];

    // ─── PASO 2: Casos Base (igual que la versión sin memoización) ───────────
    if (n == 0) return (memo[0] = 0);
    if (n == 1) return (memo[1] = 1);

    // ─── PASO 3: Llamada Recursiva (solo llega aquí si no estaba en el cuaderno)
    long long resultado = fibMemo(n - 1) + fibMemo(n - 2);

    // ─── PASO 4: Anotar el resultado en el cuaderno antes de retornar ────────
    memo[n] = resultado;
    return memo[n];
}

int main() {
    inicializarMemo(); // Siempre inicializar antes de usar

    cout << "fib(10) = " << fibMemo(10) << endl; // 55
    cout << "fib(30) = " << fibMemo(30) << endl; // 832040
    cout << "fib(50) = " << fibMemo(50) << endl; // 12586269025

    return 0;
}
```

> [!IMPORTANT]
> **El Paso 1 siempre va primero**, incluso antes de los casos base. Si no revisas el cuaderno al inicio, nunca aprovecharás lo que ya calculaste.

### ¿Qué pasa internamente con `fib(4)`?

```text
fibMemo(4)  → cuaderno vacío, calcula...
  fibMemo(3)  → calcula...
    fibMemo(2)  → calcula...
      fibMemo(1)  → caso base → retorna 1, anota memo[1]=1
      fibMemo(0)  → caso base → retorna 0, anota memo[0]=0
    → retorna 1, anota memo[2]=1
    fibMemo(1)  → PASO 1: memo[1]=1 ya existe → retorna 1 al instante ✓
  → retorna 2, anota memo[3]=2
  fibMemo(2)  → PASO 1: memo[2]=1 ya existe → retorna 1 al instante ✓
→ retorna 3, anota memo[4]=3
```

La segunda llamada a `fib(2)` y `fib(1)` **no ejecuta nada** — lee directo del cuaderno.

---

## 4. Segundo Caso Práctico: Caminos en Grilla (*Grid Traveler*)

Ahora aplicamos el mismo patrón a un problema bidimensional para demostrar que la memoización es una **técnica universal**.

**El problema:** Un robot está en la esquina superior izquierda `(1,1)` de una grilla de $R \times C$. Solo puede moverse **hacia la Derecha** o **hacia Abajo**. ¿Cuántos caminos únicos existen para llegar a la esquina inferior derecha `(R,C)`?

**¿Por qué aparecen subproblemas superpuestos?**
Dos caminos distintos pueden terminar en la **misma celda** por rutas diferentes. Desde esa celda, el sub-problema es idéntico, pero sin memoización se calcularía dos veces:

<div align="center">
  <video autoplay loop muted playsinline src="assets/l33_memo_pattern.mp4"></video>
</div>

### Implementación con Arreglo 2D como Cuaderno

Aquí el cuaderno necesita **dos dimensiones** (un índice por fila y otro por columna), algo que ya viste en **L29 — Arreglos Multidimensionales**:

```cpp
#include <iostream>
using namespace std;

const int MAX_R = 20;
const int MAX_C = 20;

// El cuaderno ahora es un arreglo 2D: memo[r][c] guarda la cantidad
// de caminos únicos desde la esquina (r,c) hasta el destino final.
long long memo2D[MAX_R][MAX_C];

void inicializarMemo2D() {
    for (int r = 0; r < MAX_R; r++)
        for (int c = 0; c < MAX_C; c++)
            memo2D[r][c] = -1;
}

long long contarCaminos(int r, int c) {
    // PASO 1: Consultar el cuaderno 2D
    if (memo2D[r][c] != -1) return memo2D[r][c];

    // PASO 2: Casos Base
    if (r == 0 || c == 0) return (memo2D[r][c] = 0); // Grilla inválida
    if (r == 1 && c == 1) return (memo2D[r][c] = 1); // Destino: 1 solo camino

    // PASOS 3 y 4: Calcular y anotar
    // Desde (r,c) se puede llegar moviéndose desde arriba (r-1,c) o desde la izquierda (r,c-1)
    memo2D[r][c] = contarCaminos(r - 1, c) + contarCaminos(r, c - 1);
    return memo2D[r][c];
}

int main() {
    inicializarMemo2D();

    cout << "Caminos en grilla 3x3: " << contarCaminos(3, 3) << endl; // 6
    cout << "Caminos en grilla 4x4: " << contarCaminos(4, 4) << endl; // 20
    cout << "Caminos en grilla 18x18: " << contarCaminos(18, 18) << endl; // 2333606220

    return 0;
}
```

> [!IMPORTANT]
> **El impacto es aún más dramático que en Fibonacci:**
> - **Sin Memoización:** $O(2^{R+C})$ → para $18 \times 18$ son más de $2.3 \times 10^{10}$ llamadas (tarda minutos).
> - **Con Memoización:** $O(R \cdot C)$ → para $18 \times 18$ son exactamente **324 estados** (menos de 1 ms).

---

## 5. Comparación de Estrategias

| Criterio | Recursión Simple | Memoización (*Top-Down*) |
| :--- | :--- | :--- |
| **Dirección** | Divide $N$ hasta llegar al caso base | Igual, pero reutiliza lo ya calculado |
| **Complejidad** | $O(2^N)$ — Exponencial | $O(N)$ — Lineal |
| **Memoria extra** | Solo la pila de llamadas | Pila + arreglo `memo[]` |
| **Dificultad** | La misma recursión del tema anterior | Añadir el arreglo `memo` y el Paso 1 |

> [!NOTE]
> Existe una tercera estrategia llamada **Tabulación (*Bottom-Up*)** que construye la tabla `memo[]` de abajo hacia arriba con un simple `for` loop, eliminando la recursión completamente. La veremos en un módulo posterior cuando estudiemos algoritmos avanzados.

---

## ❓ Preguntas de Chequeo

### Pregunta #1 — El error más común

Analiza este código con un error intencional:

```cpp
long long fibMal(int n) {
    if (n == 0) return (memo[0] = 0);   // A
    if (n == 1) return (memo[1] = 1);   // B
    memo[n] = fibMal(n-1) + fibMal(n-2); // C
    if (memo[n] != -1) return memo[n]; // D ← ¿Problema aquí?
    return memo[n];
}
```

**¿Cuál es el error y dónde debería estar la línea D?**

<details>
<summary>🔍 <strong>Ver Explicación</strong></summary>

**El error:** La consulta al cuaderno (línea D) está **después** del cálculo recursivo (línea C). Esto hace que el cuaderno **nunca se consulte** — siempre se recalcula primero. La verificación debe ser la **primera instrucción** de la función:

```cpp
long long fibBien(int n) {
    if (memo[n] != -1) return memo[n]; // ← PRIMERO: consultar cuaderno
    if (n == 0) return (memo[0] = 0);
    if (n == 1) return (memo[1] = 1);
    memo[n] = fibBien(n-1) + fibBien(n-2);
    return memo[n];
}
```

</details>

---

### Pregunta #2 — Tamaño del cuaderno

Si llamas a `fibMemo(75)`, ¿es suficiente `const int MAX_N = 50`? ¿Qué ocurre si no lo es?

<details>
<summary>🔍 <strong>Ver Respuesta</strong></summary>

**No es suficiente.** El arreglo `memo[MAX_N]` solo tiene 50 posiciones (índices 0 a 49). Al intentar acceder a `memo[75]`, estarías escribiendo **fuera de los límites del arreglo** — un *undefined behavior* que puede corromper memoria o causar un *crash*. Siempre debes asegurarte de que `MAX_N > n` para cualquier valor que vayas a calcular.

</details>

---

## 📝 Resumen de L33

1. **El Problema:** La recursión ingenua recalcula los mismos subproblemas → explosión $O(2^N)$.
2. **La Solución:** Darle a la función un **arreglo auxiliar `memo[]`** como cuaderno de apuntes.
3. **El Patrón de 4 Pasos** (siempre en este orden):
   - Consultar cuaderno → Caso base → Llamada recursiva → Anotar y retornar.
4. **Arreglos 1D y 2D** como cuadernos: la misma herramienta de Sección 04, usada de una forma nueva.
5. **El Paso 1 siempre va primero** — de lo contrario, el cuaderno nunca se consulta.

---

<div align="center">

### 🧭 Navegación y Progresión

| ⬅️ Lección Anterior | 🏠 Inicio de Sección | ➡️ Siguiente Lección |
|:------------------:|:-------------------:|:------------------:|
| [**⬅️ L32 — Problemas Recursivos**](L32_RecursiveProblems.md) | [**🏠 Recursión y Algoritmos**](../README.md) | [**L34 — Notación Big-O ➡️**](L34_BigONotation.md) |

</div>

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>