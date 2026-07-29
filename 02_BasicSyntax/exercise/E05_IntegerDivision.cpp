/*
 * E05 — Integer Division Trap
 * ---------------------------
 * Demuestra la trampa de division entera.
 *
 * Declara:
 *   int a = 1 / 3;
 *   double b = 1 / 3;
 *   double c = 1.0 / 3;
 *
 * Imprime cada variable y explica por que dan resultados diferentes.
 */

#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    int a = 1 / 3;      // int / int = int, truncates 0.333 to 0
    double b = 1 / 3;   // int / int = int (0), then stored as double 0.0
    double c = 1.0 / 3; // double / int = double, result is 0.333...

    cout << a << "\n";
    cout << b << "\n";
    cout << c << "\n";
    return 0;
}
