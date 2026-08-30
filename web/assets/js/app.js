/**
 * ============================================================================
 * LEARNINGCPP WEB PLATFORM - HIGH PERFORMANCE BUNDLE
 * Standalone, Highly Optimized, Accessible & Smooth Interaction Architecture
 * Compatible with file:// protocol and modern HTTP/HTTPS servers
 * ============================================================================
 */

(function() {
  'use strict';

  /* ==========================================================================
     1. CURRICULUM DATA MODEL (15 MODULES / 6 PHASES / 117 LESSONS)
     ========================================================================== */
  const PHASES = [
    { id: "fase-1", name: "Fase 1: Fundamentos", count: 3, subtitle: "De Cero Absoluto a tu Primer Binario: Compilador g++, tipos estáticos, Stack y control de flujo." },
    { id: "fase-2", name: "Fase 2: Funciones & Textos", count: 2, subtitle: "Modularidad y textos: Paso por valor, inmutabilidad const/constexpr y vistas de memoria std::string_view." },
    { id: "fase-3", name: "Fase 3: Colecciones", count: 2, subtitle: "Estructuras y datos: Arreglos dinámicos std::vector, structs heterogéneos y arquitectura multi-archivo .h/.cpp." },
    { id: "fase-4", name: "Fase 4: Memoria Real", count: 2, subtitle: "Arquitectura de hardware: Operador &, paso Zero-Copy const &, Heap dinámico y punteros RAII std::unique_ptr." },
    { id: "fase-5", name: "Fase 5: POO Moderna", count: 3, subtitle: "Ingeniería orientada a objetos: Encapsulamiento m_, constructores seguros, sobrecarga de operadores y VTable." },
    { id: "fase-6", name: "Fase 6: Especialización & Resiliencia", count: 3, subtitle: "Sistemas de alta resiliencia: Stack Unwinding, templates genéricos, lambdas, algoritmos STL y Capstone Final." },
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
      tagline: "struct, enum class y Agregados C++17 (Mirada a C++20)",
      project: "Bestiario RPG V1",
      description: "Agrupación de datos heterogéneos, tipado fuerte para máquinas de estado y colecciones de estructuras en memoria contigua.",
      lessons: [
        { id: "L01", title: "El caos de parámetros", desc: "Por qué colapsan las firmas de 6 variables sueltas." },
        { id: "L02", title: "Estructuras (struct)", desc: "Agrupación heterogénea y el operador punto." },
        { id: "L03", title: "Inicialización de Agregados", desc: "Inicialización uniforme {} y puente a Designated Initializers C++20." },
        { id: "L04", title: "Peligro de Números Mágicos", desc: "Fragilidad al usar enteros para representar estados." },
        { id: "L05", title: "Estados seguros enum class", desc: "Enumeraciones fuertemente tipadas con ámbito." },
        { id: "L06", title: "Colecciones de Entidades", desc: "Combinación de std::vector y structs." },
        { id: "L07", title: "Mini-proyecto Bestiario V1", desc: "Base de datos en memoria con monstruos y combate elemental." }
      ],
      bugDemos: ["D02_MissingSemicolonBug.cpp", "D03_AggregateInitOrderBug.cpp", "D04_MagicNumberBug.cpp"],
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
        { id: "L08", title: "Semántica de Movimiento", desc: "Transferencia de propiedad exclusiva con std::move." },
        { id: "L09", title: "Mini-proyecto Bestiario V3", desc: "Polimorfismo dinámico seguro en Heap con RAII total." }
      ],
      bugDemos: ["D03_NullptrDerefBug.cpp", "D05_MemoryLeakBug.cpp", "D06_UseAfterFreeBug.cpp"],
      keyDecision: "Propiedad exclusiva obligatoria con std::unique_ptr; punteros crudos como observadores no propietarios."
    },
    {
      id: "10",
      slug: "10_Classes",
      phase: "fase-5",
      phaseName: "Fase 5: POO Moderna",
      title: "Classes & Encapsulation",
      icon: "🛡️",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 8,
      tagline: "Encapsulamiento m_, constructores, inicializadores y operadores << / ==",
      project: "Simulador de Cuenta Bancaria / RPG",
      description: "Invariantes de clase, constructores seguros con listas de inicialización, métodos const y sobrecarga de operadores de flujo.",
      lessons: [
        { id: "L01", title: "De struct a class", desc: "Protección de estados corruptos e invariantes de clase." },
        { id: "L02", title: "Encapsulamiento", desc: "Acceso private vs public y convención prefijo m_." },
        { id: "L03", title: "Constructores seguros", desc: "Inicialización obligatoria mediante listas directas : m_vida{v}." },
        { id: "L04", title: "Métodos const", desc: "Garantía de inmutabilidad en métodos de solo lectura (getters)." },
        { id: "L05", title: "Sobrecarga de Operador <<", desc: "Impresión limpia directa con std::ostream&." },
        { id: "L06", title: "Sobrecarga de Operador ==", desc: "Comparación de igualdad idiomática y semántica de valor." },
        { id: "L07", title: "Separación de Clases", desc: "Implementación en .h (declaración) y .cpp (definición)." },
        { id: "L08", title: "Mini-proyecto Cuenta Bancaria", desc: "Clase encapsulada con validación estricta de transacciones." }
      ],
      bugDemos: ["D01_CorruptStateBug.cpp", "D03_UninitializedMemberBug.cpp", "D04_NonConstGetterBug.cpp"],
      keyDecision: "Encapsulamiento estricto con m_ y constructores que protejan las invariantes."
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
      tagline: "Herencia simple, visibilidad protected, llamada a constructores y Object Slicing",
      project: "Jerarquía de Entidades RPG",
      description: "Reutilización de código con herencia simple (: public), llamada ordenada a constructores base y diagnóstico del corte de objetos (Object Slicing).",
      lessons: [
        { id: "L01", title: "Duplicación de Código", desc: "Por qué copiar campos en 10 clases rompe la mantenibilidad." },
        { id: "L02", title: "Herencia Simple (: public)", desc: "Relación 'Es-Un' y extensión de clases base." },
        { id: "L03", title: "Visibilidad protected", desc: "Acceso para clases hijas manteniendo aislamiento exterior." },
        { id: "L04", title: "Llamada al Constructor Base", desc: "Paso de parámetros obligatorios de la clase hija a la base." },
        { id: "L05", title: "Orden de Destrucción", desc: "Secuencia física de inicialización y limpieza en memoria." },
        { id: "L06", title: "La Trampa de Object Slicing", desc: "Pérdida fatal de atributos al pasar derivados por valor." },
        { id: "L07", title: "Mini-proyecto Jerarquía RPG", desc: "Sistema de personajes derivados (Guerrero, Mago) con atributos compartidos." }
      ],
      bugDemos: ["D04_MissingBaseConstructorBug.cpp", "D06_ObjectSlicingBug.cpp"],
      keyDecision: "Herencia simple y explícita; prevención de Object Slicing mediante referencias/punteros."
    },
    {
      id: "12",
      slug: "12_Polymorphism",
      phase: "fase-5",
      phaseName: "Fase 5: POO Moderna",
      title: "Polymorphism & VTable",
      icon: "🎭",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 8,
      tagline: "virtual, VTable, override, interfaces puras = 0 y dynamic_cast",
      project: "Motor de Batalla Polimórfico",
      description: "Comportamiento dinámico en tiempo de ejecución, comprensión física de la tabla virtual (VTable), destructores virtuales y contratos puros.",
      lessons: [
        { id: "L01", title: "Enlace Estático (Early Binding)", desc: "Por qué los punteros base ignoran los métodos hijos." },
        { id: "L02", title: "Funciones virtual", desc: "Enlace dinámico (Late Binding) y despacho en runtime." },
        { id: "L03", title: "Cómo funciona la VTable", desc: "Puntero vptr y tabla virtual física en memoria RAM." },
        { id: "L04", title: "La Cláusula override", desc: "Prevención de errores de firma detectados por el compilador." },
        { id: "L05", title: "Destructores Virtuales", desc: "La trampa de la fuga de memoria al destruir derivados vía puntero base." },
        { id: "L06", title: "Interfaces Puras (= 0)", desc: "Clases abstractas y contratos obligatorios de diseño." },
        { id: "L07", title: "Downcasting con dynamic_cast", desc: "Inspección segura de tipos en tiempo de ejecución (RTTI)." },
        { id: "L08", title: "Mini-proyecto Motor de Batalla", desc: "Bucle de combate polimórfico con std::vector<std::unique_ptr<Entidad>>." }
      ],
      bugDemos: ["D01_EarlyBindingBug.cpp", "D04_MissingOverrideBug.cpp", "D05_NonVirtualDestructorBug.cpp"],
      keyDecision: "Destructores virtuales obligatorios en toda clase base polimórfica y override estricto."
    },
    {
      id: "13",
      slug: "13_ErrorHandling",
      phase: "fase-6",
      phaseName: "Fase 6: Especialización & Resiliencia",
      title: "Error Handling & Exceptions",
      icon: "⚡",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 7,
      tagline: "Stack Unwinding, std::exception, std::optional, noexcept y RAII",
      project: "Cargador Resiliente de Archivos",
      description: "Manejo profesional de errores, desenrollado de pila seguro con RAII, superación de códigos de error arcaicos con std::optional y cláusula noexcept.",
      lessons: [
        { id: "L01", title: "Códigos de Retorno vs Excepciones", desc: "Fragilidad al ignorar códigos de error clásicos." },
        { id: "L02", title: "Mecanismo try / catch / throw", desc: "Propagación controlada de fallos en el hilo de ejecución." },
        { id: "L03", title: "Stack Unwinding & RAII", desc: "Garantía de liberación automática de recursos ante fallos." },
        { id: "L04", title: "Jerarquía std::exception", desc: "Uso de runtime_error, invalid_argument y creación de excepciones propias." },
        { id: "L05", title: "Captura por const &", desc: "Prevención de Object Slicing al capturar excepciones derivadas." },
        { id: "L06", title: "std::optional de C++17", desc: "Manejo idiomático y de alto rendimiento de valores opcionales sin lanzar excepciones." },
        { id: "L07", title: "Cláusula noexcept", desc: "Optimización y garantías de no-lanzamiento en destructores y movimiento." }
      ],
      bugDemos: ["D03_RawPointerUnwindingLeakBug.cpp", "D05_ExceptionSlicingBug.cpp"],
      keyDecision: "Uso de std::optional para flujos esperados y excepciones para fallos excepcionales; RAII total."
    },
    {
      id: "14",
      slug: "14_TemplatesAndLambdas",
      phase: "fase-6",
      phaseName: "Fase 6: Especialización & Resiliencia",
      title: "Templates & Lambdas",
      icon: "✨",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 8,
      tagline: "Templates de función/clase, if constexpr, lambdas y C++20 Concepts",
      project: "Contenedor Genérico Seguro (Mini-Vector)",
      description: "Programación genérica sin costo en runtime (polimorfismo estático), templates en archivos .hpp, bifurcación en tiempo de compilación y lambdas modernas.",
      lessons: [
        { id: "L01", title: "Sobrecarga vs Polimorfismo Estático", desc: "El costo de mantener 10 funciones idénticas con distinto tipo." },
        { id: "L02", title: "Templates de Función (template<typename T>)", desc: "Generación de código especializado por el compilador." },
        { id: "L03", title: "Por qué los templates van en .hpp", desc: "Resolución del clásico Linker Error (undefined reference)." },
        { id: "L04", title: "Templates de Clase", desc: "Estructuras de datos genéricas parametrizadas por tipo." },
        { id: "L05", title: "Parámetros No-Tipo (NTTP)", desc: "Paso de constantes fijas a templates en tiempo de compilación." },
        { id: "L06", title: "if constexpr de C++17", desc: "Bifurcación estática sin generar código muerto en binario." },
        { id: "L07", title: "Expresiones Lambda", desc: "Funciones anónimas con clausura de captura [=, &]." },
        { id: "L08", title: "Evolución C++20: Concepts", desc: "Restricción de tipos con sintaxis limpia y mensajes de error legibles." }
      ],
      bugDemos: ["D03_TemplateLinkerErrorBug.cpp", "D07_DanglingLambdaCaptureBug.cpp"],
      keyDecision: "Definición completa de templates en archivos de cabecera (.hpp) e if constexpr para branching estático."
    },
    {
      id: "15",
      slug: "15_STLAlgorithms",
      phase: "fase-6",
      phaseName: "Fase 6: Especialización & Resiliencia",
      title: "STL Algorithms & Capstone",
      icon: "🏆",
      status: "planned",
      statusLabel: "Planificado",
      lessonsCount: 8,
      tagline: "Algoritmos STL, iteradores, Erase-Remove, C++20 Ranges y Capstone Final",
      project: "Motor RPG Definitivo (Capstone Final)",
      description: "Superación definitiva de bucles manuales mediante <algorithm>, seguridad de iteradores, tuberías C++20 Ranges y proyecto integrador de fin de curso.",
      lessons: [
        { id: "L01", title: "Algoritmos vs Bucles Manuales", desc: "Expresividad con all_of, any_of y count_if vs range-for idiomático." },
        { id: "L02", title: "Invalidación de Iteradores", desc: "Prevención de fallos con Erase-Remove Idiom (y std::erase_if C++20)." },
        { id: "L03", title: "Búsqueda y Predicados", desc: "std::find_if y min_element retornando std::optional." },
        { id: "L04", title: "Transformación y Reducción", desc: "Mapeo funcional con std::transform y std::accumulate." },
        { id: "L05", title: "Ordenamiento Avanzado", desc: "std::sort con lambdas y comparadores multicriterio." },
        { id: "L06", title: "Evolución C++20: Ranges & Views", desc: "Mirada al futuro: evaluación perezosa y tuberías funcionales |." },
        { id: "L07", title: "Asincronía Básica", desc: "Ejecución paralela de tareas en segundo plano con std::async y std::future." },
        { id: "L08", title: "El Motor RPG Definitivo (Capstone)", desc: "Arquitectura multi-archivo que consolida armónicamente los 15 módulos." }
      ],
      bugDemos: ["D01_RawLoopOffByOneBug.cpp", "D02_IteratorInvalidationBug.cpp", "D07_DataRaceIntroBug.cpp"],
      keyDecision: "Privilegiar claridad e idiomaticidad: usar algoritmos STL para transformaciones y range-for para secuencias directas."
    }
  ];

  /* ==========================================================================
     2. MODULES EXPLORER & MODAL
     ========================================================================== */
  class ModulesExplorer {
    constructor(containerId, modalId) {
      this.container = document.getElementById(containerId);
      this.modal = document.getElementById(modalId);
      this.activePhase = 'fase-1';
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
        <button type="button" class="tab-btn ${p.id === this.activePhase ? 'active' : ''}" data-phase="${p.id}" role="tab" aria-selected="${p.id === this.activePhase}">
          <span>${p.name}</span>
          <span class="tab-btn-count">${p.count}</span>
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
            <button type="button" class="btn btn-secondary btn-switch-phase" data-target-phase="${prevPhase.id}" style="font-size: var(--font-size-xs);">
              &larr; ${prevPhase.name}
            </button>
          ` : `<div></div>`}
          ${nextPhase ? `
            <button type="button" class="btn btn-primary btn-switch-phase" data-target-phase="${nextPhase.id}" style="font-size: var(--font-size-xs);">
              ${nextPhase.name} &rarr;
            </button>
          ` : `
            <button type="button" class="btn btn-secondary btn-switch-phase" data-target-phase="all" style="font-size: var(--font-size-xs);">
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
          e.preventDefault();
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
            this.activePhase = 'all';
            this.renderTabs();
          }
          this.renderModules();
        });
      }

      this.container.addEventListener('click', (e) => {
        const switchBtn = e.target.closest('.btn-switch-phase');
        if (switchBtn) {
          e.preventDefault();
          this.activePhase = switchBtn.dataset.targetPhase;
          this.renderTabs();
          this.renderModules();
          return;
        }

        const card = e.target.closest('.module-card');
        if (!card) return;
        e.preventDefault();
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
            e.preventDefault();
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
      const modalGithubBtn = this.modal.querySelector('#modal-github-btn');

      const githubModuleUrl = `https://github.com/MiniLux0/LearningCpp/tree/main/${mod.slug}`;
      const githubTheoryUrl = `https://github.com/MiniLux0/LearningCpp/tree/main/${mod.slug}/theory`;
      const githubLabUrl = `https://github.com/MiniLux0/LearningCpp/tree/main/${mod.slug}/lab`;
      const githubExerciseUrl = `https://github.com/MiniLux0/LearningCpp/tree/main/${mod.slug}/exercise`;

      if (modalGithubBtn) {
        modalGithubBtn.href = githubModuleUrl;
      }

      modalTitle.innerHTML = `
        <div style="display: flex; align-items: center; justify-content: space-between; width: 100%; gap: var(--space-3); flex-wrap: wrap;">
          <div style="display: flex; align-items: center; gap: var(--space-3);">
            <span class="module-id-badge" style="font-size: 0.9rem; padding: 0.25rem 0.6rem;">${mod.id}</span>
            <div>
              <div style="font-size: var(--font-size-xs); color: var(--text-muted); font-family: var(--font-family-mono); text-transform: uppercase; letter-spacing: 0.05em;">
                ${mod.phaseName}
              </div>
              <h2 style="font-size: var(--font-size-xl); font-family: var(--font-family-display); font-weight: 700; margin-top: 2px;">${mod.title}</h2>
            </div>
          </div>
          <a href="${githubModuleUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary" style="font-size: 0.75rem; padding: 0.35rem 0.75rem; display: inline-flex; align-items: center; gap: 5px;" aria-label="Abrir módulo en GitHub">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            <span>GitHub</span>
          </a>
        </div>
      `;

      modalContent.innerHTML = `
        <div style="margin-bottom: var(--space-5);">
          <p style="color: var(--text-secondary); font-size: var(--font-size-sm); line-height: 1.6;">
            ${mod.description}
          </p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-3); margin-bottom: var(--space-5);">
          <a href="${githubExerciseUrl}" target="_blank" rel="noopener noreferrer" style="text-decoration: none; background: var(--bg-surface); padding: var(--space-3) var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-subtle); display: block; transition: all 0.2s ease;">
            <div style="font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; display: flex; align-items: center; justify-content: space-between;">
              <span>Proyecto Integrador</span>
              <span style="color: var(--color-cyan); font-size: 0.68rem;">Retos ↗</span>
            </div>
            <div style="font-weight: 600; font-size: var(--font-size-sm); margin-top: 2px; color: var(--text-primary);">
              ${mod.project}
            </div>
          </a>
          <div style="background: var(--bg-surface); padding: var(--space-3) var(--space-4); border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <div style="font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em;">Estado del Módulo</div>
            <div style="font-weight: 600; font-size: var(--font-size-sm); margin-top: 2px; display: flex; align-items: center; gap: 6px; color: ${mod.status === 'completed' ? 'var(--color-success)' : 'var(--text-muted)'};">
              <span class="status-dot" style="background: ${mod.status === 'completed' ? 'var(--color-success)' : 'var(--zinc-600)'};"></span>
              ${mod.status === 'completed' ? 'Listo para estudiar' : 'En desarrollo'}
            </div>
          </div>
        </div>

        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: var(--space-3);">
          <h4 style="font-size: var(--font-size-sm); font-family: var(--font-family-display); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-primary); margin: 0;">
            Lecciones Teóricas (${mod.lessons.length})
          </h4>
          <a href="${githubTheoryUrl}" target="_blank" rel="noopener noreferrer" style="font-size: 0.75rem; color: var(--color-cyan); text-decoration: none; font-weight: 600;">
            Abrir carpeta theory/ ↗
          </a>
        </div>

        <div style="display: flex; flex-direction: column; gap: var(--space-2); margin-bottom: var(--space-5);">
          ${mod.lessons.map(l => `
            <a href="${githubTheoryUrl}" target="_blank" rel="noopener noreferrer" class="lesson-link-card" title="Abrir lección en GitHub">
              <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                <span class="lesson-link-badge">
                  ${l.id}
                </span>
                <div>
                  <div style="font-weight: 600; font-size: var(--font-size-sm); color: var(--text-primary);">${l.title}</div>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 2px;">${l.desc}</div>
                </div>
              </div>
              <span class="lesson-action-tag">
                <span>Estudiar</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </span>
            </a>
          `).join('')}
        </div>

        ${mod.bugDemos && mod.bugDemos.length > 0 ? `
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: var(--space-3);">
            <h4 style="font-size: var(--font-size-sm); font-family: var(--font-family-display); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-primary); margin: 0;">
              Demos de Bugs Intencionales (Break-First)
            </h4>
            <a href="${githubLabUrl}/demos" target="_blank" rel="noopener noreferrer" style="font-size: 0.75rem; color: #f43f5e; text-decoration: none; font-weight: 600;">
              Abrir lab/demos/ ↗
            </a>
          </div>
          <div style="display: flex; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-5);">
            ${mod.bugDemos.map(b => `
              <a href="${githubLabUrl}/demos" target="_blank" rel="noopener noreferrer" class="demo-link-badge" title="Ver código del demo en GitHub">
                <span>🐞 ${b}</span>
                <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
              </a>
            `).join('')}
          </div>
        ` : ''}

        <div style="padding: var(--space-4); background: var(--bg-surface); border-radius: var(--radius-md); border-left: 3px solid var(--text-primary);">
          <div style="font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600;">Decisión Arquitectónica Clave</div>
          <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-top: 4px; line-height: 1.5;">${mod.keyDecision}</p>
        </div>
      `;

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
     3. CODE COPY MANAGER
     ========================================================================== */
  class CodeCopyManager {
    static init() {
      document.querySelectorAll('pre').forEach(pre => {
        if (pre.querySelector('.code-copy-btn')) return;
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'code-copy-btn';
        btn.setAttribute('aria-label', 'Copiar código al portapapeles');
        btn.innerHTML = `
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          <span>Copiar</span>
        `;

        btn.addEventListener('click', async (e) => {
          e.preventDefault();
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
     4. MANIM LIGHTBOX VISUAL MODAL
     ========================================================================== */
  class ManimLightbox {
    constructor(modalId) {
      this.modal = document.getElementById(modalId);
      if (!this.modal) return;
      this.data = {
        compilation: {
          title: "El Pipeline del Compilador (C++ a Binario x86_64)",
          src: "assets/animations/l00_compilation.gif",
          alt: "Pipeline del Compilador C++",
          breakdown: [
            { tag: "Preprocesador", desc: "Expande las directivas #include e inserta el contenido crudo de las cabeceras." },
            { tag: "Compilador (g++)", desc: "Genera el Árbol AST y traduce a código de máquina x86_64 optimizado." },
            { tag: "Linker", desc: "Enlaza símbolos y bibliotecas estándar para generar el archivo ejecutable final." }
          ]
        },
        narrowing: {
          title: "Narrowing Conversions & Inicialización Uniforme {}",
          src: "assets/animations/l02_narrowing_conversion.gif",
          alt: "Narrowing Conversions en memoria",
          breakdown: [
            { tag: "Peligro en C++ Clásico", desc: "Asignar un double a un int trunca silenciosamente la información sin avisar." },
            { tag: "Inicialización Uniforme {}", desc: "Obliga al compilador a emitir un error estático ante conversiones destructivas." },
            { tag: "Seguridad en RAM", desc: "Garantiza que toda variable contenga exactamente el valor y tipo declarado." }
          ]
        },
        division: {
          title: "La Trampa de la División Entera (ALU)",
          src: "assets/animations/l03_division_entera.gif",
          alt: "División entera a nivel de ALU",
          breakdown: [
            { tag: "Operación en CPU", desc: "Al dividir dos enteros (7 / 2), el registro ALU descarta la parte fraccional arrojando 3." },
            { tag: "Solución Estática", desc: "Uso obligatorio de static_cast<double>(a) para forzar aritmética en coma flotante (3.5)." },
            { tag: "Casting C++ Moderno", desc: "static_cast es explícito y verificado en tiempo de compilación frente a C-casts arcaicos." }
          ]
        },
        shadowing: {
          title: "Variable Shadowing en el Stack",
          src: "assets/animations/l03_variable_shadowing.gif",
          alt: "Variable Shadowing en memoria",
          breakdown: [
            { tag: "Stack Externo", desc: "Variable original viva en el marco del bloque superior." },
            { tag: "Llaves {}", desc: "Apertura de un nuevo ámbito que oculta la variable externa con el mismo nombre." },
            { tag: "Cierre de Bloque", desc: "Destrucción de la variable local interna, revelando nuevamente la original." }
          ]
        },
        switch: {
          title: "Switch Jump Table & Prevención de Fallthrough",
          src: "assets/animations/l04_switch_fallthrough.gif",
          alt: "Switch Jump Table",
          breakdown: [
            { tag: "Jump Table O(1)", desc: "El compilador optimiza el switch convirtiéndolo en un salto de dirección directo." },
            { tag: "El Peligro Fallthrough", desc: "Omitir el break provoca que la CPU ejecute en cascada todos los casos siguientes." },
            { tag: "Control Moderno", desc: "Uso de break y atributos C++17 como [[fallthrough]] cuando la caída es intencional." }
          ]
        },
        passbyvalue: {
          title: "La Trampa del Clon: Pass-by-Value en Stack",
          src: "assets/animations/l04_pass_by_value.gif",
          alt: "Pass-by-value en la pila",
          breakdown: [
            { tag: "Stack Frame main()", desc: "Almacena la variable original en su dirección física de memoria." },
            { tag: "Stack Frame función()", desc: "Copia/clona el valor en una nueva dirección aislada sin mutar el original." },
            { tag: "Solución Idiomática", desc: "Usar referencias 'const &' para operar con costo cero de copia (Zero-Copy)." }
          ]
        },
        const: {
          title: "Blindaje de Inmutabilidad (const) en RAM",
          src: "assets/animations/l01_const_memory.gif",
          alt: "Escudo inmutable const",
          breakdown: [
            { tag: "Celda en Stack", desc: "La variable recibe un candado de solo lectura verificado por el compilador." },
            { tag: "Intento de Mutación", desc: "El compilador emite un error estático antes de que el programa pueda ejecutarse." },
            { tag: "Constexpr", desc: "Permite evaluar expresiones fijas en tiempo de compilación con cero sobrecarga en runtime." }
          ]
        },
        stringview: {
          title: "Vistas Zero-Copy con std::string_view",
          src: "assets/animations/l04_string_view_ref.gif",
          alt: "Vistas Zero-Copy string_view",
          breakdown: [
            { tag: "Problema de std::string", desc: "Pasar texto por valor fuerza asignación dinámica y copia costosa en Heap." },
            { tag: "string_view (Puntero + Tamaño)", desc: "Ventana no propietaria de solo 16 bytes que apunta al texto existente." },
            { tag: "Rendimiento C++17", desc: "Inspección de cadenas de texto con costo O(1) y cero fragmentación de memoria." }
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
        card.addEventListener('click', (e) => {
          e.preventDefault();
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

      if (closeBtn) closeBtn.addEventListener('click', (e) => { e.preventDefault(); this.close(); });
      if (closeFooterBtn) closeFooterBtn.addEventListener('click', (e) => { e.preventDefault(); this.close(); });
      if (this.modal) {
        this.modal.addEventListener('click', (e) => {
          if (e.target === this.modal) {
            e.preventDefault();
            this.close();
          }
        });
      }

      if (replayBtn) {
        replayBtn.addEventListener('click', (e) => {
          e.preventDefault();
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
        media.innerHTML = `<img src="${item.src}" alt="${item.alt}" style="max-width: 100%; max-height: 48vh; object-fit: contain; display: block; margin: 0 auto; border-radius: var(--radius-sm);" />`;
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
     5. MAIN APPLICATION INITIALIZATION
     ========================================================================== */
  function initApp() {
    // 1. Theme Management (Dark / Light)
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const savedTheme = localStorage.getItem('learningcpp_theme') || (prefersDark ? 'dark' : 'dark');

    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggleBtn) {
      themeToggleBtn.addEventListener('click', (e) => {
        e.preventDefault();
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

    // 2. Mobile Navigation Drawer
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileNavBackdrop = document.getElementById('mobile-nav-backdrop');
    const mobileNavCloseBtn = document.getElementById('mobile-nav-close-btn');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

    const openMobileMenu = (e) => {
      if (e && e.preventDefault) e.preventDefault();
      if (mobileNavBackdrop) {
        mobileNavBackdrop.classList.add('open');
        mobileNavBackdrop.setAttribute('aria-hidden', 'false');
        if (mobileMenuBtn) mobileMenuBtn.setAttribute('aria-expanded', 'true');
      }
    };

    const closeMobileMenu = (e) => {
      if (e && e.preventDefault) e.preventDefault();
      if (mobileNavBackdrop) {
        mobileNavBackdrop.classList.remove('open');
        mobileNavBackdrop.setAttribute('aria-hidden', 'true');
        if (mobileMenuBtn) mobileMenuBtn.setAttribute('aria-expanded', 'false');
      }
    };

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openMobileMenu);
    if (mobileNavCloseBtn) mobileNavCloseBtn.addEventListener('click', closeMobileMenu);
    if (mobileNavBackdrop) {
      mobileNavBackdrop.addEventListener('click', (e) => {
        if (e.target === mobileNavBackdrop) closeMobileMenu(e);
      });
    }

    mobileNavLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href && href.startsWith('#')) {
          const target = document.querySelector(href);
          if (target) {
            e.preventDefault();
            closeMobileMenu();
            setTimeout(() => {
              target.scrollIntoView({ behavior: 'smooth' });
            }, 100);
          } else {
            closeMobileMenu();
          }
        } else {
          closeMobileMenu();
        }
      });
    });

    // 3. Initialize Core Components
    new ModulesExplorer('modules-grid-container', 'module-detail-modal');
    new ManimLightbox('manim-lightbox-modal');
    CodeCopyManager.init();

    // 4. Mobile Interactive Comparison Hub
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
        badCode: "int x; (Valor indeterminado)",
        goodCode: "int x{0}; (Uniforme)",
        advantage: "Previene lectura de valores residuales indeterminados (UB) y conversiones estrechas."
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
        advantage: "Destrucción determinista y gestión segura de ownership en Heap mediante RAII."
      },
      {
        num: "06",
        title: "Números Aleatorios",
        badCode: "rand() % N (Sesgado)",
        goodCode: "std::mt19937 (&lt;random&gt;)",
        advantage: "Distribución uniforme determinista de alta calidad para simulación y juegos (No criptográfico)."
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
        pill.addEventListener('click', (e) => {
          e.preventDefault();
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
      tab.addEventListener('click', (e) => {
        e.preventDefault();
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
        const toggleAccordion = (e) => {
          if (e && e.preventDefault) e.preventDefault();
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
            toggleAccordion(e);
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
