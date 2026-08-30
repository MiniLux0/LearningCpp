# L01: ¿Qué es una función y por qué las necesitamos?

Imagina que eres el gerente de un restaurante muy exitoso. Si te piden 50 hamburguesas en un día, no vas a cocinar cada una paso a paso tú mismo; tu cabeza explotaría. En lugar de eso, contratas a un cocinero, le enseñas los pasos una sola vez, le pones un nombre a su labor y, de ahora en adelante, simplemente "lo llamas" cuando lo necesitas para delegar el trabajo. 

Ese es el concepto abstracto. A partir de este momento, soltaremos la analogía del restaurante y usaremos los términos reales de la ingeniería de software: **Funciones**, **Invocación (Llamadas)**, **Parámetros** y **Valores de Retorno**.

En C++, una **función** es un bloque de código empaquetado bajo un identificador (nombre) único, diseñado para realizar una tarea específica, permitiendo la reutilización del código y evitando la repetición.

---

## La anatomía de una Función

Para definir una función, C++ requiere una estructura estricta compuesta por 4 partes, conocida como la "firma" o *signature*. Observa esta plantilla:

```cpp
TipoDeRetorno nombreDeLaFuncion(Parametros) {
    // Instrucciones (El cuerpo)
}
```

<div align="center">
  <img src="assets/l01_anatomy_of_a_function.gif" alt="Anatomía de una función en C++">
</div>

#### 🔍 Traducción Visual de la Firma y Componentes:
* **Panel Izquierdo (`matematica.cpp`):** Código fuente de la función `sumar` con sus cuatro componentes analizados.
* **1. Tipo de Retorno (`int` - Verde):** Define el tipo de dato garantizado que la función inyectará de vuelta al llamador.
* **2. Identificador (`sumar` - Cian):** Nombre único mediante el cual el flujo de ejecución invoca y transfiere el control a la rutina.
* **3. Parámetros (`(int a, int b)` - Oro):** Canales de entrada que reciben y alojan las variables clonadas por *Pass-by-value*.
* **4. Scope Local (`{ ... }` - Púrpura):** Cuerpo y frontera estricta de memoria; toda variable interna se destruye al alcanzar la llave de cierre `}`.

Si escribiéramos una función real para sumar números, se vería así:

```cpp
int sumar(int a, int b) {
    int resultado{a + b};
    return resultado;
}
```

Vamos a desarmarlo pieza por pieza:

1. **`int` (Tipo de retorno):** Declara el tipo de dato que la función devolverá al terminar su ejecución. Si devuelve un número entero, usamos `int`. Si la función ejecuta una acción sin devolver datos, usaríamos la palabra clave `void` (vacío).
2. **`sumar` (Identificador):** Es el nombre con el que invocaremos a la función desde otras partes del código. Debe ser descriptivo (Ej. `calcularArea`, no `calc`).
3. **`(int a, int b)` (Parámetros):** Son los "inputs" o datos de entrada que la función necesita para operar. 
4. **`{ ... }` (El cuerpo):** Define el bloque de ejecución (Scope) donde ocurre la lógica interna, invisible para el resto del programa.
5. **`return`:** La instrucción final que envía el dato procesado (output) de vuelta al bloque de código que invocó la función.

---

## Invocación (Llamando a la función)

Definir la función no hace que se ejecute; solo le enseña al compilador *cómo* ejecutarla. Para que ocurra el procesamiento, debes **invocar (llamar) a la función** desde el punto de entrada principal del programa: el `main()`.

> [!WARNING]
> **Regla de Arquitectura Estricta (Temporal):** Por ahora, toda función nueva que definas **DEBE** declararse físicamente arriba del `main()`. C++ es un lenguaje compilado de arriba hacia abajo. Si el `main()` intenta invocar una función que está escrita más abajo, el compilador abortará con un error de identificador desconocido (*was not declared in this scope*).

```cpp
#include <iostream>

// 1. DEFINICIÓN DE LA FUNCIÓN
int sumar(int a, int b) {
    return a + b; 
}

// 2. PUNTO DE ENTRADA PRINCIPAL
int main() {
    // INVOCACIÓN: Llamamos a la función inyectándole los argumentos 5 y 10.
    // El 'output' de la función lo atrapamos en una variable inicializada con {}.
    int total{sumar(5, 10)};
    
    std::cout << "La suma es: " << total << '\n';
    
    return 0; // El main() también es una función que retorna un int al Sistema Operativo
}
```

Al llamar a `sumar(5, 10)`, el flujo de ejecución pausa temporalmente el `main()`, salta hacia la función `sumar`, ejecuta sus pasos en privado, y luego regresa al `main()` trayendo consigo el resultado (`15`).

---

> 🧪 **Laboratorio:** Observa cómo las funciones se comunican con el `main()` a través de invocaciones claras. Abre el archivo [`../lab/L01_Anatomy.cpp`](../lab/L01_Anatomy.cpp).
>
> 🏋️ **Ejercicio:** El código de la recepción de invitados es un monolito gigante. Extrae esa lógica y delégala a una función paramétrica. Atrévete con el reto en [`../exercise/E01_ConstructorDeSaludos/E01_ConstructorDeSaludos.cpp`](../exercise/E01_ConstructorDeSaludos/E01_ConstructorDeSaludos.cpp).

---

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste.

<details>
<summary><b>1. Si una función está diseñada exclusivamente para imprimir texto en la consola y no necesita devolver ningún valor numérico ni texto al main, ¿qué "Tipo de Retorno" debe usar?</b></summary>

> Debe usar la palabra clave `void`, que indica explícitamente que la función no tiene output de retorno.
</details>

<details>
<summary><b>2. Si defines tu función debajo del `main()`, ¿por qué falla la compilación?</b></summary>

> Porque el compilador lee el archivo de arriba hacia abajo de forma secuencial (Single-pass parsing por defecto). Cuando llega a la invocación en el `main()`, todavía no sabe que la función existe más abajo, por lo que asume que es un identificador inválido.
</details>

---

| ⬅️ [Anterior: README.md](../README.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Retornando valores](L02_Return.md) |
|---|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
