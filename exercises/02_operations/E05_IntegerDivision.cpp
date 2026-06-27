/*
 * E05 — Integer Division Trap
 * ---------------------------
 * Demuestra la trampa de division entera.
 *
 * Pregunta: ¿Por que a, b y c dan resultados diferentes?
 */

#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    int a = 1 / 3;
    double b = 1 / 3;
    double c = 1.0 / 3;

    cout << fixed;
    cout << "int a = 1 / 3      -> " << a << "\n";
    cout << "double b = 1 / 3   -> " << setprecision(15) << b << "\n";
    cout << "double c = 1.0 / 3 -> " << setprecision(15) << c << "\n";

    cout << "\nExplicacion:\n";
    cout << "- 1 / 3 es division entera: 0 (trunca decimales)\n";
    cout << "- 1.0 / 3 promueve a double: 0.3333...\n";

    return 0;
}
