#include <iostream>
#include <cstring>
#include <cassert>

using namespace std;

// E09 — Safe miStrcpy (Buffer Overflow Prevention)
bool miStrcpy(char dest[], int destSize, const char src[]) {
    int srcLen = static_cast<int>(strlen(src));
    if (srcLen + 1 > destSize) {
        return false; // Insufficient buffer capacity
    }
    for (int i = 0; i <= srcLen; i++) { // Copies characters including '\0'
        dest[i] = src[i];
    }
    return true;
}

int main() {
    char buffer[10];
    bool ok1 = miStrcpy(buffer, 10, "Hello");
    cout << "Copy 'Hello' into buffer(10): " << (ok1 ? "SUCCESS" : "FAILED") 
         << " -> \"" << buffer << "\"" << endl;

    bool ok2 = miStrcpy(buffer, 10, "Supercalifragilistic");
    cout << "Copy 'Supercalifragilistic' into buffer(10): " << (ok2 ? "SUCCESS" : "FAILED") << endl;

    assert(ok1 == true);
    assert(ok2 == false);

    return 0;
}
