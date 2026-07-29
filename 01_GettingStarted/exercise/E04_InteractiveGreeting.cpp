// ============================================================================
// E04 — Interactive Greeting Exercise
// ============================================================================
// Problem Statement:
// Ask the user to enter their name and age using `cin >>`, then output a personalized greeting.
// ============================================================================

#include <iostream>
#include <string>

using namespace std;

int main() {
    string name;
    int age;

    cout << "Enter your first name: ";
    cin >> name;

    cout << "Enter your age: ";
    cin >> age;

    cout << "\nHello, " << name << "! You are " << age << " years old.\n";
    return 0;
}
