# L05 · Primer contacto con datos y entrada segura

> **Módulo 01 — Getting Started**

---

## Reteniendo información en la memoria

Hasta ahora, nuestros programas han sido mudos y ciegos: imprimen un mensaje fijo y terminan. Para hacer algo útil, un programa necesita recordar información (como tu nombre, tu edad, o el puntaje de un juego). 

Para que el programa recuerde algo, necesita reservar un pequeño espacio en la memoria RAM de tu computadora. A ese espacio le ponemos un nombre para encontrarlo fácilmente. Eso es una **variable**.

En C++ moderno, crear una variable es decirle a la computadora tres cosas:
1. El **tipo** de dato (qué forma tiene la información: texto, números enteros, etc.).
2. El **nombre** (cómo la vas a llamar).
3. Su valor **inicial** (siempre entre llaves `{}`).

```cpp
#include <string> // Necesario para guardar texto (cadenas de caracteres)

int edad{0};            // Un número entero (int), inicia en 0
std::string nombre{""}; // Texto (string), inicia vacío
```

### La trampa de las variables sin inicializar
A diferencia de otros lenguajes de programación que te cuidan, C++ prioriza la velocidad. Si no usas las llaves `{}` para darle un valor inicial a tu variable, C++ simplemente reserva el espacio en la RAM, pero **no lo limpia**. 

La RAM recicla espacio todo el tiempo. Si no limpias tu variable al crearla, contendrá "basura" (datos aleatorios de algún programa anterior que usó ese mismo espacio). Las llaves `{}` garantizan que tu memoria arranca limpia y segura.

---

## Escuchando al usuario (`std::cin`)

<div align="center">
  <img src="assets/l05_cin_extraction.gif" alt="Extracción de entrada tipada con std::cin hacia la memoria RAM">
</div>

#### 🔍 Traducción Visual del Flujo de Entrada:
* **Panel Izquierdo (`main.cpp`):** La instrucción `std::cin >> edad;` abre el canal de extracción.
* **Operador `>>` (Canal de entrada):** Lee los caracteres desde el flujo de entrada estándar (*stdin*), los parsea al tipo correspondiente (`int`).
* **Panel Derecho (Memoria RAM Stack):** Deposita el valor resultante directamente en la celda física `0x7FFEE8` asignada a la variable.

Ya sabemos imprimir con `std::cout` (Character Output). Para escuchar lo que el usuario escribe en el teclado, usamos su opuesto: **`std::cin`** (Character Input).

Fíjate cómo el operador de flechas se invierte. En `cout`, las flechas apuntan hacia la pantalla (`<<`). En `cin`, las flechas **extraen** información desde el teclado hacia tu variable (`>>`).

```cpp
#include <iostream>
#include <string>

int main() {
    std::string nombre_usuario{""}; // Memoria limpia

    // 1. Imprimimos una pregunta
    std::cout << "Escribe tu nombre: ";

    // 2. Esperamos que el usuario escriba y presione Enter.
    // Lo que escriba, se guarda en la variable.
    std::cin >> nombre_usuario;

    // 3. Imprimimos usando la variable
    std::cout << "Hola, " << nombre_usuario << "!\n";

    return 0;
}
```

Al igual que un rompecabezas, puedes encadenar variables y texto libre usando múltiples flechas `<<` dentro del mismo `cout`, lo que te permite armar frases personalizadas como en el ejemplo número 3 de arriba.

> 🧪 **Laboratorio:** Conecta el teclado con la memoria de tu programa. Abre el archivo [`../lab/L05_DatosYEntradaSegura.cpp`](../lab/L05_DatosYEntradaSegura.cpp).
>
> 🐞 **Demo de Bug (Opcional):** Mira qué pasa cuando olvidas limpiar la memoria RAM. Ejecuta la trampa en [`../lab/demos/D04_UninitializedBug.cpp`](../lab/demos/D04_UninitializedBug.cpp).
>
> 🏋️ **Ejercicio:** Es hora de saludar al usuario interactivamente. Atrévete con el reto en [`../exercise/E04_InteractiveGreeting/E04_InteractiveGreeting.cpp`](../exercise/E04_InteractiveGreeting/E04_InteractiveGreeting.cpp).

---

## ✦ Resumen

- Una **variable** es un espacio en la memoria (RAM) con un nombre y un tipo, que usamos para guardar datos.
- Para usar variables de texto necesitas incluir `#include <string>`.
- **Regla de oro de C++ moderno:** Siempre inicializa tus variables usando llaves `{}` (ej. `int x{0};`) para no arrastrar basura de la memoria RAM.
- `std::cin >>` extrae el texto que el usuario teclea y lo introduce en una variable.

---

## ✦ Preguntas de autochequeo

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques en internet — si no puedes responderlas de memoria, relee la sección correspondiente.

<details>
<summary><b>1. Si declaras la variable <code>int puntaje;</code> sin inicializarla con <code>{}</code>, ¿por qué podría ser peligroso si imprimes su valor inmediatamente después en la pantalla?</b></summary>

> Porque C++ no limpia la memoria por defecto. Esa variable contendrá "basura" aleatoria (datos que quedaron en ese pedazo de la RAM usados por algún programa anterior), lo que puede causar bugs impredecibles en tu programa.
</details>

<details>
<summary><b>2. Observando la dirección de las flechas, ¿por qué en <code>std::cout</code> se usan <code>&lt;&lt;</code> y en <code>std::cin</code> se usan <code>&gt;&gt;</code>? ¿Hacia dónde "apuntan" los datos en cada caso?</b></summary>

> En `cout <<`, las flechas empujan la información hacia afuera (hacia la pantalla). En `cin >>`, las flechas extraen la información desde la consola hacia adentro (hacia tu variable). Las flechas siempre apuntan al destino final del dato.
</details>

<details>
<summary><b>3. ¿Qué biblioteca debes incluir con <code>#include</code> en la parte superior de tu archivo si planeas almacenar palabras o frases?</b></summary>

> Debes incluir la biblioteca `<string>`, que contiene las herramientas necesarias para crear variables de texto (cadenas de caracteres).
</details>

---

| ⬅️ [Anterior: Formato y comentarios](L04_FormatoSalidaComentarios.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Mini-proyecto terminal](L06_MiniProyectoAppInteractiva.md) |
|---|---|---|

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>