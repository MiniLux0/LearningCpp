#include <iostream>
using namespace std;

int main() {

    int lionAge;
    int elephantAge = 15;
    string pwd;

    cout << "Enter the lion's age: ";
    cin >> lionAge;

    if (lionAge < 18) {
        cout << "The lion is younger\n";
    }

    if (lionAge >= 18) {
        cout << "The lion is older\n";
    }

    if (elephantAge <= 18) {
        cout << "The elephant is younger\n";
    }

    return 0;
}
