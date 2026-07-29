#include <iostream>
using namespace std;

int main() {

    int n;

    cout << "Enter a number: ";
    cin >> n;

    while (n >= 0) {
        cout << n << " ";
        n--;  // 🔥 importante: actualizar la variable
    }

    cout << "\nDone!\n";

    return 0;
}