# L04 · Operadores relacionales y lógicos

> **Módulo 02 — Fundamental Types**

---

## La computadora hace preguntas

En la vida real, tomas decisiones constantemente comparando cosas: ¿tengo *más* de 18 años para entrar al cine? ¿mi saldo es *igual* al precio del café? 

En programación, necesitamos que la computadora también haga estas preguntas. Para ello usamos los **operadores relacionales**. Su único trabajo es comparar dos valores y responder con un simple "sí" o "no". 

- `==` (Igual a): Pregunta "¿son idénticos?".
- `!=` (Distinto de): Pregunta "¿son diferentes?".
- `<` (Menor que): Pregunta "¿el primero es más pequeño?".
- `>` (Mayor que): Pregunta "¿el primero es más grande?".
- `<=` (Menor o igual que).
- `>=` (Mayor o igual que).

Imagina que comparas el nivel de agua en dos vasos. Si el vaso A tiene 200ml y el vaso B tiene 150ml, la pregunta `A > B` responderá que "sí".

## La respuesta de la máquina: el tipo bool

Cuando haces una pregunta matemática como `5 + 3`, la respuesta es un número (`8`). Pero cuando haces una pregunta relacional como `5 > 3`, la respuesta no es un número normal; la respuesta es "verdadero" o "falso".

¿Recuerdas el tipo `bool` de nuestra primera lección? Fue creado exactamente para guardar el resultado de estas comparaciones.

```cpp
int edad_juan{15};
int edad_requerida{18};

// La computadora evalúa la comparación y guarda el resultado
bool puede_entrar{edad_juan >= edad_requerida}; // Guarda false
```

*Nota interna:* Para la memoria RAM, "verdadero" se guarda físicamente como un `1` y "falso" como un `0`. Sin embargo, nosotros escribimos y leemos `true` o `false` en el código para que tenga sentido humano. De aquí en adelante, trabajaremos siempre con `true` y `false`.

---

## La trampa más famosa de la programación: `=` vs `==`

Existe un error de novato (e incluso de veterano) que es increíblemente peligroso porque es silencioso. Observa la diferencia entre estos dos símbolos:

- `=` (Un solo igual) es una **orden**. Le dice a la máquina: "Destruye lo que haya en la caja y mete este nuevo valor".
- `==` (Doble igual) es una **pregunta**. Le dice a la máquina: "¿El valor de la caja es idéntico a este otro?".

Si confundes la pregunta con la orden al tomar una decisión, C++ obedecerá la orden en silencio:

```cpp
int x{10};

// ¡CUIDADO! Esto no pregunta si x es 5. 
// Esto destruye el 10, guarda un 5 dentro de x, y C++ lo asume como un éxito (verdadero).
if (x = 5) { 
    // ...
}

// ESTO es lo correcto. Una pregunta inofensiva que devuelve falso.
if (x == 5) {
    // ...
}
```

---

## Combinando preguntas: Operadores lógicos

A veces, una sola pregunta no basta. Piensa en salir a la calle: "Necesito llevar paraguas **Y** tener tiempo". Ambas condiciones tienen que ser ciertas a la vez. O en una tienda: "Puedo pagar con tarjeta **O** en efectivo". Basta con que una de las dos sea cierta.

En C++ usamos los **operadores lógicos** para encadenar preguntas:

> 💡 **Nota de la industria:** Aunque en español los llamaríamos "Y", "O" y "NO", en el mundo del desarrollo de software todo el mundo se refiere a ellos por su nombre en inglés: **AND**, **OR** y **NOT**. Es un estándar universal que mantendremos durante el resto del curso.

### 1. El operador AND (`&&`)
Ambas condiciones deben ser ciertas. Si una sola falla, todo es falso.
```cpp
bool tiene_dinero{true};
bool tiene_tiempo{false};
bool va_al_cine{tiene_dinero && tiene_tiempo}; // Resultado: false
```

### 2. El operador OR (`||`)
Con que una sola condición sea cierta, todo el resultado es verdadero. Solo es falso si *todas* las opciones fallan.
```cpp
bool paga_efectivo{false};
bool paga_tarjeta{true};
bool compra_exitosa{paga_efectivo || paga_tarjeta}; // Resultado: true
```

### 3. El operador NOT (`!`)
Es un rebelde que invierte la respuesta. Si era verdadero, lo vuelve falso.
```cpp
bool llueve{true};
bool dia_soleado{!llueve}; // Invierte el true y guarda false
```

<div align="center">
  <img src="assets/l04_operadores_logicos.gif" alt="Animación visualizando las compuertas lógicas &&, ||, !">
</div>

#### 🔍 Traducción Visual de Lógica Booleana:
* **Compuerta AND (`&&`):** Evalúa ambas señales booleanas; requiere que ambas sean `true` para emitir señal de paso.
* **Operador de Igualdad (`==`):** Inspecciona el valor en memoria sin mutar la celda, a diferencia de la asignación destructiva (`=`).
* **Insignia de Seguridad:** Previene errores lógicos de bifurcación accidental en sentencias condicionales.

---

> 🧪 **Laboratorio:** Juega con las reglas del club VIP y observa de primera mano la trampa mortal del signo igual. Abre el archivo [`../lab/L04_OperadoresRelacionalesYLogicos.cpp`](../lab/L04_OperadoresRelacionalesYLogicos.cpp).
>
> 🏋️ **Ejercicio:** Eres el responsable del Sistema de Acceso VIP. Repara las compuertas lógicas y usa el doble igual `==` correctamente en [`../exercise/E04_SistemaDeAcceso/E04_SistemaDeAcceso.cpp`](../exercise/E04_SistemaDeAcceso/E04_SistemaDeAcceso.cpp).

---

## ✦ Resumen

- Los **operadores relacionales** (`==`, `<`, `>`, etc.) sirven para comparar valores.
- El resultado de una comparación siempre es un valor de tipo **`bool`** (`true` o `false`).
- Confundir la asignación `=` con la comparación `==` es un error silencioso muy común.
- Los **operadores lógicos** (`&&`, `||`, `!`) nos permiten combinar múltiples comparaciones o invertir sus resultados.

---

## ✦ Preguntas de autochequeo

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques en internet — si no puedes responderlas de memoria, relee la sección correspondiente.

<details>
<summary><b>1. Si tienes el código <code>bool resultado{10 == 15};</code>, ¿qué tipo de dato se almacena y cuál es su valor interno para la memoria?</b></summary>

> Se almacena un tipo `bool`. El valor evaluado es `false` (falso), lo que internamente la memoria RAM guarda como un `0`.
</details>

<details>
<summary><b>2. Estás leyendo el código de un amigo y ves la instrucción <code>if (vidas = 0)</code>. ¿Por qué esto es un bug grave y qué hace exactamente C++ al leerlo?</b></summary>

> Es un bug porque está usando un solo igual (`=`), que es una orden de asignación, en lugar de un doble igual (`==`), que es una pregunta de comparación. C++ no preguntará cuántas vidas tiene; en su lugar, destruirá el valor actual de `vidas`, lo reemplazará por un `0` en silencio y evaluará la orden, arruinando los datos del programa.
</details>

<details>
<summary><b>3. En una atracción mecánica, los pasajeros deben medir más de 120 cm O estar acompañados por un adulto. ¿Qué operador lógico usarías para programar esta regla y por qué?</b></summary>

> Usaría el operador O (`||`). Este operador hace que el resultado final sea verdadero si al menos *una* de las dos condiciones se cumple, que es exactamente lo que requiere la regla de la atracción.
</details>

---

| ⬅️ [Anterior: Operadores aritméticos](L03_OperadoresAritmeticos.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Conversión segura](L05_ConversionSegura.md) |
|---|---|---|

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
