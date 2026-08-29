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

> [!NOTE]
> **Planificación de Animación (manim-composer):**
> *`l03_void_action.gif`*: Un hilo de ejecución (punto de luz) sale del `main()`. Ingresa al Scope de `void imprimirAlerta()`. Ejecuta la línea de código provocando un destello rojo en el sistema (Efecto Secundario), y el punto de luz simplemente retorna a su origen al llegar a la llave de cierre `}`, sin transportar ninguna caja de datos.

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
