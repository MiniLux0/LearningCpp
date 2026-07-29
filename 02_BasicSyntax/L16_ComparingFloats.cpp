/*
 * L16 — Comparing Floats
 * ----------------------
 * Comparar floats con == es peligroso por errores de precision.
 * Solucion: usar un epsilon (tolerancia).
 *
 * Ejecuta este programa y observa los resultados.
 */

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {

    // Ejemplo 1: El problema
    float a = 0.1 + 0.2;
    float b = 0.3;

    cout << "=== The Problem ===\n"; 
    cout << fixed;
    cout << "a (0.1 + 0.2) = " << a << "\n";
    cout << "b (0.3)       = " << b << "\n";
    cout << "a == b? " << (a == b ? "true" : "false") << "\n\n";

    // Ejemplo 1b: Otros valores donde float falla
    float c = 1.1f + 1.2f;
    float d = 2.3f;

    cout << "=== Another Case ===\n";
    cout << setprecision(10);
    cout << "c (1.1 + 1.2) = " << c << "\n";
    cout << "d (2.3)       = " << d << "\n";
    cout << "c == d? " << (c == d ? "true" : "false") << "\n";
    cout << "c - d = " << (c - d) << "\n\n";

    // Ejemplo 2: La solucion con epsilon
    float epsilon = 0.000001;

    cout << "=== The Solution ===\n";
    cout << "epsilon = " << epsilon << "\n";
    cout << "|a - b| = " << abs(a - b) << "\n";
    cout << "|a - b| < epsilon? " << (abs(a - b) < epsilon ? "true" : "false") << "\n\n";

    // Ejemplo 3: Comparando con double
    double x = 0.1 + 0.2;
    double y = 0.3;

    cout << "=== Double Precision ===\n";
    cout << setprecision(20);
    cout << "x (0.1 + 0.2) = " << x << "\n";
    cout << "y (0.3)       = " << y << "\n";
    cout << "x == y? " << (x == y ? "true" : "false") << "\n";
    cout << "x - y = " << (x - y) << "\n";

    return 0;
}
