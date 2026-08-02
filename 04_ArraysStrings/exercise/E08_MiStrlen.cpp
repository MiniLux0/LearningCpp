#include <iostream>
using namespace std;

// Exercise 8 — miStrlen
// Implements your own version of strlen from scratch (without using <cstring>).
int miStrlen(const char s[])
{
    int contador = 0;
    for (int i = 0; s[i] != '\0'; i++)
    {
        contador++;
    }
    return contador;
}

int main()
{
    char s1[] = "Hola";
    char s2[] = "Programacion C++";

    cout << "miStrlen(\"Hola\") (expected 4): " << miStrlen(s1) << endl;
    cout << "miStrlen(\"Programacion C++\") (expected 16): " << miStrlen(s2) << endl;

    return 0;
}
