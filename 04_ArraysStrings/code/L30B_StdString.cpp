#include <iostream>
#include <string>
#include <cassert>
#include <stdexcept>

using namespace std;

// ============================================================================
// L30B — DEMONSTRATION OF <string> LIBRARY & string OBJECT
// Stanford CS106B Chapter 3 (Sections 3.1 - 3.4)
// ============================================================================

// Inspection Function (Efficient Constant Reference Passing)
void printStringInfo(const string& label, const string& s) {
    cout << label << ": \"" << s << "\"" << endl;
    cout << "  - Length (length/size): " << s.length() << " characters" << endl;
    cout << "  - Is empty?             " << (s.empty() ? "YES" : "NO") << endl;
    if (!s.empty()) {
        cout << "  - First character (front): '" << s.front() << "'" << endl;
        cout << "  - Last character (back):   '" << s.back() << "'" << endl;
    }
    cout << "----------------------------------------------------" << endl;
}

int main() {
    cout << "=== FULL DEMONSTRATION OF #include <string> ===" << endl << endl;

    // --- 1. STRING INITIALIZATION FORMS ---
    cout << "--- 1. Initialization Forms ---" << endl;
    string s1;                     // 1. Empty string
    string s2 = "Hello C++";       // 2. Direct assignment
    string s3{"World"};            // 3. Uniform initialization {}
    string s4(5, '*');             // 4. Fill initialization (5 asterisks "*****")
    string s5 = s2;                // 5. Copy
    string s6(s2, 0, 5);           // 6. Substring ("Hello")

    printStringInfo("s1 (Empty)", s1);
    printStringInfo("s2 (Direct)", s2);
    printStringInfo("s3 (Uniform)", s3);
    printStringInfo("s4 (Fill)", s4);
    printStringInfo("s5 (Copy)", s5);
    printStringInfo("s6 (Partial)", s6);

    // --- 2. CHARACTER ACCESS: [] vs .at() ---
    cout << "\n--- 2. Character Access: operator[] vs .at() ---" << endl;
    string title = "Programming";
    cout << "title[0]   = '" << title[0] << "'" << endl;
    cout << "title.at(3) = '" << title.at(3) << "'" << endl;

    // Safe exception catching with .at() out of bounds
    try {
        cout << "Attempting to access title.at(100)..." << endl;
        char c = title.at(100);
        (void)c;
    } catch (const out_of_range& e) {
        cout << "Exception caught successfully: " << e.what() << endl;
    }

    // --- 3. SEARCHING (find, rfind) & SUBSTRINGS (substr) ---
    cout << "\n--- 3. Searching and Substrings ---" << endl;
    string sentence = "The C++ language is a powerful language";

    size_t pos1 = sentence.find("language");       // 8
    size_t pos2 = sentence.find("language", 9);    // 30 (starts searching from index 9)
    size_t notFound = sentence.find("Python");     // string::npos

    cout << "First occurrence of 'language': " << pos1 << endl;
    cout << "Second occurrence of 'language': " << pos2 << endl;
    if (notFound == string::npos) {
        cout << "'Python' was not found (returns string::npos)." << endl;
    }

    string sub1 = sentence.substr(8, 8); // Extracts "language"
    string sub2 = sentence.substr(30);   // Extracts "language" (to the end)
    cout << "substr(8, 8): \"" << sub1 << "\"" << endl;
    cout << "substr(30):   \"" << sub2 << "\"" << endl;

    // --- 4. MUTATION (+, +=, insert, erase, replace, clear) ---
    cout << "\n--- 4. String Mutation ---" << endl;
    string msg = "Hello";
    cout << "Original:      \"" << msg << "\"" << endl;

    msg += " World";
    cout << "After +=:      \"" << msg << "\"" << endl;

    msg.insert(5, " Dear");
    cout << "After insert:  \"" << msg << "\"" << endl;

    msg.replace(6, 4, "Awesome");
    cout << "After replace: \"" << msg << "\"" << endl;

    msg.erase(5, 8);
    cout << "After erase:   \"" << msg << "\"" << endl;

    msg.clear();
    cout << "After clear(): length = " << msg.length() << endl;

    return 0;
}
