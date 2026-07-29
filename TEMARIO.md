# Temario — Learning C++

> Plan de aprendizaje personal siguiendo **MIT 6.096 Introduction to C++ (IAP 2011)**.
> Complementado con el curso de **John Purcell** (Udemy) y recursos propios.

---

## Visión General del Curso

| Dato | Valor |
|------|-------|
| **Base académica** | MIT 6.096 — 10 lecturas, 4 problem sets, 1 proyecto final |
| **Complemento** | John Purcell — C++ Tutorial for Complete Beginners (Udemy) |
| **Estándar** | C++17 (`-std=c++17`) |
| **Compilador** | GCC 15.2.0 (WinLibs) |
| **Lecciones totales** | L01 – L60 (8 secciones) |

---

## Mapa de Secciones

| # | Carpeta | MIT Lecture | Lecciones | Estado |
|---|---------|-------------|-----------|:------:|
| 01 | `01_GettingStarted` | Lecture 1 — Introduction | L01 – L05 | ✅ |
| 02 | `02_BasicSyntax` | Lecture 2 — Flow of Control | L06 – L22 | 🔄 |
| 03 | `03_Subroutines` | Lecture 3 — Functions | L23 – L26 | ✅ |
| 04 | `04_ArraysStrings` | Lecture 4 — Arrays and Strings | L27 – L30 | 🔄 |
| 05 | `05_Pointers` | Lecture 5 — Pointers | L31 – L38 | ⬜ |
| 06 | `06_Classes` | Lecture 6 — Classes | L39 – L44 | ⬜ |
| 07 | `07_OOP` | Lecture 7 — OOP & Inheritance | L45 – L52 | ⬜ |
| 08 | `08_MemoryManagement` | Lecture 8 — Memory Management | L53 – L60 | ⬜ |

> [!NOTE]
> Las Lectures 9 (Advanced Topics I: Templates, STL, Operator Overloading) y 10 (Advanced Topics II: File I/O, Enums, Exceptions, Friend, Casting) están fuera del alcance actual. Los PDFs están en `files/lectures/` como referencia.

---

## Temario Detallado

---

### 📘 Section 01 — Getting Started (L01–L05) · MIT Lecture 1 ✅

> **Objetivo**: Entender qué es C++, el proceso de compilación, y escribir el primer programa.

| # | Lección | Temas |
|---|---------|-------|
| L01 | Introducing C++ | Qué es C++, historia (Bjarne Stroustrup, 1979), lenguajes compilados vs interpretados, por qué C++ (velocidad, control de hardware, portabilidad) |
| L02 | Screen Resolution | Píxeles, resolución, cómo las computadoras representan todo como números |
| L03 | Setup and Installation | Compilador (GCC), IDE (VSCode), primera compilación |
| L04 | Hello World | `#include <iostream>`, `main()`, `cout <<`, `return 0`, tokens (keywords, identifiers, literals, operators, punctuation, whitespace), comments (`//`, `/* */`), namespaces (`std::`), escape sequences (`\n`, `\t`, `\\`) |
| L05 | Outputting Text | Encadenamiento de `<<`, múltiples `cout`, formato de salida |

**Conceptos MIT Lecture 1:**
- Pipeline de compilación: Source → Preprocessor → Compiler → Object File → Linker → Executable
- 6 categorías de tokens
- Tipos de datos primitivos: `char` (1B), `int` (4B), `bool` (1B), `double` (8B)
- Variables: declaración, inicialización, naming rules
- Input con `cin >>` (dirección de datos: `>>` = terminal→variable, `<<` = variable→terminal)
- Debugging: errores de compilación vs errores de runtime

**📄 PDF**: [Lecture01_Introduction.pdf](files/lectures/Lecture01_Introduction.pdf)
**📋 Assignment**: [Assignment01.pdf](files/assignments/Assignment01.pdf) — Hello World, scope, statistics, primes, ternary, factorial

---

### 📘 Section 02 — Basic Syntax (L06–L22) · MIT Lecture 2 🔄

> **Objetivo**: Dominar variables, tipos, operadores, condicionales y loops.

| # | Lección | Temas |
|---|---------|-------|
| L06 | Variables | `int`, `double`, `char`, `bool`, `string`, declaración e inicialización, operadores aritméticos (`+`, `-`, `*`, `/`, `%`), incremento (`++`, `--`) |
| L07 | Strings | `#include <string>`, concatenación con `+`, `string` vs `char*` |
| L08 | User Input | `cin >>`, lectura de múltiples variables |
| L09 | Binary Numbers | Sistema binario (base 2), bits y bytes, representación en memoria, overflow |
| L10 | Integer Types | `short`, `int`, `long`, `long long`, `sizeof`, `<climits>` (INT_MAX, INT_MIN) |
| L11 | Floating Point Types | `float` (4B) vs `double` (8B), `fixed`, `setprecision`, notación científica, error de precisión |
| L12 | Char and Bool | `char` como entero pequeño (ASCII), casting `(int)`, `(char)`, aritmética ASCII, `bool` |
| L13 | If | `if (condición) { ... }`, operadores relacionales (`>`, `<`, `>=`, `<=`, `==`, `!=`) |
| L14 | If-Else | `if-else`, mutuamente exclusivo, escape de comillas `\"` |
| L15 | If-Else If-Else | Cadena de condiciones, operadores lógicos (`&&`, `\|\|`, `!`) |
| L16 | Comparing Floats | Por qué `==` falla con floats, solución con epsilon (`abs(a-b) < epsilon`), `<cmath>` |
| L17 | Conditions | Operadores lógicos en profundidad, tablas de verdad, evaluación non-zero = true |
| L18 | While Loops | `while (condición) { ... }`, actualización de variable, prevención de loops infinitos |
| L19 | Do-While Loops | `do { ... } while (condición);`, ejecución garantizada mínimo 1 vez, menú interactivo |
| L20 | For Loops | `for (init; cond; incr)`, equivalencia con while, loops anidados, patrones de impresión |
| L21 | Break and Continue | `break` (salir del loop), `continue` (saltar iteración) |
| L22 | Switch | `switch(expr) { case: ... break; default: }`, fall-through, cuándo usar vs if-else |

**Conceptos MIT Lecture 2:**
- Operadores relacionales y lógicos (tablas de verdad AND, OR, NOT)
- Regla C++: `0` = false, cualquier non-zero = true
- `switch-case` con `break` y `default`
- `do-while` requiere `{}` obligatorios y `;` al final
- Loops anidados y condicionales anidados

**📄 PDF**: [Lecture02_FlowOfControl.pdf](files/lectures/Lecture02_FlowOfControl.pdf)
**📋 Assignment**: [Assignment01.pdf](files/assignments/Assignment01.pdf) — Scope, statistics, primes, ternary operator, factorial debugging

---

### 📘 Section 03 — Subroutines (L23–L26) · MIT Lecture 3 ✅

> **Objetivo**: Funciones reutilizables, parámetros, prototipos y organización de código.

| # | Lección | Temas |
|---|---------|-------|
| L23 | Functions | Anatomía: return type, name, parameters, body, `return`. Por qué funciones (readability, maintainability, reuse). Orden de parámetros importa |
| L24 | Return Values | Regla: tipo retorno = tipo `return`. `void` (sin retorno, no es tipo de variable). Early return / guard clauses. Function overloading (por tipo y cantidad). Promoción `char` → `int` |
| L25 | Function Parameters | Pass by value (default, copia) vs pass by reference (`&`, alias). `swap` como caso clásico. Output parameters (retornar múltiples valores). `int&` vs `int*` (referencia vs puntero) |
| L26 | Headers and Prototypes | Compilador de una pasada (arriba→abajo). Function prototypes (declaraciones adelantadas). Recursión mutua. Patrón `.h` + `.cpp`. Distribución de librerías: `.h` + `.dll/.so` |

**Conceptos MIT Lecture 3:**
- Recursión: caso base + paso recursivo (Fibonacci)
- Variable scope: global, function, block (loops/if)
- Out-of-scope errors y cómo arreglarlos
- `<cmath>` — `pow()`, `sqrt()` como ejemplo de librería estándar
- Linker: resuelve prototipos contra implementaciones compiladas

**📄 PDF**: [Lecture03_Functions.pdf](files/lectures/Lecture03_Functions.pdf)
**📋 Assignment**: [Assignment02.pdf](files/assignments/Assignment02.pdf) — Default args, function fixing, sums overloading, Monte Carlo π, array operations, pointers & strings

---

### 📘 Section 04 — Arrays & Strings (L27–L30) · MIT Lecture 4 🔄

> **Objetivo**: Arrays estáticos, multidimensionales, C-strings y sus funciones de librería.

| # | Lección | Temas |
|---|---------|-------|
| L27 | Array Basics | Memoria contigua, 3 formas de inicializar, acceso 0-based, `sizeof(arr)/sizeof(arr[0])`, inicialización parcial (resto = 0), recorrido con `for` y range-based `for`, peligro de acceso fuera de rango |
| L28 | Arrays as Parameters | Nombre del array = dirección de inicio. Paso por dirección automático (sin `&`). `const` para proteger de escritura. `for` compacto con `i++` post-incremento. Contraste con `int` normal (copia vs dirección) |
| L29 | Multidimensional Arrays | Arrays 2D y 3D, inicialización (parcial, plana, anidada). `sizeof` para filas/columnas. Paso a funciones: `int m[][COLS]` (primera dimensión omitible). Array de C-strings (`char nombres[3][20]`) |
| L30 | C-Strings | `char[]` terminado en `'\0'`. `<cctype>`: `isalpha`, `isupper`, `tolower`, `toupper`, `isdigit`, `ispunct`. `<cstring>`: `strcpy`, `strcat`, `strlen`, `strcmp`, `strchr`. `cin.getline()`. Normalizar y verificar palíndromo. Contar palabras |

**Conceptos MIT Lecture 4:**
- Arrays SIEMPRE se pasan por referencia (dirección, no copia)
- `const int array[]` protege de modificación accidental
- Arrays multidimensionales: layout secuencial en memoria, regla de dimensiones en funciones
- C-strings: `'\0'` obligatorio, `<cctype>` y `<cstring>`

**📄 PDF**: [Lecture04_ArraysAndStrings.pdf](files/lectures/Lecture04_ArraysAndStrings.pdf)
**📋 Assignment**: [Assignment02.pdf](files/assignments/Assignment02.pdf) — printArray, reverse, transpose, pointer-offset notation, string length sin `[]`

---

### 📘 Section 05 — Pointers (L31–L38) · MIT Lecture 5 ⬜

> **Objetivo**: Punteros, aritmética de punteros, referencias, y la relación arrays-punteros.

| # | Lección | Temas |
|---|---------|-------|
| L31 | Pointers | Variables y memoria (`&x` = dirección, `*(&x)` = valor). Qué es un puntero (variable que almacena dirección). Visualización con diagramas de memoria |
| L32 | Arithmetic | Declarar punteros (`tipo *nombre`). Usar valores: dereferenciar como l-value (`*ptr = 5`), imprimir dirección (base 16). Pasar punteros a funciones (pass-by-reference vía `*`) |
| L33 | Pointers and Arrays | Nombre de array = puntero al primer elemento. Por qué arrays se pasan por referencia. Por qué índices empiezan en 0 |
| L34 | Pointer Arithmetic | Suma/resta de punteros. Step size automático (`sizeof(tipo)`). Resta de punteros = cantidad de elementos. Notación subíndice `arr[3]` == notación offset `*(arr+3)` |
| L35 | Char Arrays | `char *` strings. Literales de string: inmutables (read-only memory). Arrays de char: mutables. `char curso[] = {'6','.','0','9','6','\0'}` vs `char *curso = "6.096"` |
| L36 | Reversing a String | Algoritmo de reversa in-place con dos índices (`i=0, j=len-1`). Swap e incremento/decremento |
| L37 | References | `int &x = y` — alias (otro nombre para la misma variable). Diferencias vs punteros: (1) no necesita `*`, (2) no se puede reasignar, (3) no puede ser nula. Auto-dereferenced pointers |
| L38 | Const with Pointers | `const int *p` (dato inmutable, puntero reasignable). `int * const p` (dato mutable, puntero fijo). `const int * const p` (ambos fijos). Punteros nulos (`0`/`nullptr`), no inicializados, y dangling (memoria liberada). Los múltiples usos de `*` y `&` |

**Conceptos MIT Lecture 5:**
- `*` dual: declaración de puntero vs operador de dereference
- `&` dual: declaración de referencia vs operador address-of
- 3 variantes de `const` con punteros
- Punteros nulos, no inicializados, dangling — crashes en runtime
- Referencias: deben inicializarse, no reasignables, pre-dereferenced
- String literals en read-only memory: modificar = crash

**📄 PDF**: [Lecture05_Pointers.pdf](files/lectures/Lecture05_Pointers.pdf)
**📋 Assignment**: [Assignment02.pdf](files/assignments/Assignment02.pdf) — Swap con `&` y con `*`, pointer-to-pointer swap, pointer arithmetic en strings

---

### 📘 Section 06 — Classes (L39–L44) · MIT Lecture 6 ⬜

> **Objetivo**: Definir tipos propios con `class`, encapsulación, constructores, y separación `.h`/`.cpp`.

| # | Lección | Temas |
|---|---------|-------|
| L39 | Classes | Motivación (agrupar datos relacionados vs muchas variables sueltas). Sintaxis `class { ... };`. Fields/members. Tipos de datos heterogéneos |
| L40 | Data Members | Instancias (`MITStudent student1;`). Acceso con dot operator (`variable.campo`). Fields que son otras clases (composición — `Vector` contiene 2 `Point`). Copia de campos en asignación |
| L41 | Constructors & Destructors | Constructor default (sin args). Constructor parametrizado. Sobrecarga de constructors. Eliminación del default al definir cualquier constructor personalizado. Restauración con default args |
| L42 | Getters & Setters | Access modifiers: `public` vs `private`. Encapsulación vía getters (`getX()`). Default: `class` = private, `struct` = public. `struct` vs `class` en C++ (funcionalmente idénticos) |
| L43 | Overloading Constructors | Múltiples constructores con distintas firmas. Constructor de copia (default = memberwise/shallow). Bug de shallow copy con punteros. Deep copy con `strdup` / allocación manual |
| L44 | This Keyword | Puntero implícito `this` a la instancia actual. `this->campo` para desambiguar. Métodos (funciones miembro con instancia implícita). Implementación separada `.h`/`.cpp` con `::` |

**Conceptos MIT Lecture 6:**
- Pasar clases a funciones: por valor (copia) vs por referencia (`&`)
- Métodos: funciones dentro de una clase con acceso implícito a fields
- Scope resolution operator `::` para implementaciones fuera de la clase
- Shallow copy bug: dos instancias compartiendo el mismo puntero → corrupción
- Deep copy: allocar memoria separada en copy constructor

**📄 PDF**: [Lecture06_Classes.pdf](files/lectures/Lecture06_Classes.pdf)
**📋 Assignment**: [Assignment03.pdf](files/assignments/Assignment03.pdf) — Point class, PointArray (dynamic), Polygon abstract, Rectangle, Triangle, Pig Latin

---

### 📘 Section 07 — Object-Oriented Programming (L45–L52) · MIT Lecture 7 ⬜

> **Objetivo**: Herencia, polimorfismo, funciones virtuales, y diseño orientado a objetos.

| # | Lección | Temas |
|---|---------|-------|
| L45 | Initialization Lists | Member initializer syntax (`:` antes del body). Inicializar `const` members y constructores base. Orden de inicialización = orden de declaración |
| L46 | Encapsulation | Filosofía OOP: procedural vs orientado a objetos. Packaging datos + operaciones. Interfaces públicas. Data hiding / black box. Message passing entre objetos |
| L47 | Inheritance | Jerarquías de clases (`class Car : public Vehicle`). Base class vs derived class. Invocar constructor base en initializer list |
| L48 | Overriding | Redefinir métodos del base en derived. "Programming by difference" (solo lo nuevo/cambiado). Herencia NO puede remover funcionalidad |
| L49 | Polymorphism | "Many shapes". Sustituibilidad: pasar `Car` donde se espera `Vehicle*`. Binding en compile-time vs runtime |
| L50 | Virtual Functions | `virtual` keyword → dynamic dispatch (resolución en runtime). Una vez virtual, siempre virtual en toda la jerarquía. `ptr->member` = `(*ptr).member` |
| L51 | Abstract Classes | Funciones virtual puras (`= 0`). Clase abstracta = interfaz pura (no instanciable). Forzar implementación en derivadas |
| L52 | Multiple Inheritance | `class Car : public Vehicle, public InsuredItem`. Ambigüedad de nombres (`Vehicle::x` vs `InsuredItem::x`). Diamond problem. ⚠️ Evitar salvo estricta necesidad |

**Conceptos MIT Lecture 7:**
- 3 pilares OOP: Encapsulation, Inheritance, Polymorphism
- Is-a (herencia) vs Has-a (composición) — nunca herencia para Has-a
- `protected`: accesible en derivadas, oculto fuera
- Virtual propagation: se hereda a todos los niveles
- Multiple inheritance: dreaded diamond, ambigüedad

**📄 PDF**: [Lecture07_OOP.pdf](files/lectures/Lecture07_OOP.pdf)
**📋 Assignment**: [Assignment03.pdf](files/assignments/Assignment03.pdf) — Polygon abstract, Rectangle/Triangle subclasses, virtual area(), polymorphic printAttributes()

---

### 📘 Section 08 — Memory Management (L53–L60) · MIT Lecture 8 ⬜

> **Objetivo**: Stack vs heap, `new`/`delete`, memory leaks, destructores, RAII, deep copy.

| # | Lección | Temas |
|---|---------|-------|
| L53 | Copy Constructors | Constructor review (arrays de objetos, nested objects). Supresión del default constructor. Copy constructor por defecto (shallow). Bug con punteros compartidos |
| L54 | New Operator | Stack vs heap memory. `new tipo` → allocación en heap, retorna puntero. Lifetime: persiste hasta `delete`. Uso correcto vs memory leaks |
| L55 | Returning Objects | Retornar objetos de funciones. Peligro: retornar dirección de variable local (dangling pointer). Solución: allocar con `new` |
| L56 | Allocating Memory | Memory leaks (allocar sin `delete`). Leaks dentro de loops — `delete` DENTRO del loop, no después. Use-after-free. Double delete = crash. Solo `delete` lo que se pidió con `new` |
| L57 | Arrays and Functions | `new tipo[n]` para arrays dinámicos (tamaño en runtime). `delete[] arr` (obligatorio `[]` para arrays). Arrays estáticos requieren tamaño constante en compilación |
| L58 | Destructors | `~Clase()` — se invoca al hacer `delete` (heap) o al salir de scope (stack). Limpieza de recursos |
| L59 | RAII | Clase que envuelve memoria del heap (ej. `IntegerArray`). Constructor alloca (`new[]`), destructor libera (`delete[]`). Patrón Resource Acquisition Is Initialization |
| L60 | Deep Copy | Bug del copy constructor default con punteros (shallow copy → double free / dangling). Copy constructor propio: allocar nueva memoria + copiar elementos. Rule of Three |

**Conceptos MIT Lecture 8:**
- Stack: automático, muere al salir de scope
- Heap: manual (`new`/`delete`), persiste hasta liberar
- Memory leaks: memoria allocada que nunca se libera
- Reglas de matching: `new` ↔ `delete`, `new[]` ↔ `delete[]`
- Nunca `delete` memoria del stack
- Shallow copy: dos objetos comparten puntero → corrupción + crash
- Deep copy: allocar memoria separada, copiar datos
- RAII: constructor adquiere, destructor libera

**📄 PDF**: [Lecture08_MemoryManagement.pdf](files/lectures/Lecture08_MemoryManagement.pdf)
**📋 Assignment**: [Assignment03.pdf](files/assignments/Assignment03.pdf) — PointArray con `new[]`/`delete[]`, resize, deep copy constructor, destructor

---

## Material de Referencia (Fuera del Alcance Actual)

### MIT Lecture 9 — Advanced Topics I
Templates (function/class), specialization, non-type params, default args. STL (vector, list, map, set, iterators). Operator overloading (+, <<, member vs non-member).

### MIT Lecture 10 — Advanced Topics II
File I/O (`<fstream>`), `getline`, enums, project architecture (Manager pattern). References return, `const` member functions. Exceptions (`try`/`catch`/`throw`). `friend`. Preprocessor macros. Casting (`static_cast`, `dynamic_cast`, `reinterpret_cast`, `const_cast`).

**📄 PDFs**: [Lecture09](files/lectures/Lecture09_AdvancedTopicsI.pdf) · [Lecture10](files/lectures/Lecture10_AdvancedTopicsII.pdf)
**📋 Assignment**: [Assignment04.pdf](files/assignments/Assignment04.pdf) — Templated min, casting, templated Stack, Graph

---

## Assignments MIT

| # | Archivo | Lectures | Temas principales |
|---|---------|----------|-------------------|
| 01 | [Assignment01.pdf](files/assignments/Assignment01.pdf) | 1–2 | Hello World, scope, statistics, primes, ternary, factorial, switch |
| 02 | [Assignment02.pdf](files/assignments/Assignment02.pdf) | 3–5 | Functions, default args, overloading, Monte Carlo π, arrays, pointers, strings |
| 03 | [Assignment03.pdf](files/assignments/Assignment03.pdf) | 6–8 | Point/PointArray classes, Polygon abstract, inheritance, polymorphism, memory, Pig Latin |
| 04 | [Assignment04.pdf](files/assignments/Assignment04.pdf) | 9–10 | Templates, casting, templated Stack, Graph |
| FP | [FinalProject.pdf](files/project/FinalProject.pdf) | 1–10 | Proyecto integrador: juego o base de datos (10-15 hrs, console-based, OOP + STL) |

**Solutions**: [Sol01](files/solutions/Solution01.pdf) · [Sol02](files/solutions/Solution02.pdf) · [Sol03](files/solutions/Solution03.pdf) · [Sol04](files/solutions/Solution04.pdf)

---

## Estructura de Carpetas (Post-Reestructuración)

```
LearningCpp/
├── 01_GettingStarted/          # L01–L05  · Lecture 1 ✅
│   ├── L01–L05 .cpp
│   └── summary/
├── 02_BasicSyntax/             # L06–L22  · Lecture 2 🔄
│   └── L06–L22 .cpp
├── 03_Subroutines/             # L23–L26  · Lecture 3 ✅
│   ├── code/    theory/    exercise/
├── 04_ArraysStrings/           # L27–L30  · Lecture 4 🔄
│   ├── code/    theory/    exercise/
├── 05_Pointers/                # L31–L38  · Lecture 5 ⬜
│   ├── code/    theory/    exercise/
├── 06_Classes/                 # L39–L44  · Lecture 6 ⬜
│   ├── code/    theory/    exercise/
├── 07_OOP/                     # L45–L52  · Lecture 7 ⬜
│   ├── code/    theory/    exercise/
├── 08_MemoryManagement/        # L53–L60  · Lecture 8 ⬜
│   ├── code/    theory/    exercise/
├── exercises/                  # E01–E10
├── files/                      # PDFs de MIT 6.096
│   ├── lectures/    assignments/    solutions/    project/
├── README.md
├── TEMARIO.md                  # ← Este archivo
├── CHANGELOG.md
├── GLOSSARY.md
├── MISTAKES.md
└── RESOURCES.md
```
