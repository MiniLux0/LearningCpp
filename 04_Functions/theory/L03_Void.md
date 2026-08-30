# L03: Funciones `void` y los Efectos Secundarios (Side Effects)

En la lección anterior vimos que las funciones procesan un input y nos entregan un dato resultante, obligándonos a respetar una **Firma de Retorno**.

Pero, ¿qué sucede si diseñamos una rutina cuyo único propósito es interactuar con un dispositivo externo o realizar una acción en el sistema? Por ejemplo, enviar un correo electrónico, guardar un archivo en el disco duro o imprimir texto en la consola. A esto se le conoce en la ingeniería de software como **Efectos Secundarios (Side Effects)**.

Si una función solo ejecuta acciones (*Efectos Secundarios*) y no necesita inyectar ningún dato de vuelta al flujo principal del programa, declaramos su tipo de retorno como `void` (vacío).

---

## La anatomía de la Acción Pura (`void`)

Una función de tipo `void` se escribe de la misma manera que una función matemática, pero rompe una regla fundamental: **no está obligada a finalizar con la instrucción `return`**.

```cpp
void imprimirAlerta() {
    std::cout << "¡Peligro! Temperatura crítica en el reactor.\n";
    // El hilo de ejecución terminará de forma segura al alcanzar la llave }
}
```

<div align="center">
  <img src="assets/l03_void_action.gif" alt="Acciones y efectos secundarios en funciones void de C++">
</div>

#### 🔍 Traducción Visual de Funciones Void y Efectos Secundarios:
* **Panel Izquierdo (`alerta.cpp`):** Código fuente invocando la función `imprimirAlerta()`.
* **Invocación Pura:** El hilo de control se transfiere al cuerpo de la función sin reservar memoria de retorno.
* **Side Effect (Terminal I/O):** Se emite el texto `"Peligro!"` hacia la consola sin modificar variables en la RAM.
* **Cierre de Scope:** Al tocar `}`, el hilo regresa al `main()` transportando **cero bytes de datos**.
* **Trampa de Asignación Ilegal:** Intentar capturar la rutina (`int x{imprimirAlerta()}`) aborta la compilación (*void value not ignored*).

Si bajo cierta condición crítica necesitas abortar la ejecución de una rutina `void` antes de que alcance el final de su Scope, puedes invocar la instrucción `return;` (sola, sin datos):

```cpp
void procesar(int nivel) {
    if (nivel < 0) {
        return; // Aborta la rutina inmediatamente y devuelve el control al main.
    }
    std::cout << "Procesando...";
}
```

---

## La trampa del Tipo de Retorno Incompleto

Aquí es donde los desarrolladores sufren su primer error de compilación frustrante con `void`.

Si la firma de tu rutina no transfiere datos de regreso, **es físicamente imposible inicializar una variable atrapando su ejecución**.

```cpp
// ESTO GENERARÁ UN ERROR FATAL DE COMPILACIÓN:
int resultado{imprimirAlerta()}; 
```

Si intentas hacer esto, el compilador C++ abortará el proceso lanzando el error: *`void value not ignored as it ought to be`*. En términos de sistema, estás intentando asignar un flujo vacío a una dirección de memoria entera, lo cual es ilegal.

Para invocar (llamar) a una función `void`, simplemente ejecútala como una instrucción independiente:

```cpp
// ESTO ES LO CORRECTO:
imprimirAlerta();
```

---

> 🧪 **Laboratorio:** Veamos cómo los hilos de ejecución de las rutinas `void` abordan el procesamiento y el aborto temprano. Abre el archivo [`../lab/L03_Void.cpp`](../lab/L03_Void.cpp).
>
> 🐞 **Demo de Bug:** Obliga al compilador a abortar el proceso intentando asignar la ejecución vacía a una dirección en memoria. Ejecuta la trampa en [`../lab/demos/D03_VoidCaptureBug.cpp`](../lab/demos/D03_VoidCaptureBug.cpp).
>
> 🏋️ **Ejercicio:** El código de inicialización del hotel es un desastre y el becario asignó ilegalmente un bloque `void` a una variable. Atrévete con el reto en [`../exercise/E03_PanelDeBienvenida/E03_PanelDeBienvenida.cpp`](../exercise/E03_PanelDeBienvenida/E03_PanelDeBienvenida.cpp).

---

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques respuestas en librerías avanzadas ni conceptos no vistos.

<details>
<summary><b>Autochequeo: ¿Puedes imprimir el resultado de una función void pasándola directamente a <code>std::cout</code>?</b></summary>

> **No.** 
> Intentar ejecutar `std::cout << imprimirAlerta();` también provocará un error de compilación. `std::cout` requiere procesar un flujo de datos válido (como texto o números) y no tiene la arquitectura para ingerir un tipo de retorno incompleto (`void`).

</details>

---

| ⬅️ [Anterior: Retornando valores](L02_Return.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Parámetros por valor](L04_Parameters.md) |
|---|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
