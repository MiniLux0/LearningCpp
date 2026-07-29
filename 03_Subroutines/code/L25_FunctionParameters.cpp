#include <iostream>
using namespace std;

// ============================================================================
// L25 — FUNCTION PARAMETERS: PASS BY VALUE vs PASS BY REFERENCE
// ============================================================================

// ---------------------------------------------------------------------------
// 1. PASS BY VALUE (por valor) — DEFAULT en C++
//    El parámetro es una COPIA del argumento.
//    Cambios dentro de la función NO afectan la variable original.
// ---------------------------------------------------------------------------

void incrementByValue(int a) {
    a = a + 1;
    cout << "a in incrementByValue: " << a << endl;
}

// ---------------------------------------------------------------------------
// 2. PASS BY REFERENCE (por referencia) — usa &
//    El parámetro es un ALIAS de la variable original.
//    Cambios dentro de la función SÍ afectan la variable original.
// ---------------------------------------------------------------------------

int incrementByRef(int &a) {
    a = a + 1;
    cout << "a in incrementByRef: " << a << endl;
    return a;
}

// ---------------------------------------------------------------------------
// 3. EJEMPLO CLÁSICO: swap — IMPOSIBLE con pass-by-value
//    ¿Por qué? Porque con pass-by-value intercambias COPIAS locales,
//    no las variables originales de main.
// ---------------------------------------------------------------------------

void swapByValue(int a, int b) {  // SIN &
    int t = a;
    a = b;
    b = t;
    cout << "  dentro de swapByValue: a=" << a << ", b=" << b << endl;
}

void swapByRef(int &a, int &b) {  // CON &
    int t = a;
    a = b;
    b = t;
    cout << "  dentro de swapByRef: a=" << a << ", b=" << b << endl;
}

// ---------------------------------------------------------------------------
// 4. RETORNAR MÚLTIPLES VALORES — PARÁMETROS DE SALIDA (output parameters)
//    return solo devuelve UN valor. Para "devolver" más:
//    usa parámetros por REFERENCIA como "salidas disfrazadas".
// ---------------------------------------------------------------------------

// divide devuelve el COCIENTE por return, y el RESTO por referencia
int divide(int numerator, int denominator, int &remainder) {
    remainder = numerator % denominator;  // escribe en remainder (alias de rem en main)
    return numerator / denominator;       // devuelve cociente por return
}

// ---------------------------------------------------------------------------
// MAIN - Demostración
// ---------------------------------------------------------------------------

int main() {
    cout << "=== PASS BY VALUE ===" << endl;
    int q = 3;
    cout << "q antes: " << q << endl;
    incrementByValue(q);
    cout << "q despues: " << q << endl;  // SIGUE SIENDO 3
    cout << "  -> q NO cambió (a era una copia en distinta dirección de memoria)" << endl;

    cout << "\n=== PASS BY REFERENCE ===" << endl;
    int r = 3;
    cout << "r antes: " << r << endl;
    incrementByRef(r);
    cout << "r despues: " << r << endl;  // AHORA ES 4
    cout << "  -> r SÍ cambió (a es alias de r, misma dirección)" << endl;

    cout << "\n=== SWAP BY VALUE (NO FUNCIONA) ===" << endl;
    int x = 3, y = 5;
    cout << "x=" << x << ", y=" << y << " (antes)" << endl;
    swapByValue(x, y);
    cout << "x=" << x << ", y=" << y << " (despues - SIN CAMBIOS)" << endl;

    cout << "\n=== SWAP BY REFERENCE (FUNCIONA) ===" << endl;
    x = 3; y = 5;
    cout << "x=" << x << ", y=" << y << " (antes)" << endl;
    swapByRef(x, y);
    cout << "x=" << x << ", y=" << y << " (despues - INTERCAMBIADOS)" << endl;

    cout << "\n=== RETORNAR MÚLTIPLES VALORES: divide (cociente + resto) ===" << endl;
    int num = 14, den = 4, rem;
    int result = divide(num, den, rem);
    cout << num << " / " << den << " = " << result << " (cociente)" << endl;
    cout << num << " % " << den << " = " << rem << " (resto, via output param)" << endl;
    cout << "Comprobación: " << result << " * " << den << " + " << rem << " = " << result * den + rem << endl;

// Pregunta de chequeo: ¿qué pasa SIN & en remainder?
    // Sin &: remainder es una COPIA LOCAL. Se calcula el resto, se guarda en la copia,
    // la función termina, la copia se destruye. rem en main queda SIN INICIALIZAR (basura).
    // Con &: remainder es ALIAS de rem. Escribir en remainder ESCRIBE DIRECTAMENTE en rem.

    cout << "\n=== PREGUNTA CHEQUEO: POR QUÉ int &remainder Y NO int remainder? ===" << endl;
    cout << "Con 'int remainder' (sin &):" << endl;
    cout << "  - remainder es una COPIA local dentro de divide" << endl;
    cout << "  - remainder = numerator % denominator guarda el resto... en la copia" << endl;
    cout << "  - divide termina -> copia se destruye" << endl;
    cout << "  - rem en main NUNCA se entera -> queda con BASURA (sin inicializar)" << endl;
    cout << "Con 'int &remainder' (con &):" << endl;
    cout << "  - remainder es un ALIAS (referencia) de rem en main" << endl;
    cout << "  - Escribir en remainder ESCRIBE DIRECTAMENTE en rem" << endl;
    cout << "  - divide termina -> rem ya tiene el valor correcto" << endl;
    cout << "  - IMPORTANTE: & aquí es REFERENCIA (alias), NO puntero." << endl;
    cout << "    Referencia: se usa como variable normal (sin * ni ->)" << endl;
    cout << "    Puntero (int*): guarda dirección, necesita * para acceder (Lección 5)" << endl;

    cout << "\n=== PASS BY REFERENCE CON RETORNO (int + &) ===" << endl;
    int r = 3;
    int resultado = incrementByRef(r);  // r = 4, resultado = 4
    cout << "r = " << r << ", resultado = " << resultado << endl;

    return 0;
}

/*
RESUMEN CLAVE L25:
------------------
PASS BY VALUE (default):
  void f(int a)     // copia
  - a y variable original: distinta dirección memoria
  - cambios en a NO afectan original
  - seguro, pero no permite modificar

PASS BY REFERENCE (&):
  void f(int &a)    // alias
  - a ES la variable original (misma dirección)
  - cambios en a SÍ afectan original
  - necesario para: swap, modificar argumento, evitar copias grandes

OUTPUT PARAMETERS (parámetros de salida):
  void f(int in, int &out)
  - "in"  = entrada  (normalmente por valor o const&)
  - "out" = salida   (por referencia no-const)
  - Permite "retornar" múltiples valores
  - Ejemplo canónico: divide(cociente por return, resto por &out)

REFERENCIA vs PUNTERO (distinción crucial):
  int &ref = x;  // alias, sin sintaxis extra al usar
  int *ptr = &x; // variable que guarda dirección, usa *ptr para acceder
  - Referencia: no puede ser nula, no se puede reasignar, sintaxis transparente
  - Puntero: puede ser nullptr, se puede reasignar, sintaxis explícita (*ptr)

PASS BY REFERENCE CON RETORNO (int + &):
  int f(int &a) { a++; return a; }
  - & modifica el original (alias)
  - return devuelve valor adicional
  - Ambos mecanismos funcionan SIMULTÁNEAMENTE e independientemente

PREGUNTA CHEQUEO SWAP:
---------------------
swap(int a, int b) sin &:
  main: q=3, r=5
  swap(q, r) -> intercambia COPIAS locales
  main imprime: q=3, r=5  (¡sin cambios!)
*/

int incrementByRef(int &a) {
    a = a + 1;
    return a;
}