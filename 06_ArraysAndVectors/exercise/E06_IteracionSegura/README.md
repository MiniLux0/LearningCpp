# Reto E06: Iteración Segura

## Contexto
El observatorio sismológico nacional procesa lecturas de sensores de vibración terrestre almacenadas en un vector. El algoritmo de cálculo de energía acumulada fue escrito por un becario usando un bucle `for` tradicional con un índice manual.

Debido a un error de tipeo (`i <= lecturas.size()`), el bucle genera un fallo *Off-By-One* intentando acceder a una posición fuera de límites, provocando que la alerta sísmica temprana falle. Tu misión es modernizar el procesador sismológico migrando todo el cálculo a bucles idiomáticos `range-based for`.

## Tu Misión
Abre el archivo `E06_IteracionSegura.cpp`:
1. Reemplaza el bucle con índice vulnerable por un `range-based for` que sume todas las intensidades sísmicas.
2. Utiliza otro `range-based for` para contar cuántas lecturas superaron el umbral crítico de peligro (`5.0` grados).
3. Calcula el promedio de intensidad de las lecturas.

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 -Wall -Wextra E06_IteracionSegura.cpp -o app
./app
```

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
