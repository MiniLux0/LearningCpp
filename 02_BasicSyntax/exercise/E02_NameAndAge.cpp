/*
 * E02 — Name and Age
 * ------------------
 * Ask the user for their name (string) and age (int).
 * Print: "Hello [name], you are [age] years old."
 *
 * Example:
 *   Input:  Carlos, 20
 *   Output: Hello Carlos, you are 20 years old.
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
