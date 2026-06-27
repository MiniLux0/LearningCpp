/*
 * E08 — Age Classifier
 * --------------------
 * Pide la edad de una persona y clasificala:
 *   0-12:   "Nino"
 *   13-17:  "Adolescente"
 *   18-64:  "Adulto"
 *   65+:    "Adulto mayor"
 *
 * Ejemplo:
 *   Input:  25
 *   Output: Adulto
 */

#include <iostream>
using namespace std;

int main() {

    int age;

    cout << "Enter your age: ";
    cin >> age;

    if (age >= 0 && age <= 12) {
        cout << "Nino\n";
    } else if (age >= 13 && age <= 17) {
        cout << "Adolescente\n";
    } else if (age >= 18 && age <= 64) {
        cout << "Adulto\n";
    } else if (age >= 65) {
        cout << "Adulto mayor\n";
    } else {
        cout << "Edad invalida\n";
    }

    return 0;
}
