#include <iostream>
using namespace std;

int main() {

    int opcion;

    do {
        cout << "\nMENU\n";
        cout << "1. Saludar\n";
        cout << "2. Decir tu nombre\n";
        cout << "3. Salir\n";
        cout << "Elige una opcion: ";
        cin >> opcion;

        if (opcion == 1) {
            cout << "Hola!\n";
        } else if (opcion == 2) {
            cout << "Tu nombre es ??? (aun no implementado)\n";
        } else if (opcion == 3) {
            cout << "Saliendo...\n";
        } else {
            cout << "Opcion invalida\n";
        }

    } while (opcion != 3); // 🔥 se repite hasta que elija salir

    return 0;
}