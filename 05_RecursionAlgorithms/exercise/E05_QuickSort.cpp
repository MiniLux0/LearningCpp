#include <iostream>
#include <vector>
#include <utility>
#include <cstdlib>
#include <string>
using namespace std;

// ============================================================================
// EJERCICIO 5 — QUICKSORT CON PARTICIONADO LOMUTO
// Complejidad objetivo: Tiempo O(n log n) promedio, Espacio O(log n) in-place.
// ============================================================================

int partitionLomuto(int arr[], int low, int high) {
    int pivot = arr[high]; // Pivote al final
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionLomuto(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// ── SISTEMA DE VERIFICACIÓN ROBUSTO ─────────────────────────────────────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [❌ FALLÓ] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automáticas de QuickSort..." << endl;

    int datos[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(datos) / sizeof(datos[0]);
    int esperado[] = {1, 5, 7, 8, 9, 10};

    quickSort(datos, 0, n - 1);
    for (int i = 0; i < n; i++) {
        verificar(datos[i] == esperado[i], "Elementos no coinciden en posición " + to_string(i));
    }
    cout << "  [PASO] Test 1: QuickSort Lomuto OK" << endl;

    cout << "\n¡TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E05: QuickSort Lomuto ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
