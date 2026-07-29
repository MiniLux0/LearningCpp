#include <iostream>
using namespace std;

// ============================================================================
// L26 — HEADERS AND PROTOTYPES
// ============================================================================

// ---------------------------------------------------------------------------
// PROBLEMA: El compilador lee de arriba hacia abajo
// Necesita saber la SIGNATURE (retorno + parámetros) ANTES de llamar
// ---------------------------------------------------------------------------

// SOLUCIÓN: Function Prototype (declaración adelantada)
// Solo la firma, sin cuerpo - "promesa" de que existe la función
int bar();  // prototype: "existe bar(), toma 0 args, devuelve int"

int foo() {
    return bar() * 2;  // OK: compilador ya conoce signature de bar
}

// Implementación real (puede ir después, o en otro .cpp)
int bar() {
    return 3;
}

// ---------------------------------------------------------------------------
// MUTUAL RECURSION: foo llama a bar, bar llama a foo
// Sin prototypes, NO HAY ORDEN que funcione
// ---------------------------------------------------------------------------

// Prototypes ANTES de usar
int mutuoFoo(int n);
int mutuoBar(int n);

int mutuoFoo(int n) {
    if (n <= 0) return 1;
    return mutuoBar(n - 1) * 2;
}

int mutuoBar(int n) {
    if (n <= 0) return 1;
    return mutuoFoo(n - 1) + 1;
}

// ---------------------------------------------------------------------------
// HEADER PATTERN: .h (interface) + .cpp (implementación)
// En la práctica real:
//   mylib.h  -> prototypes (declaraciones)
//   mylib.cpp -> definiciones (cuerpos)
//   main.cpp -> #include "mylib.h" y usa las funciones
// ---------------------------------------------------------------------------

// Simulamos el .h aquí (prototypes)
int square(int x);
int cube(int x);

// Simulamos el .cpp aquí (implementaciones)
// Nombres de parámetros en prototype NO importan (solo tipos)
int square(int z) {   // prototype decía (int x), aquí (int z) - OK
    return z * z;
}

int cube(int x) {
    return x * square(x);
}

// ---------------------------------------------------------------------------
// PREGUNTA DE CHEQUEO:
// ¿Por qué librerías compiladas (.dll/.so) se distribuyen solo con .h?
// Respuesta: El .h contiene TODO lo que el compilador necesita para
// generar código que LLAME a la función:
//   - nombre
//   - tipo de retorno
//   - tipos de parámetros
// El .cpp (implementación) ya está compilado dentro del .dll/.so.
// El usuario NO necesita ver el código fuente, solo la INTERFAZ.
// ---------------------------------------------------------------------------

int main() {
    cout << "=== L26: Headers and Prototypes ===\n\n";

    cout << "1. Prototype basico:\n";
    cout << "   foo() = " << foo() << "  (llama a bar() declarado despues via prototype)\n\n";

    cout << "2. Mutual recursion (foo <-> bar):\n";
    cout << "   mutuoFoo(3) = " << mutuoFoo(3) << "\n";
    cout << "   mutuoBar(3) = " << mutuoBar(3) << "\n\n";

    cout << "3. Header pattern (square/cube):\n";
    cout << "   square(5) = " << square(5) << "\n";
    cout << "   cube(3) = " << cube(3) << "  (cube llama a square)\n\n";

    cout << "4. Nombres de parametros en prototype NO importan:\n";
    cout << "   prototype: int square(int z);\n";
    cout << "   implementacion: int square(int x) { return x * x; }\n";
    cout << "   -> Compila perfecto, solo importa: int square(int)\n\n";

    cout << "=== RESUMEN CLAVE ===\n";
    cout << "Prototype = firma (retorno + tipos params) SIN cuerpo\n";
    cout << "Permite llamar funciones antes de definirlas\n";
    cout << "Resuelve recursion mutua\n";
    cout << ".h = prototypes (interface), .cpp = implementacion\n";
    cout << "Librerias compiladas: distribuyen .h + .dll/.so, NO .cpp\n";
    cout << "El .h tiene todo lo que el COMPILADOR necesita para generar llamadas\n";

    return 0;
}

/*
RESUMEN CLAVE L26:
------------------
PROBLEMA:
  - Compilador C++ lee de arriba a abajo, una pasada
  - Para llamar f(), necesita saber: retorno + tipos params
  - Si definicion de f() esta despues (u otro archivo) -> ERROR

SOLUCION: Function Prototype
  int f(int x);  // firma + punto y coma, SIN { cuerpo }

PROTOTYPE:
  - Solo importa: tipo retorno + tipos params (orden)
  - Nombres de params NO importan (pueden cambiar)
  - Es una "promesa" al compilador

HEADER PATTERN:
  // miLib.h
  int square(int);
  int cube(int);

  // miLib.cpp
  #include "miLib.h"
  int square(int x) { return x * x; }
  int cube(int x) { return x * square(x); }

  // main.cpp
  #include "miLib.h"
  int main() { cout << cube(3); }

POR QUE .h + .dll/.so SIN .cpp:
  - .h = interface (que necesita el COMPILADOR para verificar llamadas)
  - .dll/.so = implementacion ya compilada (maquina)
  - Usuario compila su codigo contra .h, linkea contra .dll/.so
  - No necesita ver COMO se implementa, solo QUE firma tiene
*/