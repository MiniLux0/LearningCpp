# L29 — Arreglos Multidimensionales: Matrices, Layout en Memoria y Funciones

> **Concepto central:** C++ no tiene matrices "reales" en hardware. Un arreglo 2D `int m[3][4]` es una **abstracción sintáctica** guardada como un bloque **1D contiguo en memoria** siguiendo el orden de filas (Row-Major Order).

---

## Objetivos de aprendizaje

- [ ] Comprender cómo se representan las matrices 2D y 3D en la memoria RAM (Row-Major Order)
- [ ] Dominar la sintaxis de declaración, inicialización explícita, parcial y a cero
- [ ] Aplicar la regla de dimensiones obligatorias en parámetros de funciones (`int m[][COLS]`)
- [ ] Calcular dinámicamente filas y columnas usando `sizeof`
- [ ] Manipular arreglos 2D de caracteres (arreglos de strings C-style)

---

## 1. La idea central: Row-Major Order (Fila Mayor)

Una matriz 2D de `3 filas x 4 columnas` (`int m[3][4]`) en C++ no es una grilla física. En memoria RAM, las filas se colocan **consecutivamente una después de otra**:

```
Conceptualmente (Grilla 3x4):
        Col 0   Col 1   Col 2   Col 3
Fila 0 [  1  ] [  2  ] [  3  ] [  4  ]
Fila 1 [  5  ] [  6  ] [  7  ] [  8  ]
Fila 2 [  9  ] [ 10  ] [ 11  ] [ 12  ]

En Memoria RAM (Bloque contiguo de 12 ints = 48 bytes):
+---+---+---+---+---+---+---+---+---+----+----+----+
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
+---+---+---+---+---+---+---+---+---+----+----+----+
  <--- Fila 0 ---> <--- Fila 1 ---> <--- Fila 2 --->
```

### Cálculo de dirección por el compilador

Para acceder a `m[i][j]`, el compilador realiza la fórmula de direccionamiento offset:

$$\text{Dirección}(m[i][j]) = \text{Dirección Base} + (i \times \text{COLS} + j) \times \text{sizeof(tipo)}$$

- `m[0][0]` → $(0 \times 4 + 0) = 0$
- `m[1][2]` → $(1 \times 4 + 2) = 6$ → posición offset 6 (elemento `7`)
- **Conclusión:** `int m[2][4]` e `int m[8]` ocupan exactamente los mismos bytes en memoria.

---

## 2. Declaración e Inicialización

### A. Asignación directa por índices
```cpp
int m[2][3];
m[0][0] = 1; m[0][1] = 2; m[0][2] = 3;
m[1][0] = 4; m[1][1] = 5; m[1][2] = 6;
```

### B. Inicialización con llaves anidadas (Recomendado por claridad)
```cpp
int m[3][4] = {
    {1, 2, 3, 4},   // Fila 0
    {5, 6, 7, 8},   // Fila 1
    {9, 10, 11, 12} // Fila 2
};
```

### C. Inicialización aplanada (Aprovecha row-major order)
```cpp
int m[2][4] = {6, 0, 9, 6, 2, 0, 1, 1};
// Fila 0: 6, 0, 9, 6
// Fila 1: 2, 0, 1, 1
```

### D. Inicialización parcial (Ceros implícitos)
Si no especificas todos los elementos, los faltantes se rellenan automáticamente con `0`:
```cpp
int parcial[2][3] = {{1, 2}, {3}};
// Resulta en:
// {1, 2, 0}
// {3, 0, 0}

int ceros[3][4] = {0}; // Rellena los 12 elementos con 0
```

---

## 3. Regla de Dimensiones: ¿Por qué la segunda dimensión es OBLIGATORIA?

Al declarar e inicializar en un solo paso, la **primera dimensión (filas)** se puede omitir y el compilador la deduce:

```cpp
int m[][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}}; // Correcto: deduce 2 filas
```

Sin embargo, las **dimensiones secundarias (columnas) NUNCA se pueden omitir**:
```cpp
// int m[2][] = {{1, 2}, {3, 4}}; // ❌ ERROR DE COMPILACIÓN
```

> **¿Por qué?** Para calcular `m[i][j]`, la fórmula requiere conocer $\text{COLS}$ ($i \times \text{COLS} + j$). Sin el número de columnas, el compilador no sabe cuántos elementos saltar para avanzar a la siguiente fila.

---

## 4. Pasar Matrices Multidimensionales a Funciones

Debido al decaimiento a puntero, al pasar una matriz a una función, la **primera dimensión es opcional**, pero **todas las demás dimensiones deben ser fijadas**:

```cpp
// Definición de la función (COLS = 4 obligatorio)
void imprimir2D(const int m[][4], int filas) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < 4; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}

// Llamada en main:
int matriz[3][4] = {...};
imprimir2D(matriz, 3);
```

---

## 5. Cálculo de Filas y Columnas con `sizeof`

Cuando la matriz se encuentra en el mismo scope de su declaración:

```cpp
int matriz[3][4];

int totalBytes = sizeof(matriz);        // 3 * 4 * 4 = 48 bytes
int bytesFila  = sizeof(matriz[0]);     // 4 * 4 = 16 bytes
int bytesElem  = sizeof(matriz[0][0]);  // 4 bytes

int filas = sizeof(matriz) / sizeof(matriz[0]);       // 48 / 16 = 3
int cols  = sizeof(matriz[0]) / sizeof(matriz[0][0]); // 16 / 4  = 4
```

---

## 6. Arreglos Tridimensionales (3D)

Un arreglo 3D se puede visualizar como un volumen (capas $\times$ filas $\times$ columnas):

```cpp
int cubo[2][3][4] = {0}; // 2 matrices de 3x4 (total 24 enteros)
cubo[1][2][3] = 99;      // Capa 1, Fila 2, Columna 3

// Recorrido anidado triple:
for (int c = 0; c < 2; c++) {
    for (int f = 0; f < 3; f++) {
        for (int col = 0; col < 4; col++) {
            // procesar cubo[c][f][col]
        }
    }
}
```

---

## 7. Arreglos de C-Strings (Matriz 2D de `char`)

Una matriz `char nombres[FILAS][LONGITUD]` se comporta como una lista de cadenas de texto C-style:

```cpp
char nombres[3][20] = {"Ana", "Carlos", "Beatriz"};

// nombres[0] es una C-string "Ana\0"
// nombres[1] es "Carlos\0"
// nombres[2] es "Beatriz\0"

for (int i = 0; i < 3; i++) {
    cout << "Persona " << i + 1 << ": " << nombres[i] << endl;
}
```

---

## 8. Preguntas de Chequeo

<details>
<summary><strong>1. ¿Por qué <code>int arr[2][4]</code> y <code>int arr[8]</code> son idénticos en memoria RAM?</strong></summary>

Porque ambos reservan 8 enteros consecutivos en memoria (32 bytes). La notación 2D `[2][4]` es solo una abstracción que usa la fórmula `i * 4 + j` para acceder a los índices.
</details>

<details>
<summary><strong>2. ¿Por qué la firma <code>void f(int m[][])</code> causa error de compilación?</strong></summary>

Porque sin especificar el número de columnas (`COLS`), la función no puede calcular el salto entre filas `i * COLS + j`. La primera dimensión se puede omitir, pero las columnas deben ser fijas.
</details>

---

## 9. Ejercicio Propuesto

> **Transpuesta de una matriz cuadrada in-place (3x3):**
> Escribe una función `void transpuesto(int m[3][3])` que intercambie `m[i][j]` con `m[j][i]` para todo $i < j$.

```cpp
void transpuesto(int m[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            int aux = m[i][j];
            m[i][j] = m[j][i];
            m[j][i] = aux;
        }
    }
}
```

---

## Archivos relacionados

- [`L29_MultidimensionalArrays.cpp`](../code/L29_MultidimensionalArrays.cpp) — Demostración de matrices 2D, 3D, funciones y arreglos de strings

## Navegación

| ← Anterior | Siguiente → |
|------------|-------------|
| [L28 — Arrays as Parameters](L28_ArraysAsParameters.md) | [L30 — C-Strings](L30_CStrings.md) |
