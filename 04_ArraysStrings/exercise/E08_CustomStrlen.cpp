#include <iostream>
#include <cassert>

using namespace std;

// E08 — Reimplementing strlen from Scratch
int miStrlen(const char s[]) {
    int len = 0;
    while (s[len] != '\0') {
        len++;
    }
    return len;
}

int main() {
    char text[] = "Hello C++";
    int len = miStrlen(text);

    cout << "Length of \"" << text << "\": " << len << endl;
    assert(len == 9);

    return 0;
}
