# L05: Conversión Segura (`static_cast`)

Imagina que tienes `7` pizzas y quieres dividirlas entre `2` amigos. Matemáticamente, a cada uno le tocan `3.5` pizzas. Pero si le pides a C++ que haga esta división usando números enteros (`int`), te llevarás una sorpresa.

## La Trampa de la División Entera

Cuando divides un entero entre otro entero en C++, el resultado **siempre** será un entero. El compilador simplemente **trunca** (corta) los decimales, sin redondear.

```cpp
int pizzas{7};
int amigos{2};

// Resultado: 3 (Los decimales se descartan)
int porcion_entera{pizzas / amigos}; 
```

Incluso si intentas guardar el resultado en un `double` (un número con decimales), el daño ya está hecho:

```cpp
int pizzas{7};
int amigos{2};

// Primero hace la division entera (7/2 = 3), luego lo guarda como double (3.0)
double porcion{pizzas / amigos}; 
```

## La Solución: `static_cast`

Para que C++ haga una división decimal, al menos uno de los números involucrados debe ser un tipo de punto flotante (`double`). 

Aquí es donde entra **`static_cast`**. Es como una máquina transformadora que toma una variable de un tipo y devuelve una *copia* temporal convertida a otro tipo, sin modificar la variable original.

### Sintaxis de `static_cast`

```cpp
static_cast<NuevoTipo>(variable)
```

Aplicándolo a nuestro problema de las pizzas:

```cpp
int pizzas{7};
int amigos{2};

// Convertimos temporalmente 'pizzas' a double.
// Al dividir un double (7.0) entre un int (2), C++ hace una división decimal.
double porcion_correcta{static_cast<double>(pizzas) / amigos}; 
```

<div align="center">
  <img src="assets/l05_static_cast.gif" alt="Animación de static_cast transformando un int a double">
</div>

#### 🔍 Traducción Visual de `static_cast<T>()`:
* **Bloque original (`int 4B`):** La variable conserva su tipo y valor original en memoria (`15`).
* **Operador `static_cast<double>()`:** Genera un valor temporal promovido a 8 bytes (`15.0`) evaluado en tiempo de compilación.
* **Resultado:** Permite operaciones aritméticas mixtas exactas sin recurrir a los peligrosos C-style casts `(double)x`.

## La Muerte del "C-Style Cast"

Si buscas en internet, es posible que encuentres código antiguo que hace las conversiones así:

```cpp
// PELIGRO: Estilo C antiguo. NUNCA USAR EN ESTE CURSO.
double porcion{(double)pizzas / amigos};
```

Esto se llama "C-Style Cast" (conversión al estilo C). En C++ moderno, esto está **estrictamente prohibido**. ¿Por qué?
1. Es muy difícil de buscar en el código (buscar `()` es imposible, buscar `static_cast` es fácil).
2. Es peligroso: fuerza la conversión sin importar si es segura o no. `static_cast` le avisa al compilador que verifique si la conversión tiene sentido.

> 🧪 **Laboratorio:** Veamos cómo `static_cast` nos salva la vida. Abre el archivo [`../lab/L05_ConversionSegura.cpp`](../lab/L05_ConversionSegura.cpp).
>
> 🐞 **Demo de Bug (Opcional):** Experimenta la pérdida de datos de primera mano. Ejecuta la trampa en [`../lab/demos/D05_DivisionEnteraBug.cpp`](../lab/demos/D05_DivisionEnteraBug.cpp).
>
> 🏋️ **Ejercicio:** Es hora de arreglar un programa de calificaciones escolares. Atrévete con el reto en [`../exercise/E05_Promedio/E05_Promedio.cpp`](../exercise/E05_Promedio/E05_Promedio.cpp).

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste...

<details>
<summary><b>1. Si tienes `int x{9};` y haces `x / 2`, ¿cuál es el resultado exacto?</b></summary>

> El resultado es `4`. En la división entera, los decimales simplemente se truncan (se cortan), no se redondean.
</details>

<details>
<summary><b>2. ¿La variable original se modifica al usar `static_cast`?</b></summary>

> No. `static_cast` crea una *copia temporal* convertida. La variable original se mantiene intacta en la RAM.
</details>

| ⬅️ [Anterior: Operadores Relacionales y Lógicos](L04_OperadoresRelacionalesYLogicos.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: La Magia de auto](L06_MagiaDeAuto.md) |
|---|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
