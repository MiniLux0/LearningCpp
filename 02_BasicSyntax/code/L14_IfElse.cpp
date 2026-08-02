#include <iostream>
using namespace std;

int main() {

    int lionAge;
    int elephantAge;

    cout << "Enter the lion's age: ";
    cin >> lionAge;

    if (lionAge < 18) {
        cout << "\"The lion is younger\"\n";
    } else {
        cout << "\"The lion is older\"\n";
    }

    cout << "Enter the elephant's age: ";
    cin >> elephantAge;

    if (elephantAge <= 18) {
        cout << "\"The elephant is younger\"\n";
    } else {
        cout << "\"The elephant is older\"\n";
    }

    return 0;
}
