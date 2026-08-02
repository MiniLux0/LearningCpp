#include <iostream>
#include <cctype>
using namespace std;

// Exercise 10 — Count vowels
// Counts how many vowels (uppercase or lowercase) the string s has.
int contarVocales(const char s[])
{
    int contador = 0;
    for (int i = 0; s[i] != '\0'; i++){
        char c = tolower(s[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
        {
            contador++;
        }
    }
    return contador;
}

int main()
{
    char s1[] = "Education";
    char s2[] = "AEIOU aeiou";
    
    cout << "contarVocales(\"Education\") (expected 5): " << contarVocales(s1) << endl;
    cout << "contarVocales(\"AEIOU aeiou\") (expected 10): " << contarVocales(s2) << endl;

    return 0;
}
