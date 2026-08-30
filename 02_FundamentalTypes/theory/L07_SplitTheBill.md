# L07: Mini-proyecto "Split the Bill"
> **Módulo 02 — Fundamental Types**

Hemos llegado al final del Módulo 02. Has aprendido sobre la memoria, los tipos primitivos, cómo inicializarlos de forma segura (`{}`), cómo operarlos matemáticamente, cómo hacer conversiones sin perder datos (`static_cast`) y cómo la computadora responde a preguntas (`bool`).

Es momento de juntar todas estas piezas del rompecabezas en un mini-proyecto real.

## El Problema

Imagina que estás en un restaurante con tus amigos. Llega la cuenta y deciden dividirla a partes iguales. Sin embargo, no todo es tan sencillo:
1. Necesitas calcular el total con propina.
2. Debes dividir el monto exacto (sin perder centavos por la división entera).
3. Tienes que asegurarte de que los datos ingresados sean válidos (ej. la cantidad de amigos no puede ser cero o negativa).

Como **aún no sabemos cómo tomar decisiones condicionales** (no hemos aprendido a usar `if`), nuestro programa simplemente imprimirá un "Estado de Validación" usando tipos `bool` (`1` para válido, `0` para error).

<div align="center">
  <img src="assets/l07_split_the_bill.gif" alt="Animación mostrando el flujo de datos desde la cuenta hasta la división por persona">
</div>

#### 🔍 Traducción Visual del MiniProyecto "Split the Bill":
* **Tipos Mixtos (`double` y `int`):** Gestión de montos monetarios de punto flotante (`total`) combinados con cantidades enteras discretas (`personas`).
* **Cálculo con `static_cast`:** Promoción explícita para evitar pérdidas de centavos por truncamiento de división entera.
* **Terminal OS:** Desglose final de facturación con precisión decimal formateada para el usuario.

## Integrando lo aprendido

Este mini-proyecto requiere la combinación de:
- **`double` y `int`**: Para manejar dinero y personas.
- **`static_cast<double>()`**: Para evitar la división entera al dividir la cuenta.
- **Operadores Relacionales (`>`, `<=`)**: Para validar que la propina no sea negativa y que el número de amigos sea válido.
- **Operadores Lógicos (`&&`)**: Para crear una validación maestra (ej. `bool todo_ok = (amigos > 0) && (propina >= 0);`).

> 🧪 **Laboratorio:** Acompáñanos a construir el núcleo de la calculadora paso a paso. Abre el archivo [`../lab/L07_SplitTheBill.cpp`](../lab/L07_SplitTheBill.cpp).
>
> 🏋️ **Ejercicio:** Es tu turno de brillar. Completa el desarrollo del sistema de facturación en [`../exercise/E07_SplitTheBill/E07_SplitTheBill.cpp`](../exercise/E07_SplitTheBill/E07_SplitTheBill.cpp).

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques respuestas en librerías avanzadas ni conceptos no vistos.

<details>
<summary><b>1. Si aún no sabemos usar `if`, ¿cómo puede el usuario saber si ingresó datos incorrectos?</b></summary>

> Podemos evaluar la validez matemática en una variable `bool` (ej. `bool datos_validos = amigos > 0;`) e imprimir esa variable en consola. El usuario verá un `1` si todo es correcto, o un `0` si cometió un error lógico.
</details>

<details>
<summary><b>2. Si la cuenta es de `int cuenta{100};` y son `int amigos{3};`, ¿por qué debemos usar `static_cast`?</b></summary>

> Porque de lo contrario, `100 / 3` resultará en la división entera `33`, y se perderá `1` dólar en el vacío de la memoria. Necesitamos `static_cast<double>(cuenta)` para forzar la división decimal y obtener `33.33`.
</details>

| ⬅️ [Anterior: La magia de auto](L06_MagiaDeAuto.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente Módulo: Scope & Control Flow](../../03_ScopeAndControlFlow/README.md) |
|---|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
