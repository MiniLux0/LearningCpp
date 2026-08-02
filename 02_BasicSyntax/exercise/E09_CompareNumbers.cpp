/*
 * E09 — Compare Numbers
 * ---------------------
 * Asks for two integer numbers.
 * Prints which one is greater, or if they are equal.
 *
 * Example:
 *   Input:  10, 20
 *   Output: 20 is greater
 */

#include <iostream>
using namespace std;

int main() {

    double value1;
    double value2;

    cout << "Enter the first number: ";
    cin >> value1;

    cout << "Enter the second number: ";
    cin >> value2;

    if(value1 > value2){
        cout << value1 << " is greater than " << value2;
    } else if(value1 < value2){
        cout << value1 << " is less than " << value2;
    } else{
        cout << value1 << " is equal to " << value2;
    }



    return 0;
}
