#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age: ";
    cin >> age;

    if (age < 18) {
        cout << "You are a minor." << "\n";
    } else if (age >= 18 && age <= 65) {
        cout << "You are an adult and within the retirement range." << "\n";
    } else {
        cout << "You are not within the retirement range." << "\n";
    }

    return 0;
}
