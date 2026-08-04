#include <iostream>
using namespace std;

// Exercise 2 — Fibonacci
// Return the nth Fibonacci number (0-indexed).
// Big-O naive: Time O(2^n), Space O(n).
// Big-O with memoization: Time O(n), Space O(n).

// Naive recursive Fibonacci — observe exponential call growth
long long fibNaive(int n) {
    if (n <= 0) return 0;   // base case
    if (n == 1) return 1;   // base case
    return fibNaive(n - 1) + fibNaive(n - 2);
}

// Memoized Fibonacci — avoids redundant calls
long long memo[100] = {};   // initialized to 0

long long fibMemo(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    if (memo[n] != 0) return memo[n];   // already computed
    memo[n] = fibMemo(n - 1) + fibMemo(n - 2);
    return memo[n];
}

int main() {
    cout << "--- Fibonacci (Naive) ---" << endl;
    for (int i = 0; i <= 10; i++) {
        cout << "fib(" << i << ") = " << fibNaive(i) << endl;
    }

    cout << "\n--- Fibonacci (Memoized) ---" << endl;
    for (int i = 0; i <= 15; i++) {
        cout << "fib(" << i << ") = " << fibMemo(i) << endl;
    }

    // Observe: fib(0)=0, fib(1)=1 (base cases)
    cout << "\nfib(0) = " << fibMemo(0) << "  (should be 0)" << endl;
    cout << "fib(1) = " << fibMemo(1) << "  (should be 1)" << endl;

    return 0;
}
