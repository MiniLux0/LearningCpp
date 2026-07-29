// ============================================================================
// E03 — Namespaces Exercise
// ============================================================================
// Problem Statement:
// Demonstrate both explicit `std::` scope resolution and `using namespace std;`
// in two separate helper functions.
// ============================================================================

#include <iostream>

void explicitScope() {
    std::cout << "Using explicit std:: prefix\n";
}

using namespace std;

void globalDirective() {
    cout << "Using global namespace std directive\n";
}

int main() {
    explicitScope();
    globalDirective();
    return 0;
}
