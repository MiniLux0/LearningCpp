// ============================================================================
// L20 — For Loops & Nested Loops
// ============================================================================
// Objective: Learn how to write counted for-loops, step increments, and nested loops.
// ============================================================================

#include <iostream>

using namespace std;

int main() {
    cout << "=== For Loops & Nested Loops ===\n\n";

    // 1. Basic counting for loop (0 to 4)
    cout << "1. Counting Loop (0 to 4):\n  ";
    for (int i = 0; i < 5; ++i) {
        cout << i << " ";
    }
    cout << "\n\n";

    // 2. Custom step increment (even numbers)
    cout << "2. Custom Step Increment (Even numbers 0 to 8):\n  ";
    for (int i = 0; i < 10; i += 2) {
        cout << i << " ";
    }
    cout << "\n\n";

    // 3. Nested Loops (Grid Coordinate Pattern)
    cout << "3. Nested Loops (3x4 Grid Coordinates):\n";
    for (int row = 1; row <= 3; ++row) {          // Outer loop (rows)
        for (int col = 1; col <= 4; ++col) {      // Inner loop (columns)
            cout << "(" << row << "," << col << ") ";
        }
        cout << "\n";
    }

    return 0;
}