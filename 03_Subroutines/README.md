<div align="center">

# 🚀 Sección 03: Subrutinas — Funciones, Paso por Referencia y Cabeceras

> **Lecciones**: L23 – L26  
> 🏛️ **Fuente Académica Base**: MIT 6.096 (Lectura 03) / Stanford CS106L (Lecturas 03 y 04) / Stanford CS106B (Capítulo 2)  
> 📝 **Resumen Ejecutivo**: 📝 [**`summary/03_Subroutines_Notes.md`**](summary/03_Subroutines_Notes.md)  
> 🎯 **Enfoque Principal**: Subrutinas, tipos de retorno, paso por valor vs paso por referencia (`&`, `const &`), sobrecarga de funciones, prototipos de cabecera (`.h`) y ámbito/vida de variables.

---

### 🧭 Navegación del Módulo

| ⬅️ Módulo Anterior | 📂 Ubicación Actual | ➡️ Siguiente Módulo |
|:------------------:|:-------------------:|:------------------:|
| [**⬅️ Sección 02: Sintaxis Básica**](../02_BasicSyntax/README.md) | **Sección 03: Subrutinas** | [**Sección 04: Arreglos y Cadenas ➡️**](../04_ArraysStrings/README.md) |

</div>

---

## 📌 Visión General del Módulo

Este módulo abarca la modularización de código en C++: declaraciones y firmas de funciones, tipos de retorno, paso por valor vs referencia (`&`, `const &`), sobrecarga de funciones, compilación separada mediante archivos de cabecera (`.h` / `.cpp`) y gestión de ámbito de variables.

---

## 📋 Inventario de Lecciones, Teoría y Código

| # | Nombre de Lección | 📘 Nota Teórica | 💻 Laboratorio de Código | Conceptos Técnicos Clave | Estatus |
|---|-------------------|-----------------|--------------------------|--------------------------|:-------:|
| **L23** | **Fundamentos de Funciones** | 📘 [`theory/L23_Functions.md`](theory/L23_Functions.md) | 💻 [`code/L23_Functions.cpp`](code/L23_Functions.cpp) | Declaración de funciones, parámetros, tipo de retorno, `void`, principio DRY. | ✅ |
| **L24** | **Valores de Retorno** | 📘 [`theory/L24_ReturnValues.md`](theory/L24_ReturnValues.md) | 💻 [`code/L24_ReturnValues.cpp`](code/L24_ReturnValues.cpp) | Sentencia `return`, flujo de datos, sobrecarga de funciones. | ✅ |
| **L25** | **Parámetros y Referencias** | 📘 [`theory/L25_FunctionParameters.md`](theory/L25_FunctionParameters.md) | 💻 [`code/L25_FunctionParameters.cpp`](code/L25_FunctionParameters.cpp) | Paso por valor vs referencia (`&`), optimización con `const &`. | ✅ |
| **L26** | **Cabeceras y Prototipos** | 📘 [`theory/L26_HeadersAndPrototypes.md`](theory/L26_HeadersAndPrototypes.md) | 💻 [`code/L26_HeadersAndPrototypes.cpp`](code/L26_HeadersAndPrototypes.cpp) | Prototipos de función, separación `.h` / `.cpp`, guardas de inclusión `#pragma once`. | ✅ |

---

## 🎯 Ejercicios Prácticos (E01 – E05)

> 📖 **Guía de Ejercicios**: 📂 [**`exercise/README.md`**](exercise/README.md)

| # | Nombre del Ejercicio | Tema | 💻 Archivo de Solución | Estatus |
|---|----------------------|------|------------------------|:-------:|
| **E01** | **Fundamentos de Funciones** | Declaración y retorno de funciones | 💻 [`exercise/E01_FunctionBasics.cpp`](exercise/E01_FunctionBasics.cpp) | ✅ |
| **E02** | **Paso por Referencia** | Mutación directa con `&` | 💻 [`exercise/E02_PassByReference.cpp`](exercise/E02_PassByReference.cpp) | ✅ |
| **E03** | **Función Swap** | Intercambio *in-place* con referencias | 💻 [`exercise/E03_SwapFunction.cpp`](exercise/E03_SwapFunction.cpp) | ✅ |
| **E04** | **Sobrecarga de Funciones** | Sobrecarga por tipo de parámetro | 💻 [`exercise/E04_Overloading.cpp`](exercise/E04_Overloading.cpp) | ✅ |
| **E05** | **Prototipos de Cabecera** | Prototipos y compilación separada | 💻 [`exercise/E05_HeaderPrototypes.cpp`](exercise/E05_HeaderPrototypes.cpp) | ✅ |

---

## 📚 Alineación con Fuentes Académicas

| Lecciones | Fuente Académica PDF | Temas Teóricos Clave |
|-----------|----------------------|----------------------|
| **L23–L25** | 📄 [`MIT 6.096 Lectura 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) | Marcos en la pila de subrutinas, tipos de retorno, paso por valor vs referencia, sobrecarga. |
| **L26** | 📄 [`MIT 6.096 Lectura 03`](../files/mit6096/lectures/Lecture03_Functions.pdf) \| [`CS106L Lectura 03`](../files/cs106l/lectures/WLecture_3_Init_and_Ref.pdf) | Prototipos de función, separación `.h` / `.cpp`, guardas de inclusión `#pragma once`. |

---

## 🛠️ Guías de Compilación

Subdirectorios `code/` y `exercise/` incluyen archivos `makefile`:
- ⚙️ **Tutorial de Compilación**: [`docs/COMPILATION_GUIDE.md`](../docs/COMPILATION_GUIDE.md)
- 🛠️ **Referencia de Makefile**: [`docs/MAKEFILE_GUIDE.md`](../docs/MAKEFILE_GUIDE.md)

---
*MiniLux0 — Learning C++ Section 03*

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> � 2026</sub>
</div>