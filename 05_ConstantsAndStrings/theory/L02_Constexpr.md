# Lección 02: Evaluación en Tiempo de Compilación (`constexpr`)

En la lección anterior, aprendimos a volver inmutables nuestras variables usando `const`. Esto protege los datos de mutaciones accidentales una vez que el programa ya está ejecutándose (*Tiempo de Ejecución* o *Runtime*).

Pero C++ Moderno (desde C++11) introdujo un optimizador mucho más estricto llamado `constexpr` (Constant Expression). 

Para entender la diferencia, imagina la preparación de una receta:
*   **`const` (Runtime):** Esperas a que el cliente pida su comida para cocinarla y sellarla en un recipiente cerrado. Es seguro, pero tuviste que esperar al cliente para procesar la orden.
*   **`constexpr` (Compile-time):** Cocinas y sellas la comida *antes* de abrir el restaurante. Cuando el cliente llega, la entrega es instantánea.

## El Compilador hace el trabajo pesado

Si declaras una variable como `constexpr`, le estás exigiendo al compilador que resuelva su valor (o sus operaciones matemáticas) **antes** de que el programa sea ejecutado. A esto se le llama **Evaluación en Tiempo de Compilación (Compile-time Evaluation)**.

<div align="center">
  <img src="assets/l02_constexpr_compiletime.gif" alt="Evaluación en tiempo de compilación con constexpr">
</div>

#### 🔍 Traducción Visual del Modelo de Memoria:
* **Fase 1 (Compilador `g++`):** El compilador detecta `constexpr`, extrae los operandos (`7 * 24`) y ejecuta el cálculo aritmético internamente antes de crear el ejecutable.
* **Fase 2 (Binario / Runtime):** La instrucción de multiplicación desaparece del ejecutable final y es reemplazada directamente por la constante calculada `[ 168 ]`.
* **Insignia `0 Ciclos de CPU`:** Durante la ejecución, el hardware no invoca la ALU (Unidad Aritmética Lógica) para multiplicar; simplemente carga el valor estático precalculado en memoria instantáneamente.

```cpp
// 1. El compilador conoce estos valores por adelantado
constexpr int horasPorDia{24};
constexpr int minutosPorHora{60};

// 2. OPTIMIZACIÓN: El compilador multiplicará 24 * 60 POR TI durante la compilación.
// El ejecutable final contendrá directamente el número 1440, sin hacer sumas en vivo.
constexpr int minutosPorDia{horasPorDia * minutosPorHora}; 
```

### ¿Cuándo usar `constexpr` en lugar de `const`?

La regla de la industria de C++ Moderno es:
**Si el valor se puede evaluar o calcular por adelantado durante la compilación, usa SIEMPRE `constexpr`.** 

Esto hace que tus programas (especialmente motores gráficos y sistemas embebidos) sean ultra rápidos, ya que la CPU no desperdiciará ciclos realizando cálculos repetitivos durante el *Runtime*; el trabajo ya fue resuelto por el compilador días antes.

---

> 🧪 **Laboratorio:** ¡Veamos cómo optimizar cálculos! Abre [`../lab/L02_Constexpr.cpp`](../lab/L02_Constexpr.cpp).
>
> 🐞 **Demo de Bug:** Intenta engañar al compilador pidiéndole que evalúe inputs de usuario. Ejecuta la trampa en [`../lab/demos/D02_RuntimeConstexprBug.cpp`](../lab/demos/D02_RuntimeConstexprBug.cpp).
>
> 🏋️ **Ejercicio:** La NASA necesita ahorrar ciclos de CPU. Atrévete con el reto en [`../exercise/E02_OptimizadorDeCalculos/E02_OptimizadorDeCalculos.cpp`](../exercise/E02_OptimizadorDeCalculos/E02_OptimizadorDeCalculos.cpp).

---

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste. No intentes adivinar con conocimientos externos.

<details>
<summary><b>1. Si solicitas al usuario que ingrese su edad mediante <code>std::cin</code>, ¿puedes almacenar ese dato en una variable <code>constexpr</code>?</b></summary>

> No. El compilador procesa las instrucciones `constexpr` antes de que el programa inicie, por lo que es imposible que procese un input que dependerá del usuario (Runtime). Para proteger datos que se asignan en tiempo de ejecución, debes usar `const`.
</details>

---

| ⬅️ [Anterior: L01_Const.md](L01_Const.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: L03_String.md](L03_String.md) |
|---|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
