#include <iostream>
#include <utility> // std::swap
using namespace std;

// ============================================================================
// L37 — QUICKSORT: ORDENAMIENTO RÁPIDO O(N log N) IN-PLACE
// ============================================================================

void imprimirArreglo(const int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Función de particionado (Lomuto Scheme)
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Selecciona el último elemento como pivote
    int i = low - 1;       // Índice de elementos menores que el pivote

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1; // Posición definitiva del pivote
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Subarreglo izquierdo
        quickSort(arr, pi + 1, high); // Subarreglo derecho
    }
}

int main() {
    cout << "=== L37: QuickSort O(N log N) In-Place ===" << endl;

    int datos[] = {10, 80, 30, 90, 40, 50, 70};
    int n = sizeof(datos) / sizeof(datos[0]);

    cout << "Original: ";
    imprimirArreglo(datos, n);

    quickSort(datos, 0, n - 1);

    cout << "Ordenado con QuickSort: ";
    imprimirArreglo(datos, n);

    return 0;
}
