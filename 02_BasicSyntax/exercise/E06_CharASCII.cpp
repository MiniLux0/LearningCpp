/*
 * E06 — Char ASCII
 * ----------------
 * Pide un caracter al usuario.
 * Imprime su valor ASCII usando (int).
 * Imprime el siguiente caracter sumando 1.
 *
 * Ejemplo:
 *   Input:  A
 *   ASCII:  65
 *   Siguiente: B
 */

#include <iostream>
using namespace std;

int main()
{
    char cValue;
    cout << "Enter a caracter: ";
    cin >> cValue;

    cout << "ASCII Value: " << (int)cValue <<"\n";
    cout << "Next ASCII Value: " << char((int)cValue + 1) << ", ASCII Value: " << (int)cValue + 1 << "\n";
    return 0;
}
