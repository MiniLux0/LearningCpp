#include <iostream>
#include <vector>
using namespace std;

// ============================================================================
// L36 — MERGESORT: ORDENAMIENTO POR MEZCLA O(N log N)
// ============================================================================

void imprimirArreglo(const int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Función para combinar dos subarreglos ordenados: arr[left..mid] y arr[mid+1..right]
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) { arr[k] = L[i]; i++; k++; }
    while (j < n2) { arr[k] = R[j]; j++; k++; }
}

void mergeSort(int arr[], int left, int right) {
    if (left >= right) return; // Caso Base

    int mid = left + (right - left) / 2;

    mergeSort(arr, left, mid);      // Subarreglo izquierdo
    mergeSort(arr, mid + 1, right);  // Subarreglo derecho
    merge(arr, left, mid, right);    // Combinar ambas mitades
}

int main() {
    cout << "=== L36: MergeSort O(N log N) ===" << endl;

    int datos[] = {38, 27, 43, 3, 9, 82, 10};
    int n = sizeof(datos) / sizeof(datos[0]);

    cout << "Original: ";
    imprimirArreglo(datos, n);

    mergeSort(datos, 0, n - 1);

    cout << "Ordenado con MergeSort: ";
    imprimirArreglo(datos, n);

    return 0;
}
