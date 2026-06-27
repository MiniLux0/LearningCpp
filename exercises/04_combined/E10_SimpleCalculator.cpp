/*
 * E10 — Simple Calculator
 * -----------------------
 * Pide dos numeros (double) y un operador (+, -, *, /).
 * Realiza la operacion e imprime el resultado.
 * Si el operador no es valido, imprime un error.
 * Si es division por cero, imprime un error.
 *
 * Ejemplo:
 *   Input:  10, 3, +
 *   Output: 10 + 3 = 13
 */

#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    double a, b;
    char op;

    cout << "Enter first number: ";
    cin >> a;

    cout << "Enter operator (+, -, *, /): ";
    cin >> op;

    cout << "Enter second number: ";
    cin >> b;

    cout << fixed;

    if (op == '+') {
        cout << a << " + " << b << " = " << setprecision(2) << a + b << "\n";
    } else if (op == '-') {
        cout << a << " - " << b << " = " << setprecision(2) << a - b << "\n";
    } else if (op == '*') {
        cout << a << " * " << b << " = " << setprecision(2) << a * b << "\n";
    } else if (op == '/') {
        if (b == 0) {
            cout << "Error: division por cero\n";
        } else {
            cout << a << " / " << b << " = " << setprecision(2) << a / b << "\n";
        }
    } else {
        cout << "Error: operador no valido '" << op << "'\n";
    }

    return 0;
}
