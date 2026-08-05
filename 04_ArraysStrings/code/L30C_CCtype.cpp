#include <iostream>
#include <cctype>
#include <string>

using namespace std;

// ============================================================================
// L30C — <cctype> LIBRARY & CHARACTER CLASSIFICATION / TRANSFORMATION
// Stanford CS106B Chapter 3 (Section 3.3)
// ============================================================================

void inspectCharacter(char c) {
    auto u = static_cast<unsigned char>(c);
    cout << "Inspecting character '" << c << "' (ASCII " << static_cast<int>(u) << "):" << endl;
    cout << "  - isalpha:  " << (isalpha(u) ? "YES" : "NO") << endl;
    cout << "  - isdigit:  " << (isdigit(u) ? "YES" : "NO") << endl;
    cout << "  - isalnum:  " << (isalnum(u) ? "YES" : "NO") << endl;
    cout << "  - islower:  " << (islower(u) ? "YES" : "NO") << endl;
    cout << "  - isupper:  " << (isupper(u) ? "YES" : "NO") << endl;
    cout << "  - isspace:  " << (isspace(u) ? "YES" : "NO") << endl;
    cout << "  - ispunct:  " << (ispunct(u) ? "YES" : "NO") << endl;
    cout << "  - tolower:  '" << static_cast<char>(tolower(u)) << "'" << endl;
    cout << "  - toupper:  '" << static_cast<char>(toupper(u)) << "'" << endl;
    cout << "----------------------------------------------------" << endl;
}

int main() {
    cout << "=== DEMONSTRATION OF #include <cctype> ===" << endl << endl;

    inspectCharacter('A');
    inspectCharacter('z');
    inspectCharacter('7');
    inspectCharacter('!');
    inspectCharacter(' ');

    return 0;
}
