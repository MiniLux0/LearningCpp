#include <iostream>
using namespace std;

// Exercise 4 — Increment everything
// Adds delta to each element of the array.
void incrementarTodo(int arr[], int size, int delta) {
    for (int i = 0; i < size; i++) {
        arr[i] += delta;
    }
}

void imprimir(const int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int datos[] = {10, 20, 30};
    int n = sizeof(datos) / sizeof(datos[0]);

    cout << "Original: ";
    imprimir(datos, n);

    incrementarTodo(datos, n, 5);

    cout << "Result (expected 15 25 35): ";
    imprimir(datos, n);

    return 0;
}

// Theoretical explanation:
// In C++, C-style arrays are not passed by value (the full content of the array is not copied).
// When passing `datos` to `incrementarTodo`, the array name "decays" to a pointer to its first element (`int*`).
// Therefore, the function receives the memory address of the original array in `main`.
// Any modification with `arr[i] += delta` directly alters the values of the original array.
// (Note: We will delve deeper into passing by address and pointer arithmetic in the upcoming `06_Pointers` module).