#include <iostream>
using namespace std;

// Exercise 1 — Maximum
// Returns the maximum value of the array.
int maximo(const int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int main() {
    int datos1[] = {3, 7, 2, 9, 5};
    int n1 = sizeof(datos1)/sizeof(datos1[0]);

    cout << "Maximum value Data 1: "<< maximo(datos1, n1) << endl;

    return 0;
}
