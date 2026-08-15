# 📝 Sección 03: Subrutinas y Funciones — Resumen de Estudio y Notas

Resumen ejecutivo y notas de estudio de la **Sección 03: Subrutinas y Funciones** del curso de C++ (MIT 6.096 Lectura 03 / Stanford CS106L Lectura 01 y 03 / Stanford CS106B Capítulo 2).
Cubre la anatomía de funciones en C++, tipos de retorno, paso por valor vs paso por referencia (`&`, `const &`), sobrecarga de funciones, separación en prototipos y archivos de cabecera (`.h` / `.cpp`) y gestión de ámbito de variables.

---

## 🧭 Tabla de Contenidos

1. [Lecciones y Teoría](#-lecciones-y-teoría)
2. [Ejercicios Prácticos (E01 – E05)](#-ejercicios-prácticos-e01--e05)
3. [Resumen por Lección](#-resumen-por-lección)
   - [L23 — Fundamentos de Funciones](#l23--fundamentos-de-funciones)
   - [L24 — Valores de Retorno](#l24--valores-de-retorno)
   - [L25 — Parámetros y Referencias](#l25--parámetros-y-referencias)
   - [L26 — Cabeceras y Prototipos](#l26--cabeceras-y-prototipos)
4. [Buenas Prácticas y Patrones Clave](#-buenas-prácticas-y-patrones-clave)

---

## 📘 Lecciones y Teoría

| Lección | Título | Nota Teórica | Laboratorio de Código |
| :--- | :--- | :--- | :--- |
| **L23** | Fundamentos de Funciones | 📘 [`l23_functions.md`](../theory/l23_functions.md) | 💻 [`l23_functions.cpp`](../code/l23_functions.cpp) |
| **L24** | Valores de Retorno | 📘 [`l24_return_values.md`](../theory/l24_return_values.md) | 💻 [`l24_return_values.cpp`](../code/l24_return_values.cpp) |
| **L25** | Parámetros y Referencias | 📘 [`L25_FunctionParameters.md`](../theory/L25_FunctionParameters.md) | 💻 [`L25_FunctionParameters.cpp`](../code/L25_FunctionParameters.cpp) |
| **L26** | Cabeceras y Prototipos | 📘 [`L26_HeadersAndPrototypes.md`](../theory/L26_HeadersAndPrototypes.md) | 💻 [`L26_HeadersAndPrototypes.cpp`](../code/L26_HeadersAndPrototypes.cpp) |

---

## 🎯 Ejercicios Prácticos (E01 – E05)

| # | Ejercicio | Tema | Archivo de Código | Estatus |
| :---: | :--- | :--- | :--- | :---: |
| **E01** | Fundamentos de Funciones | Declaración, llamadas y retorno | 💻 [`E01_FunctionBasics.cpp`](../exercise/E01_FunctionBasics.cpp) | ✅ |
| **E02** | Paso por Referencia | Modificación directa usando `&` | 💻 [`E02_PassByReference.cpp`](../exercise/E02_PassByReference.cpp) | ✅ |
| **E03** | Función Swap | Intercambio de variables con referencias | 💻 [`E03_SwapFunction.cpp`](../exercise/E03_SwapFunction.cpp) | ✅ |
| **E04** | Sobrecarga de Funciones | Sobrecarga por tipo de parámetro | 💻 [`E04_Overloading.cpp`](../exercise/E04_Overloading.cpp) | ✅ |
| **E05** | Prototipos de Cabecera | Prototipos y compilación separada | 💻 [`E05_HeaderPrototypes.cpp`](../exercise/E05_HeaderPrototypes.cpp) | ✅ |

---

## 💡 Resumen por Lección

### L23 — Fundamentos de Funciones
- Una función es un bloque de código reutilizable.
- Firma básica: `tipoRetorno nombreFuncion(listaParametros)`.
- Si la función no devuelve ningún valor, el tipo de retorno se declara como `void`.
- Aplica el principio **DRY (*Don't Repeat Yourself*)**.

### L24 — Valores de Retorno
- La sentencia `return` devuelve un valor a la función invocadora e interrumpe la ejecución inmediatamente.
- **Sobrecarga de Funciones:** C++ permite definir múltiples funciones con el mismo nombre siempre que sus firmas difieran en la cantidad o tipo de parámetros.

### L25 — Parámetros y Referencias
- **Paso por Valor:** Copia el valor del argumento. Los cambios dentro de la función no afectan la variable original.
- **Paso por Referencia (`&`):** Pasa un alias a la celda de memoria original. Permite mutar la variable del invocador directamente.
- **Referencia Constante (`const &`):** Evita el costo de duplicar memoria pesada (ej. `const string&`) manteniendo la variable inmutable.

### L26 — Cabeceras y Prototipos
- **Prototipos (*Forward Declarations*):** Informan al compilador la firma de una función antes de su uso, resolviendo dependencias de orden.
- **Separación `.h` / `.cpp`:** Las declaraciones van en archivos de cabecera (`.h`), mientras la implementación reside en archivos `.cpp`.
- **Guardas de Inclusión:** Uso de `#pragma once` o `#ifndef` para prevenir errores de doble inclusión en el enlazador.

---

## 🛡️ Buenas Prácticas y Patrones Clave

1. **Principio de Responsabilidad Única:** Diseñar funciones cortas que realicen una sola tarea bien definida.
2. **`using namespace std;` en archivos de código:** Simplifica la escritura de `cout`, `cin`, `endl`, `string`, `vector`.
3. **`const &` para lectura eficiente:** Usar referencias constantes `const T&` para pasar objetos sin costo de copia.
4. **Guardas de cabecera:** Incluir siempre `#pragma once` en archivos `.h`.

---

*Sección 03 completada al 100%*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>