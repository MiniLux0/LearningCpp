/*
 * E09 — Compare Numbers
 * ---------------------
 * Pide dos numeros enteros.
 * Imprime cual es mayor, o si son iguales.
 *
 * Ejemplo:
 *   Input:  10, 20
 *   Output: 20 es mayor
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
        cout << value1 << " equal to " << value2;
    }



    return 0;
}
