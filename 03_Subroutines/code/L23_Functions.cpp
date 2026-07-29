#include <iostream>
using namespace std;

int raiseToPower(int base, int exponent) {
    int result = 1;
    for (int i = 0; i < exponent; i = i + 1) {
        result = result * base;
    }
    return result;
}

int resta(int a, int b) {
    return a - b;
}

int main() {
    cout << "=== L23: Functions ===" << endl;
    cout << "3^4  = " << raiseToPower(3, 4) << endl;
    cout << "6^5  = " << raiseToPower(6, 5) << endl;
    cout << "12^10= " << raiseToPower(12, 10) << endl;

    cout << "\nOrden de parametros importa:" << endl;
    cout << "raiseToPower(2, 3) = " << raiseToPower(2, 3) << " (2^3)" << endl;
    cout << "raiseToPower(3, 2) = " << raiseToPower(3, 2) << " (3^2)" << endl;

    cout << "\nChequeo resta:" << endl;
    cout << "resta(10, 3) = " << resta(10, 3) << endl;
    cout << "resta(3, 10) = " << resta(3, 10) << endl;

    return 0;
}