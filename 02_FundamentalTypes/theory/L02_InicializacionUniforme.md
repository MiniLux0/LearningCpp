# L02 · Inicialización uniforme moderna

> **Módulo 02 — Fundamental Types**

---

## Dar vida a una variable

En la lección anterior vimos que los tipos de datos le dicen a la computadora cuánto espacio reservar. Ahora necesitamos poner un valor dentro de ese espacio. A este proceso se le llama **inicialización**.

En C++ moderno (desde C++11 en adelante), existe una forma estándar, segura y universal de inicializar cualquier cosa. Se llama **inicialización uniforme**, y utiliza las llaves `{}`.

La sintaxis es simple y directa: primero el tipo, luego el nombre que inventes, y finalmente el valor entre llaves.

```cpp
int edad{25};
double temperatura{36.5};
bool esta_lloviendo{false};
```

Esta es la forma en la que escribiremos código a lo largo de todo el curso. No obstante, si miras tutoriales antiguos en internet, verás que la inmensa mayoría de la gente usa el signo de igual (`=`), así: `int edad = 25;`. 

Si el signo `=` funciona, ¿por qué C++ se tomó la molestia de inventar las llaves `{}`? La respuesta tiene que ver con un problema grave e invisible del que las llaves te protegen.

---

## El peligro silencioso: Pérdida de datos (Narrowing)

Imagina que estás programando un videojuego y tienes una variable entera (`int`) para las balas restantes de un jugador. Por un error en una fórmula matemática, intentas guardarle un número con decimales (un `double`).

Si usas el estilo clásico con `=`, mira lo que ocurre:

```cpp
// Estilo clásico (inseguro)
int balas_restantes = 4.9; 
```

¿Qué hace C++ aquí? En lugar de avisarte que estás intentando meter un decimal en una caja de enteros, **C++ obedece en silencio**. Corta el `.9`, lo tira a la basura, y guarda el `4`. 

A esto se le llama **conversión de estrechamiento** (o *narrowing conversion* en inglés). Es increíblemente peligroso porque ocurre sin ninguna advertencia, alterando los datos de tu programa y causando bugs que son muy difíciles de rastrear, ya que el código parece correcto a simple vista.

<div align="center">
  <img src="assets/l02_narrowing_conversion.gif" alt="Comparación entre inicialización con = y con {} en C++">
</div>

#### 🔍 Traducción Visual de la Protección con `{}`:
* **Estilo clásico (`=`):** Permite que un `double` (`3.99`) se trunque a `3` silenciosamente perdiendo la fracción decimal.
* **Inicialización Uniforme (`{}`):** El compilador `g++` bloquea la asignación y aborta la compilación con un error `narrowing conversion`.
* **Beneficio:** Evita errores lógicos indetectables y pérdidas de precisión en tiempo de ejecución.

---

## El escudo protector de C++ moderno

C++ moderno introdujo las llaves `{}` precisamente para solucionar este problema. La inicialización uniforme es estricta: **no permite la pérdida de datos silenciosa**.

Si intentas cometer exactamente el mismo error usando las llaves, mira lo que pasa:

```cpp
// C++ moderno (seguro)
int balas_restantes{4.9}; 
```

Cuando intentes compilar esto, el compilador **se negará a crear el ejecutable** y te lanzará un error de compilación:

> `error: narrowing conversion of '4.9' from 'double' to 'int'`

> 🧪 **Laboratorio:** Ve a la carpeta de demostraciones de errores para compilar esto y ver el error protector con tus propios ojos. Abre [`../lab/demos/D02_NarrowingBug.cpp`](../lab/demos/D02_NarrowingBug.cpp).

En programación, un error de compilación es tu mejor amigo. Significa que la herramienta detectó un problema en tu lógica antes de que el programa siquiera llegara a ejecutarse. Las llaves `{}` actúan como un escudo protector que obliga a que el dato que quieres guardar encaje perfectamente en el tipo de memoria que reservaste.

---

> 🧪 **Laboratorio:** Comprueba la diferencia entre el truncamiento silencioso y la sintaxis moderna correcta ejecutando el archivo [`../lab/L02_InicializacionUniforme.cpp`](../lab/L02_InicializacionUniforme.cpp).
>
> 🏋️ **Ejercicio:** Es hora de proteger tu código contra la pérdida de datos. Resuelve el reto de Narrowing en [`../exercise/E02_ProteccionNarrowing/E02_ProteccionNarrowing.cpp`](../exercise/E02_ProteccionNarrowing/E02_ProteccionNarrowing.cpp).

---

## ✦ Resumen

- **Inicialización** es el proceso de darle un valor a una variable en el momento en que se crea.
- En C++ moderno, la única forma recomendada de inicializar variables es la **inicialización uniforme** usando llaves `{}`.
- Usar el signo `=` (estilo clásico) permite conversiones de estrechamiento (*narrowing*), donde se pierden datos (como decimales) sin que el compilador te avise.
- Las llaves `{}` son estrictas: si el valor no cabe sin perder información, detienen la compilación y te salvan de un bug silencioso.

---

## ✦ Preguntas de autochequeo

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques en internet — si no puedes responderlas de memoria, relee la sección correspondiente.

<details>
<summary><b>1. Si declaras <code>int x = 8.5;</code>, ¿qué valor se guarda realmente en <code>x</code> y cómo se llama este fenómeno?</b></summary>

> Se guarda el valor `8`. El compilador corta el decimal `.5` y lo desecha sin avisar. A este fenómeno peligroso se le llama **conversión de estrechamiento** (o *narrowing conversion*).
</details>

<details>
<summary><b>2. ¿Qué ventaja principal ofrece escribir <code>int x{8.5};</code> frente a usar el signo <code>=</code> en el mismo caso?</b></summary>

> La inicialización uniforme con llaves `{}` es estricta y actúa como un escudo. En lugar de obedecer en silencio y perder datos, el compilador arrojará un error de compilación negándose a crear el ejecutable, salvándote de un bug silencioso.
</details>

<details>
<summary><b>3. Sabiendo cómo actúan las llaves <code>{}</code>, ¿el compilador te dejaría hacer <code>double temperatura{36};</code> (guardar un entero en un decimal)? Piensa en si hay o no pérdida de información en este caso específico.</b></summary>

> Sí, te dejaría hacerlo sin problema. El escudo de las llaves `{}` solo detiene la compilación cuando hay pérdida de información (*narrowing*). Guardar un entero como 36 dentro de un `double` no pierde datos (se convierte en 36.0), ya que el `double` tiene capacidad de sobra.
</details>

---

| ⬅️ [Anterior: Tipos Primitivos](L01_TiposPrimitivos.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Operadores aritméticos](L03_OperadoresAritmeticos.md) |
|---|---|---|

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
