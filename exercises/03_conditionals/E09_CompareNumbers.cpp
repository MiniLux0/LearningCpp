/*
 * E09 — Compare Numbers
 * ---------------------
 * Pide dos numeros enteros.
 * Imprime cual es mayor, o si son iguales.
 *
 * Ejemplo:
 *   Input:  10, 20
 *   Output: 20 es mayor
 */

#include <iostream>
using namespace std;

int main() {

    int a, b;

    cout << "Enter first number: ";
    cin >> a;

    cout << "Enter second number: ";
    cin >> b;

    if (a > b) {
        cout << a << " es mayor\n";
    } else if (b > a) {
        cout << b << " es mayor\n";
    } else {
        cout << "Son iguales\n";
    }

    return 0;
}
