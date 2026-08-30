# 🏛️ Arquitectura y Decisiones Pedagógicas del Curso LearningCpp

Este documento es el **registro arquitectónico maestro** de *LearningCpp*. Contiene la filosofía pedagógica, la estructura de fases y módulos, y las 20 decisiones técnicas fundamentales que gobiernan el diseño de todo el temario.

---

## 1. 🎯 Identidad y Filosofía Pedagógica

1. **Nivel "Cero Absoluto" y Principio de la Escalera:**
   - La audiencia no tiene conocimientos previos de RAM, compiladores ni buffers.
   - Cada lección se apoya **únicamente** en lo explicado en las lecciones anteriores. Cero saltos mágicos de conocimiento.
   - Cero jerga elitista o referencias académicas abstractas.

2. **La Regla del Desvanecimiento (Scaffolding & Fading):**
   - **El Puente Técnico:** Se permite una metáfora cotidiana (ej. "std::string es un tren", "std::cin es una tubería") exclusivamente en la introducción de un tema nuevo para romper el hielo.
   - **Fading Total:** A partir del segundo párrafo de la teoría, y en **todo** el código fuente, la metáfora desaparece y se adopta la terminología profesional de la industria (*Undefined Behavior, Compile-time Evaluation, Type Errors, Buffer Extraction Failure, Dangling View, Const Correctness, Stack Unwinding*).

3. **Filosofía "Break-First, Fix-Later":**
   - Cada característica de C++ Moderno existe porque algo en el lenguaje clásico era inseguro o propenso a errores.
   - En lugar de presentar la sintaxis en abstracto, el alumno primero **experimenta el dolor del fallo en un demo de bug intencional (`DXX_`)**, y luego aprende la solución idiomática moderna.

4. **Modelos Mentales de Memoria (Hardware Real):**
   - Se enseña cómo funciona la memoria física (Stack vs Heap, direcciones `0x...`, alineación y ciclos de vida de variables).

---

## 2. 🗺️ Estructura General del Plan de Estudios (15 Módulos / 6 Fases)

```text
FASE 1 — Fundamentos
  ├── M01: Getting Started (7 lecciones) ─────────────── [✅ Completo]
  ├── M02: Fundamental Types (7 lecciones) ───────────── [✅ Completo]
  └── M03: Scope & Control Flow (8 lecciones) ────────── [✅ Completo]

FASE 2 — Funciones y Textos
  ├── M04: Functions (8 lecciones) ───────────────────── [✅ Implementado]
  └── M05: Constants & Strings (6 lecciones) ─────────── [✅ Completo]

FASE 3 — Colecciones y Entidades
  ├── M06: Arrays & Vectors (9 lecciones) ────────────── [⏳ Planificado]
  └── M07: Compound Types [Structs & Enums] (7 lecciones) [⏳ Planificado]

FASE 4 — Memoria
  ├── M08: References & Addresses (8 lecciones) ──────── [⏳ Planificado]
  └── M09: Dynamic Memory & Smart Pointers (9 lecciones) [⏳ Planificado]

FASE 5 — POO Moderna
  ├── M10: Classes & Encapsulation (10 lecciones) ────── [⏳ Planificado]
  ├── M11: Inheritance (7 lecciones) ─────────────────── [⏳ Planificado]
  └── M12: Polymorphism (8 lecciones) ────────────────── [⏳ Planificado]

FASE 6 — Resiliencia & Especialización
  ├── M13: Error Handling & std::optional (7 lecciones) ─ [⏳ Planificado]
  ├── M14: Templates & Generic Programming (8 lecciones) ─ [⏳ Planificado]
  └── M15: STL Algorithms & Pipelines (8 lecciones) ──── [⏳ Planificado]
```

---

## 3. 📜 Bitácora de Decisiones Arquitectónicas (Secciones 1 a 20)

### 1. El Problema del "Mundo Real" y la Decisión de Simplificar
* Se eliminaron proyectos pesados tempranos basados en interfaces de terminal complejas que abrumaban al principiante.
* Cada módulo se enfoca en una única gran idea cognitiva, respaldada por mini-proyectos de consola directos y claros.

### 2. El Veto Absoluto a "using namespace std" y "std::endl"
* `using namespace std;` está terminantemente prohibido para evitar la colisión de nombres y enseñar el alcance explícito desde el primer día.
* `std::endl` está vetado; se utiliza siempre `'\n'` para evitar forzar *buffer flushes* innecesarios que degradan el rendimiento.

### 3. La Filosofía del "Cero Legado" vs la Excepción de C-Arrays (M06)
* No se enseña código de C antiguo (`printf`, `malloc`, `free`) como estilo de programación.
* **La única excepción:** En M06 se enseña un arreglo de C (`int arr[5]`) con el único propósito de detonar un *Buffer Overflow* visual en un demo de bug (`D01`), justificando inmediatamente el uso de `std::vector::at()`.

### 4. La Reestructuración de M02 (Fundamental Types)
* Se reorganizó en 7 lecciones con inicialización uniforme `{}` obligatoria, casting explícito seguro con `static_cast`, y el miniproyecto "Split the Bill".

### 5. La Reestructuración de M03 (Scope & Control Flow)
* Se diseñaron 8 lecciones estructuradas con 7 demos de bugs dedicados (`D01` a `D07`), abordando *Shadowing*, *Fallthrough* en `switch`, y bucles infinitos.

### 6. La Reestructuración de M04 (Functions)
* Se implementaron 8 lecciones completas con RNG moderno (`<random>`), evitando el uso arcaico de `rand()`, y culminando en el generador de atributos de RPG.

### 7. La Reestructuración de M05 (Constants & Strings)
* Se dividió claramente el mundo de la inmutabilidad: `const` en tiempo de ejecución vs `constexpr` en tiempo de compilación.
* Se introdujo `std::string_view` como vista de solo lectura no propietaria, advirtiendo sobre la trampa mortal de las vistas colgantes (*Dangling Views*).

### 8. La Reestructuración de M06 (Arrays & Vectors)
* Expandido a 9 lecciones. Se introdujo el manejo seguro de límites con `.at()` y la captura básica de `std::out_of_range` con `try/catch` como mecanismo de contención antes de la teoría profunda de M13.

### 9. La Reestructuración de M07 (Compound Types)
* 7 lecciones dedicadas a `struct` y `enum class`. Se prohíben los enums clásicos de C en favor de los enums fuertemente tipados con ámbito, cerrando con el Bestiario RPG V1.

### 10. La Gran División de Memoria (M08 vs M09)
* **M08 (References & Addresses):** Trata *exclusivamente* direcciones de memoria (`&`) y paso por referencia (`const &`), resolviendo el dolor del *pass-by-value* de estructuras pesadas.
* **M09 (Dynamic Memory & Smart Pointers):** Trata el Heap, punteros crudos (`*`), fugas de memoria, `std::unique_ptr`, `std::make_unique` y la semántica de movimiento con `std::move`. Veto absoluto a `new[]` y `delete[]` manuales en favor de vectores.

### 11. El Veto a `std::shared_ptr` Temprano
* En M09 se enseña exclusivamente la propiedad única con `std::unique_ptr`. Se previene la sobreingeniería y las fugas por referencias circulares.

### 12. La Semántica de Movimiento como Transferencia de Propiedad (M09)
* Se enseña `std::move` como un cast que convierte a rvalue para transferir la propiedad de punteros inteligentes únicos sin clonar recursos.

### 13. El Bucle del Ciclo de Aprendizaje en Teoría
* Todo archivo de teoría `.md` incluye enlaces estandarizados a su Laboratorio (`lab/`), Demo de Bug (`lab/demos/DXX_`) y Reto (`exercise/EXX_`).

### 14. Estandarización Total de Banners y Cero Emojis en Código C++
* Se prohíbe el uso de emojis dentro de archivos `.cpp` (código y comentarios). Se implementan banners estandarizados limpios en todos los archivos del curso.

### 15. Decisiones Arquitectónicas de Clases y Encapsulamiento (Módulo 10)
* Expandido a 10 lecciones para cubrir 4 brechas críticas:
  - Const Correctness en métodos miembro (`const` member functions).
  - Sobrecarga básica de operadores (`operator<<` y `operator==`).
  - Arquitectura multi-archivo (`.h` para interfaz y `.cpp` para implementación con `Clase::`).
  - Constructores estrictos (Member Initializer List, `-Wreorder`, pérdida del constructor por defecto y `explicit`).

### 16. Decisiones Arquitectónicas de Herencia (Módulo 11)
* **Veto a la Herencia Múltiple con Estado:** En C++ moderno, la herencia múltiple de clases de implementación es considerada un anti-patrón tóxico. Se mantiene herencia simple 100%.
* **La Trampa de la Herencia Oculta:** Inyección obligatoria de `D02b_PrivateInheritanceBug.cpp` para ilustrar el error de omitir el calificador `public` (`class M : B` ➔ herencia privada por defecto).
* **Regla de Encapsulamiento en Subclases:** Atributos estrictamente `private` en la clase base; acceso a derivados exclusivamente mediante métodos/getters `protected`.
* **Object Slicing (L06):** Trampa definitiva al intentar guardar derivadas por valor en `std::vector<Base>`, sirviendo como gancho emocional para el Polimorfismo (M12).

### 17. Clímax Arquitectónico del Polimorfismo Dinámico (Módulo 12)
* **Destructor Virtual Obligatorio (L04):** Dado el uso de `std::unique_ptr<Base>`, omitir `virtual ~Base() = default;` es un Comportamiento Indefinido y fuga de memoria garantizada (`D04_VirtualDestructorLeakBug.cpp`).
* **Impresión Polimórfica Idiomática (L07):** `operator<<` no-virtual delegando en un método protegido `virtual void imprimir() const = 0;`.
* **Herencia Múltiple Exclusiva para Interfaces Puras (L05):** Clases abstractas puras como única excepción permitida para herencia múltiple (`IGuardable`).

### 18. Decisiones Arquitectónicas y Resiliencia (Módulo 13)
* **Vindicación de RAII y Stack Unwinding:** Demostrar que los punteros crudos fugan memoria ante un `throw`, mientras que `std::unique_ptr` destruye automáticamente sus recursos durante el vuelo (`D02_RawPointerLeakOnThrowBug.cpp`).
* **Prohibición de Captura por Valor:** Prohibido `catch (std::exception e)`; obligatorio `catch (const std::exception& e)` para erradicar el *Object Slicing* en excepciones.
* **Constructores que se Niegan a Nacer:** Uso de excepciones para evitar la creación de objetos zombi cuando los invariantes no se satisfacen.
* **Separación de Responsabilidades (`std::optional`):** Excepciones para fallos graves; `std::optional<T>` y `std::nullopt` para ausencias normales sin sobrecarga de desenrollado de pila.
* **La Trampa de Rendimiento de `noexcept`:** El demo `D06_VectorCopyFallbackBug.cpp` ilustra cómo omitir `noexcept` en constructores de movimiento fuerza copias profundas pesadas en `std::vector` (`std::move_if_noexcept`).

### 19. Decisiones Arquitectónicas y Metaprogramación (Módulo 14)
* **El Modelo de Inclusión de Cabeceras:** El demo `D03_TemplateLinkerBug.cpp` demuestra que separar plantillas en archivos `.cpp` rompe el enlazador con `undefined reference`. Las plantillas deben residir en cabeceras (`.hpp` / `.h`).
* **Ambigüedad de Deducción (`D02_TemplateDeductionBug.cpp`):** En `template <typename T>` no hay conversiones implícitas automáticas (`max(5, 5.5)`), forzando el dominio de `<double>` y plantillas multiparámetro.
* **Eficiencia en Stack con NTTP:** Parámetros No-Tipo (`template <typename T, std::size_t N>`) para buffers contiguos sin memoria dinámica en el Heap.
* **Trampa Mortal de Capturas en Lambdas (`D07_DanglingLambdaCaptureBug.cpp`):** Prevención del *Use-After-Free* al capturar por referencia `[&]` en lambdas que sobreviven al ámbito creador.

### 20. Culminación del Plan de Estudios y Capstone (Módulo 15)
* **Claridad ante todo (Algoritmos STL vs Bucles Manuales):** Privilegiar algoritmos estándar declarativos (`std::all_of`, `std::any_of`, `std::count_if`, `std::transform`) cuando aporten expresividad y seguridad, reservando `range-based for` para secuencias directas.
* **Invalidación de Iteradores:** El demo `D02_IteratorInvalidationBug.cpp` ilustra el fallo de memoria al mutar colecciones durante la iteración tradicional, enseñando el *Erase-Remove Idiom* canónico de C++17 y el puente a `std::erase_if` de C++20.
* **Mirada al Futuro (C++20 Ranges):** Bloque comparativo sobre evaluación perezosa (*Lazy Evaluation*) con `std::views` y el operador tubería `|`.
* **Concurrencia y Asincronía Básica:** El demo `D07_DataRaceIntroBug.cpp` para comprender *Data Races* y la ejecución de tareas en segundo plano con `std::async` y `std::future`.
* **El Capstone Final ("El Motor RPG Definitivo" - L08):** Consolidación armónica de los 15 módulos del curso en una arquitectura multi-archivo modular y robusta.

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
