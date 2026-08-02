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

// 1. Selection Sort - O(N^2) (Sección 10.1)
void selectionSort(int arr[], int n, int& comp, int& swaps) {
    comp = 0; swaps = 0;
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            comp++;
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            swap(arr[i], arr[minIdx]);
            swaps++;
        }
    }
}

// 2. Insertion Sort - O(N^2) peor caso, O(N) mejor caso (Sección 10.1)
void insertionSort(int arr[], int n, int& comp, int& shifts) {
    comp = 0; shifts = 0;
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0) {
            comp++;
            if (arr[j] > key) {
                arr[j + 1] = arr[j];
                shifts++;
                j--;
            } else {
                break;
            }
        }
        arr[j + 1] = key;
    }
}

// 3. Bubble Sort - O(N^2) con optimización de parada temprana (Sección 10.1)
void bubbleSort(int arr[], int n, int& comp, int& swaps) {
    comp = 0; swaps = 0;
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            comp++;
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swaps++;
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

int main() {
    cout << "=== L35: Algoritmos de Ordenamiento Cuadráticos ===" << endl;

    int comp = 0, movs = 0;

    int datos1[] = {64, 25, 12, 22, 11};
    int n1 = sizeof(datos1) / sizeof(datos1[0]);
    cout << "\n--- 1. Selection Sort ---" << endl;
    cout << "Original: "; imprimirArreglo(datos1, n1);
    selectionSort(datos1, n1, comp, movs);
    cout << "Ordenado: "; imprimirArreglo(datos1, n1);
    cout << "  (Comparaciones: " << comp << ", Intercambios: " << movs << ")" << endl;

    int datos2[] = {12, 11, 13, 5, 6};
    int n2 = sizeof(datos2) / sizeof(datos2[0]);
    cout << "\n--- 2. Insertion Sort ---" << endl;
    cout << "Original: "; imprimirArreglo(datos2, n2);
    insertionSort(datos2, n2, comp, movs);
    cout << "Ordenado: "; imprimirArreglo(datos2, n2);
    cout << "  (Comparaciones: " << comp << ", Desplazamientos: " << movs << ")" << endl;

    int datos3[] = {5, 1, 4, 2, 8};
    int n3 = sizeof(datos3) / sizeof(datos3[0]);
    cout << "\n--- 3. Bubble Sort ---" << endl;
    cout << "Original: "; imprimirArreglo(datos3, n3);
    bubbleSort(datos3, n3, comp, movs);
    cout << "Ordenado: "; imprimirArreglo(datos3, n3);
    cout << "  (Comparaciones: " << comp << ", Intercambios: " << movs << ")" << endl;

    return 0;
}
