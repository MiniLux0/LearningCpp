#include <iostream>
#include <cctype>
#include <cstring>
#include <cassert>

using namespace std;

// E12 — Convert C-String to Uppercase In-Place
void aMayusculas(char s[]) {
    for (int i = 0; s[i] != '\0'; i++) {
        s[i] = static_cast<char>(toupper(static_cast<unsigned char>(s[i])));
    }
}

int main() {
    char text[] = "learning c++";
    aMayusculas(text);

    cout << "Uppercase string: \"" << text << "\"" << endl;
    assert(strcmp(text, "LEARNING C++") == 0);

    return 0;
}
