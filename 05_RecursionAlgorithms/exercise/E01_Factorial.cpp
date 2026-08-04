#include <iostream>
using namespace std;

// Exercise 1 — Factorial
// Compute n! recursively.
// Big-O: Time O(n), Space O(n) due to call stack depth.

// Recursive factorial
long long factorial(int n) {
    if (n < 0) return -1;   // guard: undefined for negative
    if (n == 0) return 1;   // base case: 0! = 1
    return n * factorial(n - 1);
}

int main() {
    cout << "--- Factorial ---" << endl;

    for (int i = 0; i <= 12; i++) {
        cout << i << "! = " << factorial(i) << endl;
    }

    // Edge case: n = 0
    cout << "\n0! = " << factorial(0) << "  (should be 1)" << endl;

    // Guard for negative input
    int neg = factorial(-3);
    cout << "factorial(-3) = " << neg << "  (returns -1 as sentinel)" << endl;

    return 0;
}
