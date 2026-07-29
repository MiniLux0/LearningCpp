# Ejercicios — Módulo 04: Arrays & Strings

> Nomenclatura: `E` = ejercicio guiado, `A/B/C` = práctica independiente.

---

## L27: Array Basics

### E01 — Leer N enteros y mostrar inverso
```cpp
// Pide N, lee N enteros en un array, imprime en orden inverso
// Ejemplo: N=5, [10 20 30 40 50] → salida: 50 40 30 20 10
```

### E02 — Buscar valor (linear search)
```cpp
// Función: int buscar(const int arr[], int n, int valor)
// Devuelve índice de la primera ocurrencia, o -1 si no está
```

### E03 — Mínimo, máximo y promedio
```cpp
// Función: void stats(const int arr[], int n, int &min, int &max, double &prom)
// Un solo recorrido por el array
```

### A — Filtrar pares
```cpp
// Dado array origen, copiar solo los pares a un array destino
// Devuelve cantidad de pares copiados
// Firma: int filtrarPares(const int origen[], int n, int destino[], int maxDest)
```

### B — Rotar array k posiciones
```cpp
// Rotar a la izquierda: [1,2,3,4,5], k=2 → [3,4,5,1,2]
// In-place (sin array extra) — pista: reversar segmentos
```

---

## L28: Arrays as Parameters

### E04 — Función que recibe array + tamaño (parametrizado)
```cpp
// void procesar(int arr[], int n);
// En main: leer N, crear array dinámico, llamar a procesar
// NO hardcodear el tamaño (ej. no usar 5, 10, 100 fijos)
```

### E05 — Concatena dos arrays
```cpp
// void concatenar(const int a[], int na, const int b[], int nb, int resultado[], int &nr);
// resultado debe tener capacidad na+nb
```

### E06 — Modificar por referencia vs copia
```cpp
// Demostrar que void f(int arr[], int n) modifica el original
// y void f(const int arr[], int n) no compila si intentas modificar
```

### C — Estadísticas con template size_t N
```cpp
// template<size_t N> void stats(const int (&arr)[N], ...)
// Probar con arrays de distinto tamaño sin pasar n explícito
```

---

## L29: Multidimensional Arrays

### E07 — Suma de matrices
```cpp
// void sumar(const int a[][COLS], const int b[][COLS], int res[][COLS], int filas, int cols);
// COLS = constante global o template
```

### E08 — Transpuesta in-place (cuadrada)
```cpp
// void transpuesta(int m[][MAX], int n);  // solo triangular superior
```

### E09 — Buscar en matriz ordenada por filas y columnas
```cpp
// bool buscar(const int m[][COLS], int filas, int cols, int valor);
// Empezar en esquina sup-der: si actual > valor → izq; si < → abajo
```

### A — Matriz identidad
```cpp
// void identidad(int m[][MAX], int n);  // pone 1 en diagonal, 0 en resto
```

### B — Multiplicación de matrices
```cpp
// void multiplicar(const int a[][K], const int b[][L], int res[][L], int M, int K, int L);
// a: M×K, b: K×L, res: M×L
```

---

## L30: C-Strings

### E10 — Contar vocales
```cpp
// int contarVocales(const char s[]);  // case-insensitive
```

### E11 — Invertir string in-place
```cpp
// void invertir(char s[]);  // "hola" → "aloh"
// Usar dos índices: i=0, j=strlen(s)-1; swap e i++, j--
```

### E12 — Eliminar espacios
```cpp
// void compactar(char s[]);  // "h o l a" → "hola"
// Mismo patrón write/read que normalizar
```

### E13 — Verificar anagrama
```cpp
// bool esAnagrama(const char s1[], const char s2[]);
// Normalizar ambos (minúsculas, solo alnum), ordenar, comparar
// O contar frecuencias con array int[256] = {0}
```

### E14 — Tokenizar por delimitador
```cpp
// int split(const char s[], char delim, char tokens[][MAX_TOKEN], int maxTokens);
// "uno,dos,tres" + ',' → tokens = {"uno","dos","tres"}, devuelve 3
```

### C — Palíndromo recursivo
```cpp
// bool palRec(const char s[], int i, int j);
// Caso base: i >= j → true
// Paso: s[i] == s[j] && palRec(s, i+1, j-1)
```

---

## Entrega sugerida

```
04_ArraysStrings/
├── exercise/
│   ├── build/
│   ├── E01_ReverseArray.cpp
│   ├── E02_LinearSearch.cpp
│   ├── E03_Stats.cpp
│   ├── A_FilterEven.cpp
│   ├── B_RotateArray.cpp
│   ├── E04_ProcessArray.cpp
│   ├── E05_ConcatArrays.cpp
│   ├── E06_ConstCorrectness.cpp
│   ├── C_TemplateStats.cpp
│   ├── E07_MatrixSum.cpp
│   ├── E08_Transpose.cpp
│   ├── E09_SearchMatrix.cpp
│   ├── A_IdentityMatrix.cpp
│   ├── B_MatrixMul.cpp
│   ├── E10_CountVowels.cpp
│   ├── E11_ReverseString.cpp
│   ├── E12_CompactSpaces.cpp
│   ├── E13_Anagram.cpp
│   ├── E14_SplitString.cpp
│   └── C_PalindromeRecursive.cpp
```

> Cada `.cpp` compila independiente (`g++ E01_ReverseArray.cpp -o E01.exe`).
> En `build/` quedan los ejecutables y `.d` (dependencias).