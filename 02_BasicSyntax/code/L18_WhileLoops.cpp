#include <iostream>
using namespace std;

int main() {

    int n;

    cout << "Enter a number: ";
    cin >> n;

    while (n >= 0) {
        cout << n << " ";
        n--;  // 🔥 important: update the variable
    }

    cout << "\nDone!\n";

    return 0;
}