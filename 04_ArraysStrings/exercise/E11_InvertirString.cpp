#include <iostream>
#include <cstring>
using namespace std;

// Exercise 11 — Invert C-string in place
// Reverses the C-string s in-place.
void invertirString(char s[])
{
    int len = strlen(s);
    int i = 0;
    int j = len - 1;
    while (i < j)
    {
        swap(s[i], s[j]);
        i++;
        j--;
    }
}

int main()
{
    char s[] = "Hello World";

    cout << "Original: \"" << s << "\"" << endl;
    invertirString(s);
    cout << "Reversed (expected \"dlroW olleH\"): \"" << s << "\"" << endl;

    return 0;
}
