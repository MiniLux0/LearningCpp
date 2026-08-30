# Hoja de Repaso: Arreglos y Vectores (Arrays and Vectors)

¡Guarda esta página! Aquí tienes el resumen ejecutivo de todas las herramientas de memoria contigua, acceso seguro, iteración moderna y modularización multi-archivo del Módulo 06.

---

## 1. El Peligro de los C-Arrays (`T arr[N]`)
Los arreglos clásicos heredados de C residen en el Stack con un tamaño fijo inmutable. No conocen su propio tamaño en tiempo de ejecución y carecen por completo de verificación de límites (*Bounds Checking*). Escribir fuera de sus límites causa **Buffer Overflow** y corrupción de memoria en variables adyacentes (*Undefined Behavior*).
```cpp
// PELIGRO: Estilo C antiguo. Propenso a Buffer Overflow.
int notasAntiguas[3]{10, 8, 9};
```

---

## 2. El Estándar Moderno: `std::vector<T>`
Estructura de datos dinámica contigua administrada en el Heap. Crece automáticamente, conoce su propio tamaño mediante `.size()` y gestiona la memoria de forma segura.
```cpp
#include <vector>

// Inicialización con elementos específicos (Lista de inicialización)
std::vector<int> notas{10, 8, 9};       // Contiene: [10, 8, 9] (size = 3)

// Inicialización de tamaño con valor por defecto (Constructor de conteo)
std::vector<int> ceros(5, 0);           // Contiene: [0, 0, 0, 0, 0] (size = 5)
```

> [!WARNING]
> **Trampa de Inicialización:** `std::vector<int> v{5};` crea un vector con **1 elemento** cuyo valor es 5. En cambio, `std::vector<int> v(5);` crea un vector con **5 elementos** inicializados en 0.

---

## 3. Acceso Seguro: `.at()` vs `operator[]`
El operador de subíndice `[]` no verifica límites por razones de rendimiento puro en C antiguo. Si accedes a un índice inválido con `[]`, el programa causa comportamiento indefinido o lee memoria corrupta en silencio. El método `.at()` comprueba el rango en cada acceso y lanza la excepción `std::out_of_range` si el índice es inválido.
```cpp
std::vector<int> datos{10, 20, 30};

int valorSeguro = datos.at(1); // 20 (Verificado)
// int valorInvalido = datos.at(99); // Lanza std::out_of_range inmediatamente
```

---

## 4. Contención de Errores: `try / catch` Básico
Permite interceptar una excepción lanzada por `.at()` para evitar que el sistema operativo aborte el programa de forma abrupta.
```cpp
#include <iostream>
#include <vector>
#include <stdexcept>

std::vector<int> inventario{100, 200};

try {
    std::cout << inventario.at(5) << '\n'; // Fuera de limites
} catch (const std::out_of_range& error) {
    std::cout << "Error de acceso: " << error.what() << '\n';
}
```

---

## 5. Recorridos Idiomáticos: `range-based for`
Elimina los índices manuales, los contadores auxiliares y los errores de desfase por uno (*Off-By-One Bugs*).
```cpp
std::vector<int> puntajes{15, 30, 45};

// Lectura de solo copia (adecuada para tipos primitivos)
for (int puntaje : puntajes) {
    std::cout << puntaje << '\n';
}
```

---

## 6. Métodos Dinámicos Fundamentales
```cpp
std::vector<int> valores{};

valores.push_back(42);   // Inserta al final: [42]
valores.size();          // Retorna la cantidad de elementos (size_t)
valores.empty();         // Retorna true si size() == 0
valores.clear();         // Elimina todos los elementos (size pasa a 0)
valores.reserve(100);    // Reserva capacidad para 100 elementos en el Heap sin realocar
```

---

## 7. Arquitectura Multi-Archivo (`.h` y `.cpp`)
Separa las interfaces públicas (declaraciones) de los detalles de implementación (definiciones) para un diseño profesional y escalable.

1. **Archivo de Cabecera (`.h` / Header):**
```cpp
// Estadisticas.h
#pragma once
#include <vector>

double calcularPromedio(const std::vector<double>& notas);
```

2. **Archivo de Implementación (`.cpp`):**
```cpp
// Estadisticas.cpp
#include "Estadisticas.h"

double calcularPromedio(const std::vector<double>& notas) {
    if (notas.empty()) {
        return 0.0;
    }
    double suma{0.0};
    for (double nota : notas) {
        suma += nota;
    }
    return suma / static_cast<double>(notas.size());
}
```

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
