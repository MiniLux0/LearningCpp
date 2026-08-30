# Lección 01: Tomando Decisiones (`if` / `else`)

Hasta ahora, todos los programas que hemos escrito son como trenes en una vía recta. El programa empieza en `main()`, ejecuta la línea 1, luego la línea 2, luego la línea 3, y así hasta terminar. Pero en el mundo real, necesitamos tomar decisiones. Si llueve, llevo paraguas; de lo contrario, llevo gafas de sol. En C++, usamos `if` (si...) y `else` (de lo contrario...) para enseñarle a la computadora a desviarse de la vía principal basándose en preguntas. A partir de aquí, dejaremos las analogías de trenes y usaremos el término técnico correcto de la industria: **Control de Flujo** y **Bloques Condicionales**.

## La Anatomía de un `if`

La instrucción `if` evalúa una **expresión booleana**. Solo si el resultado de la evaluación es `true` (verdadero), el programa ejecutará el bloque de código asociado.

```cpp
bool tieneEntradaVIP{true};

if (tieneEntradaVIP) {
    std::cout << "Acceso concedido al servidor.\n";
}
```

### ¿Qué está pasando internamente?
1. La palabra clave `if` inicia la estructura de control.
2. Dentro de los paréntesis `( )` se encuentra la **condición a evaluar**. 
3. Los símbolos `{ }` (las llaves) delimitan el **bloque de ejecución condicional** (también conocido como *Scope local*, del cual hablaremos a fondo en la Lección 03). El código encapsulado aquí solo se compilará y ejecutará si la condición resulta ser verdadera.

Si `tieneEntradaVIP` fuera falso (`false`), el flujo de control ignoraría el bloque por completo, saltando a la línea inmediatamente posterior a la llave de cierre `}`.

## Añadiendo el Plan B: `else`

Cuando una condición falla, muchas veces necesitamos que el programa ejecute una ruta alternativa en lugar de simplemente no hacer nada. Para esto utilizamos la cláusula `else`. Esta estructura garantiza la **exclusión mutua**: o se ejecuta el bloque `if`, o se ejecuta el bloque `else`, pero jamás ambos.

```cpp
bool tieneEntradaVIP{false};

if (tieneEntradaVIP) {
    // Bloque primario (Condición True)
    std::cout << "Acceso concedido al servidor.\n";
} else {
    // Bloque alternativo o Fallback (Condición False)
    std::cout << "Error: Credenciales invalidas.\n";
}
```

<div align="center">
  <img src="assets/l01_if_else_flow.gif" alt="Flujo de bifurcación condicional if-else en la CPU">
</div>

#### 🔍 Traducción Visual del Flujo de Control:
* **Panel Izquierdo (`main.cpp`):** Código fuente con la condición `if (edad >= 18)`.
* **Evaluación de CPU (`Condición: true`):** La Unidad de Control evalúa la comparación lógica en un registro.
* **Bifurcación Excluyente:** Se activa únicamente la rama correspondiente (`Acceso VIP`), saltando la rama alternativa.

## Evaluando Expresiones Relacionales

Rara vez usaremos variables `bool` directas. Lo más profesional es que la condición sea el resultado de una operación relacional (`>`, `<`, `==`, `!=`).

```cpp
int nivelDelUsuario{16};

if (nivelDelUsuario >= 18) {
    std::cout << "Permiso de administrador otorgado.\n";
} else {
    std::cout << "Privilegios insuficientes.\n";
}
```

## El Error Más Común: El "Punto y Coma" Asesino

Hay una trampa arquitectónica muy peligrosa cuando aprendes a dominar el flujo de control. Nunca coloques un punto y coma `;` inmediatamente después de la condición del `if`.

```cpp
// ¡PELIGRO! Esto es un bug logico masivo:
if (nivelDelUsuario >= 18); 
{
    std::cout << "Permiso de administrador otorgado.\n";
}
```

En C++, el `;` indica el final de una instrucción. Al colocarlo ahí, el compilador asume que tu `if` tiene una "instrucción vacía". Como resultado, el bloque `{ ... }` queda completamente desconectado del condicional y se ejecutará de forma incondicional para todos los usuarios.

> 🧪 **Laboratorio:** ¡Es hora de experimentar! Abre el archivo [`../lab/L01_IfElse.cpp`](../lab/L01_IfElse.cpp).
>
> 🐞 **Demo de Bug (Opcional):** Analiza el desastre del punto y coma. Ejecuta la trampa en [`../lab/demos/D01_IfSemicolonBug.cpp`](../lab/demos/D01_IfSemicolonBug.cpp).
>
> 🏋️ **Ejercicio:** Pon a prueba tu lógica booleana. Atrévete con el reto en [`../exercise/E01_SistemaDeClima/E01_SistemaDeClima.cpp`](../exercise/E01_SistemaDeClima/E01_SistemaDeClima.cpp).

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques respuestas en librerías avanzadas ni conceptos no vistos.

<details>
<summary><b>1. Si la condición dentro de un `if` evalúa a falso y no hay ningún bloque `else`, ¿qué hace el flujo de control?</b></summary>

> Simplemente salta el bloque delimitado por las llaves `{ }` del `if` y reanuda la ejecución en la línea de código inmediatamente posterior.
</details>

<details>
<summary><b>2. ¿Por qué es un error lógico severo colocar un punto y coma justo después de `if (condicion)`?</b></summary>

> Porque el punto y coma actúa como una instrucción terminada (vacía). C++ asume que no quieres hacer nada si la condición es verdadera, desvinculando el `if` de las llaves siguientes, las cuales pasarán a ejecutarse incondicionalmente.
</details>

---

| ⬅️ [Anterior: README.md](../README.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: L02_ElseIf.md](L02_ElseIf.md) |
|:---|:---:|---:|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
