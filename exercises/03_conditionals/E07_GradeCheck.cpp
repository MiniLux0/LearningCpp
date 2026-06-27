/*
 * E07 — Grade Check
 * -----------------
 * Pide la nota de un estudiante (0-100).
 * Imprime "Aprobado" si es >= 60, "Reprobado" si es < 60.
 *
 * Ejemplo:
 *   Input:  75
 *   Output: Aprobado
 */

#include <iostream>
using namespace std;

int main() {

    int grade;

    cout << "Enter your grade (0-100): ";
    cin >> grade;

    if (grade >= 60) {
        cout << "Aprobado\n";
    } else {
        cout << "Reprobado\n";
    }

    return 0;
}
