#include <iostream>
using namespace std;

int main() {

    int opcion;

    do {
        cout << "\nMENU\n";
        cout << "1. Greet\n";
        cout << "2. Say your name\n";
        cout << "3. Exit\n";
        cout << "Choose an option: ";
        cin >> opcion;

        if (opcion == 1) {
            cout << "Hello!\n";
        } else if (opcion == 2) {
            cout << "Your name is ??? (not yet implemented)\n";
        } else if (opcion == 3) {
            cout << "Exiting...\n";
        } else {
            cout << "Invalid option\n";
        }

    } while (opcion != 3); // 🔥 repeats until exit is chosen

    return 0;
}