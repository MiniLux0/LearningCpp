#include <iostream>
using namespace std;

int main() {

    int edadLyon;
    int edadElephant = 15;
    string pwd;

    cout << "Put la age of the Lyon: ";
    cin >> edadLyon;

    if (edadLyon < 18) {
        cout << "Lyon is Younger" << "\n";
    }

    if (edadLyon >= 18) {
        cout << "Lyon is Old" << "\n";
    }

    if (edadElephant <= 18) {
        cout << "Elephant is younger"<< "\n";
    }



    return 0;
}
