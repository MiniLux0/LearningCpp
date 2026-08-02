#include <iostream>
#include <utility> // std::swap
using namespace std;

// ============================================================================
// L35 — ALGORITMOS DE ORDENAMIENTO CUADRÁTICOS O(N^2)
// ============================================================================

void imprimirArreglo(const int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// 1. Selection Sort - O(N^2)
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        swap(arr[i], arr[minIdx]);
    }
}

// 2. Insertion Sort - O(N^2) peor caso, O(N) mejor caso
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// 3. Bubble Sort - O(N^2) con optimización de parada temprana
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

int main() {
    cout << "=== L35: Algoritmos de Ordenamiento Cuadráticos ===" << endl;

    int datos1[] = {64, 25, 12, 22, 11};
    int n1 = sizeof(datos1) / sizeof(datos1[0]);

    cout << "\n--- 1. Selection Sort ---" << endl;
    cout << "Original: "; imprimirArreglo(datos1, n1);
    selectionSort(datos1, n1);
    cout << "Ordenado: "; imprimirArreglo(datos1, n1);

    int datos2[] = {12, 11, 13, 5, 6};
    int n2 = sizeof(datos2) / sizeof(datos2[0]);

    cout << "\n--- 2. Insertion Sort ---" << endl;
    cout << "Original: "; imprimirArreglo(datos2, n2);
    insertionSort(datos2, n2);
    cout << "Ordenado: "; imprimirArreglo(datos2, n2);

    int datos3[] = {5, 1, 4, 2, 8};
    int n3 = sizeof(datos3) / sizeof(datos3[0]);

    cout << "\n--- 3. Bubble Sort ---" << endl;
    cout << "Original: "; imprimirArreglo(datos3, n3);
    bubbleSort(datos3, n3);
    cout << "Ordenado: "; imprimirArreglo(datos3, n3);

    return 0;
}
