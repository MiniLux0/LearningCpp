/*
 * E04 — Float vs Double Precision
 * -------------------------------
 * Declara float y double con 1.0/3.0.
 * Impriminalos con setprecision(20) para ver la diferencia.
 *
 * Pregunta: ¿Cual tiene mas digitos significativos?
 */

#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    float f = 1.0 / 3.0;
    double d = 1.0 / 3.0;

    cout << fixed;
    cout << "float  (1.0/3.0) con precision 20: " << setprecision(20) << f << "\n";
    cout << "double (1.0/3.0) con precision 20: " << setprecision(20) << d << "\n";

    cout << "\nTamano en memoria:\n";
    cout << "float:  " << sizeof(float) << " bytes\n";
    cout << "double: " << sizeof(double) << " bytes\n";

    return 0;
}
