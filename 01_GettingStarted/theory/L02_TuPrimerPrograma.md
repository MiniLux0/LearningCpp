# L02 · Tu primer programa

> **Módulo 01 — Getting Started**

---

## Escribiendo Hola Mundo

En el mundo de la programación, existe una tradición sagrada: el primer programa que escribes en un lenguaje nuevo debe simplemente imprimir el texto "Hola Mundo" (o "Hello World") en la pantalla. Es una prueba de que todo tu sistema (editor, compilador y sistema operativo) funciona perfectamente.

Este es el código completo del "Hola Mundo" en C++ moderno:

```cpp
#include <iostream>

int main() {
    std::cout << "Hola Mundo!\n";
    return 0;
}
```

No te preocupes si parece un hechizo en otro idioma. Vamos a desarmarlo línea por línea.

---

## Anatomía de un programa C++

C++ es un lenguaje muy explícito. Todo tiene un por qué y nada sucede por arte de magia.

### 1. Preparando las herramientas (`#include`)
```cpp
#include <iostream>
```
El núcleo de C++ es extremadamente pequeño y rápido; por defecto, ni siquiera sabe cómo imprimir texto en la pantalla. Para hacer cosas útiles, necesitamos pedir prestadas herramientas de la **Biblioteca Estándar**.
El comando `#include` le dice al compilador: *"Busca el archivo llamado `iostream` (que significa Input/Output Stream) y pégalo aquí"*. Sin esta línea, intentar imprimir texto fallaría.

### 2. El punto de entrada (`int main()`)
```cpp
int main() {
```
Imagina que un programa de C++ tiene miles de líneas de código y cientos de funciones. Cuando la computadora intenta ejecutarlo, se pregunta: *"¿Por dónde empiezo?"*. 
En C++, la ejecución **siempre** empieza en la función llamada `main`. Si no hay `main`, el programa no arranca. Las llaves `{}` que abren y cierran delimitan exactamente dónde empiezan y dónde terminan las instrucciones de `main`.

### 3. Hablando con la pantalla (`std::cout`)
```cpp
    std::cout << "Hola Mundo!\n";
```
Esta es la instrucción real que hace el trabajo. 
- `std::cout` significa "Standard Character Output" (salida estándar de caracteres, es decir, tu pantalla).
- El operador `<<` (dos signos de menor) funciona como una flecha. Empuja el texto `"Hola Mundo!\n"` hacia la pantalla.
- El símbolo `\n` al final del texto le dice a la consola que presione "Enter" para hacer un salto de línea.
- **Punto y coma `;`**: En C++, casi todas las instrucciones deben terminar con un punto y coma. Es el equivalente a un punto final en una oración. Si lo olvidas, el compilador lanzará un error.

### 4. Avisando que todo salió bien (`return 0`)
```cpp
    return 0;
}
```
Cuando un programa termina, el sistema operativo (Windows, Mac, etc.) quiere saber cómo le fue. Devolver (`return`) un cero (`0`) es la convención universal en programación que significa: *"Terminé mi trabajo con éxito y sin errores"*.

---

## Del texto a la realidad: Compilando el código

<div align="center">
  <img src="assets/l02_cout_stream.gif" alt="Flujo de salida estándar con std::cout">
</div>

#### 🔍 Traducción Visual del Flujo de Salida:
* **Panel Izquierdo (`main.cpp`):** La instrucción `std::cout << "Hola Mundo\n";` empaqueta la cadena de texto.
* **Operador `<<` (Canal de flujo):** Transfiere los bytes directamente al flujo estándar de salida (*stdout*).
* **Panel Derecho (Consola OS):** La terminal del sistema operativo recibe los bytes y renderiza el texto `"Hola Mundo"` en pantalla.

Si guardas el código de arriba en un archivo llamado `L02_HolaMundo.cpp`, todavía es solo texto (código fuente). Para poder ejecutarlo, hay que compilarlo usando la terminal.

Abre tu terminal en la carpeta donde guardaste el archivo y escribe el siguiente comando:

```bash
g++ L02_HolaMundo.cpp -o programa
```

¿Qué acabas de hacer?
- `g++` llama al compilador.
- `L02_HolaMundo.cpp` es el archivo que quieres traducir.
- `-o programa` (la "o" es de "output") le dice al compilador: *"Llama al archivo ejecutable resultante `programa`"*. (En Windows generará un `programa.exe`).

Si el código no tiene errores, el compilador terminará en silencio. Ahora tienes un programa listo para usar. Para ejecutarlo desde la misma terminal:

- En Windows: `.\programa.exe`
- En Mac/Linux: `./programa`

¡Felicidades! Acabas de escribir, traducir y ejecutar tu primer programa en C++.

> 🧪 **Laboratorio:** Ve a la práctica. Abre el archivo [`../lab/L02_TuPrimerPrograma.cpp`](../lab/L02_TuPrimerPrograma.cpp).
>
> 🏋️ **Ejercicio:** Tu primer reto en código. Atrévete a resolverlo en [`../exercise/E01_HelloWorld/E01_HelloWorld.cpp`](../exercise/E01_HelloWorld/E01_HelloWorld.cpp).

---

## ✦ Resumen

- Todo programa C++ comienza su ejecución en la función obligatoria `int main()`.
- Usamos `#include <iostream>` para que C++ aprenda a mostrar texto en la pantalla.
- `std::cout <<` empuja texto hacia la consola, y cada instrucción normal debe terminar en `;`.
- El proceso se divide en dos pasos: escribir el código fuente (`.cpp`), y compilarlo en la terminal con `g++` para generar el ejecutable.

---

## ✦ Preguntas de autochequeo

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques en internet — si no puedes responderlas de memoria, relee la sección correspondiente.

<details>
<summary><b>1. Si olvidas escribir la línea <code>#include &lt;iostream&gt;</code>, ¿qué parte del programa `main` dejará de funcionar y por qué?</b></summary>

> Dejará de funcionar `std::cout`. Sin esa línea, C++ no sabe cómo interactuar con la pantalla, ya que el comando `cout` vive dentro de la biblioteca de entrada/salida (iostream) que olvidaste incluir.
</details>

<details>
<summary><b>2. Si tienes un programa C++ muy complejo con 50 funciones distintas, ¿cómo sabe la computadora qué función debe ejecutar primero?</b></summary>

> La computadora siempre buscará y ejecutará la función llamada `main`. Es el punto de entrada obligatorio de todo programa en C++.
</details>

<details>
<summary><b>3. ¿Cuál es el significado del punto y coma (<code>;</code>) al final de la instrucción <code>std::cout</code>?</b></summary>

> Actúa como un punto final en una oración. Le indica al compilador que la instrucción ha terminado. Si lo olvidas, el compilador lanzará un error porque pensará que la instrucción continúa en la siguiente línea.
</details>

---

| ⬅️ [Anterior: Instalando herramientas](L01_InstalandoHerramientas.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Namespaces y std::](L03_NamespacesYStd.md) |
|---|---|---|

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>