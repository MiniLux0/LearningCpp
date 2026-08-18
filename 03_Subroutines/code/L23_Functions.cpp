#include <iostream>
using namespace std;

int raiseToPower(int base, int exponent) {
    int result = 1;
    for (int i = 0; i < exponent; i = i + 1) {
        result = result * base;
    }
    return result;
}

int subtract(int a, int b) {
    return a - b;
}

int main() {
    cout << "=== L23: Functions ===" << endl;
    cout << "3^4  = " << raiseToPower(3, 4) << endl;
    cout << "6^5  = " << raiseToPower(6, 5) << endl;
    cout << "12^10= " << raiseToPower(12, 10) << endl;

    cout << "\nParameter order matters:" << endl;
    cout << "raiseToPower(2, 3) = " << raiseToPower(2, 3) << " (2^3)" << endl;
    cout << "raiseToPower(3, 2) = " << raiseToPower(3, 2) << " (3^2)" << endl;

    cout << "\nSubtraction check:" << endl;
    cout << "subtract(10, 3) = " << subtract(10, 3) << endl;
    cout << "subtract(3, 10) = " << subtract(3, 10) << endl;

    return 0;
}