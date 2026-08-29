# 📋 Backlog de Desarrollo — Módulos Pendientes

Este documento contiene el registro activo de trabajo para los módulos y componentes en desarrollo de **LearningCpp**. Los módulos 01 a 05 ya han sido implementados, auditados y completados en su totalidad.

---

## 🗺️ Estado General del Proyecto

* **Fase 1 (Fundamentos):**
  * `01_GettingStarted` — ✅ **Completado** (7 Lecciones)
  * `02_FundamentalTypes` — ✅ **Completado** (7 Lecciones)
  * `03_ScopeAndControlFlow` — ✅ **Completado** (8 Lecciones)
* **Fase 2 (Funciones & Textos):**
  * `04_Functions` — ✅ **Completado** (8 Lecciones)
  * `05_ConstantsAndStrings` — ✅ **Completado** (6 Lecciones)
* **Fase 3 (Colecciones):**
  * `06_ArraysAndVectors` — ⏳ **Siguiente en Cola** (9 Lecciones)
  * `07_CompoundTypes` — ⏳ **Pendiente** (7 Lecciones)
* **Fase 4 (Memoria Real):**
  * `08_ReferencesAndAddresses` — ⏳ **Pendiente** (8 Lecciones)
  * `09_DynamicMemory` — ⏳ **Pendiente** (9 Lecciones)
* **Fase 5 (POO Moderna):**
  * `10_Classes` — ⏳ **Pendiente** (10 Lecciones)
  * `11_Inheritance` — ⏳ **Pendiente** (7 Lecciones)
  * `12_Polymorphism` — ⏳ **Pendiente** (8 Lecciones)
* **Fase 6 (Nivel Profesional):**
  * `13_ErrorHandling` — ⏳ **Pendiente** (7 Lecciones)
  * `14_TemplatesAndLambdas` — ⏳ **Pendiente** (8 Lecciones)
  * `15_STLAlgorithms` — ⏳ **Pendiente** (8 Lecciones)

---

## 🎯 Backlog Detallado por Módulo

### 📦 Módulo 06: Arrays & Vectors (Fase 3)
- [ ] **L01 (Variables Sueltas vs Colecciones)**: Teoría, Lab. Por qué colapsa el código con datos dispersos.
- [ ] **L02 (C-Arrays & Buffer Overflow)**: Teoría, Demo de Bug (`D02_BufferOverflowBug.cpp`). *Trampa*: Escribir fuera del límite de `int arr[5]` (Uso de C-array solo como advertencia visual de Buffer Overflow).
- [ ] **L03 (std::vector, el estándar moderno)**: Teoría, Lab, Demo de Bug (`D03_BraceInitBug.cpp`), Reto (`E03_InventarioDinamico`). Creación e inicialización. *Trampa*: La ambigüedad de inicializar con llaves `{5}` vs paréntesis `(5)`.
- [ ] **L04 (Acceso seguro: .at() vs [])**: Teoría, Lab, Demo de Bug (`D04_SilentOutofBoundsBug.cpp`), Reto (`E04_ElIndicePerdido`). Prevenir Undefined Behavior forzando `.at()`.
- [ ] **L05 (Atrapando la bomba: try/catch básico)**: Teoría, Lab, Reto (`E05_AtrapandoLaBomba`). Captura táctica de `std::out_of_range` sin cerrar el programa.
- [ ] **L06 (Range-based for)**: Teoría, Lab, Demo de Bug (`D06_OffByOneBug.cpp`), Reto (`E06_IteracionSegura`). Reemplazo de bucles manuales con índices.
- [ ] **L07 (Métodos Esenciales de Vector)**: Teoría, Lab, Reto (`E07_CreciendoVectores`). `push_back()`, `size()`, `empty()`, `reserve()`.
- [ ] **L08 (Arquitectura Multi-Archivo)**: Teoría, Lab, Reto (`E08_RefactorizacionHeader`). Modularización con `.h`, `.cpp` y `#pragma once`.
- [ ] **L09 (Mini-proyecto)**: Registro de Calificaciones. Integración total con arquitectura multi-archivo. Reto (`E09_RegistroDeCalificaciones`).

---

### 🧩 Módulo 07: Compound Types (Fase 3)
- [ ] **L01 (El caos de parámetros sueltos)**: Teoría, Lab. Pasar múltiples variables inconexas a una función.
- [ ] **L02 (Creando estructuras: struct)**: Teoría, Lab, Demo de Bug (`D02_MissingSemicolonBug.cpp`), Reto (`E02_FichaDePersonaje`). Operador punto y el error de compilar sin `};`.
- [ ] **L03 (Designated Initializers C++20)**: Teoría, Lab, Demo de Bug (`D03_OutOfOrderInitBug.cpp`), Reto (`E03_EnsamblajeSeguro`). Inicialización nombrada `Jugador{.hp=100}` y respeto del orden de declaración.
- [ ] **L04 (El Peligro de Números Mágicos)**: Teoría, Demo de Bug (`D04_MagicNumberBug.cpp`). *Trampa*: Asignar `estado = 999` a un entero y corromper la lógica.
- [ ] **L05 (Estados Seguros: enum class)**: Teoría, Lab, Demo de Bug (`D05_EnumPrintBug.cpp`), Reto (`E05_EstadosSeguros`). Evitando contaminación de ámbito y tipos débiles.
- [ ] **L06 (Colecciones de Entidades)**: Teoría, Lab, Reto (`E06_BaseDeDatos`). Combinando vectores y structs para simular una base de datos en memoria.
- [ ] **L07 (Mini-proyecto)**: Bestiario RPG V1. Integración de iteración, structs y enums. Reto (`E07_GestorDeBestiario`).

---

### 🔗 Módulo 08: References & Addresses (Fase 4)
- [ ] **L01 (El colapso del rendimiento)**: Teoría, Demo de Bug (`D01_HeavyCloneBug.cpp`). El costo de pasar estructuras pesadas por valor (*Pass-by-value*).
- [ ] **L02 (Direcciones en RAM: &)**: Teoría, Lab. Inspección de direcciones hexadecimales de memoria física en consola.
- [ ] **L03 (Pass-by-Reference)**: Teoría, Lab, Reto (`E03_VentanaAlOriginal`). Sintaxis `&` para crear alias directos a la memoria original sin copias.
- [ ] **L04 (Mutación Accidental)**: Demo de Bug (`D04_AccidentalMutationBug.cpp`). Modificación no deseada de datos de solo lectura.
- [ ] **L05 (Referencias Constantes: const &)**: Teoría, Lab, Demo de Bug (`D05b_RangeForCopyBug.cpp`), Reto (`E05_MirarSinTocar`). La regla de oro de C++ y el bucle fotocopiadora.
- [ ] **L06 (La Amnesia de auto)**: Teoría, Demo de Bug (`D06_AutoReferenceStripBug.cpp`). El compilador recorta referencias al deducir tipos.
- [ ] **L07 (Dangling References)**: Teoría, Demo de Bug (`D07_DanglingReferenceBug.cpp`). Undefined Behavior al retornar referencias a variables locales del Stack.
- [ ] **L08 (Mini-proyecto)**: Bestiario V2 (Zero-Copy). Reto (`E08_OptimizadorDeBestiario`). Optimización de paso de colecciones en el Bestiario.

---

### 🧠 Módulo 09: Dynamic Memory & Smart Pointers (Fase 4)
- [ ] **L01 (Límite del Stack vs Heap)**: Teoría, Lab. Revelación: `std::vector` administraba memoria dinámica en el Heap.
- [ ] **L02 (Punteros Crudos: T* y *ptr)**: Teoría, Lab, Reto (`E02_ControlRemoto`). Sintaxis de punteros, desreferenciación y `nullptr`.
- [ ] **L03 (El Puntero Nulo: Segfault)**: Demo de Bug (`D03_NullPointerCrashBug.cpp`). Crasheos por accesos a memoria inválida.
- [ ] **L04 (Asignación Dinámica con new)**: Teoría, Lab, Reto (`E04_CreandoVida`). Creación manual de un objeto en el Heap (Veto a `new[]`).
- [ ] **L05 (Fugas de Memoria: Memory Leaks)**: Demo de Bug (`D05_MemoryLeakBug.cpp`). Pérdida de RAM por omitir `delete`.
- [ ] **L06 (Punteros Colgantes: Dangling Pointers)**: Demo de Bug (`D06_DanglingPointerBug.cpp`). Uso de memoria liberada (*Use-after-free*).
- [ ] **L07 (RAII y std::unique_ptr)**: Teoría, Lab, Reto (`E07_ElGuardianDeLaMemoria`). Gestión determinista exclusiva con `std::make_unique<T>()`.
- [ ] **L08 (Movimiento: std::move y Type Aliases)**: Teoría, Lab, Demo de Bug (`D08_UseAfterMoveBug.cpp`), Reto (`E08_DomandoLaMemoria`). Transferencia de propiedad única y alias de tipos con `using`.
- [ ] **L09 (Mini-proyecto)**: Bestiario V3 (Heap RAII). Reto (`E09_GestorDinamico`). Bestiario 100% migrado al Heap protegido contra fugas.

---

### 🏛️ Módulo 10: Classes & Encapsulation (Fase 5)
- [ ] **L01 (El Estado Inconsistente)**: Teoría, Demo de Bug (`D01_InconsistentStateBug.cpp`). Violación de invariantes con datos públicos.
- [ ] **L02 (El Candado de class)**: Teoría, Demo de Bug (`D02_DefaultAccessBug.cpp`). `public`, `private` y convención de nombres `m_`.
- [ ] **L03 (Métodos y const Correctness)**: Teoría, Lab, Demo de Bug (`D03_ConstMemberFunctionBug.cpp`), Reto (`E03_MetodosYConstCorrectness`). Métodos `const` invocados desde referencias inmutables.
- [ ] **L04 (Getters, Setters y Validación)**: Teoría, Lab, Reto (`E04_LaPuertaControlada`). Validación de entrada y retorno por `const &`.
- [ ] **L05 (Constructores y Member Initializer List)**: Teoría, Demo de Bug (`D05_InitOrderBug.cpp`), Reto (`E05_NacimientoSeguro`). Inicialización ordenada, `-Wreorder`, `= default;` y `explicit`.
- [ ] **L06 (Diseño OO: "Tell, Don't Ask")**: Teoría, Lab. Por qué evitar getters/setters indiscriminados.
- [ ] **L07 (Sobrecarga de Operadores: << y ==)**: Teoría, Lab, Demo de Bug (`D07_UnprintableClassBug.cpp`), Reto (`E07_OperadoresExpresivos`). Operadores idiomáticos para streams y comparaciones.
- [ ] **L08 (Clases Multi-Archivo)**: Teoría, Lab, Demo de Bug (`D08_MultipleDefinitionBug.cpp`), Reto (`E08_ArquitecturaMultiArchivo`). Separación `.h` y `.cpp` con `Clase::metodo()`.
- [ ] **L09 (Destructores y RAII)**: Teoría, Lab, Reto (`E09_ElUltimoAdios`). Ciclo de vida y destrucción determinista (`~Clase()`).
- [ ] **L10 (Mini-proyecto)**: Bestiario V4 (Clases Encapsuladas). Reto (`E10_BestiarioPOO`). Clases POO multi-archivo con invariantes blindadas.

---

### 🧬 Módulo 11: Inheritance (Fase 5)
- [ ] **L01 (El anti-patrón de Copiar y Pegar)**: Teoría, Demo de Bug (`D01_DuplicationBug.cpp`). Mantenimiento insostenible en entidades clonadas.
- [ ] **L02 (Herencia Simple: : public)**: Teoría, Lab, Demo de Bug (`D02b_PrivateInheritanceBug.cpp`), Reto (`E02_ExtrayendoLoComun`). Relación IS-A y prevención de herencia privada accidental.
- [ ] **L03 (Visibilidad protected)**: Teoría, Lab, Reto (`E03_LlavesDeFamilia`). Atributos `private` protegidos con getters `protected`.
- [ ] **L04 (Cadenas de Constructores)**: Demo de Bug (`D04_ConstructorChainBug.cpp`), Reto (`E04_NaciendoEnCadena`). Delegación obligatoria hacia el constructor base en inicializadores.
- [ ] **L05 (Ciclo de Vida en Herencia)**: Teoría, Lab. Construcción Padre➔Hijo y destrucción inversa Hijo➔Padre.
- [ ] **L06 (Object Slicing)**: Teoría, Demo de Bug (`D06_ObjectSlicingBug.cpp`), Reto (`E06_DetectandoSlicing`). Las trampas del rebanado en asignación y colecciones por valor (`vector<Base>`).
- [ ] **L07 (Mini-proyecto)**: Jerarquía del Bestiario. Reto (`E07_ArbolDeEntidades`). Jerarquía en 3 niveles: `Entidad` ➔ `Monstruo` ➔ `Jefe`.

---

### 🎭 Módulo 12: Polymorphism (Fase 5)
- [ ] **L01 (Early Binding)**: Teoría, Demo de Bug (`D01_StaticBindingBug.cpp`). Enlace estático al tipo del puntero en compilación.
- [ ] **L02 (virtual y VTable)**: Teoría, Lab, Demo de Bug (`D02_PassByValueSlicingBug.cpp`), Reto (`E02_DespachoDinamico`). Despacho dinámico en runtime y la tabla virtual `__vptr`.
- [ ] **L03 (override y final)**: Teoría, Demo de Bug (`D03_SilentTypoBug.cpp`), Reto (`E03_LaRedDeSeguridad`). Prevención de typos en firmas y sellado de métodos.
- [ ] **L04 (El Destructor Virtual)**: Teoría, Demo de Bug (`D04_VirtualDestructorLeakBug.cpp`), Reto (`E04_DestruccionPolimorfica`). Fuga de memoria letal al destruir con `unique_ptr<Base>`.
- [ ] **L05 (Interfaces Puras: = 0)**: Teoría, Lab, Reto (`E05_ElContratoPuro`). Clases abstractas puras y herencia múltiple de interfaces.
- [ ] **L06 (Colecciones Polimórficas)**: Teoría, Demo de Bug (`D06_UnsafeDowncastBug.cpp`), Reto (`E06_ColeccionDeMonstruos`). `vector<unique_ptr<Base>>` y `dynamic_cast` seguro.
- [ ] **L07 (Impresión Polimórfica Idiomática)**: Teoría, Lab, Reto (`E07_ImpresionPolimorfica`). Integrar `operator<<` con `virtual void imprimir() const = 0`.
- [ ] **L08 (Mini-proyecto)**: El Coliseo (Game Loop Polimórfico). Reto (`E08_GameLoopPolimorfico`). Motor de combate dinámico sin `if/else` de tipo.

---

### 🛡️ Módulo 13: Error Handling & Modern Resilience (Fase 6)
- [ ] **L01 (La Fragilidad de Códigos de Retorno)**: Teoría, Demo de Bug (`D01_IgnoredReturnCodeBug.cpp`). Errores ignorados vs fallos ruidosos.
- [ ] **L02 (Stack Unwinding)**: Teoría, Lab, Demo de Bug (`D02_RawPointerLeakOnThrowBug.cpp`), Reto (`E02_StackUnwindingSeguro`). Mecánica de vuelo y seguridad con RAII.
- [ ] **L03 (La Jerarquía std::exception)**: Teoría, Lab, Demo de Bug (`D03_ExceptionSlicingBug.cpp`), Reto (`E03_CapturaPolimorfica`). Captura por `const std::exception&` sin slicing.
- [ ] **L04 (Excepciones de Dominio y Constructores)**: Teoría, Lab, Demo de Bug (`D04_ZombieObjectBug.cpp`), Reto (`E04_ConstructoresBlindados`). Constructores que abortan objetos zombi y re-lanzamiento `throw;`.
- [ ] **L05 (std::optional C++17)**: Teoría, Lab, Demo de Bug (`D05_BadOptionalAccessBug.cpp`), Reto (`E05_BuscadorDeInventario`). Ausencias esperadas con `std::nullopt`.
- [ ] **L06 (La Garantía de noexcept)**: Teoría, Lab, Demo de Bug (`D06_VectorCopyFallbackBug.cpp`), Reto (`E06_OptimizandoMovimiento`). `std::move_if_noexcept` y optimización de relocalización en `std::vector`.
- [ ] **L07 (Mini-proyecto)**: Motor de Mazmorras Resiliente. Reto (`E07_MotorResiliente`). Carga de mapas, parseo de archivos y excepciones de dominio.

---

### 📦 Módulo 14: Templates & Generic Programming (Fase 6)
- [ ] **L01 (La Fábrica de Código)**: Teoría, Demo de Bug (`D01_TypeDuplicationBug.cpp`). Polimorfismo estático vs dinámico (cero sobrecarga en runtime).
- [ ] **L02 (Plantillas de Funciones)**: Teoría, Lab, Demo de Bug (`D02_TemplateDeductionBug.cpp`), Reto (`E02_FuncionesGenericas`). Deducción automática, conversión desactivada y multiparámetros.
- [ ] **L03 (La Trampa del Linker: Templates en Headers)**: Teoría, Lab, Demo de Bug (`D03_TemplateLinkerBug.cpp`), Reto (`E03_HeaderTemplates`). Por qué los templates deben residir obligatoriamente en archivos `.hpp`.
- [ ] **L04 (Plantillas de Clases)**: Teoría, Lab, Reto (`E04_ContenedorGenerico`). Creación del contenedor `CajaSegura<T>` con CTAD.
- [ ] **L05 (Parámetros No-Tipo: NTTP)**: Teoría, Lab, Reto (`E05_BufferEstatico`). Buffers estáticos en el Stack sin tocar el Heap.
- [ ] **L06 (Lambdas Modernas)**: Teoría, Lab, Reto (`E06_FiltrosConLambdas`). Funciones anónimas instantáneas y predicados.
- [ ] **L07 (Capturas y Dangling References)**: Teoría, Lab, Demo de Bug (`D07_DanglingLambdaCaptureBug.cpp`), Reto (`E07_CapturasSeguras`). Trampa fatal del paso por referencia en capturas asíncronas.
- [ ] **L08 (Mini-proyecto)**: Pipeline Genérico de Eventos. Reto (`E08_PipelineGenerico`). Bus de eventos genérico desacoplado de alto rendimiento.

---

### ⚡ Módulo 15: STL Algorithms, Ranges & Capstone (Fase 6)
- [ ] **L01 (La Muerte del Bucle Manual)**: Teoría, Demo de Bug (`D01_RawLoopOffByOneBug.cpp`), Reto (`E01_RefactorizandoBucles`). Filosofía "No Raw Loops" (`std::all_of`, `std::count_if`).
- [ ] **L02 (Iteradores y su Invalidación)**: Teoría, Lab, Demo de Bug (`D02_IteratorInvalidationBug.cpp`), Reto (`E02_RecorridoSeguro`). `begin()`, `end()` y eliminación segura con `std::erase_if` (C++20).
- [ ] **L03 (Búsqueda y Predicados)**: Teoría, Lab, Reto (`E03_BuscadorAvanzado`). `std::find_if` y `std::min_element` con lambdas y `std::optional`.
- [ ] **L04 (Transformación y Reducción)**: Teoría, Lab, Reto (`E04_TransformadorDeDatos`). Mapeo funcional con `std::transform` y `std::accumulate`.
- [ ] **L05 (Ordenamiento y Comparadores Custom)**: Teoría, Lab, Reto (`E05_OrdenamientoCustom`). `std::ranges::sort` con comparadores multicriterio.
- [ ] **L06 (C++20 Ranges y Vistas)**: Teoría, Lab, Reto (`E06_PipelinesConRanges`). Vistas perezosas y composición con tuberías `|` sin copias.
- [ ] **L07 (Concurrencia Básica)**: Teoría, Lab, Demo de Bug (`D07_DataRaceIntroBug.cpp`), Reto (`E07_CargaAsincrona`). Asincronía con `std::async` y `std::jthread`.
- [ ] **L08 (Capstone Final del Curso)**: El Motor RPG Definitivo. Reto (`E08_MotorRPGDefinitivo`). Integración total de los 15 módulos en una arquitectura profesional completa.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
