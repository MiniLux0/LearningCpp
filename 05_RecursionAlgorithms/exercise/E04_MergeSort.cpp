#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

// ============================================================================
// EJERCICIO 4 — MERGESORT (ORDENAMIENTO POR MEZCLA)
// Complejidad objetivo: Tiempo O(n log n), Espacio O(n) auxiliar (temp[]).
// Usa la misma tecnica del arreglo temporal que L37 — sin vector.
// ============================================================================

const int MAX_N = 10000;

// Mezcla dos mitades ya ordenadas dentro de arr[] usando un arreglo temporal
void merge(int arr[], int low, int mid, int high) {
    int temp[MAX_N];

    int p1 = low;      // Puntero mitad izquierda [low..mid]
    int p2 = mid + 1;  // Puntero mitad derecha   [mid+1..high]
    int k  = low;

    while (p1 <= mid && p2 <= high) {
        if (arr[p1] <= arr[p2]) temp[k++] = arr[p1++];
        else                    temp[k++] = arr[p2++];
    }
    while (p1 <= mid)  temp[k++] = arr[p1++];
    while (p2 <= high) temp[k++] = arr[p2++];

    for (int i = low; i <= high; i++)
        arr[i] = temp[i];
}

void mergeSort(int arr[], int low, int high) {
    if (low >= high) return; // Caso Base: subarreglo de 1 elemento

    int mid = low + (high - low) / 2;
    mergeSort(arr, low, mid);
    mergeSort(arr, mid + 1, high);
    merge(arr, low, mid, high);
}

// ── SISTEMA DE VERIFICACION ROBUSTO ──────────────────────────────────────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [FALLO] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automaticas de MergeSort..." << endl;

    // Test 1: Arreglo desordenado
    int datos[]    = {38, 27, 43, 3, 9, 82, 10};
    int esperado[] = {3, 9, 10, 27, 38, 43, 82};
    int n = sizeof(datos) / sizeof(datos[0]);

    mergeSort(datos, 0, n - 1);
    for (int i = 0; i < n; i++)
        verificar(datos[i] == esperado[i], "Elemento en pos " + to_string(i) + " no coincide");
    cout << "  [PASO] Test 1: Arreglo desordenado ordenado correctamente OK" << endl;

    // Test 2: Arreglo ya ordenado (no debe cambiar)
    int ordenado[] = {1, 2, 3, 4, 5};
    int m = sizeof(ordenado) / sizeof(ordenado[0]);
    mergeSort(ordenado, 0, m - 1);
    for (int i = 0; i < m; i++)
        verificar(ordenado[i] == i + 1, "Arreglo ya ordenado no debe cambiar");
    cout << "  [PASO] Test 2: Arreglo ya ordenado permanece igual OK" << endl;

    // Test 3: Un solo elemento (caso base directo)
    int solo[] = {42};
    mergeSort(solo, 0, 0);
    verificar(solo[0] == 42, "Arreglo de 1 elemento debe permanecer igual");
    cout << "  [PASO] Test 3: Arreglo de 1 elemento OK" << endl;

    cout << "\n TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E04: MergeSort O(N log N) ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
