/*
 * L16 — Comparing Floats
 * ----------------------
 * Comparing floats using == is dangerous due to precision errors.
 * Solution: use an epsilon (tolerance).
 *
 * Run this program and observe the results.
 */

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {

    // Example 1: The problem
    float a = 0.1 + 0.2;
    float b = 0.3;

    cout << "=== The Problem ===\n"; 
    cout << fixed;
    cout << "a (0.1 + 0.2) = " << a << "\n";
    cout << "b (0.3)       = " << b << "\n";
    cout << "a == b? " << (a == b ? "true" : "false") << "\n\n";

    // Example 1b: Other values where float fails
    float c = 1.1f + 1.2f;
    float d = 2.3f;

    cout << "=== Another Case ===\n";
    cout << setprecision(10);
    cout << "c (1.1 + 1.2) = " << c << "\n";
    cout << "d (2.3)       = " << d << "\n";
    cout << "c == d? " << (c == d ? "true" : "false") << "\n";
    cout << "c - d = " << (c - d) << "\n\n";

    // Example 2: The solution with epsilon
    float epsilon = 0.000001;

    cout << "=== The Solution ===\n";
    cout << "epsilon = " << epsilon << "\n";
    cout << "|a - b| = " << abs(a - b) << "\n";
    cout << "|a - b| < epsilon? " << (abs(a - b) < epsilon ? "true" : "false") << "\n\n";

    // Example 3: Comparing with double
    double x = 0.1 + 0.2;
    double y = 0.3;

    cout << "=== Double Precision ===\n";
    cout << setprecision(20);
    cout << "x (0.1 + 0.2) = " << x << "\n";
    cout << "y (0.3)       = " << y << "\n";
    cout << "x == y? " << (x == y ? "true" : "false") << "\n";
    cout << "x - y = " << (x - y) << "\n";

    return 0;
}
