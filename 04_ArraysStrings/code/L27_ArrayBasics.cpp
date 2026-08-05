#include <iostream>

using namespace std;

// ============================================================================
// L27 — 1D STATIC ARRAYS: MEMORY LAYOUT & INDEXING
// Stanford CS106B Chapter 11 / MIT 6.096 Lecture 04
// ============================================================================

int main() {
    cout << "=== 1D STATIC ARRAYS & MEMORY LAYOUT ===" << endl << endl;

    // 1. Explicit size declaration & uniform initialization {}
    int grades[4]{10, 20, 30, 40};

    // 2. Zero initialization (all elements set to 0)
    int zeroes[5]{};

    // 3. Partial initialization (remaining elements set to 0)
    int partial[5]{10, 20};

    // 4. Inferred size by compiler
    double prices[]{19.99, 5.50, 42.0};
    int inferredSize = sizeof(prices) / sizeof(prices[0]);

    cout << "--- 1. Traversal and Address Layout ---" << endl;
    for (int i = 0; i < 4; i++) {
        cout << "grades[" << i << "] = " << grades[i] 
             << " | RAM Address: " << &grades[i] << endl;
    }

    cout << "\n--- 2. Inferred Array Size ---" << endl;
    cout << "Inferred elements count in prices[]: " << inferredSize << endl;
    for (int i = 0; i < inferredSize; i++) {
        cout << "prices[" << i << "] = $" << prices[i] << endl;
    }

    cout << "\n--- 3. Partial & Zero Initialization ---" << endl;
    cout << "partial[0] = " << partial[0] << ", partial[2] = " << partial[2] << endl;
    cout << "zeroes[0]  = " << zeroes[0]  << ", zeroes[4]  = " << zeroes[4]  << endl;

    return 0;
}