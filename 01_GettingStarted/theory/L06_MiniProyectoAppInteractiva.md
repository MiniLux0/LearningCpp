# L06 · Mini-proyecto: App interactiva de terminal

> **Módulo 01 — Getting Started**

---

## El problema de los espacios en blanco

En la lección anterior usamos `std::cin >> nombre;` para guardar lo que el usuario escribía. Funciona perfecto para nombres como *"María"* o *"Juan"*. 

Pero, ¿qué pasa si el programa te pide tu nombre completo y escribes *"María López"*? Si usas el comando `std::cin >>`, el programa guardará *"María"*, y perderá por completo *"López"*.

### ¿Por qué sucede esto?
En C++, el operador de extracción `>>` está diseñado para leer una sola palabra a la vez. Cuando encuentra el primer espacio en blanco (o un Enter), asume que ya terminó su trabajo de lectura. *"López"* se queda flotando en el teclado (buffer) esperando ser leído por un futuro comando. Esto causa que todo el programa colapse y las siguientes preguntas se respondan solas con esa basura sobrante.

<div align="center">
  <img src="assets/l06_io_pipeline.gif" alt="Pipeline interactivo de entrada y salida con std::cout y std::cin">
</div>

#### 🔍 Traducción Visual del Pipeline Interactivo:
* **Paso 1 (Prompt con `std::cout`):** El programa despliega la solicitud de datos (`"Nombre: "`) en la terminal.
* **Paso 2 (Entrada con `std::cin`):** El usuario escribe `"Link"`, y los datos se asignan en la variable.
* **Paso 3 (Respuesta formateada):** El programa concatena y renderiza el resultado final (`"Hola Link!"`) en la consola.

## La solución: std::getline()

Si quieres leer frases completas, nombres compuestos o cualquier texto que pueda tener espacios intermedios, debes usar una herramienta distinta de la biblioteca estándar llamada **`std::getline()`** (obtener línea).

Su funcionamiento es simple: le das el comando de entrada (`cin`) y la variable donde quieres que guarde la línea entera.

```cpp
#include <iostream>
#include <string>

int main() {
    std::string nombre_completo{""};
    
    std::cout << "Por favor, escribe tu nombre completo: ";
    
    // Lee toda la línea entera, espacios incluidos, hasta el Enter.
    std::getline(std::cin, nombre_completo);
    
    std::cout << "Registro guardado: " << nombre_completo << "\n";
    return 0;
}
```

> ⚠️ **Regla práctica de oro:** 
> - Si esperas solo un número o una sola palabra clave: usa `std::cin >> variable;`
> - Si esperas texto, nombres o frases del usuario: usa `std::getline(std::cin, variable);`

---

## Proyecto Final del Módulo

Has aprendido cómo comunicarte con el sistema, dar formato a la pantalla con saltos de línea, declarar memoria limpia con inicialización uniforme y capturar nombres compuestos usando `getline`.

El archivo de código correspondiente a esta lección (`L06_MiniProyectoAppInteractiva.cpp`) integra todo esto en un solo programa: un Generador de Perfil de Usuario que solicita varios datos combinados e imprime una tarjeta final perfectamente estructurada en la terminal.

> 🧪 **Laboratorio:** Junta todo lo aprendido. Abre el archivo [`../lab/L06_MiniProyectoAppInteractiva.cpp`](../lab/L06_MiniProyectoAppInteractiva.cpp).
>
> 🐞 **Demo de Bug (Opcional):** Sufre el bug de los espacios en `cin` por ti mismo. Ejecuta la trampa en [`../lab/demos/D05_CinSpacesBug.cpp`](../lab/demos/D05_CinSpacesBug.cpp).
>
> 🏋️ **Ejercicio:** Imprime un recibo de compra perfecto arreglando el buffer. Atrévete con el reto en [`../exercise/E05_FormattedReceipt/E05_FormattedReceipt.cpp`](../exercise/E05_FormattedReceipt/E05_FormattedReceipt.cpp).

¡Felicidades! Has completado la parte teórica del Módulo 01, tienes las bases para crear programas interactivos en la terminal y estás escribiendo C++ moderno y limpio.

---

## ✦ Resumen

- `std::cin >>` detiene su lectura en el momento exacto en el que encuentra un espacio en blanco. Es ideal para leer números sueltos, pero terrible para frases.
- Para leer texto con espacios (como un nombre completo), C++ nos provee la función `std::getline(std::cin, variable)`.
- `std::getline()` lee absolutamente todo lo que el usuario teclea hasta que presiona la tecla Enter.

---

## ✦ Preguntas de autochequeo

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques en internet — si no puedes responderlas de memoria, relee la sección correspondiente.

<details>
<summary><b>1. Si un usuario escribe la dirección <code>"Calle Falsa 123"</code> e intentas capturarla usando únicamente <code>std::cin &gt;&gt; direccion;</code>, ¿qué texto exacto quedará guardado finalmente en la variable <code>direccion</code>?</b></summary>

> Quedará guardada únicamente la palabra `"Calle"`. El comando `cin >>` se detiene en el primer espacio en blanco, dejando el resto de la dirección atorada en el buffer.
</details>

<details>
<summary><b>2. ¿Qué función debes utilizar para asegurarte de que una variable capture con éxito todo un párrafo tecleado por el usuario, sin importar los espacios intermedios?</b></summary>

> Debes usar `std::getline(std::cin, variable)`. Esta función lee todo el texto continuo hasta que el usuario presione la tecla Enter.
</details>

---

| ⬅️ [Anterior: Datos y entrada segura](L05_DatosYEntradaSegura.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente Módulo: Fundamental Types](../../02_FundamentalTypes/README.md) |
|---|---|---|

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>