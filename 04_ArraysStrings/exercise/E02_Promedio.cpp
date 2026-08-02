#include <iostream>
using namespace std;

// Exercise 2 — Average
// Calculates the average of the elements.
double promedio(const int arr[], int size) {
    double suma = 0;
    for (int i = 0; i < size; i++) {
        suma = suma + arr[i];
    }
    return suma/size;
}



int main() {
    int datos1[] = {10, 20, 30, 40};
    int n1 = sizeof(datos1) / sizeof(datos1[0]);
    cout << "Test 1 (expected 25.0): " << promedio(datos1, n1) << endl;

    int datos2[] = {5, 5, 6};
    int n2 = sizeof(datos2) / sizeof(datos2[0]);
    cout << "Test 2 (expected ~5.333): " << promedio(datos2, n2) << endl;

    return 0;
}
