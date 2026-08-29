# L02: Retornando valores y la Firma Estricta

En la lección anterior vimos que las funciones pueden tener un tipo de retorno explícito, como `int`, o pueden ser funciones de acción pura (`void`). 

Imagina una máquina expendedora: cuando insertas dinero y presionas un botón, esperas que la máquina te entregue una lata. Si hace el ruido mecánico pero no cae nada por la ranura, la transacción ha fallado. De la misma manera, en C++, cuando defines que una función devolverá un dato (`int`, `double`, `std::string`), estás firmando un contrato estricto con el compilador: **Garantizas que, al finalizar la rutina, la función inyectará un dato de ese tipo exacto de vuelta al flujo que la invocó**.

A partir de aquí, abandonamos la máquina expendedora. Hablaremos de **Caminos Lógicos**, **Salida de Ejecución** y **Comportamiento Indefinido**.

La instrucción clave para cumplir el contrato de retorno es `return`.

---

## La instrucción `return`

Cuando el hilo de ejecución lee la instrucción `return` dentro de una función, ocurren dos eventos inmediatos:
1. **Inyección del output:** El valor especificado se transfiere al `main()` (o a la función que hizo la llamada).
2. **Destrucción del Scope:** La ejecución de la función aborta y se destruye inmediatamente. Cualquier código escrito debajo de un `return` ejecutado jamás será alcanzado (conocido como *Dead Code* o Código Muerto).

```cpp
int calcularDoble(int numero) {
    int resultado{numero * 2};
    
    return resultado; // 1. Retorna el valor. 2. ¡Destruye la ejecución local!
    
    // DEAD CODE (Código Muerto)
    std::cout << "Esta línea jamás se imprimirá en la consola.";
}
```

> [!NOTE]
> **Planificación de Animación (manim-composer):**
> *`l02_return_value.gif`*: Un bloque de Scope (caja) recibe un parámetro de entrada. Un algoritmo lo transforma en un nuevo valor. Al ejecutar la línea `return`, el nuevo valor sale disparado por una tubería de regreso al `main()`, y la caja de Scope colapsa y desaparece de la pantalla, demostrando el cierre del hilo de ejecución secundario.

---

## La trampa del Comportamiento Indefinido (Undefined Behavior)

¿Qué ocurre si prometes retornar un `int` en la firma de tu función, pero olvidas colocar el `return`, o solo lo colocas dentro de un bloque `if` condicional?

```cpp
int obtenerDescuento(int edad) {
    if (edad > 60) {
        return 50; // ¡Contrato cumplido para mayores de 60!
    }
    // ¿Y si tiene 20 años? ¡El hilo de ejecución escapa sin retornar nada!
}
```

En lenguajes interpretados modernos, esto podría generar un error automático o devolver un valor nulo seguro. Sin embargo, C++ prioriza la velocidad cruda. Si olvidas el `return`, C++ no detendrá la ejecución, sino que el programa leerá la basura binaria que casualmente esté flotando en esa posición de la memoria RAM, devolviendo números caóticos y catastróficos. 

A esta fuga de seguridad se le conoce en la industria como **Undefined Behavior (Comportamiento Indefinido)**.

> [!WARNING]
> Debes garantizar matemáticamente que **todos los caminos lógicos (Code Paths)** de tu función converjan en un `return` explícito.

---

> 🧪 **Laboratorio:** Observa cómo las funciones evalúan diferentes caminos lógicos de forma segura. Abre el archivo [`../lab/L02_Return.cpp`](../lab/L02_Return.cpp).
>
> 🐞 **Demo de Bug:** Experimenta el caos de leer RAM basura (*Undefined Behavior*) ejecutando la trampa en [`../lab/demos/D02_UndefinedReturnBug.cpp`](../lab/demos/D02_UndefinedReturnBug.cpp).
>
> 🏋️ **Ejercicio:** El motor de cálculo arquitectónico está inyectando mediciones corruptas al sistema debido a un *Undefined Behavior*. Atrévete con el reto en [`../exercise/E02_CalculadoraDeArea/E02_CalculadoraDeArea.cpp`](../exercise/E02_CalculadoraDeArea/E02_CalculadoraDeArea.cpp).

---

<details>
<summary><b>Autochequeo: ¿Es posible devolver dos valores distintos usando dos `return` consecutivos en la misma línea lógica?</b></summary>

> **No.** 
> Recuerda que el primer `return` que el hilo de ejecución alcance destruirá el entorno de la función instantáneamente. Si necesitas devolver múltiples valores estructurados simultáneamente, aprenderemos a aglomerarlos usando un `struct` en el próximo módulo.

</details>

---

| ⬅️ [Anterior: Anatomía de una función](L01_Anatomy.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Funciones void](L03_Void.md) |
|---|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
