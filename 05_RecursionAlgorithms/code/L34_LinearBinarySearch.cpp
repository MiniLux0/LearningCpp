#include <iostream>
using namespace std;

// ============================================================================
// L34 — BÚSQUEDA LINEAL Y BÚSQUEDA BINARIA (ITERATIVAS Y RECURSIVAS)
// ============================================================================

// 1. Búsqueda Lineal Iterativa - O(N)
int busquedaLineal(const int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
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

// 3. Búsqueda Binaria Iterativa - O(log N) (Requiere arreglo ordenado)
int busquedaBinaria(const int arr[], int size, int target) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2; // Seguro contra overflow
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

// 4. Búsqueda Binaria Recursiva - O(log N)
int busquedaBinariaRecursiva(const int arr[], int low, int high, int target) {
    if (low > high) return -1; // Caso Base: No encontrado

    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid; // Caso Base: Encontrado

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
    int posLineal = busquedaLineal(datosDesordenados, nDes, 19);
    cout << "Buscar 19 (Iterativo): " << (posLineal != -1 ? "Encontrado en índice " + to_string(posLineal) : "No encontrado") << endl;
    
    int posLinealRec = busquedaLinealRecursiva(datosDesordenados, nDes, 88);
    cout << "Buscar 88 (Recursivo): " << (posLinealRec != -1 ? "Encontrado en índice " + to_string(posLinealRec) : "No encontrado") << endl;

    int datosOrdenados[] = {5, 12, 19, 27, 33, 45, 58, 64, 72, 89, 93};
    int nOrd = sizeof(datosOrdenados) / sizeof(datosOrdenados[0]);

    cout << "\n--- 2. Búsqueda Binaria en Arreglo Ordenado ---" << endl;
    int target = 45;
    int posBin = busquedaBinaria(datosOrdenados, nOrd, target);
    cout << "Buscar " << target << " (Binaria Iterativa): Encontrado en índice " << posBin << endl;

    int posBinRec = busquedaBinariaRecursiva(datosOrdenados, 0, nOrd - 1, 89);
    cout << "Buscar 89 (Binaria Recursiva): Encontrado en índice " << posBinRec << endl;

    return 0;
}
