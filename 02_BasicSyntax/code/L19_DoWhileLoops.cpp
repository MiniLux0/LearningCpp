#include <iostream>
using namespace std;

int main() {

    int option;

    do {
        cout << "\nMENU\n";
        cout << "1. Greet\n";
        cout << "2. Say your name\n";
        cout << "3. Exit\n";
        cout << "Choose an option: ";
        cin >> option;

        if (option == 1) {
            cout << "Hello!\n";
        } else if (option == 2) {
            cout << "Your name is ??? (not yet implemented)\n";
        } else if (option == 3) {
            cout << "Exiting...\n";
        } else {
            cout << "Invalid option\n";
        }

    } while (option != 3); // 🔥 repeats until exit is chosen

    return 0;
}