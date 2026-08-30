# L03 · Operadores Aritméticos y la trampa de la división entera

> **Módulo 02 — Fundamental Types**

---

## Las herramientas de la calculadora

Hasta ahora aprendimos a reservar cajas en la memoria (`int`, `double`) y a ponerles un valor inicial de forma segura usando las llaves `{}`. Pero un programa que solo guarda datos es como una caja fuerte: segura, pero aburrida. 

Para que los datos sean útiles, necesitamos transformarlos. En programación, usamos símbolos especiales llamados **operadores** para realizar cálculos. En C++, los operadores aritméticos básicos son casi idénticos a los que aprendiste en la escuela:

- Suma: `+`
- Resta: `-`
- Multiplicación: `*` (usamos el asterisco)
- División: `/` (usamos la barra diagonal)

```cpp
int manzanas{5};
int peras{3};
int total_frutas{manzanas + peras}; // Inicializa con 8
```

---

## El orden importa: Precedencia

Imagina que estás leyendo un libro. No lees las palabras al azar, las lees de izquierda a derecha y de arriba abajo. C++ hace lo mismo con las matemáticas, pero sigue una regla estricta llamada **precedencia de operadores**.

Si escribes `2 + 3 * 4`, podrías pensar que el resultado es `20` (sumar 2+3 da 5, y 5 por 4 es 20). Sin embargo, C++ calculará `14`.

¿Por qué? Porque la multiplicación y la división son operaciones más "pesadas" que la suma y la resta. C++ siempre buscará y resolverá primero las multiplicaciones y divisiones antes de sumar o restar lo que quede. 

Si quieres cambiar el orden normal de lectura y forzar a que una suma se haga primero, tienes que encerrarla entre paréntesis `()`, tal como en matemáticas: `(2 + 3) * 4` sí dará `20`.

Si necesitas el resultado exacto con decimales, la regla es simple: **al menos uno de los números involucrados debe ser un tipo decimal (`double`)**. 

<div align="center">
  <img src="assets/l03_division_entera.gif" alt="Comportamiento de la división entera vs división de punto flotante en C++">
</div>

#### 🔍 Traducción Visual de la División en la ALU:
* **`int / int` (Truncamiento en ALU):** `5 / 2` produce `2`. La parte fraccional `.5` se descarta sin redondeo.
* **`double / int` (Promoción de tipo):** `5.0 / 2` asciende la operación a tipo `double`, conservando el resultado decimal exacto `2.5`.

```cpp
double rebanadas_pizza{7.0}; // Al ser double, no trunca
int personas{2};
double resultado{rebanadas_pizza / personas}; // 3.5 Exacto
```

> 🧪 **Laboratorio:** Para ver cómo esta trampa destruye el cálculo de un promedio de calificaciones, ejecuta la demostración en [`../lab/demos/D01_TrampaDivisionEntera.cpp`](../lab/demos/D01_TrampaDivisionEntera.cpp).

---

## El operador "sobrante": Módulo (%)

Existe un operador más que usamos constantemente en programación: el módulo, representado por el símbolo `%`. 

No tiene nada que ver con porcentajes. El módulo **solo te devuelve el residuo** (lo que sobra) de una división entera. 

Imagina que tienes 10 cartas (`int cartas{10}`) y quieres repartirlas equitativamente entre 3 jugadores (`int jugadores{3}`). 
Si haces `10 / 3`, sabes que a cada jugador le tocan 3 cartas. Pero, ¿cuántas cartas te quedan en la mano sin repartir? Ese es el trabajo del módulo:

```cpp
int cartas{10};
int jugadores{3};
int sobran{cartas % jugadores}; // El resultado será 1
```

El operador módulo `%` es increíblemente útil. Por ejemplo, es la herramienta estrella para saber si un número es par o impar: si divides cualquier número entre 2, y el módulo (`% 2`) te da `0`, significa que no sobró nada, por lo tanto el número es par.

---

> 🧪 **Laboratorio:** Pon a prueba la calculadora de C++ y experimenta el extraño comportamiento de la división entera por ti mismo. Abre el archivo [`../lab/L03_OperadoresAritmeticos.cpp`](../lab/L03_OperadoresAritmeticos.cpp).
>
> 🏋️ **Ejercicio:** ¿Puedes organizar una fiesta sin que los cálculos salgan mal? Repara los bugs matemáticos en el reto [`../exercise/E03_RepartoDePizzas/E03_RepartoDePizzas.cpp`](../exercise/E03_RepartoDePizzas/E03_RepartoDePizzas.cpp).

---

## ✦ Preguntas de autochequeo

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques en internet — si no puedes responderlas de memoria, relee la sección correspondiente.

<details>
<summary><b>1. Si tu código dice <code>int resultado{10 - 2 * 3};</code>, ¿qué número guardará la variable y por qué?</b></summary>

> Guardará el número `4`. C++ usa la precedencia de operadores, por lo que primero resuelve la multiplicación (`2 * 3 = 6`) y luego hace la resta (`10 - 6 = 4`).
</details>

<details>
<summary><b>2. Haces la operación <code>15 / 4</code> usando dos variables de tipo <code>int</code>. ¿Qué valor te dará C++ y por qué no es 3.75?</b></summary>

> Dará `3`. Como ambos números son enteros (`int`), C++ hace una división entera. Solo calcula cuántas veces cabe completamente el 4 en el 15, y desecha el resto porque el tipo `int` no tiene la capacidad física de almacenar decimales.
</details>

<details>
<summary><b>3. Si quieres saber si el número de la variable <code>int dia</code> es múltiplo de 7, ¿qué operador usarías y qué resultado deberías esperar si efectivamente es múltiplo?</b></summary>

> Usarías el operador módulo (`%`). Si haces `dia % 7` y el resultado es `0`, significa que no hubo ningún residuo (sobrante) en la división, por lo tanto es un múltiplo exacto de 7.
</details>

---

| ⬅️ [Anterior: Inicialización uniforme](L02_InicializacionUniforme.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Operadores relacionales](L04_OperadoresRelacionalesYLogicos.md) |
|---|---|---|

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
