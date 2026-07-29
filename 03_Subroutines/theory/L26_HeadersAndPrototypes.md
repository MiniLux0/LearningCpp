# L26 — Headers and Prototypes (Encabezados y Prototipos)

> **Concepto central**: El compilador C++ lee **una sola vez, de arriba a abajo**. Para llamar una función, necesita saber su **firma** (retorno + tipos de parámetros) **antes** de la llamada. Los *prototypes* resuelven esto adelantando esa información.

---

## 🎯 Objetivos de aprendizaje

- [ ] Entender por qué el compilador necesita ver la firma antes de llamar
- [ ] Saber escribir y usar *function prototypes* (declaraciones adelantadas)
- [ ] Resolver recursión mutua con prototypes
- [ ] Separar interfaz (`.h`) de implementación (`.cpp`)
- [ ] Explicar por qué librerías compiladas se distribuyen con `.h` + `.dll/.so` (sin `.cpp`)

---

## 1️⃣ El problema: compilador de una pasada

```cpp
int main() {
    foo();  // ❌ ERROR: ¿qué es foo? ¿devuelve int? ¿void? ¿qué params?
}

void foo() { cout << "hola"; }  // definida DESPUÉS
```

El compilador llega a `foo()` en `main` y **no sabe**:
- Qué tipo devuelve
- Qué parámetros espera
- Si la llamada es válida

---

## 2️⃣ La solución: Function Prototype

```cpp
void foo();  // PROTOTYPE: solo firma, punto y coma, SIN cuerpo

int main() {
    foo();  // ✅ OK: compilador ya conoce la firma
}

void foo() { cout << "hola"; }  // definición (puede ir después)
```

### Qué es un prototype
| Elemento | Ejemplo |
|----------|---------|
| Tipo retorno | `void` |
| Nombre | `foo` |
| Parámetros (tipos) | `()` — vacío = cero args |
| Terminador | `;` (punto y coma, **no** llaves) |

> **Regla**: Solo importan **tipos** y **orden**. Nombres de parámetros son opcionales e irrelevantes.

```cpp
// Estos tres prototypes son IDÉNTICOS para el compilador:
int square(int x);
int square(int z);
int square(int);      // nombres omitidos: OK
```

---

## 3️⃣ Caso donde reordenar NO alcanza: recursión mutua

```cpp
// foo llama a bar, bar llama a foo — no hay orden lineal posible
int foo(int n) { return bar(n - 1) + 1; }
int bar(int n) { return foo(n - 1) * 2; }  // foo no vista aún!
```

**Prototypes resuelven esto:**

```cpp
int foo(int);  // prototype
int bar(int);  // prototype

int foo(int n) { return n <= 0 ? 1 : bar(n - 1) + 1; }
int bar(int n) { return n <= 0 ? 1 : foo(n - 1) * 2; }
```

---

## 4️⃣ Header Pattern: `.h` + `.cpp` (separación real)

### `milib.h` — **Interface** (qué hace, cómo se llama)
```cpp
#ifndef MILIB_H
#define MILIB_H

int square(int);     // prototype
int cube(int);       // prototype

#endif
```

### `milib.cpp` — **Implementación** (cómo lo hace)
```cpp
#include "milib.h"

int square(int x) { return x * x; }
int cube(int x)   { return x * square(x); }
```

### `main.cpp` — **Usuario** (usa la librería)
```cpp
#include "milib.h"

int main() {
    cout << cube(3);  // 27
}
```

### Flujo de compilación

```mermaid
flowchart LR
    A[main.cpp] -->|#include "milib.h"| B[Compilador]
    C[milib.cpp] -->|#include "milib.h"| D[Compilador]
    B --> E[main.o]
    D --> F[milib.o]
    E --> G[Linker]
    F --> G
    G --> H[ejecutable]
```

| Archivo | Quién lo ve | Qué contiene |
|---------|-------------|--------------|
| `.h` (header) | **Todos** (main, otros .cpp, usuarios) | Prototypes, tipos, constantes, `inline`/`constexpr` |
| `.cpp` | **Solo compilador** (unidad de traducción) | Cuerpos de funciones, detalles privados |

---

## 5️⃣ Pregunta de chequeo: ¿Por qué `.dll/.so` + `.h` sin `.cpp`?

> **Respuesta**: El `.h` contiene **todo lo que el COMPILADOR necesita** para generar código que LLAME a la función:
> - Nombre de la función
> - Tipo de retorno
> - Tipos y orden de parámetros
>
> El `.cpp` (implementación) ya fue **compilado a código máquina** dentro del `.dll` (Windows) o `.so` (Linux/macOS).
>
> El usuario compila su código contra el `.h` (interfaz), y el **linker** resuelve las llamadas contra el `.dll/.so` (implementación binaria).
>
> **No necesita ver el código fuente** — solo la *firma* (el "menú del restaurante").

---

## 📋 Resumen rápido L26

| Concepto | Clave |
|----------|-------|
| **Prototype** | `tipo nombre(tipos_params);` — firma + `;`, sin `{}` |
| **Nombres params** | Irrelevantes en prototype (solo tipos importan) |
| **Uso** | Llamar antes de definir, recursión mutua |
| **Header `.h`** | Interfaz pública: prototypes, tipos, `constexpr`, `inline` |
| **Source `.cpp`** | Implementación privada: cuerpos de funciones |
| **Distribución librería** | `.h` + `.dll/.so` (binario) — **nunca** `.cpp` |

---

## 🔗 Archivos relacionados

- [`../L26_HeadersAndPrototypes.cpp`](../L26_HeadersAndPrototypes.cpp) — Implementación completa ejecutable

## 🔗 Navegación

| ← Anterior | Siguiente → |
|------------|-------------|
| [L25 — Function Parameters](L25_FunctionParameters.md) | [L27 — Array Basics](../04_ArraysStrings/theory/L27_ArrayBasics.md) |