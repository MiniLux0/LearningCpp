#include <iostream>
using namespace std;

// Exercise 6 — Power Function (recursive)
// Version A — Naive: Time O(exp), Space O(exp)
// Version B — Fast exponentiation: Time O(log exp), Space O(log exp)
// Key identity: base^exp = (base^(exp/2))^2  when exp is even
//               base^exp = base * base^(exp-1) when exp is odd

// Version A: naive — multiply base exp times
double powerNaive(double base, int exp) {
    if (exp == 0) return 1.0;           // base case: x^0 = 1
    if (exp < 0)  return 1.0 / powerNaive(base, -exp);  // handle negatives
    return base * powerNaive(base, exp - 1);
}

// Version B: fast exponentiation — halve the exponent each call
double powerFast(double base, int exp) {
    if (exp == 0) return 1.0;
    if (exp < 0)  return 1.0 / powerFast(base, -exp);
    if (exp % 2 == 0) {
        double half = powerFast(base, exp / 2);
        return half * half;             // reuse result — avoids extra call
    }
    return base * powerFast(base, exp - 1);
}

int main() {
    cout << "--- Power Function ---" << endl;

    cout << "\n[Naive — O(exp)]" << endl;
    cout << "2^10  = " << powerNaive(2.0, 10)  << endl;
    cout << "3^5   = " << powerNaive(3.0, 5)   << endl;
    cout << "2^0   = " << powerNaive(2.0, 0)   << endl;
    cout << "2^-3  = " << powerNaive(2.0, -3)  << endl;

    cout << "\n[Fast — O(log exp)]" << endl;
    cout << "2^10  = " << powerFast(2.0, 10)   << endl;
    cout << "3^5   = " << powerFast(3.0, 5)    << endl;
    cout << "2^0   = " << powerFast(2.0, 0)    << endl;
    cout << "2^-3  = " << powerFast(2.0, -3)   << endl;
    cout << "5^20  = " << powerFast(5.0, 20)   << endl;

    return 0;
}
