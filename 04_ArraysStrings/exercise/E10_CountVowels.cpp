#include <iostream>
#include <cctype>
#include <cassert>

using namespace std;

// E10 — Count Vowels in C-String with <cctype>
int contarVocales(const char s[]) {
    int count = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        char ch = static_cast<char>(tolower(static_cast<unsigned char>(s[i])));
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            count++;
        }
    }
    return count;
}

int main() {
    char text[] = "Programming CS106B";
    int vowels = contarVocales(text);

    cout << "Vowels in \"" << text << "\": " << vowels << endl;
    assert(vowels == 5);

    return 0;
}
