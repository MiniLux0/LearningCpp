# L03 · Namespaces y el universo std::

> **Módulo 01 — Getting Started**

---

## ¿Por qué escribimos std::?

<div align="center">
  <img src="assets/l03_namespaces_resolution.gif" alt="Resolución de colisión de nombres usando namespaces y operador ::">
</div>

#### 🔍 Traducción Visual de Espacios de Nombres:
* **Panel Izquierdo (`main.cpp`):** Invocaciones a funciones con idéntico identificador (`dibujar()`).
* **Operador `::` (Resolución de Ámbito):** Enrutador que selecciona inequívocamente el ámbito de destino.
* **Panel Derecho (Ámbitos Aislados):** `namespace Graficos` y `namespace Audio` encapsulan sus propios símbolos, evitando colisiones de enlace (*Linker Collisions*).

En la lección anterior viste que para imprimir en la pantalla escribíamos `std::cout`. Si `cout` es el comando que imprime, ¿qué significa el `std::` que lo acompaña?

Imagina que estás en un salón de clases y gritas: *"¡Daniel, ven aquí!"*. Si hay tres personas llamadas Daniel en el salón, los tres se van a confundir. Para solucionar esto, usamos los apellidos: *"¡Daniel Martínez, ven aquí!"*.

En C++, ocurre exactamente lo mismo. Como programadores de todo el mundo escriben herramientas para C++, es muy probable que dos personas distintas creen una herramienta con el mismo nombre. Para evitar "choques de nombres" (colisiones), C++ inventó los **namespaces** (espacios de nombres). Un namespace es simplemente el "apellido" de tu código.

Cuando los creadores de C++ hicieron la Biblioteca Estándar, decidieron ponerle el apellido **`std`** (abreviatura de *standard*) a absolutamente todo. Por lo tanto, el nombre completo de la herramienta para imprimir es `std::cout`. 

Los dos puntos dobles `::` son simplemente la forma en que C++ conecta el apellido con el nombre (se lee: *"busca cout dentro del universo std"*).

---

## Las 3 formas de usar el universo std::

Escribir `std::` todo el tiempo puede ser tedioso. C++ te da opciones, pero debes elegir con cuidado porque algunas son consideradas malas prácticas en el mundo profesional.

### 1. La forma explícita (Recomendada)
Escribes `std::` cada vez que usas algo de la biblioteca estándar.
```cpp
#include <iostream>

int main() {
    std::cout << "Esta es la forma más segura.\n";
    return 0;
}
```
**Veredicto:** Es la mejor práctica. Deja tu código 100% claro y previene cualquier confusión. Úsala siempre que puedas.

### 2. La inclusión localizada (Punto medio)
Le dices al compilador que, dentro de esta función, cuando digas `cout` te refieres específicamente al de `std`.
```cpp
#include <iostream>

int main() {
    using std::cout; // Aviso local
    
    cout << "Ahora puedo usar cout sin el apellido.\n";
    return 0;
}
```
**Veredicto:** Aceptable si vas a usar `cout` muchísimas veces dentro de una misma función y quieres ahorrar espacio.

### 3. La inclusión global (Peligrosa)
Le dices al compilador: *"Abre el universo std por completo. A partir de ahora, asume que cualquier palabra que no reconozcas pertenece a std"*.
```cpp
#include <iostream>

using namespace std; // Se aplica a todo el archivo

int main() {
    cout << "Es cómodo, pero peligroso en proyectos grandes.\n";
    return 0;
}
```
**Veredicto:** ⚠️ **Evítalo**. Aunque en muchos tutoriales de internet se usa para ahorrar tiempo, abrir todo el namespace globalmente anula por completo el propósito de los apellidos. En un proyecto real, causará choques de nombres tarde o temprano.

> 🧪 **Laboratorio:** Comprueba por ti mismo qué pasa cuando omites el `std::`. Abre el archivo [`../lab/L03_NamespacesYStd.cpp`](../lab/L03_NamespacesYStd.cpp).
>
> 🏋️ **Ejercicio:** El código de este programa está roto por abusar de las malas prácticas. Arréglalo en [`../exercise/E02_Namespaces/E02_Namespaces.cpp`](../exercise/E02_Namespaces/E02_Namespaces.cpp).

---

## ✦ Resumen

- Un **namespace** actúa como el "apellido" de las herramientas de código para evitar que dos nombres iguales choquen entre sí.
- Toda la Biblioteca Estándar de C++ vive dentro del namespace `std`.
- Los dos puntos `::` conectan el namespace con la herramienta (`std::cout`).
- Escribir `using namespace std;` a nivel global es considerado una mala práctica en la industria moderna; es mejor ser explícito (`std::cout`).

---

## ✦ Preguntas de autochequeo

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques en internet — si no puedes responderlas de memoria, relee la sección correspondiente.

<details>
<summary><b>1. ¿Qué problema exacto solucionan los "namespaces" en C++? (Piensa en la analogía del salón de clases).</b></summary>

> Solucionan los "choques de nombres" (colisiones). Si dos programadores crean una herramienta distinta pero le ponen exactamente el mismo nombre, el compilador se confundiría sin un namespace (apellido) que las diferencie.
</details>

<details>
<summary><b>2. ¿Qué significa la abreviatura <code>std</code>?</b></summary>

> Es la abreviatura de *standard*. Es el "apellido" que C++ le puso a todas las herramientas oficiales que vienen incluidas de fábrica en el lenguaje.
</details>

<details>
<summary><b>3. ¿Por qué en un entorno profesional se desaconseja escribir <code>using namespace std;</code> al principio de un archivo?</b></summary>

> Porque abre todo el universo `std` de golpe, anulando el propósito de los apellidos. En proyectos grandes, esto aumenta drásticamente el riesgo de que una herramienta tuya choque con alguna de las cientos de herramientas que existen dentro de `std`.
</details>

---

| ⬅️ [Anterior: Tu primer programa](L02_TuPrimerPrograma.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Formato y comentarios](L04_FormatoSalidaComentarios.md) |
|---|---|---|

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>