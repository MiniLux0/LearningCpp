#include <iostream>
#include <cstring>
#include <utility>
#include <cassert>

using namespace std;

// E11 — In-Place C-String Reversal
void invertirString(char s[]) {
    int low = 0;
    int high = static_cast<int>(strlen(s)) - 1;
    while (low < high) {
        swap(s[low], s[high]);
        low++;
        high--;
    }
}

int main() {
    char text[] = "Stanford";
    invertirString(text);

    cout << "Reversed string: \"" << text << "\"" << endl;
    assert(strcmp(text, "drofnats") == 0);

    return 0;
}
