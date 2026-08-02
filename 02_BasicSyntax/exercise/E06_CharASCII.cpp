/*
 * E06 — Char ASCII
 * ----------------
 * Asks the user for a character.
 * Prints its ASCII value using (int).
 * Prints the next character by adding 1.
 *
 * Example:
 *   Input:  A
 *   ASCII:  65
 *   Next:   B
 */

#include <iostream>
using namespace std;

int main()
{
    char cValue;
    cout << "Enter a character: ";
    cin >> cValue;

    cout << "ASCII Value: " << (int)cValue <<"\n";
    cout << "Next ASCII Value: " << char((int)cValue + 1) << ", ASCII Value: " << (int)cValue + 1 << "\n";
    return 0;
}
