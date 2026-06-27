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

int main() {

    char ch;

    cout << "Enter a character: ";
    cin >> ch;

    cout << "ASCII value: " << (int)ch << "\n";
    cout << "Next character: " << (char)(ch + 1) << "\n";

    return 0;
}
