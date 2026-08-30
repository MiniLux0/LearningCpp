# Lección 04: Interceptando el tren (`switch`)

Cuando tenemos múltiples opciones exactas para elegir, llenar el código de cadenas gigantes de `else if` se vuelve agotador y difícil de leer. Imagina el menú de un restaurante donde presionas un número para elegir tu combo. Piensa en la herramienta que soluciona esto como un sistema de vías de tren: el programa desvía el tren (tu variable) directamente hacia el andén que coincida exactamente con su número. En C++, esta herramienta es la estructura **`switch`**. A partir de este momento, abandonaremos los trenes para hablar con propiedad de la industria: **Selección Directa**, **Ramas de Ejecución** y **Fuga de Flujo (Fallthrough)**.

## Anatomía de un Switch

El bloque condicional `switch` está optimizado para comprobar **igualdades directas** contra valores enteros, caracteres o tipos enumerados (no soporta rangos lógicos ni textos `std::string`).

```cpp
int comboElegido{2};

switch (comboElegido) {
    case 1:
        std::cout << "Hamburguesa servida.\n";
        break;
    case 2:
        std::cout << "Pizza servida.\n";
        break;
    default:
        std::cout << "Combo no existe.\n";
        break;
}
```

### Mecánica de Ejecución
1. **`switch (comboElegido)`:** Inicia la estructura de control y recibe la expresión a evaluar. 
2. **`case 2:`** Es la **rama o etiqueta de destino**. El flujo saltará de inmediato a la etiqueta que coincida con el valor evaluado.
3. **`break;`** Es el **interruptor de escape**. Instruye al flujo de control a abandonar inmediatamente el bloque `switch`.
4. **`default:`** Actúa como el bloque *fallback* o plan de contingencia (equivalente al `else` solitario). Se ejecuta si ninguna etiqueta previa coincidió.

## Fuga de Flujo Incontrolada (Fallthrough)

A diferencia del `if / else`, donde el flujo abandona la estructura automáticamente tras ejecutar su bloque, el `switch` tiene una naturaleza de caída libre.

Si omites la instrucción `break;`, **el flujo ignorará las fronteras semánticas y continuará ejecutando todo el código de las ramas inferiores**, uno tras otro, hasta encontrar un `break` explícito o alcanzar el cierre del `switch`. A esta fuga de ejecución se le denomina **Fallthrough**.

```cpp
// ¡PELIGRO! Faltan las instrucciones 'break'
int piso{2};

switch (piso) {
    case 2:
        std::cout << "Llegando al piso 2.\n"; // El flujo salta aqui...
        // ¡No hay break! Ocurre un Fallthrough hacia la siguiente rama.
    case 1:
        std::cout << "Llegando al piso 1.\n";
}
// Esto imprimirá AMBOS mensajes, corrompiendo la logica del programa.
```

<div align="center">
  <img src="assets/l04_switch_fallthrough.gif" alt="Efecto Fallthrough en una sentencia switch">
</div>

#### 🔍 Traducción Visual de Jump Table y Fallthrough:
* **Panel Izquierdo (`main.cpp`):** Código fuente con `switch (opcion)` donde `case 2` carece de `break`.
* **Tabla de Saltos (Derecha):** El flujo salta directamente a `case 2: pause()`.
* **Caída en Cascada (Fallthrough):** Al no encontrar la orden `break`, la CPU continúa ejecutando ciegamente las instrucciones de `case 3: stop()`.

## Vulnerabilidad del Scope Compartido

El `switch` tiene una arquitectura de memoria particularmente peligrosa. Todo el bloque delimitado por el `switch` comparte un **único Scope Local**. Las etiquetas `case` no son habitaciones separadas; son solo marcas de lectura en el suelo.

Debido a esto, si declaras e **inicializas** una variable nueva dentro de un `case`, el compilador abortará el proceso. Esto previene que el programa inicie la variable en la rama A, pero que luego la rama B intente usarla habiéndose saltado su declaración.

**La Solución Estricta:** Si requieres alojamiento de memoria local dentro de una rama, **debes crear un Scope Local manual encerrando el `case` entre llaves `{ }`**.

```cpp
switch (opcion) {
    case 1: { // <-- Inicializamos un Scope Local privado
        int recompensa{50}; // Seguro. Su ciclo de vida ocurre aqui dentro.
        std::cout << "Ganaste " << recompensa << "\n";
        break;
    } // <-- La variable local es destruida de la memoria RAM.
}
```

> 🧪 **Laboratorio:** ¡Es hora de experimentar! Abre el archivo [`../lab/L04_Switch.cpp`](../lab/L04_Switch.cpp).
>
> 🐞 **Demo de Bug (Opcional):** Aprende de los errores comunes. Ejecuta la trampa en [`../lab/demos/D04_ScopeAndFallthroughBug.cpp`](../lab/demos/D04_ScopeAndFallthroughBug.cpp).
>
> 🏋️ **Ejercicio:** Pon a prueba lo aprendido. Atrévete con el reto en [`../exercise/E04_SelectorDeClase/E04_SelectorDeClase.cpp`](../exercise/E04_SelectorDeClase/E04_SelectorDeClase.cpp).

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste...

<details>
<summary><b>1. Si quiero comprobar si la variable `peso` es mayor a 500, ¿es viable utilizar la arquitectura `switch`?</b></summary>

> No. El control `switch` está diseñado estrictamente para igualdades absolutas (valores enteros o caracteres fijos). Para evaluar rangos lógicos, se debe utilizar `if` / `else if`.
</details>

<details>
<summary><b>2. ¿Qué ocurre si un caso (como `case 1:`) se escribe vacío y no contiene la instrucción `break`?</b></summary>

> Se produce un *Fallthrough* intencional. La ejecución caerá directamente en el siguiente caso de la lista. Esta es una técnica válida si deseas que múltiples etiquetas compartan exactamente el mismo bloque de código.
</details>

---

| ⬅️ [Anterior: L03_BlocksAndScope.md](L03_BlocksAndScope.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: L05_WhileDoWhile.md](L05_WhileDoWhile.md) |
|:---|:---:|---:|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
