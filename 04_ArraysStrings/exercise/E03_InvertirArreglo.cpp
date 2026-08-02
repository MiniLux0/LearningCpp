#include <iostream>
#include <utility> // std::swap
using namespace std;

// Exercise 3 — In-Place Reversal

// Version 1: Using while with std::swap
void invertir(int arr[], int size) {
    int i = 0;
    int j = size - 1;
    while (i < j) {
        swap(arr[i], arr[j]);
        i++;
        j--;
    }
}

// Version 2: Using for with std::swap
void invertirFor(int arr[], int size) {
    for (int i = 0, j = size - 1; i < j; i++, j--) {
        swap(arr[i], arr[j]);
    }
}

// Version 3: Using while with manual swap (without std::swap)
void invertirManual(int arr[], int size) {
    int i = 0;
    int j = size - 1;
    while (i < j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i++;
        j--;
    }
}

void imprimir(const int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int datos1[] = {1, 2, 3, 4, 5};
    int n1 = sizeof(datos1) / sizeof(datos1[0]);

    cout << "Original 1: ";
    imprimir(datos1, n1);

    invertir(datos1, n1);
    cout << "Reversed with while + std::swap: ";
    imprimir(datos1, n1);

    int datos2[] = {10, 20, 30, 40};
    int n2 = sizeof(datos2) / sizeof(datos2[0]);

    cout << "\nOriginal 2: ";
    imprimir(datos2, n2);

    invertirFor(datos2, n2);
    cout << "Reversed with for + std::swap:   ";
    imprimir(datos2, n2);

    int datos3[] = {100, 200, 300, 400, 500};
    int n3 = sizeof(datos3) / sizeof(datos3[0]);

    cout << "\nOriginal 3: ";
    imprimir(datos3, n3);

    invertirManual(datos3, n3);
    cout << "Reversed with while + manual:    ";
    imprimir(datos3, n3);

    return 0;
}
