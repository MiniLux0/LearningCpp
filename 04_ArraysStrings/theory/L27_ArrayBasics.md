# L27: Array Basics — Declaración, Inicialización y Acceso por Índice

## 1. La idea central: memoria contigua

Una variable normal (`int x;`) reserva **un espacio** para **un valor**.

Un **arreglo** (`int arr[4];`) reserva **un bloque contiguo** de memoria para **varios valores del mismo tipo**, todos seguidos uno tras otro.

```
memoria:  [casa 2000] [casa 2001] [casa 2002] [casa 2003]  ← 4 bytes = 1 int
          [casa 2004] [casa 2005] [casa 2006] [casa 2007]  ← 2º int
          [casa 2008] [casa 2009] [casa 2010] [casa 2011]  ← 3º int
          [casa 2012] [casa 2013] [casa 2014] [casa 2015]  ← 4º int
          ↑ dirección de inicio (arr[0])
```

**El índice no "busca" — calcula una dirección:**
```
dirección_de_arr[i] = dirección_inicio + i × sizeof(tipo)
```

- `arr[0]` → offset 0 → dirección_inicio
- `arr[1]` → offset 1 × 4 = 4 bytes → dirección_inicio + 4
- `arr[2]` → offset 2 × 4 = 8 bytes → dirección_inicio + 8

Por eso el primer índice es **0**: no te mueves, ya estás en el inicio.

---

## 2. Tres formas de inicializar

### Forma 1: Declarar y asignar después
```cpp
int arr[4];
arr[0] = 6;
arr[1] = 0;
arr[2] = 9;
arr[3] = 6;
```

### Forma 2: Inicializar en la declaración (tamaño explícito)
```cpp
int arr[4] = {6, 0, 9, 6};
```

### Forma 3: Tamaño inferido por el compilador
```cpp
int arr[] = {6, 0, 9, 6, 2, 0, 1, 1};  // tamaño = 8
```
El compilador **cuenta los elementos** y fija la dimensión. Ventaja: no hay riesgo de que el tamaño y la lista de valores se desincronicen.

---

## 3. Inicialización parcial → el resto son ceros

```cpp
int arr[5] = {1, 2};  // arr = {1, 2, 0, 0, 0}
int ceros[10] = {0};  // todos ceros
```

Regla: **los elementos no especificados se inicializan a 0** (value-initialization).

---

## 4. Acceso por índice

```cpp
int datos[5] = {10, 20, 30, 40, 50};

cout << datos[0];   // 10
cout << datos[4];   // 50

int i = 2;
cout << datos[i];        // 30  (variable como índice)
cout << datos[i + 1];    // 40  (expresión como índice)
```

**Rango válido:** `0` a `n-1` (donde `n` = dimensión).
- `datos[5]` → **comportamiento indefinido** (lee/escribe fuera del bloque)
- No hay error de compilación ni de ejecución garantizado — corrompe memoria silenciosamente.

---

## 5. Tamaño del arreglo en tiempo de ejecución

```cpp
int arr[5] = {10, 20, 30, 40, 50};
int n = sizeof(arr) / sizeof(arr[0]);  // 5 (C++98 compatible)

// C++17: std::size (requiere <iterator>)
#include <iterator>
int n17 = std::size(arr);  // 5 — más claro, funciona con cualquier contenedor
```

> **Ojo:** `sizeof(arr) / sizeof(arr[0])` solo funciona en el **scope donde se declaró** el arreglo. Si pasas el arreglo a una función, "decae" a puntero y `sizeof` devuelve el tamaño del puntero (8 bytes en 64 bits), no del arreglo. `std::size` tiene la misma limitación.

---

## 6. Recorrido típico

```cpp
// for clásico con índice
for (int i = 0; i < n; i++) {
    cout << arr[i] << ' ';
}

// range-based for (C++11) — solo lectura o modificación por referencia
for (int x : arr) {
    cout << x << ' ';
}

for (int &x : arr) {
    x *= 2;  // modifica el original
}

// C++17: structured bindings no aplican a arrays nativos directamente
// pero std::array sí los soporta
```

---

## 7. Pregunta de chequeo

> **Si escribes `int datos[5];` sin inicializar y luego haces `cout << datos[2];` — ¿qué imprime?**

**Respuesta:** **Basura (valor indeterminado)**.
- La declaración reserva el bloque contiguo, pero **no lo limpia**.
- Esos bytes contienen lo que hubiera antes en esa memoria.
- No es 0, no es error — es "lo que sea que haya ahí".

---

## 8. Ejercicio propuesto

> **Escribe un programa que:**
>
> - Declare un arreglo de enteros de tamaño 6 (usa una constante o variable para el tamaño, no lo repitas como número mágico en el loop — aquí es donde vigilo tu patrón de "números fijos")
> - Le pida al usuario los 6 valores uno por uno con `cin`
> - Los imprima todos de nuevo, separados por espacio

```cpp
#include <iostream>
using namespace std;

int main() {
    const int TAM = 6;           // constante para el tamaño — sin hardcodear 6 en el loop
    int valores[TAM];

    for (int i = 0; i < TAM; i++) {
        cout << "valor[" << i << "]: ";
        cin >> valores[i];
    }

    cout << "\nValores leidos: ";
    for (int i = 0; i < TAM; i++) {
        cout << valores[i] << ' ';
    }
    cout << endl;
    return 0;
}
```

> **Nota C++17:** En código moderno, para tamaño decidido en ejecución se prefiere `std::vector<int>` (header `<vector>`), que gestiona memoria automáticamente y conoce su tamaño con `.size()`. Los arreglos nativos de tamaño fijo son para cuando la dimensión se conoce en compilación.

---

## Archivos relacionados

- [`L27_ArrayBasics.cpp`](../code/L27_ArrayBasics.cpp) — Código ejecutable con declaración, inicialización y recorrido de arreglos

### 🧭 Navigation & Progression
| ⬅️ Previous Module | 🏠 Section Home | ➡️ Next Lesson |
|:------------------:|:---------------:|:--------------:|
| [**L26 — Headers & Prototypes**](../../03_Subroutines/theory/L26_HeadersAndPrototypes.md) | [**Arrays & Strings**](../) | [**L28 — Arrays as Parameters**](L28_ArraysAsParameters.md) |