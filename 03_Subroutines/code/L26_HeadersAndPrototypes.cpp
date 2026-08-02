#include <iostream>
using namespace std;

// ============================================================================
// L26 — HEADERS AND PROTOTYPES
// ============================================================================

// ---------------------------------------------------------------------------
// PROBLEM: The compiler reads from top to bottom
// It needs to know the SIGNATURE (return type + parameters) BEFORE calling
// ---------------------------------------------------------------------------

// SOLUTION: Function Prototype (forward declaration)
// Only the signature, no body - a "promise" that the function exists
int bar();  // prototype: "bar() exists, takes 0 args, returns int"

int foo() {
    return bar() * 2;  // OK: compiler already knows bar's signature
}

// Actual implementation (can go after, or in another .cpp file)
int bar() {
    return 3;
}

// ---------------------------------------------------------------------------
// MUTUAL RECURSION: foo calls bar, bar calls foo
// Without prototypes, NO ORDER works
// ---------------------------------------------------------------------------

// Prototypes BEFORE use
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
// HEADER PATTERN: .h (interface) + .cpp (implementation)
// In real practice:
//   mylib.h  -> prototypes (declarations)
//   mylib.cpp -> definitions (bodies)
//   main.cpp -> #include "mylib.h" and uses the functions
// ---------------------------------------------------------------------------

// We simulate the .h here (prototypes)
int square(int x);
int cube(int x);

// We simulate the .cpp here (implementations)
// Parameter names in prototype DO NOT matter (only types)
int square(int z) {   // prototype said (int x), here (int z) - OK
    return z * z;
}

int cube(int x) {
    return x * square(x);
}

// ---------------------------------------------------------------------------
// CHECK QUESTION:
// Why are compiled libraries (.dll/.so) distributed only with .h?
// Answer: The .h contains EVERYTHING the compiler needs to
// generate code that CALLS the function:
//   - name
//   - return type
//   - parameter types
// The .cpp (implementation) is already compiled inside the .dll/.so.
// The user DOES NOT need to see the source code, just the INTERFACE.
// ---------------------------------------------------------------------------

int main() {
    cout << "=== L26: Headers and Prototypes ===\n\n";

    cout << "1. Basic prototype:\n";
    cout << "   foo() = " << foo() << "  (calls bar() declared after via prototype)\n\n";

    cout << "2. Mutual recursion (foo <-> bar):\n";
    cout << "   mutuoFoo(3) = " << mutuoFoo(3) << "\n";
    cout << "   mutuoBar(3) = " << mutuoBar(3) << "\n\n";

    cout << "3. Header pattern (square/cube):\n";
    cout << "   square(5) = " << square(5) << "\n";
    cout << "   cube(3) = " << cube(3) << "  (cube calls square)\n\n";

    cout << "4. Parameter names in prototype DO NOT matter:\n";
    cout << "   prototype: int square(int z);\n";
    cout << "   implementation: int square(int x) { return x * x; }\n";
    cout << "   -> Compiles perfectly, only matters: int square(int)\n\n";

    cout << "=== KEY SUMMARY ===\n";
    cout << "Prototype = signature (return + param types) WITHOUT body\n";
    cout << "Allows calling functions before defining them\n";
    cout << "Resolves mutual recursion\n";
    cout << ".h = prototypes (interface), .cpp = implementation\n";
    cout << "Compiled libraries: distribute .h + .dll/.so, NOT .cpp\n";
    cout << "The .h has everything the COMPILER needs to generate calls\n";

    return 0;
}

/*
KEY SUMMARY L26:
------------------
PROBLEM:
  - C++ compiler reads from top to bottom, one pass
  - To call f(), it needs to know: return type + param types
  - If f() definition is after (or in another file) -> ERROR

SOLUTION: Function Prototype
  int f(int x);  // signature + semicolon, WITHOUT { body }

PROTOTYPE:
  - Only matters: return type + param types (order)
  - Param names DO NOT matter (can change)
  - It is a "promise" to the compiler

HEADER PATTERN:
  // myLib.h
  int square(int);
  int cube(int);

  // myLib.cpp
  #include "miLib.h"
  int square(int x) { return x * x; }
  int cube(int x) { return x * square(x); }

  // main.cpp
  #include "miLib.h"
  int main() { cout << cube(3); }

WHY .h + .dll/.so WITHOUT .cpp:
  - .h = interface (what the COMPILER needs to verify calls)
  - .dll/.so = already compiled implementation (machine code)
  - User compiles their code against .h, links against .dll/.so
  - Doesn't need to see HOW it is implemented, only WHAT signature it has
*/