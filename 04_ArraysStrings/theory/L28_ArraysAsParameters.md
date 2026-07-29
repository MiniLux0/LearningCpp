# L28 — Arrays como Parámetros: Paso por Dirección y `const`

> **Concepto central:** Cuando pasas un arreglo a una función, no se copian los elementos — se copia solo la **dirección de inicio**. La función accede a la **misma memoria** que `main()`. Por eso no necesitas `&` como con variables normales.

## Objetivos de aprendizaje

- [ ] Entender por qué los arreglos se pasan "por dirección" automáticamente
- [ ] Contrastar con el paso por valor de un `int` normal (Lección 3)
- [ ] Usar `const` para proteger un arreglo de escritura accidental
- [ ] Leer el `for` compacto con `i++` en el índice (post-incremento)
- [ ] Escribir una función que modifique un arreglo in-place (sin `const`)

---

## 1. El nombre del arreglo es la dirección de inicio

Cuando declaras `int arr[] = {1, 2, 3, 4, 5, 6, 7};`, el nombre `arr` no es "los 7 valores" — es la **dirección** de la primera casa en memoria:

```
arr → dirección de inicio (ej. casa 2000)
       [1] [2] [3] [4] [5] [6] [7]
        ↑
   arr apunta aquí
```

Cuando llamas a `sum(arr, 7)`:
- **No** se copian los 7 elementos uno por uno
- Se copia **solo esa dirección** — un solo número (4 u 8 bytes)
- La función recibe esa dirección y "camina" por las **mismas casas** que `main()`

---

## 2. Contraste con `int` normal (sin `&`)

Esto es lo que hace especial a los arreglos frente a lo que vimos en L29 (Pass by Value):

```cpp
// Variable normal — se COPIA el valor
void intentarModificar(int x) {
    x = 999;  // solo modifica la copia local
}

int main() {
    int miVariable = 42;
    intentarModificar(miVariable);
    // miVariable sigue siendo 42 — se copió el valor
    // Son dos casas de memoria distintas
}
```

| Qué se pasa | ¿Qué se copia? | ¿Modifica el original? |
|-------------|-----------------|------------------------|
| `int x` (sin `&`) | El **valor** completo | ❌ No — son dos casas distintas |
| `int arr[]` | Solo la **dirección** | ✅ Sí — misma casa de memoria |
| `int &x` (con `&`) | **Alias** (referencia) | ✅ Sí — como vimos en L29 |

> **Importante:** Con arreglos no hay copia de contenido, solo copia de la **dirección**. Por eso se comporta "como si" fuera paso por referencia, sin necesitar `&`.

---

## 3. `const` — "solo lee, no modifiques"

Como el arreglo se pasa por dirección, **sin `const` la función podría modificar tu arreglo original** sin que te des cuenta. `const` es una salvaguarda:

```cpp
int sum(const int array[], const int length) {
    // array[0] = 999;  ← ❌ ERROR de compilación: array es const
    long sum = 0;
    for (int i = 0; i < length; i++) {
        sum += array[i];
    }
    return sum;
}
```

- ✅ `const int array[]` = promesa al compilador: **"esta función solo puede leer, no escribir"**
- ❌ Si intentas romper la promesa → **error de compilación** — te protege
- Sin `const`, hacer `array[0] = 999;` dentro de `sum()` **sí modificaría** `arr` en `main()`

---

## 4. El `for` compacto con `i++` en el índice

En la lectura, `sum` usa un estilo compacto que comprime todo en una línea:

```cpp
for(int i = 0; i < length; sum += array[i++]);
```

Desglose:
```
for (inicialización;  condición;      actualización)          cuerpo;
     int i = 0;       i < length;     sum += array[i++]      ;  ← VACÍO
```

**El cuerpo del loop es el `;` vacío.** Todo el trabajo ocurre en la "actualización".

### `i++` (post-incremento) dentro de `array[i++]`

Hace **dos cosas** en un paso:
1. **Usa** el valor actual de `i` para leer → `array[i]`
2. **Después**, incrementa `i` en 1

Equivale a:
```cpp
sum += array[i];  // usa i tal como está
i++;              // luego incrementa i
```

### Recorrido paso a paso con `{1, 2, 3, 4, 5, 6, 7}`

| Vuelta | `i` al entrar | `array[i]` | `sum` después | `i` al salir |
|--------|---------------|------------|---------------|--------------|
| 1      | 0             | 1          | 0 + 1 = 1     | 1            |
| 2      | 1             | 2          | 1 + 2 = 3     | 2            |
| 3      | 2             | 3          | 3 + 3 = 6     | 3            |
| 4      | 3             | 4          | 6 + 4 = 10    | 4            |
| 5      | 4             | 5          | 10 + 5 = 15   | 5            |
| 6      | 5             | 6          | 15 + 6 = 21   | 6            |
| 7      | 6             | 7          | 21 + 7 = 28   | 7            |
| —      | 7             | —          | — (sale)      | —            |

`i` llega a 7 (`length`) → condición falsa → loop termina → `return 28`.

> **Nota:** El estilo compacto es válido pero difícil de leer. En código legible se escribe así:
> ```cpp
> for (int i = 0; i < length; i++) {
>     sum += array[i];
> }
> ```

---

## 5. Pregunta de chequeo

<details>
<summary><strong>Si quitas el <code>const</code> de <code>array[]</code> en <code>sum</code>, y dentro haces <code>array[0] = 999;</code>, ¿qué pasa con <code>arr</code> en <code>main()</code>?</strong></summary>

El primer elemento de `arr` en `main()` **queda modificado a 999**. La función está escribiendo directamente en la misma memoria que `main()` usa, porque el arreglo se pasó por dirección — no es una copia.

</details>

<details>
<summary><strong>¿Y por qué es distinto a un <code>int</code> pasado sin <code>&</code>?</strong></summary>

Con `void func(int x) { x = 999; }` se **copia el valor** a `x` — son dos casas distintas. Modificar `x` no toca la variable original. Con arreglos no hay copia de contenido, solo copia de la **dirección** — por eso se modifica el original sin necesitar `&`.

</details>

---

## 6. Ejercicio: `duplicar` — modificación in-place

> Escribe `void duplicar(int arr[], int length)` que multiplique por 2 cada elemento, modificando el original (**sin** `const`). Luego en `main()`, muestra el arreglo antes y después para comprobar que sí cambió.

```cpp
void duplicar(int arr[], int length) {
    for (int i = 0; i < length; i++) {
        arr[i] *= 2;
    }
}
```

- **Sin `const`** porque la función necesita **escribir** en el arreglo
- El cambio se refleja en `main()` porque se pasó la dirección, no una copia

---

## Resumen clave L28

| Concepto | Detalle |
|----------|---------|
| Nombre del arreglo | Es la **dirección de inicio** del bloque en memoria |
| Al pasar a función | Se copia solo la **dirección**, no los elementos |
| Sin `const` | La función **puede modificar** el arreglo original |
| Con `const` | La función **solo puede leer** — el compilador prohíbe escritura |
| `i++` post-incremento | Primero **usa** `i`, **después** incrementa |
| Contraste con `int` | `int` normal se **copia** (valor) — arreglo se pasa por **dirección** |

---

## Archivos relacionados

- [`L28_ArraysAsParameters.cpp`](../code/L28_ArraysAsParameters.cpp) — Código ejecutable con `sum()`, `duplicar()` y contraste `int`

## Navegación

| ← Anterior | Siguiente → |
|------------|-------------|
| [L27 — Array Basics](L27_ArrayBasics.md) | [L29 — Multidimensional Arrays](L29_MultidimensionalArrays.md) |
