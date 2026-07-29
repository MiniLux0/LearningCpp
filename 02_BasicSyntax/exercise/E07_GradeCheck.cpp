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

int main()
{

    double dValue;

    cout << "Enter your note: ";
    cin >> dValue;

    if(dValue >= 60){
        cout << "Approved";
    } else{
        cout<< "Dissproved";
    }

    return 0;
}
