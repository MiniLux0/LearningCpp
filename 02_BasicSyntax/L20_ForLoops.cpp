#include <iostream>
using namespace std;

int main() {

    int num;

    for (int i = 0; i < 5; i++) {
        cout << "Intent " << i << ": Enter a positive number: ";
        cin >> num;

        if (num > 0) {
            cout << "Valid number!\n";
        } else {
            cout << "Invalid number\n";
        }
    }
    
    for(int i = 0; i < 5; i = i + 2)
    cout << i << " ";

    return 0;
}