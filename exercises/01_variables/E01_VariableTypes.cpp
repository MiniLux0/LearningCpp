/*
 * E01 — Variable Types
 * --------------------
 * Declara una variable de cada tipo: int, double, char, bool.
 * Asignale un valor e imprimela con cout.
 *
 * Salida esperada:
 *   int: 42
 *   double: 3.14
 *   char: A
 *   bool: 1
 */

#include <iostream>
using namespace std;

int main() {

    int myInt = 42;
    double myDouble = 3.14;
    char myChar = 'A';
    bool myBool = true;

    cout << "int: " << myInt << "\n";
    cout << "double: " << myDouble << "\n";
    cout << "char: " << myChar << "\n";
    cout << "bool: " << myBool << "\n";

    return 0;
}
