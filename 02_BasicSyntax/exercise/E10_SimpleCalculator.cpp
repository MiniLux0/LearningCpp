/*
 * E10 — Simple Calculator
 * -----------------------
 * Asks for two numbers (double) and an operator (+, -, *, /).
 * Performs the operation and prints the result.
 * If the operator is not valid, prints an error.
 * If there is a division by zero, prints an error.
 *
 * Example:
 *   Input:  10, 3, +
 *   Output: 10 + 3 = 13.00
 */

#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    double value1;
    double value2;
    char cValue;

    cout << "Enter the first number: ";
    cin >> value1;

    cout << "Enter the second number: ";
    cin >> value2;

    cout << "Enter the operator: ";
    cin >> cValue;

    cout << fixed << setprecision(2);

    if (cValue == '+') { 
        cout << value1 << " + " << value2 << " = " << value1 + value2 << "\n";
    } else if (cValue == '-') {
        cout << value1 << " - " << value2 << " = " << value1 - value2 << "\n";
    } else if (cValue == '*') {
        cout << value1 << " * " << value2 << " = " << value1 * value2 << "\n";
    } else if (cValue == '/') {
        if (value2 == 0) {
            cout << "Error: division by zero\n";
        } else {
            cout << value1 << " / " << value2 << " = " << value1 / value2 << "\n";
        }
    } else {
        cout << "Error: invalid operator '" << cValue << "'\n";
    }

    return 0;
}
