// ============================================================================
// L21 — Loop Control: break and continue
// ============================================================================
// Objective: Learn how to exit loops early using 'break' and skip iterations using 'continue'.
// ============================================================================

#include <iostream>

using namespace std;

int main() {
    cout << "=== Loop Control Statements: break & continue ===\n\n";

    // 1. Using 'break' to exit a loop early when a target is found
    int target = 7;
    cout << "1. Searching for target (" << target << ") using break:\n";
    for (int i = 1; i <= 10; ++i) {
        if (i == target) {
            cout << "  Target " << target << " found at step " << i << "! Exiting loop.\n";
            break; // Exits the loop immediately
        }
        cout << "  Checking value " << i << "...\n";
    }

    // 2. Using 'continue' to skip even numbers
    cout << "\n2. Printing only ODD numbers (skipping even numbers with continue):\n  ";
    for (int i = 1; i <= 10; ++i) {
        if (i % 2 == 0) {
            continue; // Skips the rest of the loop body for even numbers
        }
        cout << i << " ";
    }
    cout << "\n";

    return 0;
}
