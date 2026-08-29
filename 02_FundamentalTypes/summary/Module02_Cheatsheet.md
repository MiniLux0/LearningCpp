# Módulo 02 — Fundamental Types: Cheatsheet

Referencia rápida de los conceptos y patrones clave del Módulo 02.

---

## Resumen por lección

### L01 — Tipos primitivos y la memoria
- La RAM solo contiene ceros y unos. Un **tipo de dato** le dice al compilador cuánto espacio físico leer y cómo interpretar esos datos.
- **Tipos fundamentales:**
  - `int`: Números enteros (ej. `5`, `-10`). Ocupa típicamente 4 bytes.
  - `double`: Números con decimales (ej. `3.14`, `-0.99`). Ocupa típicamente 8 bytes.
  - `bool`: Valores booleanos, verdadero (`true`) o falso (`false`).
  - `char`: Un solo carácter (ej. `'A'`, `'?'`). Internamente guarda un número pequeño (código ASCII).
- **El operador `sizeof`:** Devuelve la cantidad exacta de bytes que un tipo de dato ocupa en la memoria.
  ```cpp
  std::cout << sizeof(double); // Imprime el tamaño en bytes
  ```

### L02 — Inicialización uniforme moderna
- **Inicialización:** Darle un valor a una variable al momento de crearla.
- En C++ moderno SIEMPRE usamos **llaves `{}`**.
- **El peligro del signo `=` (Narrowing conversion):** El estilo clásico con `=` permite el truncamiento silencioso (perder datos sin avisar).
  ```cpp
  int balas = 4.9; // Inseguro: Guarda 4 y desecha .9 sin avisar.
  ```
- **El escudo protector de las llaves:** Si intentas perder información, el compilador se negará a compilar.
  ```cpp
  int balas{4.9}; // SEGURO: Error de compilación (narrowing conversion).
  ```

### L03 — Operadores Aritméticos
- **Básicos:** Suma (`+`), Resta (`-`), Multiplicación (`*`), División (`/`).
- **Precedencia:** `*` y `/` se resuelven antes que `+` y `-`. Usa paréntesis `()` para forzar el orden, ej. `(2 + 3) * 4`.
- **Trampa de la división entera:** Dividir dos enteros SIEMPRE da un entero y desecha los decimales.
  ```cpp
  int porciones{7 / 2}; // Da 3. Pierde el .5
  ```
- Para obtener decimales, al menos uno debe ser `double` (ej. `7.0 / 2`).
- **Módulo (`%`):** Devuelve el **residuo** de una división entera. Útil para saber si es par (`x % 2 == 0`) o múltiplo.

### L04 — Operadores Relacionales y Lógicos
- Se utilizan para hacer preguntas y devuelven un `bool` (`true` o `false`).
- **Relacionales (Comparación):**
  - Igual a: `==` (OJO: no confundir con el `=` de asignación).
  - Diferente de: `!=`
  - Mayor que: `>` / Menor que: `<`
  - Mayor o igual que: `>=` / Menor o igual que: `<=`
- **Lógicos (Combinar preguntas):**
  - **AND (`&&`):** Todo debe ser verdadero. (Ej. `edad >= 18 && tiene_ticket`).
  - **OR (`||`):** Al menos uno debe ser verdadero. (Ej. `es_vip || tiene_pase_libre`).
  - **NOT (`!`):** Invierte el resultado. Lo verdadero lo hace falso y viceversa. (Ej. `!esta_lloviendo`).

### L05 — Conversión Segura (`static_cast`)
- La división de dos enteros causa división entera, truncando silenciosamente los decimales (ej. `5 / 2 = 2`).
- Usa `static_cast<T>(var)` para pedirle al compilador que cree temporalmente una copia de otro tipo y fuerce la división decimal.
  ```cpp
  int a{5};
  double exacto{static_cast<double>(a) / 2}; // Da 2.5
  ```
- **Prohibido:** El C-style cast `(double)a` es peligroso y no se utiliza en C++ moderno.

### L06 — La Magia de `auto`
- Le pide al compilador que deduzca el tipo de dato por nosotros, pero **el tipo fijado nunca cambia** (C++ no es dinámico como Python).
- **El Peligro (Amnesia):** Oculta qué tipo de variable estamos manejando, causando bugs de lectura y división.
- **Regla de Oro:** Úsalo SOLAMENTE cuando el tipo sea dolorosamente obvio en la misma línea (como al aplicar un `static_cast`).

### L07 — Mini-proyecto "Split the Bill"
- Síntesis de todo el Módulo 02, logrando validaciones lógicas y cálculos exactos sin necesidad de saber usar bloques condicionales (`if`).

---

## Patrones clave del Módulo 02

```cpp
#include <iostream>

int main() {
    // 1. Inicialización uniforme siempre (tipos primitivos)
    int edad{18};
    double dinero_bolsillo{25.50};
    char inicial_nombre{'M'};
    bool es_estudiante{true};

    // 2. Comprobar tamaños de memoria física
    std::cout << "Memoria usada por int: " << sizeof(int) << " bytes\n";

    // 3. Evitar la división entera si buscamos exactitud
    double precio_por_amigo{dinero_bolsillo / 2}; // 25.50 es double, esto es seguro.

    // 4. Operadores relacionales y lógicos
    bool puede_entrar{ (edad >= 18) || es_estudiante };
    bool tiene_dinero_suficiente{ dinero_bolsillo >= 15.0 };
    bool acceso_concedido{ puede_entrar && tiene_dinero_suficiente };

    std::cout << "¿Puede entrar al cine? " << acceso_concedido << "\n";

    return 0;
}
```

---

## Checklist antes de pasar al Módulo 03

- [ ] Entiendo que un `double` requiere físicamente más RAM que un `int`.
- [ ] Inicializo TODAS mis variables usando llaves `{}`.
- [ ] Entiendo qué es una conversión de estrechamiento (narrowing) y cómo las llaves me protegen.
- [ ] Sé la diferencia entre el operador `=` (asignación/peligroso) y `==` (comparación).
- [ ] Entiendo por qué `5 / 2` da `2` en C++ y sé usar `static_cast<double>()` para solucionarlo sin perder precisión.
- [ ] Sé usar `&&` y `||` para evaluar múltiples condiciones a la vez.
- [ ] Comprendo que `auto` no convierte a C++ en un lenguaje dinámico y aplico la "Regla de Oro" contra la amnesia.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
