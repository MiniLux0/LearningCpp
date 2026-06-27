#include <iostream>
using namespace std;

int main() {

    int edadLyon;
    int edadElephant;

    cout << "Put la age of the Lyon: ";
    cin >> edadLyon;

    if (edadLyon < 18) {
        cout << "\"Lyon is Younger\"\n";
    } else {
        cout << "\"Lyon is Old\"\n";
    }

    cout << "Put la age of the Elephant: ";
    cin >> edadElephant;

    if (edadElephant <= 18) {
        cout << "\"Elephant is younger\"\n";
    } else{
        cout << "\"Elephant is Old\"\n";
    }

    return 0;
}
