/*
 * E04 — Float vs Double Precision
 * -------------------------------
 * Declara float y double con 1.0/3.0.
 * Impriminalos con setprecision(20) para ver la diferencia.
 *
 * Pregunta: ¿Cual tiene mas digitos significativos?
 * 
 * Answer : double has more significant digits than float
 */

 
#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    float fvalue = 1.0/3.0;
    double dvalue = 1.0/3.0;
    cout << fvalue << "\n";
    cout << dvalue << "\n";
    cout << fixed;
    cout << setprecision(20) << fvalue << "\n";
    cout << setprecision(20) << dvalue << "\n";

    return 0;
}
