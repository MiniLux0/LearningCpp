// ============================================================================
// E05 — Function Prototypes & Header Organization Exercise
// ============================================================================
// Problem Statement:
// Declare function prototypes above main() for 'isEven' and 'calculateFactorial'.
// Implement their definitions below main().
// ============================================================================

#include <iostream>

using namespace std;

// 1. Function Prototypes (Forward Declarations)
bool isEven(int number);
long long calculateFactorial(int n);

int main() {
    int val = 6;
    cout << "Is " << val << " even? " << (isEven(val) ? "Yes" : "No") << "\n";
    cout << "Factorial of " << val << " = " << calculateFactorial(val) << "\n";

    return 0;
}

// 2. Function Definitions below main()
bool isEven(int number) {
    return number % 2 == 0;
}

long long calculateFactorial(int n) {
    long long fact = 1;
    for (int i = 1; i <= n; ++i) {
        fact *= i;
    }
    return fact;
}