// ============================================================================
// L03 — Code Structure, Comments & Best Practices
// ============================================================================
// Objective: Learn how to write clear, readable, and documented C++ code.
// ============================================================================

#include <iostream>

// Since L02, we can use 'using namespace std;' in beginner scripts
// so we don't have to write 'std::' before cout, cin, and endl every time.
using namespace std;

int main() {
    // Single-line comment: Explaining the code below
    cout << "Good code is self-explanatory, but comments add context!\n";

    // Rule 1: Always use clear indentation inside curly braces {}
    cout << "Rule 1: Format your code neatly with indentation.\n";

    // Rule 2: Don't forget semicolons at the end of statements!
    cout << "Rule 2: Every statement ends with a semicolon (;).\n";

    return 0; // Return 0 indicates clean exit
}
