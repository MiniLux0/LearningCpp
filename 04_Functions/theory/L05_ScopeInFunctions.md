# L05: Ámbito Local y el Aislamiento de Memoria (Scope)

En el Módulo 03 aprendimos que cualquier variable declarada dentro de unas llaves `{}` se destruye al salir de ellas. A esta frontera la denominamos **Scope** (Ámbito). 

Dado que las funciones son bloques de código delimitados por llaves, obedecen exactamente esta misma regla, actuando como bóvedas insonorizadas: lo que ocurre dentro de una función, es invisible para el exterior. El `main()` no tiene acceso a las variables declaradas dentro de tus funciones delegadas, y viceversa.

A partir de este momento dejaremos la analogía de la bóveda para hablar con rigor técnico del **Ciclo de Vida de Memoria (Lifetime)** y el **Ocultamiento de la Información (Information Hiding)**.

---

## El Aislamiento de Identificadores (Shadowing y Coexistencia)

Debido a que cada función posee un entorno de memoria completamente aislado (Scope Local), puedes declarar variables utilizando exactamente los mismos identificadores (nombres) en diferentes rutinas sin generar colisiones ni sobreescrituras en la memoria.

```cpp
void cargarInventarioJugadorUno() {
    int monedas{500}; // Este bloque de memoria es exclusivo de este Scope.
}

void cargarInventarioJugadorDos() {
    int monedas{10}; // Esta es una dirección de memoria diferente; no hay colisión.
}
```

> [!NOTE]
> **Planificación de Animación (manim-composer):**
> *`l05_function_scope.gif`*: Dos cuadrículas de memoria RAM (una etiquetada `main` y otra `funcion`). Ambas declaran una variable llamada `puntuacion`. Cuando la cámara hace zoom sobre las cuadrículas, la animación revela que los punteros hexadecimales de memoria (ej. `0x7ff0` y `0x7ff8`) son físicamente distintos, demostrando que los identificadores coexisten sin chocar porque su Scope no se solapa.

---

## La trampa de la Fuga de Scope (`not declared in this scope`)

Un error arquitectónico clásico al modularizar código es olvidar que **es ilegal invocar una variable local desde un Scope externo**. Las variables nacen cuando se declaran y mueren (se libera su memoria) al alcanzar la llave de cierre `}` de su función.

```cpp
void calcularImpuestos() {
    int total_impuestos{42};
    // Al alcanzar esta llave, 'total_impuestos' es eliminada de la RAM.
}

int main() {
    calcularImpuestos();
    
    // 🐞 ERROR FATAL DE COMPILACIÓN:
    // El compilador abortará: "total_impuestos was not declared in this scope".
    std::cout << total_impuestos; 
}
```

El `main()` no tiene autorización ni capacidad técnica para leer lo que se calculó en el Scope local de `calcularImpuestos()`. Cuando la rutina terminó su ciclo, el bloque de memoria fue liberado de la RAM. 

**¿La solución arquitectónica?** Si requieres que un dato generado en una rutina delegada sobreviva a la destrucción del Scope y sea accesible por el `main()`, debes **inyectarlo explícitamente hacia el bloque invocador usando `return`**.

---

> 🧪 **Laboratorio:** Comprueba en el compilador cómo dos variables con el mismo identificador coexisten pacíficamente si sus Scopes están aislados. Abre el archivo [`../lab/L05_ScopeInFunctions.cpp`](../lab/L05_ScopeInFunctions.cpp).
>
> 🐞 **Demo de Bug:** Observa el aborto de compilación al intentar invocar un bloque de memoria destruido o ajeno. Ejecuta la trampa en [`../lab/demos/D05_LocalVariableBug.cpp`](../lab/demos/D05_LocalVariableBug.cpp).
>
> 🏋️ **Ejercicio:** El escáner de seguridad colapsó al intentar auditar una variable atrapada en el aislamiento de una sub-rutina. Atrévete con el reto en [`../exercise/E05_CamaraDeAislamiento/E05_CamaraDeAislamiento.cpp`](../exercise/E05_CamaraDeAislamiento/E05_CamaraDeAislamiento.cpp).

---

| ⬅️ [Anterior: Parámetros por valor](L04_Parameters.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Diseñando con funciones (Refactoring)](L06_Refactoring.md) |
|---|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
