#include <iostream>
using namespace std;

// ============================================================================
// L25 — FUNCTION PARAMETERS: PASS BY VALUE vs PASS BY REFERENCE
// ============================================================================

// 1. PASS BY VALUE (copy)
void incrementByValue(int a) {
    a = a + 1;
    cout << "a in incrementByValue: " << a << endl;
}

// 2. PASS BY REFERENCE (&)
int incrementByRef(int &a) {
    a = a + 1;
    cout << "a in incrementByRef: " << a << endl;
    return a;
}

// 3. SWAP DEMONSTRATION
void swapByValue(int a, int b) {
    int t = a;
    a = b;
    b = t;
    cout << "  inside swapByValue: a=" << a << ", b=" << b << endl;
}

void swapByRef(int &a, int &b) {
    int t = a;
    a = b;
    b = t;
    cout << "  inside swapByRef: a=" << a << ", b=" << b << endl;
}

// 4. MULTIPLE OUTPUT PARAMETERS
int divide(int numerator, int denominator, int &remainder) {
    remainder = numerator % denominator;
    return numerator / denominator;
}

int main() {
    cout << "=== PASS BY VALUE ===" << endl;
    int q = 3;
    cout << "q before: " << q << endl;
    incrementByValue(q);
    cout << "q after: " << q << endl;

    cout << "\n=== PASS BY REFERENCE ===" << endl;
    int r = 3;
    cout << "r before: " << r << endl;
    incrementByRef(r);
    cout << "r after: " << r << endl;

    cout << "\n=== SWAP BY VALUE (NO EFFECT) ===" << endl;
    int x = 3, y = 5;
    cout << "x=" << x << ", y=" << y << " (before)" << endl;
    swapByValue(x, y);
    cout << "x=" << x << ", y=" << y << " (after)" << endl;

    cout << "\n=== SWAP BY REFERENCE (WORKS) ===" << endl;
    x = 3; y = 5;
    cout << "x=" << x << ", y=" << y << " (before)" << endl;
    swapByRef(x, y);
    cout << "x=" << x << ", y=" << y << " (after)" << endl;

    cout << "\n=== OUTPUT PARAMETERS: divide ===" << endl;
    int num = 14, den = 4, rem;
    int result = divide(num, den, rem);
    cout << num << " / " << den << " = " << result << " (quotient)" << endl;
    cout << num << " % " << den << " = " << rem << " (remainder)" << endl;

    return 0;
}