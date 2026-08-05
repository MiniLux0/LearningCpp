#include <iostream>
#include <cstring>

using namespace std;

// ============================================================================
// L30A — <cstring> LIBRARY & C-STYLE STRINGS (char[])
// Stanford CS106B Chapter 3 (Section 3.5) / MIT 6.096 Lecture 04
// ============================================================================

int main() {
    cout << "=== <cstring> LIBRARY & C-STYLE STRINGS ===" << endl << endl;

    // 1. Declaration and Null Sentinel '\0'
    char str1[] = "Hello";
    char str2[] = "World";

    cout << "--- 1. String Capacity & Length ---" << endl;
    cout << "str1 content: \"" << str1 << "\", str2: \"" << str2 << "\"" << endl;
    cout << "  - sizeof(str1): " << sizeof(str1) << " bytes (Includes '\\0')" << endl;
    cout << "  - strlen(str1): " << strlen(str1) << " chars (Excludes '\\0')" << endl;

    cout << "\n--- 2. String Manipulation Functions ---" << endl;
    char buffer[30];

    // strcpy: Copy string
    strcpy(buffer, "Learning ");
    cout << "After strcpy: \"" << buffer << "\"" << endl;

    // strcat: Concatenate string
    strcat(buffer, "C++ Programming");
    cout << "After strcat: \"" << buffer << "\"" << endl;

    // strcmp: Lexicographical comparison
    cout << "\n--- 3. String Comparison (strcmp) ---" << endl;
    char a[] = "Apple";
    char b[] = "Banana";

    int comp = strcmp(a, b);
    if (comp < 0) {
        cout << "\"" << a << "\" comes BEFORE \"" << b << "\" lexicographically." << endl;
    } else if (comp > 0) {
        cout << "\"" << a << "\" comes AFTER \"" << b << "\" lexicographically." << endl;
    } else {
        cout << "Strings are identical." << endl;
    }

    // strchr: Search character
    cout << "\n--- 4. Character Search (strchr) ---" << endl;
    char text[] = "Computer Science";
    char* pos = strchr(text, 'S');

    if (pos != nullptr) {
        cout << "Found 'S' at position: " << (pos - text) << endl;
        cout << "Remaining text: \"" << pos << "\"" << endl;
    }

    return 0;
}