# L24 — Return Values (Valores de Retorno)

> **Concepto central**: Una función devuelve **exactamente un valor** cuyo tipo debe coincidir con la declaración.

---

## 🎯 Objetivos de aprendizaje

- [ ] Entender la regla básica: tipo de retorno = tipo del valor en `return`
- [ ] Saber cuándo y cómo usar `void`
- [ ] Entender que `void` no es tipo de variable
- [ ] Usar *early return* (return anticipado) como *guard clause*
- [ ] Comprender *function overloading* (sobrecarga por parámetros)
- [ ] Resolver promoción de `char` en resolución de sobrecarga

---

## 1. Regla básica: el tipo debe coincidir

```cpp
int foo() {
    return "hello";  // ❌ ERROR: "hello" es const char*, no int
}

char* foo() {
    return "hello";  // ✅ OK: coincide char*
}
```

| Declaración | `return` válido | `return` inválido |
|-------------|-----------------|-------------------|
| `int f()` | `42`, `x + y` | `"hola"`, `3.14` |
| `double f()` | `3.14`, `42` (promoción) | `"hola"` |
| `string f()` | `"hola"`, `s` | `42` |
| `void f()` | `return;` (solo salida) | `return 5;` ❌ |

> **Regla**: *El tipo de lo que retornas debe coincidir con el tipo de retorno declarado.*

---

## 2. `void` — cuando no retornas nada

```cpp
void printNumber(int num) {
    cout << "number is " << num << endl;
    // return;  // opcional en void
    // return 5; // ❌ ERROR: void no puede retornar valor
}

int main() {
    printNumber(4);  // number is 4
    return 0;
}
```

### ⚠️ Trampa clásica: `void` no es tipo de variable

```cpp
int main() {
    void x;  // ❌ ERROR: void solo existe como tipo de RETORNO
    return 0;
}
```

> `void` significa "esta función no produce valor" — no "un valor vacío".

---

## 3. Return anticipado (Early Return) — Guard Clauses

El `return` sale **inmediatamente** de la función, sin importar código posterior.

```cpp
void printNumberIfEven(int num) {
    if (num % 2 == 1) {
        cout << "odd number" << endl;
        return;  // sale AQUÍ si es impar
    }
    cout << "even number; number is " << num << endl;
}
```

**Patrón Guard Clause**: valida precondiciones al inicio, retorna temprano si fallan.

```cpp
double divideSeguro(double a, double b) {
    if (b == 0.0) return 0.0;  // guard clause
    return a / b;
}
```

---

## 4. Function Overloading (Sobrecarga)

Mismo nombre, **distintos parámetros** (tipo o cantidad). El compilador elige según los **argumentos** de la llamada.

```cpp
// Sobrecarga por TIPO
void printOnNewLine(int x) {
    cout << "Integer: " << x << endl;
}
void printOnNewLine(char* x) {
    cout << "String: " << x << endl;
}

// Sobrecarga por CANTIDAD
void printOnNewLine(int x) {
    cout << "1 integer: " << x << endl;
}
void printOnNewLine(int x, int y) {
    cout << "2 integers: " << x << " and " << y << endl;
}
```

| Llamada | Resuelve a |
|---------|------------|
| `printOnNewLine(3)` | `void printOnNewLine(int)` |
| `printOnNewLine("hello")` | `void printOnNewLine(char*)` |
| `printOnNewLine(10)` | `void printOnNewLine(int)` (1 arg) |
| `printOnNewLine(10, 20)` | `void printOnNewLine(int, int)` (2 args) |

> **El tipo de retorno NO diferencia sobrecargas** — solo los parámetros.

---

## 5. Pregunta de chequeo: Promoción de `char`

```cpp
void mostrar(int x)    { cout << "int: " << x << endl; }
void mostrar(double x) { cout << "double: " << x << endl; }

mostrar(5);    // → int: 5     (coincidencia exacta int)
mostrar(5.0);  // → double: 5  (coincidencia exacta double)
mostrar('A');  // → int: 65    (char se PROMUEVE a int, NO a double)
```

### ¿Por qué `char` → `int` y no `double`?

| Conversión | Tipo | Costo |
|------------|------|-------|
| `char` → `int` | **Promoción integral** | Barata (preferida) |
| `char` → `double` | Conversión flotante | Más cara |

> En C++, `char` es un tipo entero pequeño. Su promoción natural es a `int` (su valor ASCII). El compilador elige la conversión **más barata/preferida**.

---

## 📋 Resumen clave L28

| Concepto | Regla |
|----------|-------|
| Tipo retorno | Debe coincidir exactamente con `return` |
| `void` | Sin retorno — solo `return;` |
| `void` variable | ❌ Prohibido |
| Early return | Sale ya — útil para guard clauses |
| Overloading | Mismo nombre, **distintos parámetros** |
| Retorno en overload | **No cuenta** para diferenciar |
| `char` en overload | Se promueve a `int` (no `double`) |

---

## 🔗 Archivos relacionados

- [`../L24_ReturnValues.cpp`](../L24_ReturnValues.cpp) — Implementación completa con ejemplos ejecutables

## 🔗 Navegación

| ← Anterior | Siguiente → |
|------------|-------------|
| [L23 — Functions](L23_Functions.md) | [L25 — Function Parameters](L25_FunctionParameters.md) |