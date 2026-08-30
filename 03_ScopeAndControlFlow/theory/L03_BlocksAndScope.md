# Lección 03: Bloques y el Aislamiento del Scope

En las lecciones anteriores vimos que un `if` o un `else` abre unas llaves `{ }`. A todo lo que está delimitado dentro de esas llaves se le conoce como un **Bloque de Código** (*Compound Statement*). Piensa en las llaves `{ }` como las paredes de una habitación. Si naces (eres declarado) dentro de esa habitación, no puedes salir de ella, y cuando la puerta se cierra (la llave `}`), todo lo que está adentro desaparece. A partir de aquí, abandonaremos esta analogía espacial y utilizaremos los términos arquitectónicos del lenguaje: **Local Scope** (Alcance Local) y **Ciclo de Vida en Memoria**.

## ¿Qué es el Local Scope?

En C++, las llaves actúan como límites estrictos de memoria. Cuando declaras una variable dentro de un bloque `{ }`, esa variable se asigna en la memoria RAM. Sin embargo, en el instante exacto en el que el compilador alcanza la llave de cierre `}`, **la variable es liberada y destruida de la memoria para siempre**.

A este ciclo de nacimiento y muerte se le llama *Local Scope*.

```cpp
int main() {
    int edad{20}; // Scope Exterior (main)

    if (edad >= 18) {
        // Scope Interior (Bloque if)
        bool tieneIdentificacion{true}; 
        std::cout << "Edad validada.\n";
    } // Aqui se destruye 'tieneIdentificacion'. Su memoria es liberada.

    // ¡ERROR DE COMPILACIÓN! El compilador no reconoce 'tieneIdentificacion'.
    // Esa direccion de memoria ya no nos pertenece.
    if (tieneIdentificacion) { 
        std::cout << "Puede pasar.\n";
    }

    return 0;
}
```

### Reglas Estrictas del Scope:
- **Visibilidad hacia afuera (Top-Down):** Un Scope interior tiene acceso de lectura y escritura a las variables declaradas en cualquier Scope exterior que lo contenga (como `main`).
- **Invisibilidad hacia adentro (Bottom-Up):** Un Scope exterior es completamente ciego a las variables declaradas dentro de bloques interiores.
- **Liberación Automática:** Al llegar a `}`, todo dato local es irrevocablemente borrado.

## Variable Shadowing (Ocultamiento de Nombres)

¿Qué ocurre si existe una variable en el Scope exterior, y accidentalmente declaras **otra variable con el mismo nombre** dentro de un Scope interior?

```cpp
int main() {
    int oro{100}; // La variable original del Scope exterior

    if (true) {
        // ERROR LOGICO SEVERO: Creando una nueva variable 'oro' en el Scope interior
        int oro{50}; 
        std::cout << "Oro local: " << oro << "\n"; // Imprime 50
    }

    std::cout << "Oro global: " << oro << "\n"; // Imprime 100
    return 0;
}
```

Este fenómeno se documenta como **Variable Shadowing** (Sombreamiento de Variables). El compilador de C++ no abortará el proceso; simplemente creará una nueva dirección de memoria en el bloque interior con el mismo nombre. Esta nueva variable **bloquea y oculta** a la variable original. Mientras el flujo de control permanezca en el bloque interior, cualquier mutación afectará únicamente a la variable local. Al salir del bloque, la variable local se destruye, dejando a la original intacta (y tu lógica probablemente arruinada).

<div align="center">
  <img src="assets/l03_variable_shadowing.gif" alt="Sombreado de variables en la memoria RAM Stack">
</div>

#### 🔍 Traducción Visual del Stack RAM y Shadowing:
* **Ámbito Externo (`0x7FFE00`):** Variable `oro = 100` declarada en el ámbito principal.
* **Ámbito Interno (`0x7FFE04`):** Al entrar al bloque `{ ... }`, se empuja una nueva variable `oro = 50` al Stack que **opaca** a la externa.
* **Destrucción de Ámbito (Stack Pop):** Al alcanzar `}`, la celda interna se destruye y la lectura vuelve a resolver la variable exterior `100`.

¡Jamás declares variables locales que compartan el identificador de variables en niveles superiores!

> 🧪 **Laboratorio:** ¡Es hora de experimentar! Abre el archivo [`../lab/L03_BlocksAndScope.cpp`](../lab/L03_BlocksAndScope.cpp).
>
> 🐞 **Demo de Bug (Opcional):** Aprende de los errores comunes. Ejecuta la trampa en [`../lab/demos/D03_VariableShadowingBug.cpp`](../lab/demos/D03_VariableShadowingBug.cpp).
>
> 🏋️ **Ejercicio:** Pon a prueba tu manejo de la memoria. Atrévete con el reto en [`../exercise/E03_RescateDeVariables/E03_RescateDeVariables.cpp`](../exercise/E03_RescateDeVariables/E03_RescateDeVariables.cpp).

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques respuestas en librerías avanzadas ni conceptos no vistos.

<details>
<summary><b>1. Si declaro la variable `std::string nombre{"Juan"};` dentro de un bloque `if`, ¿puedo acceder a `nombre` en la línea inmediata después de que cierre el `if`?</b></summary>

> No. La variable se aloja en memoria al entrar al bloque condicional y es destruida en el instante en que el compilador procesa la llave de cierre `}`. Fuera de ese *Local Scope*, el identificador no existe.
</details>

<details>
<summary><b>2. ¿Qué es el Variable Shadowing y por qué ocurre silenciosamente?</b></summary>

> Ocurre cuando declaras una nueva variable en un Scope interior con el mismo identificador que una variable exterior. El compilador lo permite silenciosamente porque, para él, son dos direcciones de memoria completamente distintas. La variable más profunda "sombrea" (bloquea el acceso) a la más superficial.
</details>

---

| ⬅️ [Anterior: L02_ElseIf.md](L02_ElseIf.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: L04_Switch.md](L04_Switch.md) |
|:---|:---:|---:|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
