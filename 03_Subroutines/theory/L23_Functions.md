# L23 — Functions: Why and Anatomy

> **Concepto central**: Extraer código repetido a **funciones reutilizables** con nombre, parámetros y retorno.

---

## 🎯 Por qué funciones

| Problema *copy-paste* | Solución: Función |
|------------------------|-------------------|
| Bug en una copia → arreglar en **todas** | Bug en **un lugar** |
| Código repetido = ilegible | `raiseToPower(3,4)` se **lee solo** |
| Otro programador reimplementa | Otro programador **reutiliza** |

---

## 🔬 Anatomía de una función

```cpp
int raiseToPower(int base, int exponent)  // ← SIGNATURE (firma)
{                                          // ← BODY (cuerpo)
    int result = 1;
    for (int i = 0; i < exponent; ++i) {
        result = result * base;
    }
    return result;                         // ← RETURN statement
}
```

| Parte | Qué es | Ejemplo |
|-------|--------|---------|
| **Return type** | Tipo que devuelve | `int` |
| **Name** | Identificador | `raiseToPower` |
| **Parameters** | Entradas (tipo + nombre) | `int base, int exponent` |
| **Body** | Implementación | `{ ... }` |
| **Return** | Valor de salida + salida inmediata | `return result;` |

> ⚠️ **El orden de parámetros importa**: `raiseToPower(2,3) = 8` pero `raiseToPower(3,2) = 9`

---

## 🧪 Pregunta de chequeo

```cpp
int resta(int a, int b) { return a - b; }
```

| Llamada | Resultado | Por qué |
|---------|-----------|---------|
| `resta(10, 3)` | `7` | `10 - 3` |
| `resta(3, 10)` | `-7` | `3 - 10` |

**El orden de argumentos define semántica** — no son intercambiables aunque sean mismo tipo.

---

## 📝 Código de referencia

Ver [`L23_Functions.cpp`](../L23_Functions.cpp) — incluye:
- `raiseToPower` reutilizable
- Demo de orden de parámetros
- `resta` con ambas llamadas

---

## 🔗 Archivos relacionados

- [`../L23_Functions.cpp`](../L23_Functions.cpp) — Implementación completa con ejemplos ejecutables

## 🔗 Navegación

| ← Anterior | Siguiente → |
|------------|-------------|
| [L22 — Switch](../../02_BasicSyntax/L22_Switch.cpp) | [L24 — Return Values](L24_ReturnValues.md) |