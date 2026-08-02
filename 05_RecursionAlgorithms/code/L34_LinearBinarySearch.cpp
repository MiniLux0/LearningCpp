#include <iostream>
using namespace std;

// ============================================================================
// L34 — BÚSQUEDA LINEAL Y BÚSQUEDA BINARIA (ITERATIVAS Y RECURSIVAS)
// ============================================================================

// ============================================================================
// L34 — BÚSQUEDA LINEAL Y BÚSQUEDA BINARIA (ITERATIVAS Y RECURSIVAS)
// ============================================================================

// 1. Búsqueda Lineal Iterativa - O(N) (Sección 10.2)
int busquedaLineal(const int arr[], int size, int target, int& comparaciones) {
    comparaciones = 0;
    for (int i = 0; i < size; i++) {
        comparaciones++;
        if (arr[i] == target) return i;
    }
    return -1;
}

// 2. Búsqueda Lineal Recursiva - O(N)
int busquedaLinealRecursiva(const int arr[], int size, int target, int index = 0) {
    if (index >= size) return -1;
    if (arr[index] == target) return index;
    return busquedaLinealRecursiva(arr, size, target, index + 1);
}

// 3. Búsqueda Binaria Iterativa - O(log N) (Sección 7.5 & 10.2 - Requiere arreglo ordenado)
int busquedaBinaria(const int arr[], int size, int target, int& comparaciones) {
    comparaciones = 0;
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        comparaciones++;
        int mid = low + (high - low) / 2; // Prevención de desbordamiento de entero signed 32-bit
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

// 4. Búsqueda Binaria Recursiva - O(log N) (Sección 7.5 - Eric Roberts)
int busquedaBinariaRecursiva(const int arr[], int low, int high, int target) {
    if (low > high) return -1; // Caso Base 1: No encontrado

    int mid = low + (high - low) / 2; // Prevención de desbordamiento
    if (arr[mid] == target) return mid; // Caso Base 2: Encontrado

    if (arr[mid] > target)
        return busquedaBinariaRecursiva(arr, low, mid - 1, target);
    else
        return busquedaBinariaRecursiva(arr, mid + 1, high, target);
}

int main() {
    cout << "=== L34: Búsqueda Lineal y Binaria ===" << endl;

    int datosDesordenados[] = {42, 12, 88, 7, 19, 33};
    int nDes = sizeof(datosDesordenados) / sizeof(datosDesordenados[0]);

    cout << "\n--- 1. Búsqueda Lineal en Arreglo Desordenado ---" << endl;
    int compLin = 0;
    int posLineal = busquedaLineal(datosDesordenados, nDes, 19, compLin);
    cout << "Buscar 19 (Iterativo): Encontrado en índice " << posLineal << " (" << compLin << " comparaciones)" << endl;
    
    int posLinealRec = busquedaLinealRecursiva(datosDesordenados, nDes, 88);
    cout << "Buscar 88 (Recursivo): Encontrado en índice " << posLinealRec << endl;

    int datosOrdenados[] = {5, 12, 19, 27, 33, 45, 58, 64, 72, 89, 93};
    int nOrd = sizeof(datosOrdenados) / sizeof(datosOrdenados[0]);

    cout << "\n--- 2. Búsqueda Binaria en Arreglo Ordenado ---" << endl;
    int target = 45;
    int compBin = 0;
    int posBin = busquedaBinaria(datosOrdenados, nOrd, target, compBin);
    cout << "Buscar " << target << " (Binaria Iterativa): Encontrado en índice " << posBin << " (" << compBin << " comparaciones)" << endl;

    int posBinRec = busquedaBinariaRecursiva(datosOrdenados, 0, nOrd - 1, 89);
    cout << "Buscar 89 (Binaria Recursiva): Encontrado en índice " << posBinRec << endl;

    // 3. Demostración de Escalamiento Asintótico (Simulación)
    cout << "\n--- 3. Comparativa de Escalamiento Asintótico ---" << endl;
    cout << "Para N = 1,000,000 elementos:" << endl;
    cout << "  - Búsqueda Lineal (Peor Caso): 1,000,000 comparaciones (O(N))" << endl;
    cout << "  - Búsqueda Binaria (Peor Caso): ~20 comparaciones (O(log N))" << endl;

    return 0;
}
