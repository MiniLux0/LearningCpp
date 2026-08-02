#include <iostream>
#include <cctype>
using namespace std;

// Exercise 12 — Uppercase without std::string
// Converts the string s to uppercase in-place.
void aMayusculas(char s[])
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        s[i] = toupper(static_cast<unsigned char>(s[i]));
    } 
}

int main()
{
    char s[] = "c++ is great 2026!";

    cout << "Original: \"" << s << "\"" << endl;
    aMayusculas(s);
    cout << "In uppercase (expected \"C++ IS GREAT 2026!\"): \"" << s << "\"" << endl;

    return 0;
}
