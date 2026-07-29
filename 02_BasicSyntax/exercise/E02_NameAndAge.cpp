/*
 * E02 — Name and Age
 * ------------------
 * Pide al usuario su nombre (string) y su edad (int).
 * Imprime: "Hola [nombre], tienes [edad] anios."
 *
 * Ejemplo:
 *   Input:  Carlos, 20
 *   Output: Hola Carlos, tienes 20 anios.
 */

#include <iostream>
using namespace std;

int main()
{

    string name;
    int age;

    cout << "Enter your name: ";
    cin >> name;
    cout << "Enter your age: ";
    cin >> age;

    cout << "Hi " << name << " you are " << age << " years.";
    return 0;
}
