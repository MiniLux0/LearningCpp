# L04 · Formato, salida y comentarios

> **Módulo 01 — Getting Started**

---

## Dando formato al texto: Secuencias de escape

Hasta ahora, nuestro texto se imprime exactamente como lo escribimos dentro de las comillas `" "`. Pero, ¿qué pasa si queremos organizar nuestro texto en la pantalla, hacer saltos de línea o imprimir una palabra entre comillas?

Para esto existen las **secuencias de escape**. Son combinaciones especiales de dos caracteres que siempre empiezan con una barra invertida (`\`). Cuando `std::cout` ve esa barra invertida, no imprime la letra que sigue, sino que ejecuta una acción de formato.

Aquí tienes la tabla de las secuencias más importantes que usarás:

| Secuencia | Acción que realiza | Ejemplo | Resultado en pantalla |
|:---:|---|---|---|
| `\n` | **Salto de línea** (Enter) | `"Hola\nMundo"` | Hola<br>Mundo |
| `\t` | **Tabulación** (Espacio largo) | `"ID\tNombre"` | ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nombre |
| `\"` | **Imprimir comillas** dobles | `"Dijo: \"Hola\""` | Dijo: "Hola" |
| `\\` | **Imprimir la barra** invertida | `"C:\\Carpeta"` | C:\Carpeta |

> 💡 **Nota sobre std::endl:** En muchos cursos antiguos verás que usan `std::cout << "Hola" << std::endl;` para saltar de línea. En C++ moderno preferimos usar `\n`. `std::endl` no solo salta la línea, sino que fuerza a la computadora a "vaciar" la pantalla inmediatamente (un proceso lento). Usa siempre `\n` a menos que sepas exactamente por qué necesitas vaciar la memoria.

<div align="center">
  <img src="assets/l04_newline_vs_endl.gif" alt="Diferencia de rendimiento entre salto de línea '\\n' y std::endl">
</div>

#### 🔍 Traducción Visual del Buffer y Rendimiento:
* **Instrucción `\n` (Buffer RAM):** Inserta un simple byte de salto de línea en el buffer de salida de forma instantánea.
* **Instrucción `std::endl` (Hardware Flush):** Añade `\n` y además bloquea la ejecución forzando la sincronización física del buffer (*I/O Flush*), degradando el rendimiento.
* **Veredicto Técnico:** En C++ Moderno, usa **siempre** `'\n'` por defecto.

---

## Dejando notas para los humanos: Comentarios

El compilador de C++ es estricto: lee cada palabra de tu archivo y trata de traducirla a instrucciones. Pero a veces, necesitas dejar notas en el archivo que sean solo para ti o para otros programadores.

Los **comentarios** son texto que el compilador ignora por completo. Existen dos formas de escribirlos:

### 1. Comentarios de una sola línea (`//`)
Todo lo que escribas después de `//` hasta que termine la línea será ignorado.
```cpp
std::cout << "Iniciando sistema...\n"; // Esto es ignorado por la máquina
```

### 2. Comentarios de bloque (`/* */`)
Si necesitas escribir un manual o un párrafo muy largo, encierra tu texto entre estos símbolos.
```cpp
/* 
Este es un comentario de varias líneas.
Se usa comúnmente en la cabecera de los archivos
para explicar de qué trata todo el programa.
*/
```

### La regla de oro de los comentarios

En C++ moderno, existe una regla fundamental sobre cómo comentar el código: **Los comentarios deben explicar el POR QUÉ, no el QUÉ**.

El código por sí mismo ya dice *qué* está haciendo (ej. imprimir un mensaje). Tu comentario debe aportar el contexto humano de *por qué* tomaste esa decisión.

```cpp
// ❌ MAL COMENTARIO: Repite lo obvio
std::cout << "Error 404\n"; // Imprime Error 404

// ✅ BUEN COMENTARIO: Da contexto útil
std::cout << "Error 404\n"; // Se requiere este mensaje exacto para pasar la auditoría del servidor
```

> 🧪 **Laboratorio:** Juega con el formato y los saltos de línea. Abre el archivo [`../lab/L04_FormatoSalidaComentarios.cpp`](../lab/L04_FormatoSalidaComentarios.cpp).
>
> 🏋️ **Ejercicio:** El jefe te ha pedido imprimir un menú con un formato exacto que parece imposible de encuadrar. Resuélvelo en [`../exercise/E03_EscapeSequences/E03_EscapeSequences.cpp`](../exercise/E03_EscapeSequences/E03_EscapeSequences.cpp).

---

## ✦ Resumen

- Las **secuencias de escape** inician con `\` y formatean el texto dentro de las comillas.
- `\n` es la forma moderna y recomendada de saltar de línea en C++.
- Los **comentarios** (`//` y `/* */`) son ignorados por el compilador y leídos solo por humanos.
- Un buen comentario en código profesional explica *por qué* se hizo algo, no *qué* hace.

---

## ✦ Preguntas de autochequeo

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques en internet — si no puedes responderlas de memoria, relee la sección correspondiente.

<details>
<summary><b>1. Si quieres imprimir en la pantalla el texto <code>Carpeta "Secreta"</code>, ¿por qué no puedes simplemente escribir <code>std::cout << "Carpeta "Secreta"";</code>? ¿Qué secuencia de escape necesitas?</b></summary>

> Porque las comillas dobles le indican a C++ dónde empieza y termina el texto. Si escribes comillas en el medio, C++ pensará que el texto se acabó antes de tiempo. Para imprimir comillas literales, necesitas la secuencia de escape `\"`.
</details>

<details>
<summary><b>2. Entre usar <code>\n</code> y <code>std::endl</code>, ¿cuál es la opción más rápida para la computadora y por qué?</b></summary>

> `\n` es más rápido. `std::endl` hace un salto de línea pero también "vacía" inmediatamente el buffer de memoria hacia la pantalla, lo cual es un proceso lento que no suele ser necesario en la mayoría de los casos.
</details>

<details>
<summary><b>3. Según la regla de oro, ¿por qué es una mala idea escribir un comentario que diga <code>// Suma 1 al contador</code> justo arriba de la línea donde efectivamente sumas 1 al contador?</b></summary>

> Porque explica el *QUÉ*, pero no el *POR QUÉ*. El código ya te dice claramente que se está sumando 1 al contador. Un buen comentario debería explicar la razón humana detrás de esa suma (ej. "Contamos un intento fallido del jugador").
</details>

---

| ⬅️ [Anterior: Namespaces y std::](L03_NamespacesYStd.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Datos y entrada segura](L05_DatosYEntradaSegura.md) |
|---|---|---|

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>