# L23 — Fundamentos de Subrutinas y Funciones

> [!NOTE]
> **Fundamentación Académica:** Esta lección sintetiza los conceptos de la **Lectura 03** de MIT 6.096 ([`Lecture03_Functions.pdf`](../../files/mit6096/lectures/Lecture03_Functions.pdf)) y el **Capítulo 2 (*Procedural Abstraction*, pp. 55–90)** del libro oficial de Stanford CS106B (*Programming Abstractions in C++* por Eric Roberts).

---

## 🧭 Navegación Rápida

- 📄 **Lecturas Académicas Base:**
  - 🏛️ [MIT 6.096 — Lecture 03: Function Definitions & Call Stack Frames](../../files/mit6096/lectures/Lecture03_Functions.pdf)
  - 🌲 [Stanford CS106B — Chapter 2: Procedural Abstraction](https://web.stanford.edu/class/cs106x/res/reader/CS106BX-Reader.pdf)
- 💻 **Laboratorio de Código:** [`l23_functions.cpp`](../code/l23_functions.cpp)

---

## Objetivos de Aprendizaje

- [ ] Comprender la abstracción procedural y el principio de ingeniería **DRY (*Don't Repeat Yourself*)**.
- [ ] Declarar y definir funciones especificando tipo de retorno, identificador y lista de parámetros.
- [ ] Comprender el funcionamiento de funciones de tipo `void` (subrutinas sin retorno de valor).
- [ ] Rastrear la ejecución de subrutinas y el apilado/desapilado de marcos en la pila de llamadas (*Call Stack*).

---

## 1. ¿Qué es una Función o Subrutina?

Una **función** es un bloque de código reutilizable diseñado para realizar una tarea específica. Las funciones permiten descomponer programas complejos y monolíticos en módulos independientes y fáciles de mantener.

![l23_functions](assets/l23_functions.svg)

```cpp
#include <iostream>
using namespace std;

// Definición de función void (sin valor de retorno)
void mostrarBienvenida() {
    cout << "====================================\n";
    cout << "    MODULO DE SUBRUTINAS C++ L23    \n";
    cout << "====================================\n";
}

int main() {
    mostrarBienvenida(); // Invocación 1
    mostrarBienvenida(); // Invocación 2
    return 0;
}
```

> [!TIP]
> **El Principio DRY (*Don't Repeat Yourself*):**
> Si te encuentras duplicando las mismas 5 líneas de código en múltiples lugares, encapsúlalas dentro de una función con un nombre descriptivo.

---

## 2. Anatomía de una Declaración de Función

Toda función consta de tres partes principales:

```cpp
//  TipoRetorno  NombreFunción ( Parámetros )
        void       imprimirSuma  ( int a, int b ) {
            cout << "Suma: " << (a + b) << endl;
        }
```

- **Tipo de Retorno:** Indica qué tipo de dato devuelve la función (`int`, `double`, `string`, `void`).
- **Nombre:** Identificador descriptivo en notación *camelCase*.
- **Parámetros:** Variables locales de entrada encerradas entre paréntesis `()`.

---

## ❓ Pregunta de Chequeo #1 — El Tipo de Retorno `void`

¿Qué significa que una función esté declarada con el tipo de retorno `void` (ejemplo: `void imprimirEncabezado()`)?

<details>
<summary>🔍 <strong>Ver Explicación y Respuesta</strong></summary>

> [!NOTE]
> **Respuesta:** Indica que la función NO devuelve ningún valor de datos al invocador.
>
> **Explicación:**  
> `void` le comunica al compilador que la subrutina ejecuta acciones o efectos secundarios (como imprimir en pantalla con `cout` o modificar memoria), pero no calcula ningún valor para asignarlo a variables en `main()`.

</details>

---

## 📝 Resumen de L23

1. **Modularidad:** Las funciones dividen el código en subrutinas nombradas y reutilizables.
2. **`void`:** Indica que la función no retorna datos al invocador.
3. **Reutilización:** Evita código duplicado y facilita la depuración.

---

<div align="center">

### 🧭 Navegación y Progresión

| ⬅️ Lección Anterior | 🏠 Inicio de Sección | ➡️ Siguiente Lección |
|:------------------:|:-------------------:|:------------------:|
| [**⬅️ Sección 02 Capstone**](../../02_BasicSyntax/theory/l22_switch.md) | [**🏠 Subrutines**](../README.md) | [**L24 — Valores de Retorno ➡️**](l24_return_values.md) |

</div>

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>