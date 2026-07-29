#include <iostream>


using namespace std;

int main() {
    
    int x = 1;
    // switch-case: fall-through
    switch(x) {
    case 1:
        cout << "A";
    case 2:
        cout << "B";
    case 3:
        cout << "C";
    default:
        cout << "D";
    }

    return 0;

}

