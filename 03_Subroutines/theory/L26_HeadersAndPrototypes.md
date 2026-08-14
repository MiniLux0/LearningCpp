# L26 — Declaraciones Adelantadas, Prototipos de Función y Archivos de Cabecera (`.h` / `.hpp`)

> [!NOTE]
> **Fundamentación Académica:** Esta lección sintetiza los conceptos de la **Lectura 03** de MIT 6.096 ([`Lecture03_Functions.pdf`](../../files/mit6096/lectures/Lecture03_Functions.pdf)) y la **Lectura 01** de Stanford CS106L ([`WLecture1_intro.pdf`](../../files/cs106l/lectures/WLecture1_intro.pdf)).

---

## 🧭 Navegación Rápida

- 📄 **Lecturas Académicas Base:**
  - 🏛️ [MIT 6.096 — Lecture 03: Function Prototypes & Header Files](../../files/mit6096/lectures/Lecture03_Functions.pdf)
  - ⚙️ [Stanford CS106L — Lecture 01: Multi-File Compilation & Header Guards](../../files/cs106l/lectures/WLecture1_intro.pdf)
- 💻 **Laboratorio de Código:** [`L26_HeadersAndPrototypes.cpp`](../code/L26_HeadersAndPrototypes.cpp)

---

## Objetivos de Aprendizaje

- [ ] Declarar **Prototipos de Función (*Forward Declarations*)** para informar al compilador sobre la firma de las funciones antes de su definición.
- [ ] Organizar proyectos en C++ dividiendo el código en archivos de interfaz (`.h` / `.hpp`) y archivos de implementación (`.cpp`).
- [ ] Implementar **Guardas de Inclusión (*Header Guards*)** con `#ifndef` o `#pragma once` para evitar errores de compilación por doble inclusión de símbolos.

---

## 1. Prototipos de Función (*Forward Declarations*)

El compilador de C++ lee los archivos fuente estrictamente de arriba a abajo (*top-to-bottom*). Si `main()` invoca una función definida más abajo en el archivo, el compilador genera un error de identificador no declarado.

Un **Prototipo de Función** declara únicamente la firma (tipo de retorno, nombre y parámetros) finalizando con punto y coma `;` antes de `main()`:

```cpp
#include <iostream>
using namespace std;

// 1. Prototipo de Función (Declaración Adelantada)
int sumar(int a, int b);

int main() {
    cout << "Resultado: " << sumar(5, 3) << endl; // ¡Válido! El compilador sabe que sumar() existe.
    return 0;
}

// 2. Definición de la Función
int sumar(int a, int b) {
    return a + b;
}
```

---

## 2. Archivos de Cabecera y Guardas de Inclusión (`#pragma once`)

Al dividir código en múltiples archivos `.h`, incluir la misma cabecera varias veces en diferentes unidades de traducción genera errores de redefinición de símbolos en el enlazador (*linker*). Usar `#pragma once` o guardas de preprocesador tradicionales resuelve este problema:

```cpp
#ifndef UTILIDADES_MATEMATICAS_H
#define UTILIDADES_MATEMATICAS_H

// Declaraciones de prototipos en el archivo de cabecera (.h)
int sumar(int a, int b);

#endif // UTILIDADES_MATEMATICAS_H
```

> [!TIP]
> **Práctica Moderna:**  
> Los compiladores modernos (GCC, Clang, MSVC) soportan la directiva `#pragma once` colocada en la primera línea de los archivos de cabecera como una alternativa más limpia a las guardas `#ifndef`.

---

## ❓ Pregunta de Chequeo #1 — Definiciones en Archivos `.h`

¿Por qué las definiciones completas de funciones (`{ ... }`) NO deben colocarse generalmente dentro de archivos de cabecera (`.h`)?

<details>
<summary>🔍 <strong>Ver Explicación y Diagnóstico</strong></summary>

> [!CAUTION]
> **Error de Múltiple Definición del Enlazador (*Multiple Definition Error*):**  
> Si una cabecera que contiene cuerpos de función con código ejecutable se incluye en múltiples archivos `.cpp`, el compilador genera símbolos binarios duplicados en cada archivo objeto `.o`. Al ejecutar el enlazador (*linker*), este fallará con el error `multiple definition of 'funcion'`.

</details>

---

## 📝 Resumen de L26

1. **Prototipos:** Informan al compilador sobre las firmas de las funciones antes de sus definiciones completas.
2. **Cabeceras (`.h`):** Almacenan contratos de interfaz y declaraciones.
3. **Guardas:** Usar `#pragma once` para prevenir la inclusión duplicada de cabeceras.

---

<div align="center">

### 🧭 Navegación y Progresión

| ⬅️ Lección Anterior | 🏠 Inicio de Sección | ➡️ Siguiente Sección |
|:------------------:|:-------------------:|:------------------:|
| [**⬅️ L25 — Parámetros de Funciones**](L25_FunctionParameters.md) | [**🏠 Subrutines**](../README.md) | [**Sección 04: Arreglos y Cadenas ➡️**](../../04_ArraysStrings/README.md) |

</div>

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>