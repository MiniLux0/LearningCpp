# Ejercicios de Subrutinas - C++

---

## Ejercicio A — Múltiples retornos + lógica algorítmica

Escribe una función:

```cpp
void estadisticasArreglo(int arr[], int tam, int &mayor, int &menor, double &promedio);
```

**Requisitos:**
- Recorra un arreglo de enteros
- Devuelva por referencia: el valor mayor, el menor, y el promedio
- Escribe el prototipo antes de `main()` y la implementación después
- Prueba con un arreglo de al menos 5 elementos

---

## Ejercicio B — Overloading con lógica distinta según tipo

Crea dos versiones de una función `esMayor`:

```cpp
bool esMayor(int a, int b);
bool esMayor(double a, double b, double tolerancia);
```

**Requisitos:**
- Versión `int`: compara si `a > b`
- Versión `double`: devuelve `true` solo si `a` es mayor que `b` por más del margen `tolerancia`
- Piensa por qué comparar doubles con `==` o `>` directo puede ser problemático
- Prueba ambas versiones en `main()`

---

## Ejercicio C — Pass by reference para modificar estado, sin devolver nada explícito

Escribe una función:

```cpp
void normalizarArreglo(double arr[], int tam);
```

**Requisitos:**
- Modifique el arreglo *in-place* dividiendo cada elemento entre el valor máximo del arreglo
- Resultado: todos los elementos quedan entre 0 y 1
- Pista: el arreglo ya se comporta como puntero/referencia por su naturaleza (no necesitas `&` en el parámetro)
- Esto es un adelanto de la Lección 4 (Arrays)

---