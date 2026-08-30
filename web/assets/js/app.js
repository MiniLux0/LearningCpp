/**
 * ============================================================================
 * LEARNINGCPP WEB PLATFORM - HIGH PERFORMANCE BUNDLE
 * Standalone, Highly Optimized, Accessible Architecture
 * Compatible with file:// protocol and modern HTTP/HTTPS servers
 * ============================================================================
 */

(function() {
  'use strict';

  /* ==========================================================================
     1. CURRICULUM DATA MODEL
     ========================================================================== */
  const PHASES = [
    { id: "fase-1", name: "Fase 1: Fundamentos", count: 3, subtitle: "De Cero Absoluto a tu Primer Binario: Compilador g++, tipos estáticos, Stack y control de flujo." },
    { id: "fase-2", name: "Fase 2: Funciones & Textos", count: 2, subtitle: "Modularidad y textos: Paso por valor, inmutabilidad const/constexpr y vistas de memoria std::string_view." },
    { id: "fase-3", name: "Fase 3: Colecciones", count: 2, subtitle: "Estructuras y datos: Arreglos dinámicos std::vector, structs heterogéneos y arquitectura multi-archivo .h/.cpp." },
    { id: "fase-4", name: "Fase 4: Memoria Real", count: 2, subtitle: "Arquitectura de hardware: Operador &, paso Zero-Copy const &, Heap dinámico y punteros RAII std::unique_ptr." },
    { id: "fase-5", name: "Fase 5: POO Moderna", count: 3, subtitle: "Ingeniería orientada a objetos: Encapsulamiento m_, constructores seguros, sobrecarga de operadores y VTable." },
    { id: "fase-6", name: "Fase 6: Nivel Profesional", count: 3, subtitle: "Sistemas de alta resiliencia: Stack Unwinding, templates genéricos, lambdas, C++20 Ranges y Capstone Final." },
    { id: "all", name: "Ver Todo el Roadmap", count: 15, subtitle: "Vista panorámica de los 15 módulos del plan de estudios oficial." }
  ];

  const MODULES = [
    {
      id: "01",
      slug: "01_GettingStarted",
      phase: "fase-1",
      phaseName: "Fase 1: Fundamentos",
      title: "Getting Started",
      icon: "🚀",
      status: "completed",
      statusLabel: "Completo",
      lessonsCount: 7,
      tagline: "¿Qué es programar?, compilador g++, cout/cin, namespaces y streams",
      project: "Terminal Interactiva Multi-palabra",
      description: "Iniciación desde cero absoluto. Comprensión física del hardware, anatomía de main(), flujos seguros de entrada/salida y veto a malos hábitos como using namespace std.",
      lessons: [
        { id: "L00", title: "¿Qué es programar?", desc: "100% conceptual: qué hace un compilador y por qué el hardware requiere código binario." },
        { id: "L01", title: "Instalando tus herramientas", desc: "Verificación con g++ y supervivencia básica en la terminal." },
        { id: "L02", title: "Tu primer programa", desc: "Anatomía de main(), std::cout y comando mínimo de compilación." },
        { id: "L03", title: "Namespaces y std::", desc: "Prevención de colisión de nombres globales." },
        { id: "L04", title: "Formato y salida limpia", desc: "Salto de línea '\\n' vs el costo innecesario de std::endl." },
        { id: "L05", title: "Primer contacto con datos", desc: "std::cin seguro e inicialización uniforme {0} contra basura en RAM." },
        { id: "L06", title: "Mini-proyecto Terminal", desc: "Lectura multi-palabra con std::getline y validación de buffers." }
      ],
      bugDemos: ["D04_UninitializedBug.cpp", "D05_CinSpacesBug.cpp"],
      keyDecision: "Prohibición total de using namespace std; y std::endl."
    },
    {
      id: "02",
      slug: "02_FundamentalTypes",
      phase: "fase-1",
      phaseName: "Fase 1: Fundamentos",
      title: "Fundamental Types",
      icon: "🧱",
      status: "completed",
      statusLabel: "Completo",
      lessonsCount: 7,
      tagline: "Tipado estático, {} inicialización uniforme, static_cast y auto",
      project: "Split the Bill Calculator",
      description: "Tipos primitivos (int, double, char, bool), límites físicos de sizeof, compuertas lógicas y solución de la división entera mediante casting explícito.",
      lessons: [
        { id: "L01", title: "Tipos primitivos y RAM", desc: "Límites físicos de bytes en memoria con sizeof." },
        { id: "L02", title: "Inicialización Uniforme {}", desc: "Prevención de Narrowing Conversions destructivas." },
        { id: "L03", title: "Operadores aritméticos", desc: "Precedencia y la trampa de la división entera (7 / 2 = 3)." },
        { id: "L04", title: "Operadores lógicos", desc: "Compuertas booleanas y prevención del bug 'if (x = 5)'." },
        { id: "L05", title: "Conversión static_cast", desc: "Casting explícito seguro en tiempo de compilación." },
        { id: "L06", title: "Deducción con auto", desc: "Uso idiomático de auto sin perder visibilidad en RAM." },
        { id: "L07", title: "Mini-proyecto Split the Bill", desc: "Calculadora de gastos exactos con casting de alta precisión." }
      ],
      bugDemos: ["D02_NarrowingBug.cpp", "D03_IntegerDivisionBug.cpp", "D04_AssignmentInIfBug.cpp"],
      keyDecision: "Inicialización uniforme obligatoria {} en todas las variables."
    },
    {
      id: "03",
      slug: "03_ScopeAndControlFlow",
      phase: "fase-1",
      phaseName: "Fase 1: Fundamentos",
      title: "Scope & Control Flow",
      icon: "🔀",
      status: "completed",
      statusLabel: "Completo",
      lessonsCount: 8,
      tagline: "Ámbitos, condicionales if/switch, bucles y prevención de Undefined Behavior",
      project: "Taberna RPG / Cajero Automático",
      description: "Dominio de la toma de decisiones, control de ciclos de vida de variables en el Stack, prevención de Variable Shadowing, Fallthrough y bucles infinitos.",
      lessons: [
        { id: "L01", title: "Decisiones if/else", desc: "La trampa del punto y coma asesino 'if (cond);'." },
        { id: "L02", title: "Cadenas else if", desc: "Evaluación por cortocircuito y prevención de código inalcanzable." },
        { id: "L03", title: "Bloques y Ámbito (Scope)", desc: "El bug de Variable Shadowing en el Stack." },
        { id: "L04", title: "Multi-caminos switch", desc: "Prevención de Fallthrough involuntario." },
        { id: "L05", title: "Ciclos while/do-while", desc: "Prevención de bucles infinitos en consola." },
        { id: "L06", title: "El bucle contador for", desc: "Prevención del error de desfase Off-By-One." },
        { id: "L07", title: "Break y Continue", desc: "Control de flujo en bucles anidados." },
        { id: "L08", title: "Mini-proyecto Taberna RPG", desc: "Menú interactivo resiliente con conmutación continua." }
      ],
      bugDemos: ["D01_SemicolonIfBug.cpp", "D03_ShadowingBug.cpp", "D04_FallthroughBug.cpp", "D06_OffByOneBug.cpp"],
      keyDecision: "Modelado estricto del ciclo de vida en el Stack mediante llaves {}."
    },
    {
      id: "04",
      slug: "04_Functions",
      phase: "fase-2",
      phaseName: "Fase 2: Funciones & Textos",
      title: "Functions",
      icon: "📦",
      status: "completed",
      statusLabel: "Completo",
      lessonsCount: 8,
      tagline: "Paso por valor (la trampa del clon), aislamiento en Stack y RNG <random>",
      project: "Generador de Atributos RPG",
      description: "Descomposición modular en funciones atómicas, aislamiento estricto de memoria en la pila y aleatoriedad moderna con std::mt19937.",
      lessons: [
        { id: "L01", title: "Anatomía de una función", desc: "Declaración, parámetros y separación de responsabilidades." },
        { id: "L02", title: "Retornando valores", desc: "Obligatoriedad de return en todos los caminos lógicos." },
        { id: "L03", title: "Funciones void", desc: "Acciones sin retorno y comportamiento del compilador." },
        { id: "L04", title: "Pass-by-value", desc: "Demostración de copias clonadas en la pila." },
        { id: "L05", title: "Ámbito local", desc: "Aislamiento de memoria entre funciones y main." },
        { id: "L06", title: "Refactorización modular", desc: "Descomposición de funciones monolíticas en unidades reutilizables." },
        { id: "L07", title: "Aleatoriedad <random>", desc: "Uso de std::mt19937 evitando el arcaico rand()." },
        { id: "L08", title: "Mini-proyecto Generador RPG", desc: "Simulador modular con tiradas aleatorias y atributos balanceados." }
      ],
      bugDemos: ["D02_MissingReturnBug.cpp", "D04_PassByValueBug.cpp", "D07_StaticRngBug.cpp"],
      keyDecision: "Veto absoluto a rand(); adopción obligatoria de <random> de C++11/17."
    },
    {
      id: "05",
      slug: "05_ConstantsAndStrings",
      phase: "fase-2",
      phaseName: "Fase 2: Funciones & Textos",
      title: "Constants & Strings",
      icon: "📝",
      status: "completed",
      statusLabel: "Completo",
      lessonsCount: 6,
      tagline: "const vs constexpr, std::string y vistas eficientes std::string_view",
      project: "Generador de Contraseñas Seguras",
      description: "Inmutabilidad por defecto (Const Correctness), evaluación en tiempo de compilación y manipulación segura de cadenas sin copias innecesarias.",
      lessons: [
        { id: "L01", title: "Constantes (const)", desc: "Inmutabilidad en tiempo de ejecución." },
        { id: "L02", title: "Expresiones constexpr", desc: "Cálculos resueltos directamente por el compilador." },
        { id: "L03", title: "std::string a fondo", desc: "Cadenas dinámicas y superación definitiva de char[]." },
        { id: "L04", title: "Vistas std::string_view", desc: "Paso de texto con cero costo de copia y prevención de Dangling Views." },
        { id: "L05", title: "Validación de std::cin", desc: "Limpieza y saneamiento de buffers corruptos con cin.fail()." },
        { id: "L06", title: "Mini-proyecto Generador Claves", desc: "Generador inmutable con validación estricta de entradas." }
      ],
      bugDemos: ["D01_MutationBug.cpp", "D04_DanglingStringViewBug.cpp", "D05_CinInfiniteLoopBug.cpp"],
      keyDecision: "Separación clara entre const (runtime) y constexpr (compile-time)."
    },
    {
      id: "06",
      slug: "06_ArraysAndVectors",
      phase: "fase-3",
      phaseName: "Fase 3: Colecciones",
      title: "Arrays & Vectors",
      icon: "🗄️",
      status: "planned",
      statusLabel: "Siguiente en Cola",
      lessonsCount: 9,
      tagline: "std::vector, límites seguros .at(), multi-archivo .h/.cpp",
      project: "Registro de Calificaciones",
      description: "Demostración de Buffer Overflow en arreglos de C clásico, adopción de std::vector, range-based for y separación en archivos de cabecera.",
      lessons: [
        { id: "L01", title: "Variables sueltas vs Colecciones", desc: "Colapso del código ante datos dispersos." },
        { id: "L02", title: "C-Arrays y Buffer Overflow", desc: "Demo de corrupción de memoria adyacente en C clásico." },
        { id: "L03", title: "std::vector moderno", desc: "Inicialización {5} (1 elemento) vs (5) (5 espacios)." },
        { id: "L04", title: "Acceso seguro .at()", desc: "Prevención de Undefined Behavior forzando verificación de límites." },
        { id: "L05", title: "Atrapando la bomba", desc: "Captura táctica de std::out_of_range con try/catch." },
        { id: "L06", title: "Range-based for", desc: "Iteración idiomática limpia y segura sin índices manuales." },
        { id: "L07", title: "Métodos de vector", desc: "push_back, size, empty, reserve y crecimiento en Heap." },
        { id: "L08", title: "Arquitectura Multi-Archivo", desc: "Separación profesional con .h, .cpp y #pragma once." },
        { id: "L09", title: "Mini-proyecto Calificaciones", desc: "Sistema multi-archivo de notas dinámicas y estadísticas." }
      ],
      bugDemos: ["D02_BufferOverflowBug.cpp", "D03_BraceInitBug.cpp", "D04_SilentOutofBoundsBug.cpp"],
      keyDecision: "Acceso verificado obligatorio con .at() para eliminar Undefined Behavior."
    },
    {
      id: "07",
      slug: "07_CompoundTypes",
      phase: "fase-3",
      phaseName: "Fase 3: Colecciones",
      title: "Compound Types",
      icon: "🧩",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 7,
      tagline: "struct, enum class y Designated Initializers de C++20",
      project: "Bestiario RPG V1",
      description: "Agrupación de datos heterogéneos, tipado fuerte para máquinas de estado y colecciones de estructuras en memoria contigua.",
      lessons: [
        { id: "L01", title: "El caos de parámetros", desc: "Por qué colapsan las firmas de 6 variables sueltas." },
        { id: "L02", title: "Estructuras (struct)", desc: "Agrupación heterogénea y el operador punto." },
        { id: "L03", title: "Designated Initializers", desc: "Inicialización C++20 Jugador{.hp=100} en orden estricto." },
        { id: "L04", title: "Peligro de Números Mágicos", desc: "Fragilidad al usar enteros para representar estados." },
        { id: "L05", title: "Estados seguros enum class", desc: "Enumeraciones fuertemente tipadas con ámbito." },
        { id: "L06", title: "Colecciones de Entidades", desc: "Combinación de std::vector y structs." },
        { id: "L07", title: "Mini-proyecto Bestiario V1", desc: "Base de datos en memoria con monstruos y combate elemental." }
      ],
      bugDemos: ["D02_MissingSemicolonBug.cpp", "D03_OutOfOrderInitBug.cpp", "D04_MagicNumberBug.cpp"],
      keyDecision: "Veto a los enum clásicos de C; adopción exclusiva de enum class."
    },
    {
      id: "08",
      slug: "08_ReferencesAndAddresses",
      phase: "fase-4",
      phaseName: "Fase 4: Memoria Real",
      title: "References & Addresses",
      icon: "🔗",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 8,
      tagline: "Operador &, paso por const &, alias y amnesia de auto",
      project: "Bestiario V2 (Zero-Copy)",
      description: "Inspección de direcciones físicas hexadecimales de memoria, eliminación de copias pesadas y prevención de referencias colgantes.",
      lessons: [
        { id: "L01", title: "El costo de la copia", desc: "Demostración del colapso de rendimiento por copias pesadas." },
        { id: "L02", title: "Direcciones en RAM (&)", desc: "Inspección física de direcciones hexadecimales 0x..." },
        { id: "L03", title: "Pass-by-Reference (&)", desc: "Creación de alias directos a la memoria original." },
        { id: "L04", title: "Mutación accidental", desc: "Por qué las referencias mutables corrompen datos de lectura." },
        { id: "L05", title: "Referencias const &", desc: "La regla de oro de C++ y el bucle fotocopiadora." },
        { id: "L06", title: "La amnesia de auto", desc: "Cómo auto descarta la referencia forzando auto&." },
        { id: "L07", title: "Dangling References", desc: "Retorno de referencias a variables que mueren en el Stack." },
        { id: "L08", title: "Mini-proyecto Bestiario V2", desc: "Refactorización completa con paso Zero-Copy." }
      ],
      bugDemos: ["D01_HeavyCloneBug.cpp", "D04_AccidentalMutationBug.cpp", "D07_DanglingReferenceBug.cpp"],
      keyDecision: "Regla de oro: tipos primitivos por valor, tipos pesados por const &."
    },
    {
      id: "09",
      slug: "09_DynamicMemory",
      phase: "fase-4",
      phaseName: "Fase 4: Memoria Real",
      title: "Dynamic Memory",
      icon: "🧠",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 9,
      tagline: "Heap, punteros crudos, std::unique_ptr, std::move y RAII",
      project: "Bestiario V3 (Heap RAII)",
      description: "Comprensión del límite de la pila vs la inmensidad del Heap, punteros crudos observadores y gestión automática sin fugas con std::unique_ptr.",
      lessons: [
        { id: "L01", title: "Stack vs Heap", desc: "Límites de tamaño y revelación de la memoria dinámica." },
        { id: "L02", title: "Punteros Crudos (T*)", desc: "Variables de dirección, operador * y nullptr." },
        { id: "L03", title: "El Puntero Nulo", desc: "Detección y prevención de Segmentation Faults." },
        { id: "L04", title: "Asignación con new", desc: "Creación manual y veto absoluto a new[]." },
        { id: "L05", title: "Memory Leaks", desc: "La pérdida invisible de memoria por omitir delete." },
        { id: "L06", title: "Dangling Pointers", desc: "Uso de punteros tras ejecutar delete (Use-After-Free)." },
        { id: "L07", title: "RAII & std::unique_ptr", desc: "Gestión determinista con make_unique<T>()." },
        { id: "L08", title: "Movimiento (std::move)", desc: "Transferencia de propiedad única sin clonar recursos." },
        { id: "L09", title: "Mini-proyecto Bestiario V3", desc: "Gestión de entidades dinámicas 100% gobernadas por unique_ptr." }
      ],
      bugDemos: ["D03_NullPointerCrashBug.cpp", "D05_MemoryLeakBug.cpp", "D06_DanglingPointerBug.cpp"],
      keyDecision: "Veto absoluto a new[] y delete[]; adopción estricta de RAII con std::unique_ptr."
    },
    {
      id: "10",
      slug: "10_Classes",
      phase: "fase-5",
      phaseName: "Fase 5: POO Moderna",
      title: "Classes & Encapsulation",
      icon: "🏛️",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 10,
      tagline: "Encapsulamiento m_, const methods, operadores << y constructores",
      project: "Bestiario V4 (Multi-Archivo)",
      description: "Blindaje de invariantes de datos, privacidad por defecto, constructores con Member Initializer List, explicit y sobrecarga idiomática de operadores.",
      lessons: [
        { id: "L01", title: "Estado Inconsistente", desc: "Por qué los structs públicos permiten corromper invariantes." },
        { id: "L02", title: "El candado de class", desc: "Privacidad por defecto y nomenclatura estándar m_." },
        { id: "L03", title: "Métodos y const correctness", desc: "Métodos const invocados desde referencias inmutables." },
        { id: "L04", title: "Getters y Setters", desc: "Retorno seguro por const & y validación de rangos." },
        { id: "L05", title: "Member Initializer List", desc: "Inicialización segura, -Wreorder y calificador explicit." },
        { id: "L06", title: "Tell, Don't Ask", desc: "Por qué generar getters indiscriminados destruye el diseño OO." },
        { id: "L07", title: "Sobrecarga operator<<", desc: "Integración natural e idiomática con streams y comparaciones." },
        { id: "L08", title: "Clases Multi-Archivo", desc: "Interfaces en .h e implementaciones con Clase:: en .cpp." },
        { id: "L09", title: "Destructores y RAII", desc: "Limpieza determinista al expirar el ciclo de vida." },
        { id: "L10", title: "Mini-proyecto Bestiario V4", desc: "Clases POO robustas con operadores y destructores blindados." }
      ],
      bugDemos: ["D01_InconsistentStateBug.cpp", "D03_ConstMemberFunctionBug.cpp", "D05_InitOrderBug.cpp"],
      keyDecision: "Atributos estrictamente privados con m_ y constructores con Member Initializer List."
    },
    {
      id: "11",
      slug: "11_Inheritance",
      phase: "fase-5",
      phaseName: "Fase 5: POO Moderna",
      title: "Inheritance",
      icon: "🧬",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 7,
      tagline: "Herencia simple : public, protected, constructores y Object Slicing",
      project: "Jerarquía del Bestiario",
      description: "Reutilización de lógica con la relación IS-A, encapsulamiento en clases derivadas y la trampa destructiva del Object Slicing por valor.",
      lessons: [
        { id: "L01", title: "Anti-patrón Copiar/Pegar", desc: "El costo de duplicar lógica en entidades hermanas." },
        { id: "L02", title: "Herencia Simple (: public)", desc: "Relación IS-A y prevención de herencia privada accidental." },
        { id: "L03", title: "Visibilidad protected", desc: "Atributos privados protegidos con métodos controlados." },
        { id: "L04", title: "Cadenas de Constructores", desc: "Delegación obligatoria hacia el constructor base." },
        { id: "L05", title: "Ciclo de Vida en Herencia", desc: "Construcción Padre->Hijo y destrucción inversa Hijo->Padre." },
        { id: "L06", title: "Object Slicing", desc: "La trampa de almacenar clases derivadas por valor en vector<Base>." },
        { id: "L07", title: "Mini-proyecto Jerarquía", desc: "Árbol de 3 niveles: Entidad -> Monstruo -> Jefe." }
      ],
      bugDemos: ["D02b_PrivateInheritanceBug.cpp", "D04_ConstructorChainBug.cpp", "D06_ObjectSlicingBug.cpp"],
      keyDecision: "Veto absoluto a la herencia múltiple de implementación con estado."
    },
    {
      id: "12",
      slug: "12_Polymorphism",
      phase: "fase-5",
      phaseName: "Fase 5: POO Moderna",
      title: "Polymorphism",
      icon: "🎭",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 8,
      tagline: "virtual, VTable, override, destructor virtual, interfaces puras",
      project: "El Coliseo (Game Loop Polimórfico)",
      description: "Despacho dinámico en tiempo de ejecución, tabla virtual __vptr, sellado con final, colecciones con smart pointers y downcasting seguro.",
      lessons: [
        { id: "L01", title: "Enlace Estático (Early Binding)", desc: "Por qué el compilador enlaza al tipo del puntero." },
        { id: "L02", title: "virtual y la VTable", desc: "Despacho dinámico a través de la tabla virtual __vptr." },
        { id: "L03", title: "override y final", desc: "Red de seguridad para detectar errores de firma y sellar clases." },
        { id: "L04", title: "El Destructor Virtual", desc: "La fuga de memoria letal al destruir polimórficamente." },
        { id: "L05", title: "Interfaces Puras (= 0)", desc: "Contratos abstractos puros y herencia múltiple exclusiva." },
        { id: "L06", title: "Colecciones Polimórficas", desc: "vector<unique_ptr<Base>> y dynamic_cast seguro." },
        { id: "L07", title: "Impresión Polimórfica", desc: "operator<< delegando en virtual void imprimir() const." },
        { id: "L08", title: "Mini-proyecto El Coliseo", desc: "Game Loop de combate polimórfico sin if/else de tipo." }
      ],
      bugDemos: ["D01_StaticBindingBug.cpp", "D03_SilentTypoBug.cpp", "D04_VirtualDestructorLeakBug.cpp"],
      keyDecision: "Destructor virtual obligatorio (virtual ~Base() = default;) en toda jerarquía."
    },
    {
      id: "13",
      slug: "13_ErrorHandling",
      phase: "fase-6",
      phaseName: "Fase 6: Nivel Profesional",
      title: "Error Handling & Resilience",
      icon: "🛡️",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 7,
      tagline: "Stack Unwinding, excepciones de dominio, std::optional y noexcept",
      project: "Motor de Mazmorras Resiliente",
      description: "Manejo profesional de errores, desenrollado de pila con RAII, excepciones en constructores contra objetos zombi y alternativa ligera std::optional.",
      lessons: [
        { id: "L01", title: "Fragilidad de Códigos de Retorno", desc: "Errores silenciosos ignorados en producción." },
        { id: "L02", title: "Stack Unwinding & RAII", desc: "Destrucción automática de objetos en vuelo de excepción." },
        { id: "L03", title: "Jerarquía std::exception", desc: "Captura obligatoria por const std::exception& contra slicing." },
        { id: "L04", title: "Excepciones en Constructores", desc: "Abortar creación de objetos zombi inválidos." },
        { id: "L05", title: "std::optional (C++17)", desc: "Manejo idiomático de ausencias esperadas con std::nullopt." },
        { id: "L06", title: "Garantía de noexcept", desc: "Optimización crítica de relocalización en std::vector." },
        { id: "L07", title: "Mini-proyecto Motor Resiliente", desc: "Carga de mapas y archivos con recuperación ante corrupción." }
      ],
      bugDemos: ["D01_IgnoredReturnCodeBug.cpp", "D02_RawPointerLeakOnThrowBug.cpp", "D06_VectorCopyFallbackBug.cpp"],
      keyDecision: "Captura exclusiva por referencia constante; uso de std::optional para ausencias normales."
    },
    {
      id: "14",
      slug: "14_TemplatesAndLambdas",
      phase: "fase-6",
      phaseName: "Fase 6: Nivel Profesional",
      title: "Templates & Metaprogramming",
      icon: "📦",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 8,
      tagline: "Polimorfismo estático, templates en .hpp, NTTP y lambdas modernas",
      project: "Pipeline Genérico de Eventos",
      description: "Generación de código monomórfico en tiempo de compilación con cero costo en runtime, buffers contiguos con NTTP y funciones anónimas instantáneas.",
      lessons: [
        { id: "L01", title: "La Fábrica de Código", desc: "Polimorfismo estático vs dinámico (cero sobrecarga en runtime)." },
        { id: "L02", title: "Plantillas de Funciones", desc: "Deducción automática y plantillas multiparámetro." },
        { id: "L03", title: "La Trampa del Linker", desc: "Por qué las plantillas deben residir en cabeceras (.hpp)." },
        { id: "L04", title: "Plantillas de Clases", desc: "Contenedores genéricos con deducción automática CTAD." },
        { id: "L05", title: "Parámetros No-Tipo (NTTP)", desc: "Buffers estáticos contiguos en el Stack sin tocar el Heap." },
        { id: "L06", title: "Lambdas Modernas [](){}", desc: "Funciones anónimas como predicados de primer nivel." },
        { id: "L07", title: "Capturas en Lambdas", desc: "Trampa mortal del Use-After-Free al capturar por referencia." },
        { id: "L08", title: "Mini-proyecto Pipeline", desc: "Bus de eventos genérico desacoplado de alto rendimiento." }
      ],
      bugDemos: ["D02_TemplateDeductionBug.cpp", "D03_TemplateLinkerBug.cpp", "D07_DanglingLambdaCaptureBug.cpp"],
      keyDecision: "Templates obligatoriamente en archivos de cabecera (.hpp/.h)."
    },
    {
      id: "15",
      slug: "15_STLAlgorithms",
      phase: "fase-6",
      phaseName: "Fase 6: Nivel Profesional",
      title: "STL Algorithms & Ranges",
      icon: "⚡",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 8,
      tagline: "No Raw Loops, C++20 Ranges |, std::erase_if, Capstone Final",
      project: "El Motor RPG Definitivo (Capstone Final)",
      description: "Reemplazo de bucles manuales con algoritmos estándar, composición perezosa con tuberías |, tareas asíncronas con std::jthread y consolidación de los 15 módulos.",
      lessons: [
        { id: "L01", title: "Doctrina No Raw Loops", desc: "Reemplazo de bucles por all_of, any_of y count_if." },
        { id: "L02", title: "Invalidación de Iteradores", desc: "Prevención de Segfaults con std::erase_if de C++20." },
        { id: "L03", title: "Búsqueda y Predicados", desc: "std::find_if y min_element retornando std::optional." },
        { id: "L04", title: "Transformación y Reducción", desc: "Mapeo funcional con std::transform y std::accumulate." },
        { id: "L05", title: "Ordenamiento Avanzado", desc: "std::ranges::sort con comparadores multicriterio." },
        { id: "L06", title: "C++20 Ranges & Views", desc: "Evaluación perezosa sin vectores intermedios con tuberías |." },
        { id: "L07", title: "Concurrencia Básica", desc: "Ejecución en segundo plano con std::async y std::jthread." },
        { id: "L08", title: "Capstone Final del Curso", desc: "Arquitectura multi-archivo que consolida armónicamente los 15 módulos." }
      ],
      bugDemos: ["D01_RawLoopOffByOneBug.cpp", "D02_IteratorInvalidationBug.cpp", "D07_DataRaceIntroBug.cpp"],
      keyDecision: "Doctrina estricta 'No Raw Loops': privilegiar algoritmos estándar de la STL."
    }
  ];

  /* ==========================================================================
     2. TERMINAL SIMULATOR
     ========================================================================== */
  class TerminalSimulator {
    constructor(containerId) {
      this.container = document.getElementById(containerId);
      if (!this.container) return;

      this.history = [];
      this.historyIndex = -1;
      this.currentCode = `#include <iostream>

int main() {
    int oro_del_jugador{100};
    std::cout << "Bienvenido a LearningCpp!\\n";
    std::cout << "Oro inicial en Stack: " << oro_del_jugador << "\\n";
    return 0;
}`;
      this.isCompiled = false;
      this.init();
    }

    init() {
      this.render();
      this.bindEvents();
      this.printInitialBanner();
    }

    render() {
      this.container.innerHTML = `
        <div class="terminal-header">
          <div class="terminal-dots" aria-hidden="true">
            <span class="dot dot-red"></span>
            <span class="dot dot-yellow"></span>
            <span class="dot dot-green"></span>
          </div>
          <div class="terminal-title">bash — LearningCpp Shell v2.0 (g++ 13.2 C++17/20)</div>
          <div style="font-size: 0.75rem; color: var(--text-muted);" aria-hidden="true">x86_64</div>
        </div>
        <div class="terminal-body" id="term-output" role="log" aria-live="polite"></div>
        <div class="terminal-interactive-bar">
          <span class="terminal-prompt" aria-hidden="true">user@learningcpp:~$</span>
          <input type="text" id="term-input" autocomplete="off" spellcheck="false" 
            placeholder="Prueba: 'compile', 'run', 'help', o 'modules'..." 
            style="flex: 1; background: transparent; border: none; color: #fff; font-family: var(--font-family-mono); font-size: 0.85rem; outline: none;" 
            aria-label="Línea de comandos de la terminal C++" />
          <button id="term-send-btn" class="btn btn-primary" style="padding: 0.25rem 0.75rem; font-size: 0.75rem;">Ejecutar</button>
        </div>
      `;
    }

    bindEvents() {
      const input = this.container.querySelector('#term-input');
      const sendBtn = this.container.querySelector('#term-send-btn');

      const handleCommand = () => {
        const val = input.value.trim();
        if (!val) return;
        this.history.push(val);
        this.historyIndex = this.history.length;
        this.execute(val);
        input.value = '';
      };

      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          handleCommand();
        } else if (e.key === 'ArrowUp') {
          if (this.historyIndex > 0) {
            this.historyIndex--;
            input.value = this.history[this.historyIndex];
          }
        } else if (e.key === 'ArrowDown') {
          if (this.historyIndex < this.history.length - 1) {
            this.historyIndex++;
            input.value = this.history[this.historyIndex];
          } else {
            this.historyIndex = this.history.length;
            input.value = '';
          }
        }
      });

      sendBtn.addEventListener('click', handleCommand);
    }

    printInitialBanner() {
      this.printLine('user@learningcpp:~$ ', 'cat welcome.txt', 'prompt-cmd');
      this.printLine('', '🚀 Entorno interactivo de compilación C++17/20 listo.', 'terminal-out-info');
      this.printLine('', 'Escribe "compile" para compilar tu primer programa o "help" para ver comandos.', 'terminal-out-info');
    }

    printLine(prefix, text, className = '') {
      const output = this.container.querySelector('#term-output');
      if (!output) return;

      const line = document.createElement('div');
      line.className = 'terminal-line';
      
      if (prefix) {
        const promptSpan = document.createElement('span');
        promptSpan.className = 'terminal-prompt';
        promptSpan.textContent = prefix;
        line.appendChild(promptSpan);
      }

      const textSpan = document.createElement('span');
      if (className) textSpan.className = className;
      textSpan.textContent = text;
      line.appendChild(textSpan);

      output.appendChild(line);
      output.scrollTop = output.scrollHeight;
    }

    execute(cmd) {
      this.printLine('user@learningcpp:~$ ', cmd, 'cmd-text');
      const lower = cmd.toLowerCase().trim();

      if (lower === 'clear' || lower === 'cls') {
        const output = this.container.querySelector('#term-output');
        if (output) output.innerHTML = '';
        return;
      }

      if (lower === 'help') {
        this.printLine('', 'Comandos disponibles:', 'terminal-out-info');
        this.printLine('', '  compile | g++     - Compila el programa actual con C++17 y warnings (-Wall -Wextra)', 'terminal-out-info');
        this.printLine('', '  run | ./app       - Ejecuta el binario compilado', 'terminal-out-info');
        this.printLine('', '  cat main.cpp      - Muestra el código fuente actual', 'terminal-out-info');
        this.printLine('', '  modules           - Lista los 15 módulos del plan de estudios', 'terminal-out-info');
        this.printLine('', '  test bug          - Simula la detonación de un Undefined Behavior', 'terminal-out-info');
        this.printLine('', '  clear             - Limpia la pantalla de la terminal', 'terminal-out-info');
        return;
      }

      if (lower.startsWith('g++') || lower === 'compile') {
        this.printLine('', '[INFO] g++ -std=c++17 -Wall -Wextra -O2 main.cpp -o app', 'terminal-out-info');
        setTimeout(() => {
          this.printLine('', '✔ Compilación exitosa con C++17 (0 errores, 0 warnings). Binario generado: app.exe', 'terminal-out-success');
          this.isCompiled = true;
        }, 150);
        return;
      }

      if (lower === './app' || lower === 'run' || lower === '.\\app.exe') {
        if (!this.isCompiled) {
          this.printLine('', 'bash: ./app: No such file or directory. Debes compilar primero con "compile".', 'terminal-out-error');
          return;
        }
        this.printLine('', '--- EJECUTANDO ./app ---', 'terminal-out-info');
        this.printLine('', 'Bienvenido a LearningCpp!', 'terminal-out-success');
        this.printLine('', 'Oro inicial en Stack: 100', 'terminal-out-success');
        this.printLine('', '[Proceso finalizado con código de salida: 0 (0x0)]', 'terminal-out-info');
        return;
      }

      if (lower === 'cat main.cpp' || lower === 'cat') {
        this.printLine('', this.currentCode, 'terminal-out-info');
        return;
      }

      if (lower === 'modules') {
        this.printLine('', '=== PLAN DE ESTUDIOS LEARNINGCPP (15 MÓDULOS) ===', 'terminal-out-info');
        this.printLine('', 'Fase 1: M01 (Getting Started) | M02 (Fundamental Types) | M03 (Scope & Control Flow)', 'terminal-out-success');
        this.printLine('', 'Fase 2: M04 (Functions) | M05 (Constants & Strings)', 'terminal-out-success');
        this.printLine('', 'Fase 3: M06 (Arrays & Vectors) | M07 (Compound Types)', 'terminal-out-warn');
        this.printLine('', 'Fase 4: M08 (References & Addresses) | M09 (Dynamic Memory & RAII)', 'terminal-out-warn');
        this.printLine('', 'Fase 5: M10 (Classes) | M11 (Inheritance) | M12 (Polymorphism)', 'terminal-out-warn');
        this.printLine('', 'Fase 6: M13 (Error Handling) | M14 (Templates) | M15 (STL Algorithms & Capstone)', 'terminal-out-warn');
        return;
      }

      if (lower === 'test bug') {
        this.printLine('', '[ALERTA] Detonando D03_IntegerDivisionBug.cpp...', 'terminal-out-warn');
        this.printLine('', 'Calculando division entera: 7 / 2 = 3 (PERDIDA DE PRECISION CRITICA)', 'terminal-out-error');
        this.printLine('', 'Solucion moderna aplicada: static_cast<double>(7) / 2 = 3.5', 'terminal-out-success');
        return;
      }

      this.printLine('', `bash: ${cmd}: orden no encontrada. Escribe "help" para ver la lista de comandos.`, 'terminal-out-error');
    }
  }

  /* ==========================================================================
     3. CODE PLAYGROUND ("BREAK-FIRST, FIX-LATER")
     ========================================================================== */
  const BUGS_DATA = [
    {
      id: "division",
      title: "1. La Trampa de la División Entera (7 / 2 = 3)",
      topic: "Tipos Fundamentales & Casting",
      module: "M02 (Fundamental Types - L03/L05)",
      brokenSnippet: `// ❌ FALLO CLÁSICO: División entera truncada
#include <iostream>

int main() {
    int total_cuenta{70};
    int amigos{20};
    
    // El hardware ejecuta división entera truncando los decimales
    double por_persona = total_cuenta / amigos; // 70 / 20 = 3.0 (ERROR LÓGICO)
    
    std::cout << "Monto por persona: $" << por_persona << '\\n'; 
    // Muestra $3 en lugar de $3.5 (Faltan $10 en total)
    return 0;
}`,
      fixedSnippet: `// ✅ SOLUCIÓN MODERNA: Casting explícito en compilación
#include <iostream>

int main() {
    int total_cuenta{70};
    int amigos{20};
    
    // static_cast promueve explícitamente a double antes de la división
    double por_persona{ static_cast<double>(total_cuenta) / amigos };
    
    std::cout << "Monto exacto: $" << por_persona << '\\n'; 
    // Muestra $3.5 de forma exacta sin pérdidas
    return 0;
}`,
      explanation: "En C++, cuando ambos operandos son enteros, el operador `/` descarta silenciosamente los decimales. Con `static_cast<double>()` forzamos la división en punto flotante sin recurrir a C-casts inseguros."
    },
    {
      id: "passbyvalue",
      title: "2. Pass-by-value: La Trampa del Clon Aislado",
      topic: "Funciones & Memoria en Stack",
      module: "M04 (Functions - L04) & M08",
      brokenSnippet: `// ❌ FALLO CLÁSICO: Mutar una copia aislada
#include <iostream>

void duplicarOro(int cantidad) {
    // Esta variable es un CLON en una nueva dirección del Stack
    cantidad = cantidad * 2; 
}

int main() {
    int oro{100};
    duplicarOro(oro);
    
    // El oro original jamás cambió en el main
    std::cout << "Oro: " << oro << '\\n'; // Imprime 100
    return 0;
}`,
      fixedSnippet: `// ✅ SOLUCIÓN MODERNA: Paso por referencia (Zero-Copy)
#include <iostream>

// El operador '&' enlaza directamente con la dirección de memoria original
void duplicarOro(int& cantidad) {
    cantidad = cantidad * 2; // Muta directamente la variable original
}

int main() {
    int oro{100};
    duplicarOro(oro);
    
    std::cout << "Oro mutado: " << oro << '\\n'; // Imprime 200
    return 0;
}`,
      explanation: "Por defecto, C++ clona cada argumento en el Stack (Pass-by-value). Con referencias `&` creamos un alias directo a la memoria física original, eliminando copias pesadas."
    },
    {
      id: "uninitialized",
      title: "3. La Variable sin Inicializar (Basura en RAM)",
      topic: "Inicialización Uniforme {}",
      module: "M01 (Getting Started - L05)",
      brokenSnippet: `// ❌ FALLO CLÁSICO: Basura residual en el Stack
#include <iostream>

int main() {
    int vidas_jugador; // ¡Memoria sin inicializar!
    
    // Lee lo que sea que estuviese antes en esa dirección física
    std::cout << "Vidas: " << vidas_jugador << '\\n'; 
    // Salida impredecible (Undefined Behavior): ej. 4201952 o crasheo
    return 0;
}`,
      fixedSnippet: `// ✅ SOLUCIÓN MODERNA: Inicialización uniforme {}
#include <iostream>

int main() {
    // Las llaves garantizan inicialización inmediata por defecto (0)
    int vidas_jugador{3}; 
    
    std::cout << "Vidas garantizadas: " << vidas_jugador << '\\n'; 
    // Siempre imprime 3 limpiamente
    return 0;
}`,
      explanation: "Declarar variables primitivas sin inicializar es una de las causas #1 de bugs de seguridad. C++17/20 impone la inicialización uniforme con llaves `{}`."
    },
    {
      id: "slicing",
      title: "4. Object Slicing: Destrucción de Datos en Polimorfismo",
      topic: "Herencia & Polimorfismo",
      module: "M11 (Inheritance - L06) & M12",
      brokenSnippet: `// ❌ FALLO CLÁSICO: Almacenar derivadas por valor
#include <iostream>
#include <vector>

class Base { public: virtual void atacar() { std::cout << "Base\\n"; } };
class Jefe : public Base { public: int vidaExtra{500}; void atacar() override { std::cout << "Jefe\\n"; } };

int main() {
    std::vector<Base> enemigos;
    enemigos.push_back(Jefe{}); // 💥 SLICING: 'vidaExtra' es recortada y destruida
    enemigos[0].atacar(); // Llama a Base::atacar en vez de Jefe::atacar
}
`,
      fixedSnippet: `// ✅ SOLUCIÓN MODERNA: Punteros inteligentes polimórficos
#include <iostream>
#include <vector>
#include <memory>

class Base { public: virtual void atacar() const = 0; virtual ~Base() = default; };
class Jefe : public Base { public: void atacar() const override { std::cout << "Ataque de Jefe!\\n"; } };

int main() {
    std::vector<std::unique_ptr<Base>> enemigos;
    enemigos.push_back(std::make_unique<Jefe>());
    
    enemigos[0]->atacar(); // Despacho dinámico VTable perfecto
}
`,
      explanation: "Guardar objetos derivados por valor en contenedores base recorta (*slices*) los campos especializados. La solución idiomática es `std::vector<std::unique_ptr<Base>>` con destructores virtuales."
    }
  ];

  class CodePlayground {
    constructor(containerId) {
      this.container = document.getElementById(containerId);
      if (!this.container) return;
      this.currentBugIndex = 0;
      this.init();
    }

    init() {
      this.render();
      this.bindEvents();
    }

    render() {
      const bug = BUGS_DATA[this.currentBugIndex];
      this.container.innerHTML = `
        <div class="playground-header">
          <div class="playground-title-area">
            <span class="badge badge-amber">${bug.module}</span>
            <h3 class="playground-title">${bug.title}</h3>
          </div>
          <div class="bug-tabs-scroll" role="tablist" aria-label="Selector de Bugs Educativos">
            ${BUGS_DATA.map((b, idx) => `
              <button class="btn btn-secondary bug-tab-btn ${idx === this.currentBugIndex ? 'active' : ''}" data-index="${idx}" role="tab" aria-selected="${idx === this.currentBugIndex}" style="${idx === this.currentBugIndex ? 'background: var(--text-primary); color: var(--text-inverse); font-weight: 700;' : ''}">
                Bug #${idx + 1}
              </button>
            `).join('')}
          </div>
        </div>

        <div class="diff-container">
          <!-- 1. Break-First Box -->
          <div class="diff-box">
            <div class="diff-header broken">
              <div class="diff-title-wrap">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>
                <span>1. Break-First: Código Roto</span>
              </div>
              <span class="diff-tag">Error / Bug Lógico</span>
            </div>
            <pre><code class="language-cpp">${this.escapeHtml(bug.brokenSnippet)}</code></pre>
          </div>

          <!-- 2. Fix-Later Box -->
          <div class="diff-box">
            <div class="diff-header fixed">
              <div class="diff-title-wrap">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                <span>2. Fix-Later: Solución C++17/20</span>
              </div>
              <span class="diff-tag">Seguro & Idiomático</span>
            </div>
            <pre><code class="language-cpp">${this.escapeHtml(bug.fixedSnippet)}</code></pre>
          </div>
        </div>

        <div class="playground-explanation-box">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: var(--space-2); color: var(--brand-primary); font-weight: 700; font-size: var(--font-size-sm);">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>
            <span>Modelo Mental & Hardware (Por qué ocurre)</span>
          </div>
          <p style="font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.6; margin: 0;">${bug.explanation}</p>
        </div>
      `;
    }

    escapeHtml(str) {
      return str
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
    }

    bindEvents() {
      this.container.querySelectorAll('.bug-tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const idx = parseInt(btn.dataset.index, 10);
          this.currentBugIndex = idx;
          this.render();
          this.bindEvents();
        });
      });
    }
  }

  /* ==========================================================================
     4. MODULES EXPLORER & MODAL
     ========================================================================== */
  class ModulesExplorer {
    constructor(containerId, modalId) {
      this.container = document.getElementById(containerId);
      this.modal = document.getElementById(modalId);
      this.activePhase = 'fase-1'; // Focused default: Phase 1 (3 clean cards)
      this.searchQuery = '';
      
      if (this.container) {
        this.init();
      }
    }

    init() {
      this.renderTabs();
      this.renderModules();
      this.bindEvents();
    }

    renderTabs() {
      const tabsContainer = document.getElementById('phase-tabs-container');
      if (!tabsContainer) return;

      tabsContainer.innerHTML = PHASES.map(p => `
        <button class="tab-btn ${p.id === this.activePhase ? 'active' : ''}" data-phase="${p.id}" role="tab" aria-selected="${p.id === this.activePhase}">
          ${p.name} <span style="opacity: 0.6; font-size: 0.8em; margin-left: 3px;">(${p.count})</span>
        </button>
      `).join('');
    }

    renderModules() {
      const currentPhase = PHASES.find(p => p.id === this.activePhase) || PHASES[0];
      const filtered = MODULES.filter(m => {
        const matchesPhase = this.activePhase === 'all' || m.phase === this.activePhase;
        const query = this.searchQuery.toLowerCase();
        const matchesQuery = !query || 
          m.title.toLowerCase().includes(query) ||
          m.tagline.toLowerCase().includes(query) ||
          m.description.toLowerCase().includes(query) ||
          m.lessons.some(l => l.title.toLowerCase().includes(query) || l.desc.toLowerCase().includes(query));
        return matchesPhase && matchesQuery;
      });

      if (filtered.length === 0) {
        this.container.innerHTML = `
          <div style="grid-column: 1 / -1; text-align: center; padding: var(--space-12); background: var(--bg-card); border-radius: var(--radius-xl); border: 1px dashed var(--border-strong);">
            <div style="font-size: 2.5rem; margin-bottom: var(--space-3);" aria-hidden="true">🔍</div>
            <h3>No se encontraron módulos</h3>
            <p class="text-muted" style="margin-top: var(--space-2);">Intenta buscar con otros términos (ej: 'punteros', 'vector', 'templates', 'casting').</p>
          </div>
        `;
        return;
      }

      // Calculate phase navigation indices
      const phaseList = PHASES.filter(p => p.id !== 'all');
      const currentIdx = phaseList.findIndex(p => p.id === this.activePhase);
      const prevPhase = currentIdx > 0 ? phaseList[currentIdx - 1] : null;
      const nextPhase = currentIdx >= 0 && currentIdx < phaseList.length - 1 ? phaseList[currentIdx + 1] : null;

      const totalLessonsInView = filtered.reduce((acc, m) => acc + m.lessonsCount, 0);

      const heroStripHtml = `
        <div class="phase-hero-strip" style="grid-column: 1 / -1;">
          <div>
            <div class="phase-hero-title">${currentPhase.name}</div>
            <div class="phase-hero-desc">${currentPhase.subtitle}</div>
          </div>
          <div class="phase-hero-count">
            <strong>${filtered.length}</strong> módulos · <strong>${totalLessonsInView}</strong> lecciones
          </div>
        </div>
      `;

      const cardsHtml = filtered.map(m => `
        <article class="module-card fade-in-up" data-module-id="${m.id}" tabindex="0" role="button" aria-label="Módulo ${m.id}: ${m.title}. Haz clic para ver detalles.">
          <div class="card-top">
            <span class="module-id-badge">${m.id}</span>
            <span class="status-indicator ${m.status}">
              <span class="status-dot"></span>
              ${m.status === 'completed' ? 'Disponible' : 'Próximamente'}
            </span>
          </div>

          <div class="card-main">
            <div class="module-phase-tag">${m.phaseName}</div>
            <h3 class="module-title">${m.title}</h3>
            <p class="module-desc">${m.tagline}</p>
          </div>

          <div class="card-bottom">
            <div class="module-meta">
              <span class="meta-item">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                ${m.lessonsCount} lecs
              </span>
              <span class="meta-sep">·</span>
              <span class="meta-project" title="${m.project}">${m.project}</span>
            </div>
            <span class="card-arrow" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </span>
          </div>
        </article>
      `).join('');

      const navFooterHtml = (this.activePhase !== 'all') ? `
        <div class="phase-nav-footer">
          ${prevPhase ? `
            <button class="btn btn-secondary btn-switch-phase" data-target-phase="${prevPhase.id}" style="font-size: var(--font-size-xs);">
              &larr; ${prevPhase.name}
            </button>
          ` : `<div></div>`}
          ${nextPhase ? `
            <button class="btn btn-primary btn-switch-phase" data-target-phase="${nextPhase.id}" style="font-size: var(--font-size-xs);">
              ${nextPhase.name} &rarr;
            </button>
          ` : `
            <button class="btn btn-secondary btn-switch-phase" data-target-phase="all" style="font-size: var(--font-size-xs);">
              Ver Todos los Módulos &rarr;
            </button>
          `}
        </div>
      ` : '';

      this.container.innerHTML = heroStripHtml + cardsHtml + navFooterHtml;
    }

    bindEvents() {
      const tabsContainer = document.getElementById('phase-tabs-container');
      if (tabsContainer) {
        tabsContainer.addEventListener('click', (e) => {
          const btn = e.target.closest('.tab-btn');
          if (!btn) return;
          this.activePhase = btn.dataset.phase;
          this.renderTabs();
          this.renderModules();
        });
      }

      const searchInput = document.getElementById('modules-search-input');
      if (searchInput) {
        searchInput.addEventListener('input', (e) => {
          this.searchQuery = e.target.value.trim();
          if (this.searchQuery) {
            this.activePhase = 'all'; // Auto switch to all when searching
            this.renderTabs();
          }
          this.renderModules();
        });
      }

      // Event Delegation for module clicks & phase navigation buttons
      this.container.addEventListener('click', (e) => {
        const switchBtn = e.target.closest('.btn-switch-phase');
        if (switchBtn) {
          this.activePhase = switchBtn.dataset.targetPhase;
          this.renderTabs();
          this.renderModules();
          const targetElem = document.getElementById('temario');
          if (targetElem) {
            targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
          return;
        }

        const card = e.target.closest('.module-card');
        if (!card) return;
        this.handleSelectModule(card.dataset.moduleId);
      });

      this.container.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          const card = e.target.closest('.module-card');
          if (card) {
            e.preventDefault();
            this.handleSelectModule(card.dataset.moduleId);
          }
        }
      });

      if (this.modal) {
        this.modal.addEventListener('click', (e) => {
          if (e.target === this.modal || e.target.closest('.modal-close-btn')) {
            this.closeModal();
          }
        });

        document.addEventListener('keydown', (e) => {
          if (e.key === 'Escape' && this.modal.classList.contains('open')) {
            this.closeModal();
          }
        });
      }
    }

    handleSelectModule(modId) {
      const mod = MODULES.find(m => m.id === modId);
      if (mod) {
        this.openModal(mod);
      }
    }

    openModal(mod) {
      if (!this.modal) return;
      const modalTitle = this.modal.querySelector('#modal-module-title');
      const modalContent = this.modal.querySelector('#modal-module-body');

      modalTitle.innerHTML = `
        <div style="display: flex; align-items: center; gap: var(--space-3);">
          <span class="module-id-badge" style="font-size: 0.9rem; padding: 0.25rem 0.6rem;">${mod.id}</span>
          <div>
            <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-family: var(--font-family-mono); text-transform: uppercase; letter-spacing: 0.05em;">
              ${mod.phaseName}
            </div>
            <h2 style="font-size: var(--font-size-xl); font-family: var(--font-family-display); font-weight: 700; margin-top: 2px;">${mod.title}</h2>
          </div>
        </div>
      `;

      modalContent.innerHTML = `
        <div style="margin-bottom: var(--space-5);">
          <p style="color: var(--text-secondary); font-size: var(--font-size-sm); line-height: 1.6;">
            ${mod.description}
          </p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-3); margin-bottom: var(--space-5);">
          <div style="background: var(--bg-surface); padding: var(--space-3) var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <div style="font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em;">Proyecto Integrador</div>
            <div style="font-weight: 600; font-size: var(--font-size-sm); margin-top: 2px; color: var(--text-primary);">
              ${mod.project}
            </div>
          </div>
          <div style="background: var(--bg-surface); padding: var(--space-3) var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <div style="font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em;">Estado del Módulo</div>
            <div style="font-weight: 600; font-size: var(--font-size-sm); margin-top: 2px; display: flex; align-items: center; gap: 6px; color: ${mod.status === 'completed' ? 'var(--color-success)' : 'var(--text-muted)'};">
              <span class="status-dot" style="background: ${mod.status === 'completed' ? 'var(--color-success)' : 'var(--zinc-600)'};"></span>
              ${mod.status === 'completed' ? 'Listo para estudiar' : 'En desarrollo'}
            </div>
          </div>
        </div>

        <h4 style="font-size: var(--font-size-sm); font-family: var(--font-family-display); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: var(--space-3); color: var(--text-primary); display: flex; justify-content: space-between; align-items: center;">
          <span>Lecciones del Módulo (${mod.lessons.length})</span>
          <span style="font-size: 0.72rem; color: var(--text-muted); font-weight: normal; font-family: var(--font-family-body);">Marca tus lecciones completadas</span>
        </h4>
        <div style="display: flex; flex-direction: column; gap: var(--space-2); margin-bottom: var(--space-5);">
          ${mod.lessons.map(l => {
            const isDone = window.__progressTracker && window.__progressTracker.isCompleted(mod.id, l.id);
            return `
              <div style="display: flex; justify-content: space-between; align-items: center; gap: var(--space-3); padding: var(--space-3); background: var(--bg-surface); border-radius: var(--radius-md); border: 1px solid var(--border-subtle); flex-wrap: wrap;">
                <div style="display: flex; gap: var(--space-3); align-items: flex-start; flex: 1; min-width: 200px;">
                  <span style="font-family: var(--font-family-mono); font-size: 0.75rem; color: var(--text-primary); font-weight: 700; padding: 2px 6px; background: var(--bg-muted); border: 1px solid var(--border-subtle); border-radius: 4px; height: fit-content;">
                    ${l.id}
                  </span>
                  <div>
                    <div style="font-weight: 600; font-size: var(--font-size-sm); color: var(--text-primary); text-decoration: ${isDone ? 'line-through' : 'none'}; opacity: ${isDone ? '0.7' : '1'};">${l.title}</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 2px;">${l.desc}</div>
                  </div>
                </div>
                <button class="lesson-check-btn ${isDone ? 'completed' : ''}" data-mod-id="${mod.id}" data-lesson-id="${l.id}" aria-label="Marcar lección ${l.id}">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <span>${isDone ? 'Completada' : 'Marcar'}</span>
                </button>
              </div>
            `;
          }).join('')}
        </div>

        ${mod.bugDemos && mod.bugDemos.length > 0 ? `
          <h4 style="font-size: var(--font-size-sm); font-family: var(--font-family-display); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: var(--space-3); color: var(--text-primary);">
            Demos de Bugs Intencionales (Break-First)
          </h4>
          <div style="display: flex; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-5);">
            ${mod.bugDemos.map(b => `
              <span style="font-family: var(--font-family-mono); font-size: 0.75rem; background: var(--bg-surface); border: 1px solid var(--border-subtle); padding: 4px 8px; border-radius: 4px; color: var(--text-secondary);">
                ${b}
              </span>
            `).join('')}
          </div>
        ` : ''}

        <div style="padding: var(--space-4); background: var(--bg-surface); border-radius: var(--radius-md); border-left: 3px solid var(--text-primary);">
          <div style="font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600;">Decisión Arquitectónica Clave</div>
          <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: 4px; line-height: 1.5;">${mod.keyDecision}</p>
        </div>
      `;

      // Bind lesson check button clicks inside modal
      modalContent.querySelectorAll('.lesson-check-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
          const modId = btn.dataset.modId;
          const lessonId = btn.dataset.lessonId;
          if (window.__progressTracker) {
            window.__progressTracker.toggleLesson(modId, lessonId);
            this.openModal(mod); // Re-render modal to reflect status
          }
        });
      });

      this.modal.classList.add('open');
      this.modal.setAttribute('aria-hidden', 'false');
    }

    closeModal() {
      if (!this.modal) return;
      this.modal.classList.remove('open');
      this.modal.setAttribute('aria-hidden', 'true');
    }
  }

  /* ==========================================================================
     5. RAM & HARDWARE VISUALIZER
     ========================================================================== */
  class RamVisualizer {
    constructor(containerId) {
      this.container = document.getElementById(containerId);
      if (!this.container) return;

      this.stackVariables = [
        { name: "int vidas_jugador{3}", address: "0x7ffee14b8a08", value: "3", size: "4 bytes", type: "int" }
      ];
      this.heapBlocks = [];

      this.init();
    }

    init() {
      this.render();
      this.bindEvents();
    }

    render() {
      this.container.innerHTML = `
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-xl); overflow: hidden;">
          
          <!-- Controls Bar -->
          <div class="ram-controls-bar">
            <div>
              <span style="font-family: var(--font-family-mono); font-size: 0.75rem; color: var(--zinc-400); text-transform: uppercase; letter-spacing: 0.05em;">Simulador de Memoria Física (x86_64 RAM)</span>
              <h4 style="font-size: var(--font-size-base); margin-top: 2px;">Inspección en Tiempo Real: Stack vs Heap & Ciclo RAII</h4>
            </div>
            <div class="ram-buttons-group">
              <button id="ram-btn-push-stack" class="btn btn-secondary ram-btn">
                + Push Stack
              </button>
              <button id="ram-btn-alloc-heap" class="btn btn-secondary ram-btn">
                + make_unique&lt;T&gt;
              </button>
              <button id="ram-btn-scope-exit" class="btn btn-secondary ram-btn" style="color: var(--color-warning);">
                ⚡ Salir de Ámbito {}
              </button>
              <button id="ram-btn-reset" class="btn btn-secondary ram-btn">
                ↺ Reset
              </button>
            </div>
          </div>

          <!-- Visual Memory Layout -->
          <div class="ram-memory-grid">
            
            <!-- Stack Memory -->
            <div style="background: var(--bg-surface); padding: var(--space-5);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
                <span style="font-weight: 600; font-size: 0.85rem; display: flex; align-items: center; gap: 6px;">
                  <span style="width: 8px; height: 8px; border-radius: 50%; background: #3b82f6;" aria-hidden="true"></span>
                  STACK (Pila de Ejecución)
                </span>
                <span style="font-family: var(--font-family-mono); font-size: 0.7rem; color: var(--zinc-500);">LIFO · Automática</span>
              </div>

              <div id="ram-stack-list" style="display: flex; flex-direction: column; gap: var(--space-2);">
                ${this.stackVariables.map(v => `
                  <div class="fade-in-up" style="background: rgba(59, 130, 246, 0.08); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: var(--radius-md); padding: var(--space-3); font-family: var(--font-family-mono); font-size: 0.75rem;">
                    <div style="display: flex; justify-content: space-between; color: #93c5fd; font-weight: 600; flex-wrap: wrap; gap: 4px;">
                      <span>${v.name}</span>
                      <span>${v.address}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; color: var(--zinc-400); margin-top: 4px; flex-wrap: wrap; gap: 4px;">
                      <span>Valor: <strong style="color: #fff;">${v.value}</strong></span>
                      <span>${v.size}</span>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>

            <!-- Heap Memory -->
            <div style="background: var(--bg-surface); padding: var(--space-5);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
                <span style="font-weight: 600; font-size: 0.85rem; display: flex; align-items: center; gap: 6px;">
                  <span style="width: 8px; height: 8px; border-radius: 50%; background: #10b981;" aria-hidden="true"></span>
                  HEAP (Memoria Dinámica)
                </span>
                <span style="font-family: var(--font-family-mono); font-size: 0.7rem; color: var(--zinc-500);">RAII Smart Pointers</span>
              </div>

              <div id="ram-heap-list" style="display: flex; flex-direction: column; gap: var(--space-2);">
                ${this.heapBlocks.length === 0 ? `
                  <div style="border: 1px dashed var(--border-strong); border-radius: var(--radius-md); padding: var(--space-6); text-align: center; color: var(--zinc-500); font-size: 0.75rem; font-family: var(--font-family-mono);">
                    [ Heap Vacío — Cero fugas ]<br>
                    Pulsa "+ make_unique" para crear memoria dinámica
                  </div>
                ` : this.heapBlocks.map(b => `
                  <div class="fade-in-up" style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: var(--radius-md); padding: var(--space-3); font-family: var(--font-family-mono); font-size: 0.75rem;">
                    <div style="display: flex; justify-content: space-between; color: #6ee7b7; font-weight: 600; flex-wrap: wrap; gap: 4px;">
                      <span>${b.name}</span>
                      <span>${b.address}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; color: var(--zinc-400); margin-top: 4px; flex-wrap: wrap; gap: 4px;">
                      <span>Propietario RAII: <strong style="color: #93c5fd;">${b.owner}</strong></span>
                      <span>${b.size}</span>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>

          </div>

          <!-- Log Bar -->
          <div id="ram-log-bar" style="padding: var(--space-3) var(--space-6); background: #11161d; border-top: 1px solid var(--border-subtle); font-family: var(--font-family-mono); font-size: 0.75rem; color: var(--zinc-400);" role="status" aria-live="polite">
            <span style="color: var(--text-primary); font-weight: 600;">[SYS_LOG]</span> Estado actual: 1 variable en Stack (0x7ffee14b8a08), 0 bloques dinámicos en Heap.
          </div>
        </div>
      `;
    }

    bindEvents() {
      const btnPush = this.container.querySelector('#ram-btn-push-stack');
      const btnAlloc = this.container.querySelector('#ram-btn-alloc-heap');
      const btnScope = this.container.querySelector('#ram-btn-scope-exit');
      const btnReset = this.container.querySelector('#ram-btn-reset');

      if (btnPush) {
        btnPush.addEventListener('click', () => {
          const id = this.stackVariables.length + 1;
          const hex = (0x7ffee14b8a08 + id * 8).toString(16);
          this.stackVariables.push({
            name: `double ataque{${(id * 14.5).toFixed(1)}}`,
            address: `0x${hex}`,
            value: `${(id * 14.5).toFixed(1)}`,
            size: "8 bytes",
            type: "double"
          });
          this.render();
          this.bindEvents();
          this.updateLog(`Push en Stack: variable 'ataque' alojada en 0x${hex} (+8 bytes).`);
        });
      }

      if (btnAlloc) {
        btnAlloc.addEventListener('click', () => {
          const id = this.heapBlocks.length + 1;
          const heapHex = (0x600003a201b0 + id * 32).toString(16);
          const stackHex = (0x7ffee14b8a50 + id * 8).toString(16);

          this.stackVariables.push({
            name: `std::unique_ptr<Monstruo> p${id}`,
            address: `0x${stackHex}`,
            value: `-> 0x${heapHex}`,
            size: "8 bytes (ptr)",
            type: "smart_ptr"
          });

          this.heapBlocks.push({
            id: id,
            name: `Monstruo { hp: ${100 * id}, nivel: ${id} }`,
            address: `0x${heapHex}`,
            owner: `p${id} (Stack)`,
            size: "32 bytes"
          });

          this.render();
          this.bindEvents();
          this.updateLog(`Asignación dinámica: std::make_unique<Monstruo>() asignó 32 bytes en Heap (0x${heapHex}) gobernados por p${id} en Stack.`);
        });
      }

      if (btnScope) {
        btnScope.addEventListener('click', () => {
          if (this.stackVariables.length <= 1 && this.heapBlocks.length === 0) {
            this.updateLog("No hay variables temporales de ámbito que liberar.");
            return;
          }

          const freedHeap = this.heapBlocks.length;
          this.heapBlocks = [];
          this.stackVariables = [this.stackVariables[0]];

          this.render();
          this.bindEvents();
          this.updateLog(`⚡ Cierre de bloque {}: El Stack Unwinding destruyó las variables locales y RAII liberó automáticamente ${freedHeap} bloque(s) en el Heap sin fugas (delete implícito).`);
        });
      }

      if (btnReset) {
        btnReset.addEventListener('click', () => {
          this.stackVariables = [
            { name: "int vidas_jugador{3}", address: "0x7ffee14b8a08", value: "3", size: "4 bytes", type: "int" }
          ];
          this.heapBlocks = [];
          this.render();
          this.bindEvents();
          this.updateLog("Memoria reinicializada al estado base.");
        });
      }
    }

    updateLog(msg) {
      const logBar = this.container.querySelector('#ram-log-bar');
      if (logBar) {
        logBar.innerHTML = `<span style="color: var(--text-primary); font-weight: 600;">[SYS_LOG]</span> ${msg}`;
      }
    }
  }

  /* ==========================================================================
     6. STUDENT LOCAL PROGRESS TRACKER
     ========================================================================== */
  class ProgressTracker {
    constructor(containerId) {
      this.container = document.getElementById(containerId);
      this.storageKey = 'learningcpp_completed_lessons_v1';
      this.totalLessons = MODULES.reduce((acc, m) => acc + m.lessonsCount, 0); // 117
      this.completedLessons = this.load();
      this.init();
    }

    load() {
      try {
        const data = localStorage.getItem(this.storageKey);
        return data ? new Set(JSON.parse(data)) : new Set();
      } catch {
        return new Set();
      }
    }

    save() {
      try {
        localStorage.setItem(this.storageKey, JSON.stringify(Array.from(this.completedLessons)));
      } catch {}
    }

    toggleLesson(modId, lessonId) {
      const key = `${modId}_${lessonId}`;
      if (this.completedLessons.has(key)) {
        this.completedLessons.delete(key);
      } else {
        this.completedLessons.add(key);
      }
      this.save();
      this.render();
    }

    isCompleted(modId, lessonId) {
      return this.completedLessons.has(`${modId}_${lessonId}`);
    }

    reset() {
      if (confirm("¿Deseas reiniciar tu progreso guardado en este navegador?")) {
        this.completedLessons.clear();
        this.save();
        this.render();
      }
    }

    init() {
      this.render();
    }

    render() {
      if (!this.container) return;
      const count = this.completedLessons.size;
      const percent = Math.round((count / this.totalLessons) * 100);
      this.container.innerHTML = `
        <div class="progress-info-row">
          <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
            <span style="font-weight: 700; color: var(--text-primary); font-family: var(--font-family-display);">Tu Progreso de Aprendizaje</span>
            <span class="badge badge-cyan" style="font-size: 0.7rem;">${count} / ${this.totalLessons} Lecciones</span>
          </div>
          <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-family: var(--font-family-mono); font-weight: 700; color: ${percent > 0 ? '#34d399' : 'var(--text-muted)'};">${percent}%</span>
            ${count > 0 ? `
              <button id="btn-reset-progress" style="background: none; border: none; font-size: 0.7rem; color: var(--text-muted); cursor: pointer; text-decoration: underline;">
                Reiniciar
              </button>
            ` : ''}
          </div>
        </div>
        <div class="progress-track">
          <div class="progress-fill" style="width: ${percent}%;"></div>
        </div>
      `;

      const resetBtn = this.container.querySelector('#btn-reset-progress');
      if (resetBtn) {
        resetBtn.addEventListener('click', () => this.reset());
      }
    }
  }

  /* ==========================================================================
     7. CODE COPY MANAGER (CLICK TO COPY)
     ========================================================================== */
  class CodeCopyManager {
    static init() {
      document.querySelectorAll('pre').forEach(pre => {
        if (pre.querySelector('.code-copy-btn')) return;
        const btn = document.createElement('button');
        btn.className = 'code-copy-btn';
        btn.setAttribute('aria-label', 'Copiar código al portapapeles');
        btn.innerHTML = `
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          <span>Copiar</span>
        `;

        btn.addEventListener('click', async () => {
          const codeElem = pre.querySelector('code') || pre;
          const text = codeElem.innerText;
          try {
            if (navigator.clipboard && navigator.clipboard.writeText) {
              await navigator.clipboard.writeText(text);
            } else {
              const ta = document.createElement('textarea');
              ta.value = text;
              document.body.appendChild(ta);
              ta.select();
              document.execCommand('copy');
              document.body.removeChild(ta);
            }
            btn.classList.add('copied');
            btn.innerHTML = `
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Copiado!</span>
            `;
            setTimeout(() => {
              btn.classList.remove('copied');
              btn.innerHTML = `
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                <span>Copiar</span>
              `;
            }, 2000);
          } catch (err) {
            console.error("Error al copiar:", err);
          }
        });

        pre.appendChild(btn);
      });
    }
  }

  /* ==========================================================================
     8. LIVE C++ ANTI-PATTERN LINTER
     ========================================================================== */
  class CxxLinter {
    constructor(containerId) {
      this.container = document.getElementById(containerId);
      if (!this.container) return;
      this.sampleCodes = {
        badNamespaces: `#include <iostream>\nusing namespace std; // ❌ Anti-patrón\n\nint main() {\n    cout << "Hola Mundo" << endl; // ❌ std::endl forzado\n    return 0;\n}`,
        badInit: `#include <iostream>\n\nint main() {\n    int puntos; // ❌ Basura en RAM\n    double precio = (double)100 / 3; // ❌ C-cast inseguro\n    std::cout << "Puntos: " << puntos << '\\n';\n    return 0;\n}`,
        goodModern: `#include <iostream>\n\nint main() {\n    // ✅ Inicialización uniforme {} y static_cast seguro\n    int puntos{100};\n    double precio{ static_cast<double>(100) / 3 };\n    std::cout << "Puntos garantizados: " << puntos << '\\n';\n    return 0;\n}`
      };
      this.currentCode = this.sampleCodes.badNamespaces;
      this.init();
    }

    init() {
      this.render();
      this.bindEvents();
      this.analyze();
    }

    render() {
      this.container.innerHTML = `
        <div class="linter-container">
          <div class="linter-top-bar">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-family: var(--font-family-mono); font-size: 0.75rem; color: var(--zinc-400); font-weight: 700;">AUDITOR ESTÁTICO C++17/20 EN VIVO</span>
            </div>
            <div class="linter-presets">
              <span style="font-size: 0.72rem; color: var(--text-muted); align-self: center;">Ejemplos:</span>
              <button class="linter-preset-btn" data-preset="badNamespaces">using namespace std;</button>
              <button class="linter-preset-btn" data-preset="badInit">Basura & C-Cast</button>
              <button class="linter-preset-btn" data-preset="goodModern">C++ Moderno Idiomático</button>
            </div>
          </div>

          <div class="linter-editor-area">
            <textarea id="linter-code-input" class="linter-textarea" spellcheck="false" placeholder="Escribe o pega código C++ aquí para analizarlo en vivo...">${this.currentCode}</textarea>
            <div id="linter-diagnostics" class="linter-diagnostics-panel" role="log" aria-live="polite"></div>
          </div>
        </div>
      `;
    }

    bindEvents() {
      const textarea = this.container.querySelector('#linter-code-input');
      if (textarea) {
        textarea.addEventListener('input', () => {
          this.currentCode = textarea.value;
          this.analyze();
        });
      }

      this.container.querySelectorAll('.linter-preset-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const key = btn.dataset.preset;
          if (this.sampleCodes[key]) {
            this.currentCode = this.sampleCodes[key];
            if (textarea) textarea.value = this.currentCode;
            this.analyze();
          }
        });
      });
    }

    analyze() {
      const code = this.currentCode;
      const diagPanel = this.container.querySelector('#linter-diagnostics');
      if (!diagPanel) return;

      const issues = [];
      const goods = [];

      if (/using\s+namespace\s+std\s*;/i.test(code)) {
        issues.push({
          title: "Veto a 'using namespace std;'",
          desc: "Provoca colisiones de nombres globales en proyectos medianos y grandes. Usa siempre 'std::cout', 'std::cin', 'std::string'.",
          rule: "Veto #1"
        });
      } else if (/std::/i.test(code)) {
        goods.push({
          title: "Prefijo explícito 'std::' verificado",
          desc: "Excelente. El código tiene aislamiento estricto de ámbito sin colisiones globales."
        });
      }

      if (/std::endl/i.test(code)) {
        issues.push({
          title: "Veto a 'std::endl' (Forced Flush)",
          desc: "Fuerza un vaciado de buffer (flush) costoso e innecesario que degrada el I/O. Sustitúyelo por el carácter de salto de línea '\\n'.",
          rule: "Veto #2"
        });
      } else if (/['"]\\n['"]/.test(code)) {
        goods.push({
          title: "Salto de línea '\\n' directo verificado",
          desc: "Óptimo rendimiento de E/S sin forzar flushes destructivos."
        });
      }

      if (/\b(int|double|float|char|bool)\s+[a-zA-Z_]\w*\s*;/i.test(code)) {
        issues.push({
          title: "Peligro de Basura Residual en RAM",
          desc: "Declaraste variables primitivas sin inicializar. Usa siempre inicialización uniforme: 'int x{0};', 'double y{0.0};'.",
          rule: "Inicialización Uniforme"
        });
      } else if (/\b(int|double|float|char|bool)\s+[a-zA-Z_]\w*\s*\{/i.test(code)) {
        goods.push({
          title: "Inicialización uniforme '{}' verificada",
          desc: "Previene conversiones estrechas (*Narrowing*) y garantiza memoria limpia en Stack."
        });
      }

      if (/\((int|double|float|char)\)\s*[a-zA-Z0-9_]+/i.test(code)) {
        issues.push({
          title: "C-Style Cast Inseguro detectado",
          desc: "Los castings de C '(tipo)x' anulan la verificación de tipos. Usa 'static_cast<tipo>(x)'.",
          rule: "Casting Seguro"
        });
      } else if (/static_cast<.*?>/i.test(code)) {
        goods.push({
          title: "static_cast explícito verificado",
          desc: "Conversión de tipos validada en tiempo de compilación."
        });
      }

      if (/\brand\s*\(\s*\)/i.test(code)) {
        issues.push({
          title: "Función arcaica 'rand()' detectada",
          desc: "Genera números sesgados y no uniformes. Usa <random> con 'std::mt19937' y distribuciones estándar.",
          rule: "Aleatoriedad Moderna"
        });
      }

      let html = `
        <div style="font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; font-family: var(--font-family-mono); letter-spacing: 0.05em; font-weight: 700; margin-bottom: 2px;">
          Diagnóstico en Tiempo Real (${issues.length} advertencias · ${goods.length} conformidades)
        </div>
      `;

      if (issues.length === 0 && goods.length === 0) {
        html += `
          <div style="padding: var(--space-4); color: var(--text-muted); font-size: 0.8rem; text-align: center;">
            Escribe código en el editor para auditarlo según los estándares de C++17/20.
          </div>
        `;
      } else {
        issues.forEach(iss => {
          html += `
            <div class="diagnostic-item danger">
              <div style="display: flex; justify-content: space-between; font-weight: 700;">
                <span>❌ ${iss.title}</span>
                <span class="diff-tag" style="background: rgba(244, 63, 94, 0.2);">${iss.rule}</span>
              </div>
              <div style="color: var(--text-secondary); font-size: 0.75rem; margin-top: 2px; line-height: 1.4;">${iss.desc}</div>
            </div>
          `;
        });

        goods.forEach(g => {
          html += `
            <div class="diagnostic-item success">
              <div style="font-weight: 700;">✅ ${g.title}</div>
              <div style="color: var(--text-secondary); font-size: 0.75rem; margin-top: 2px; line-height: 1.4;">${g.desc}</div>
            </div>
          `;
        });
      }

      diagPanel.innerHTML = html;
    }
  }

  /* ==========================================================================
     9. PIPELINE EXPLORER (AST & ASSEMBLY)
     ========================================================================== */
  class PipelineExplorer {
    constructor(containerId) {
      this.container = document.getElementById(containerId);
      if (!this.container) return;
      this.presets = [
        {
          id: "arithmetic",
          name: "1. Suma Aritmética",
          badge: "Función Simple",
          cpp: `int sumar(int a, int b) {\n    return a + b;\n}`,
          ast: `FunctionDecl sumar 'int (int, int)'\n|-ParmVarDecl a 'int'\n|-ParmVarDecl b 'int'\n\`-CompoundStmt\n  \`-ReturnStmt\n    \`-BinaryOperator '+' 'int'\n      |-DeclRefExpr 'a'\n      \`-DeclRefExpr 'b'`,
          asm: `sumar(int, int):\n    lea     eax, [rdi+rsi]    ; Carga directa de la suma en registro EAX\n    ret                       ; Retorna al llamador con el resultado en EAX`,
          opt: `// Optimización -O2:\n// El compilador elimina la sobrecarga de marco de pila y usa la instrucción x86 LEA.\n// Ciclos de CPU consumidos: 1 ciclo (~0.3 nanosegundos).`
        },
        {
          id: "constexpr",
          name: "2. Constexpr (Cero Costo)",
          badge: "Compile-Time",
          cpp: `constexpr int calcularArea(int base, int altura) {\n    return base * altura;\n}\n\nint main() {\n    constexpr int area = calcularArea(10, 20);\n    return area;\n}`,
          ast: `FunctionDecl constexpr calcularArea 'int (int, int)'\n\`-CompoundStmt\n  \`-ReturnStmt\n    \`-BinaryOperator '*' 'int'\nVarDecl area 'const int' constexpr cinit\n\`-ConstantExpr 'int' [value = 200]`,
          asm: `main:\n    mov     eax, 200          ; ¡El cálculo 10 * 20 fue resuelto en compilación!\n    ret                       ; Retorna el valor inmediato 200 con cero llamadas.`,
          opt: `// Optimización -O2 / constexpr:\n// CERO operaciones de multiplicación en tiempo de ejecución.\n// El binario almacena directamente el número $200.`
        },
        {
          id: "passbyref",
          name: "3. Paso por Referencia const &",
          badge: "Zero-Copy",
          cpp: `struct Jugador { int hp; char nombre[64]; };\n\nint obtenerVida(const Jugador& p) {\n    return p.hp; // Cero copias de los 68 bytes\n}`,
          ast: `FunctionDecl obtenerVida 'int (const Jugador &)'\n|-ParmVarDecl p 'const Jugador &' (LValueReference)\n\`-CompoundStmt\n  \`-ReturnStmt\n    \`-MemberExpr .hp 'int'\n      \`-DeclRefExpr 'p'`,
          asm: `obtenerVida(Jugador const&):\n    mov     eax, DWORD PTR [rdi] ; Lee los 4 bytes de hp a través del puntero RDI\n    ret`,
          opt: `// Optimización Zero-Copy:\n// En lugar de clonar 68 bytes en el Stack, pasa un puntero de 8 bytes.\n// Reducción del 88% en ancho de banda de memoria.`
        }
      ];
      this.currentPresetIndex = 0;
      this.init();
    }

    init() {
      this.render();
      this.bindEvents();
    }

    render() {
      const item = this.presets[this.currentPresetIndex];
      this.container.innerHTML = `
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-xl); overflow: hidden; box-shadow: var(--shadow-card);">
          <div style="padding: var(--space-4) var(--space-6); background: #161b22; border-bottom: 1px solid var(--border-subtle); display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: var(--space-3);">
            <div>
              <span style="font-family: var(--font-family-mono); font-size: 0.75rem; color: var(--zinc-400); font-weight: 700;">EXPLORADOR DEL PIPELINE DEL COMPILADOR (g++ / Clang x86_64)</span>
              <h4 style="font-size: var(--font-size-base); margin-top: 2px;">De Código C++ a Instrucciones Nativas de CPU</h4>
            </div>
            <div class="pipeline-tabs-nav">
              ${this.presets.map((p, idx) => `
                <button class="btn btn-secondary pipeline-preset-btn ${idx === this.currentPresetIndex ? 'active' : ''}" data-index="${idx}" style="font-size: 0.72rem; padding: 0.35rem 0.75rem; ${idx === this.currentPresetIndex ? 'background: var(--text-primary); color: var(--text-inverse); font-weight: 700;' : ''}">
                  ${p.name}
                </button>
              `).join('')}
            </div>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1px; background: var(--border-subtle);">
            
            <!-- Stage 1: C++ -->
            <div class="pipeline-stage-card">
              <div class="pipeline-stage-header">
                <span>1. Código Fuente C++</span>
                <span class="badge badge-cyan">${item.badge}</span>
              </div>
              <pre style="margin: 0; border: none; border-radius: 0; min-height: 180px;"><code class="language-cpp">${item.cpp}</code></pre>
            </div>

            <!-- Stage 2: AST -->
            <div class="pipeline-stage-card">
              <div class="pipeline-stage-header">
                <span>2. Árbol de Sintaxis (AST)</span>
                <span style="font-size: 0.7rem; color: var(--text-muted);">Clang Parser</span>
              </div>
              <pre style="margin: 0; border: none; border-radius: 0; min-height: 180px; color: #93c5fd;"><code class="language-text">${item.ast}</code></pre>
            </div>

            <!-- Stage 3: x86_64 Assembly -->
            <div class="pipeline-stage-card">
              <div class="pipeline-stage-header">
                <span>3. Ensamblador x86_64</span>
                <span style="font-size: 0.7rem; color: #34d399;">CPU Nativa</span>
              </div>
              <pre style="margin: 0; border: none; border-radius: 0; min-height: 180px; color: #6ee7b7;"><code class="language-nasm">${item.asm}</code></pre>
            </div>

          </div>

          <div style="padding: var(--space-4) var(--space-6); background: var(--bg-surface); border-top: 1px solid var(--border-subtle); font-family: var(--font-family-mono); font-size: 0.78rem; color: var(--text-secondary); line-height: 1.5;">
            ${item.opt}
          </div>
        </div>
      `;
    }

    bindEvents() {
      this.container.querySelectorAll('.pipeline-preset-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          this.currentPresetIndex = parseInt(btn.dataset.index, 10);
          this.render();
          this.bindEvents();
          CodeCopyManager.init();
        });
      });
    }
  }

  /* ==========================================================================
     10. MANIM LIGHTBOX VISUAL MODAL
     ========================================================================== */
  class ManimLightbox {
    constructor(modalId) {
      this.modal = document.getElementById(modalId);
      if (!this.modal) return;
      this.data = {
        compilation: {
          title: "El Pipeline del Compilador (C++ a Binario x86_64)",
          src: "../01_GettingStarted/theory/assets/l00_compilation.gif",
          alt: "Pipeline del Compilador C++",
          breakdown: [
            { tag: "Preprocesador", desc: "Expande las directivas #include e inserta el contenido crudo de las cabeceras." },
            { tag: "Compilador (g++)", desc: "Genera el Árbol AST y traduce a código de máquina x86_64 optimizado." },
            { tag: "Linker", desc: "Enlaza símbolos y bibliotecas estándar para generar el archivo ejecutable final." }
          ]
        },
        shadowing: {
          title: "Variable Shadowing en el Stack",
          src: "../03_ScopeAndControlFlow/theory/assets/l03_variable_shadowing.gif",
          alt: "Variable Shadowing en memoria",
          breakdown: [
            { tag: "Stack Externo", desc: "Variable original viva en el marco del bloque superior." },
            { tag: "Llaves {}", desc: "Apertura de un nuevo ámbito que oculta la variable externa con el mismo nombre." },
            { tag: "Cierre de Bloque", desc: "Destrucción de la variable local interna, revelando nuevamente la original." }
          ]
        },
        passbyvalue: {
          title: "La Trampa del Clon: Pass-by-Value en Stack",
          src: "../04_Functions/theory/assets/l04_pass_by_value.gif",
          alt: "Pass-by-value en la pila",
          breakdown: [
            { tag: "Stack Frame main()", desc: "Almacena la variable original en su dirección física de memoria." },
            { tag: "Stack Frame función()", desc: "Copia/clona el valor en una nueva dirección aislada sin mutar el original." },
            { tag: "Solución Idiomática", desc: "Usar referencias '&' o 'const &' para operar directamente sobre la dirección original." }
          ]
        },
        const: {
          title: "Blindaje de Inmutabilidad (const) en RAM",
          src: "../05_ConstantsAndStrings/theory/assets/l01_const_memory.gif",
          alt: "Escudo inmutable const",
          breakdown: [
            { tag: "Celda en Stack", desc: "La variable recibe un candado de solo lectura verificado por el compilador." },
            { tag: "Intento de Mutación", desc: "El compilador emite un error estático antes de que el programa pueda ejecutarse." },
            { tag: "Constexpr", desc: "Permite evaluar expresiones fijas en tiempo de compilación con cero sobrecarga en runtime." }
          ]
        }
      };
      this.init();
    }

    init() {
      this.bindEvents();
    }

    bindEvents() {
      document.querySelectorAll('.gallery-trigger-card').forEach(card => {
        card.addEventListener('click', () => {
          const id = card.dataset.animId;
          if (this.data[id]) {
            this.open(this.data[id]);
          }
        });
        card.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            const id = card.dataset.animId;
            if (this.data[id]) this.open(this.data[id]);
          }
        });
      });

      const closeBtn = document.getElementById('lightbox-close-btn');
      const closeFooterBtn = document.getElementById('lightbox-close-footer-btn');
      const replayBtn = document.getElementById('lightbox-replay-btn');

      if (closeBtn) closeBtn.addEventListener('click', () => this.close());
      if (closeFooterBtn) closeFooterBtn.addEventListener('click', () => this.close());
      if (this.modal) {
        this.modal.addEventListener('click', (e) => {
          if (e.target === this.modal) this.close();
        });
      }

      if (replayBtn) {
        replayBtn.addEventListener('click', () => {
          const img = this.modal.querySelector('#lightbox-media-container img');
          if (img) {
            const src = img.src.split('?')[0];
            img.src = src + '?t=' + Date.now();
          }
        });
      }
    }

    open(item) {
      const title = document.getElementById('lightbox-title');
      const media = document.getElementById('lightbox-media-container');
      const desc = document.getElementById('lightbox-description-container');

      if (title) title.textContent = item.title;
      if (media) {
        media.innerHTML = `<img src="${item.src}" alt="${item.alt}">`;
      }
      if (desc) {
        desc.innerHTML = `
          <h4 style="font-size: var(--font-size-sm); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-primary); margin-bottom: var(--space-3);">
            🧠 Traducción Visual a Memoria Física & Hardware
          </h4>
          <div style="display: flex; flex-direction: column; gap: var(--space-2);">
            ${item.breakdown.map(b => `
              <div style="display: flex; gap: var(--space-3); padding: var(--space-2) var(--space-3); background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); font-size: 0.8rem;">
                <span style="font-family: var(--font-family-mono); font-weight: 700; color: #93c5fd; min-width: 140px;">${b.tag}</span>
                <span style="color: var(--text-secondary);">${b.desc}</span>
              </div>
            `).join('')}
          </div>
        `;
      }

      this.modal.classList.add('open');
      this.modal.setAttribute('aria-hidden', 'false');
    }

    close() {
      if (!this.modal) return;
      this.modal.classList.remove('open');
      this.modal.setAttribute('aria-hidden', 'true');
    }
  }

  /* ==========================================================================
     11. MAIN APPLICATION INITIALIZATION
     ========================================================================== */
  function initApp() {
    // 1. Theme Management
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const savedTheme = localStorage.getItem('learningcpp_theme') || (prefersDark ? 'dark' : 'dark');

    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggleBtn) {
      themeToggleBtn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('learningcpp_theme', next);
        updateThemeIcon(next);
      });
    }

    function updateThemeIcon(theme) {
      if (!themeToggleBtn) return;
      themeToggleBtn.innerHTML = theme === 'dark' 
        ? `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`
        : `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;
    }

    // 2. Mobile Navigation Drawer Controls
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileNavBackdrop = document.getElementById('mobile-nav-backdrop');
    const mobileNavCloseBtn = document.getElementById('mobile-nav-close-btn');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

    const openMobileMenu = () => {
      if (mobileNavBackdrop) {
        mobileNavBackdrop.classList.add('open');
        mobileNavBackdrop.setAttribute('aria-hidden', 'false');
        if (mobileMenuBtn) mobileMenuBtn.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden';
      }
    };

    const closeMobileMenu = () => {
      if (mobileNavBackdrop) {
        mobileNavBackdrop.classList.remove('open');
        mobileNavBackdrop.setAttribute('aria-hidden', 'true');
        if (mobileMenuBtn) mobileMenuBtn.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    };

    if (mobileMenuBtn) {
      mobileMenuBtn.addEventListener('click', openMobileMenu);
    }

    if (mobileNavCloseBtn) {
      mobileNavCloseBtn.addEventListener('click', closeMobileMenu);
    }

    if (mobileNavBackdrop) {
      mobileNavBackdrop.addEventListener('click', (e) => {
        if (e.target === mobileNavBackdrop) {
          closeMobileMenu();
        }
      });
    }

    mobileNavLinks.forEach(link => {
      link.addEventListener('click', () => {
        closeMobileMenu();
      });
    });

    // 3. Initialize Core & Senior Components
    window.__progressTracker = new ProgressTracker('student-progress-widget');
    new TerminalSimulator('hero-terminal-container');
    new CodePlayground('interactive-code-playground');
    new ModulesExplorer('modules-grid-container', 'module-detail-modal');
    new CxxLinter('interactive-linter-container');
    new RamVisualizer('interactive-ram-visualizer-container');
    new PipelineExplorer('compiler-pipeline-explorer-container');
    new ManimLightbox('manim-lightbox-modal');
    CodeCopyManager.init();

    // 4. Throttled Spotlight Mouse Tracking
    let rafId = null;
    document.addEventListener('mousemove', (e) => {
      if (rafId) return;
      rafId = requestAnimationFrame(() => {
        const target = e.target.closest('.card-pillar, .module-card, .diff-box');
        if (target) {
          const rect = target.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          target.style.setProperty('--mouse-x', `${x}px`);
          target.style.setProperty('--mouse-y', `${y}px`);
        }
        rafId = null;
      });
    }, { passive: true });

    // 4B. Interactive Studio Hub Tabs
    const studioTabs = document.querySelectorAll('.studio-tab-btn');
    const studioPanels = document.querySelectorAll('.studio-tab-panel');

    studioTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const targetId = tab.dataset.tab;
        studioTabs.forEach(t => {
          t.classList.remove('active');
          t.setAttribute('aria-selected', 'false');
        });
        tab.classList.add('active');
        tab.setAttribute('aria-selected', 'true');

        studioPanels.forEach(panel => {
          panel.style.display = (panel.id === targetId) ? 'block' : 'none';
        });
      });
    });

    // 4C. Mobile Interactive Comparison Hub
    const compareData = [
      {
        num: "01",
        title: "Espacio de Nombres",
        badCode: "using namespace std;",
        goodCode: "std::cout / std::cin",
        advantage: "Cero colisiones de nombres globales en bases de código reales."
      },
      {
        num: "02",
        title: "Salto de Línea",
        badCode: "std::endl (Flush forzado)",
        goodCode: "'\\n' directo",
        advantage: "Elimina cuellos de botella de E/S evitando vaciados de buffer innecesarios."
      },
      {
        num: "03",
        title: "Inicialización de Variables",
        badCode: "int x; (Basura residual)",
        goodCode: "int x{0}; (Uniforme)",
        advantage: "Previene basura en RAM y conversiones estrechas destructivas (Narrowing)."
      },
      {
        num: "04",
        title: "Colecciones Dinámicas",
        badCode: "int arr[N]; (C-Arrays)",
        goodCode: "std::vector&lt;T&gt; con .at()",
        advantage: "Gestión automática en memoria contigua y protección ante Buffer Overflow."
      },
      {
        num: "05",
        title: "Gestión de Memoria",
        badCode: "new[] / delete[] crudos",
        goodCode: "std::unique_ptr&lt;T&gt; (RAII)",
        advantage: "Destrucción determinista de memoria en Heap 100% libre de fugas (Memory Leaks)."
      },
      {
        num: "06",
        title: "Números Aleatorios",
        badCode: "rand() % N (Sesgado)",
        goodCode: "std::mt19937 (&lt;random&gt;)",
        advantage: "Distribución uniforme real de grado industrial sin sesgos matemáticos."
      }
    ];

    const compareDisplay = document.getElementById('compare-mobile-display');
    const comparePills = document.querySelectorAll('.compare-pill-btn');

    const renderCompareCard = (index) => {
      if (!compareDisplay) return;
      const item = compareData[index] || compareData[0];
      compareDisplay.innerHTML = `
        <header class="compare-card-header">
          <span class="module-id-badge" style="font-size: 0.7rem;">${item.num}</span>
          <h3 class="compare-card-title">${item.title}</h3>
        </header>
        <div class="compare-dual-grid">
          <div class="compare-box compare-box-broken">
            <div class="compare-box-label">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
              <span>C++98 Clásico</span>
            </div>
            <div class="compare-box-content">${item.badCode}</div>
          </div>
          <div class="compare-box compare-box-fixed">
            <div class="compare-box-label">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>C++17/20 Moderno</span>
            </div>
            <div class="compare-box-content">${item.goodCode}</div>
          </div>
        </div>
        <div class="compare-advantage-box">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--brand-primary)" stroke-width="2" style="flex-shrink: 0; margin-top: 2px;" aria-hidden="true"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>
          <div><strong>Ventaja:</strong> ${item.advantage}</div>
        </div>
      `;
    };

    if (comparePills.length > 0) {
      renderCompareCard(0);
      comparePills.forEach((pill, idx) => {
        pill.addEventListener('click', () => {
          comparePills.forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          renderCompareCard(idx);
        });
      });
    }

    // 5. Platform Quick-Start Tabs
    const platformTabs = document.querySelectorAll('.platform-tab-btn');
    const platformContents = document.querySelectorAll('.platform-snippet');

    platformTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const platform = tab.dataset.platform;
        platformTabs.forEach(t => {
          t.classList.remove('active');
          t.setAttribute('aria-selected', 'false');
        });
        tab.classList.add('active');
        tab.setAttribute('aria-selected', 'true');

        platformContents.forEach(c => {
          c.style.display = (c.dataset.platform === platform) ? 'block' : 'none';
        });
      });
    });

    // 6. FAQ Accordions
    const accordionItems = document.querySelectorAll('.accordion-item');
    accordionItems.forEach(item => {
      const header = item.querySelector('.accordion-header');
      if (header) {
        const toggleAccordion = () => {
          const isActive = item.classList.contains('active');
          accordionItems.forEach(i => {
            i.classList.remove('active');
            const h = i.querySelector('.accordion-header');
            if (h) h.setAttribute('aria-expanded', 'false');
          });
          if (!isActive) {
            item.classList.add('active');
            header.setAttribute('aria-expanded', 'true');
          }
        };

        header.addEventListener('click', toggleAccordion);
        header.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            toggleAccordion();
          }
        });
      }
    });

    // 7. Global Shortcuts & Escape Handling
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.getElementById('modules-search-input');
        if (searchInput) {
          searchInput.focus();
          searchInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      } else if (e.key === 'Escape') {
        if (mobileNavBackdrop && mobileNavBackdrop.classList.contains('open')) {
          closeMobileMenu();
        }
        const lightbox = document.getElementById('manim-lightbox-modal');
        if (lightbox && lightbox.classList.contains('open')) {
          lightbox.classList.remove('open');
        }
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }

})();
