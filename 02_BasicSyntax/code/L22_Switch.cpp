// ============================================================================
// L22 — Switch-Case Statements & Fall-Through
// ============================================================================
// Objective: Learn how to use switch-case statements, break, default, and fall-through.
// ============================================================================

#include <iostream>

using namespace std;

int main() {
    cout << "=== Switch-Case Demonstration ===\n\n";

    int choice = 2;

    // 1. Standard switch-case with break statements
    cout << "1. Standard switch-case (choice = " << choice << "):\n  Selected Option: ";
    switch (choice) {
        case 1:
            cout << "Option 1: Start Game\n";
            break;
        case 2:
            cout << "Option 2: Load Game\n";
            break;
        case 3:
            cout << "Option 3: Settings\n";
            break;
        default:
            cout << "Invalid Option!\n";
            break;
    }

    // 2. Intentional Fall-Through using C++17 [[fallthrough]]
    cout << "\n2. Intentional Fall-Through Demo (Grade Evaluation):\n  ";
    char grade = 'A';
    switch (grade) {
        case 'A':
        case 'a':
            cout << "Excellent Result!\n";
            break;
        case 'B':
        case 'b':
            cout << "Good Job!\n";
            break;
        default:
            cout << "Keep practicing!\n";
            break;
    }

    return 0;
}
