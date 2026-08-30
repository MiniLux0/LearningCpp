# L06: La Magia de `auto` (y sus peligros)
> **Módulo 02 — Fundamental Types**

Imagina que estás empacando mudanzas. Si ves un televisor, no necesitas que alguien te diga "consigue una caja cuadrada y frágil", simplemente lo deduces al mirar el objeto. 

En C++, el compilador puede hacer lo mismo. Puede deducir el tipo de la variable basándose en el valor que le estás metiendo usando la palabra reservada **`auto`**.

## El compilador detective

En lugar de escribir explícitamente el tipo de dato, puedes dejar que C++ lo averigüe:

```cpp
auto edad{25};           // C++ ve un entero. Dedudice que 'edad' es un int.
auto precio{19.99};      // C++ ve decimales. Deduce que 'precio' es un double.
auto esta_abierto{true}; // C++ ve true. Deduce que 'esta_abierto' es un bool.
```

<div align="center">
  <img src="assets/l06_auto_inference.gif" alt="Inferencia estática de tipos con auto en tiempo de compilación">
</div>

#### 🔍 Traducción Visual de la Inferencia de Tipos (`auto`):
* **Declaración con `auto`:** El programador omite el tipo explícito en el código fuente.
* **Análisis de `g++`:** El compilador analiza el literal derecho (`3` ➔ `int`, `19.99` ➔ `double`) durante la compilación.
* **Inyección en Binario:** El ejecutable contiene tipos estáticos e inmutables con **cero costo de rendimiento en tiempo de ejecución**.

### C++ no es Python: La regla rígida
Un error muy común es pensar que `auto` hace que C++ sea un lenguaje de tipado dinámico como Python o JavaScript. ¡Falso! 

El compilador de C++ es estricto. Cuando usa `auto`, solo deduce el tipo **una vez** durante la compilación. Una vez que la caja tiene la etiqueta `int`, **nunca** puede guardar un `double`.

```cpp
auto x{10};  // x es un int, y SIEMPRE será un int.
x = 5.5;     // ¡PELIGRO! Esto no cambia el tipo de x a double. 
             // C++ trunca el valor e inserta un 5 dentro de x.
```

## El Peligro de la Amnesia
Si `auto` parece tan cómodo, ¿por qué no lo usamos para todo?

Porque leer el código se vuelve una pesadilla. Piensa en esto:

```cpp
auto misterio{obtener_datos_del_jugador()};
```
¿Qué es `misterio`? ¿Es su puntuación (`int`)? ¿Su tiempo de juego (`double`)? ¿Su estado de conexión (`bool`)? No lo sabemos sin leer más archivos. El código sufre de "amnesia".

Por esta razón, en este curso aplicaremos una **Regla de Oro**: 
> **Sólo usaremos `auto` cuando el tipo sea dolorosamente obvio leyendo la misma línea.**

Por ejemplo, es muy útil combinarlo con lo que aprendimos en la lección pasada (`static_cast`):

```cpp
int total{100};
int divisor{3};

// El tipo es obvio, sabemos que static_cast está forzando un double.
auto resultado{static_cast<double>(total) / divisor}; 
```

> 🧪 **Laboratorio:** Veámoslo en acción en la consola. Abre el archivo [`../lab/L06_MagiaDeAuto.cpp`](../lab/L06_MagiaDeAuto.cpp).
>
> 🐞 **Demo de Bug (Opcional):** El abuso de `auto` esconde bugs terribles de matemáticas. Ejecuta la trampa en [`../lab/demos/D06_PeligroAmnesia.cpp`](../lab/demos/D06_PeligroAmnesia.cpp).
>
> 🏋️ **Ejercicio:** Un desarrollador perezoso usó `auto` en todas partes y rompió el sistema. Arréglalo jugando al detective en [`../exercise/E06_DetectiveAuto/E06_DetectiveAuto.cpp`](../exercise/E06_DetectiveAuto/E06_DetectiveAuto.cpp).

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques respuestas en librerías avanzadas ni conceptos no vistos.

<details>
<summary><b>1. Si declaras <code>auto valor{5};</code> y luego intentas <code>valor = 3.14;</code>, ¿qué ocurre en la RAM?</b></summary>

> La variable fue declarada como `int` y esa etiqueta es permanente. C++ truncará silenciosamente `3.14` y guardará únicamente `3` en la RAM. 
</details>

<details>
<summary><b>2. ¿Por qué se dice que el abuso de `auto` causa "amnesia" en el código?</b></summary>

> Porque cuando llamas a funciones o haces operaciones complejas, ocultas el tipo de dato subyacente a los demás desarrolladores (y a ti mismo en el futuro), forzándolos a deducir el tipo mentalmente, lo cual puede llevar a errores lógicos.
</details>

| ⬅️ [Anterior: Conversión Segura](L05_ConversionSegura.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Mini-proyecto (Split the Bill)](L07_SplitTheBill.md) |
|---|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
