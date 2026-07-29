// ============================================================================
// L02 — Namespaces & Understanding 'using namespace std;'
// ============================================================================
// Objective: Understand what namespaces are, why 'std::' exists, and the pros/cons
//            of using 'using namespace std;'.
//
// KEY CONCEPTS FOR BEGINNERS:
// 1. What is a Namespace?
//    - A namespace is like a family surname or container that groups related names
//      to prevent naming conflicts (e.g., standard library tools live in 'std').
//
// 2. 'std::cout' vs 'using namespace std;'
//    - Explicit: 'std::cout' tells C++ "use cout from the std namespace".
//    - Global:   'using namespace std;' allows writing 'cout' directly, but can cause
//      naming conflicts in large software projects.
// ============================================================================

#include <iostream>

// Approach A: Explicit namespace usage (Recommended for professional C++)
void explicit_namespace_demo() {
    std::cout << "Approach A: Explicit std:: prefix (Clean & safe)\n";
}

// Approach B: Using namespace std directive
using namespace std;

void using_namespace_demo() {
    cout << "Approach B: Using 'using namespace std;' (Shorter to write)\n";
}

int main() {
    cout << "=== Namespaces in C++ ===\n\n";

    explicit_namespace_demo();
    using_namespace_demo();

    cout << "\nBest Practice Tip:\n";
    cout << "  In small beginner scripts, 'using namespace std;' is fine.\n";
    cout << "  In large projects or header files (.h), use explicit 'std::' to avoid name collisions.\n";

    return 0;
}
