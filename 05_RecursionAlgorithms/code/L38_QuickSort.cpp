#include <iostream>
#include <utility>  // swap
#include <cstdlib>  // rand
using namespace std;

// ============================================================================
// L37 — QUICKSORT: ORDENAMIENTO RÁPIDO O(N log N) IN-PLACE
// Sección 10.5 (p. 452) — Eric Roberts, Programming Abstractions in C++
// ============================================================================

void imprimirArreglo(const int arr[], int n) {
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}

// ── ESQUEMA DE HOARE (clásico de Eric Roberts, Sec. 10.5) ─────────────────
// El pivote es arr[low] (primer elemento).
// lh avanza desde la izquierda buscando elementos >= pivote.
// rh retrocede desde la derecha buscando elementos <  pivote.
// Cuando se cruzan, se intercambia el pivote con arr[rh].
int particionHoare(int arr[], int low, int high, int& comparaciones) {
    int pivot = arr[low]; // Elegir el primer elemento como pivote (Roberts, Sec. 10.5)
    int lh = low + 1;
    int rh = high;

    while (true) {
        // Avanzar lh hasta un elemento >= pivote
        while (lh <= rh) {
            comparaciones++;
            if (arr[lh] < pivot) lh++;
            else break;
        }
        // Retroceder rh hasta un elemento < pivote
        while (rh >= lh) {
            comparaciones++;
            if (arr[rh] >= pivot) rh--;
            else break;
        }
        if (lh > rh) break;
        swap(arr[lh], arr[rh]);
        lh++; rh--;
    }
    // Colocar el pivote en su posición definitiva
    swap(arr[low], arr[rh]);
    return rh; // Índice de la posición definitiva del pivote
}

void quickSortHoare(int arr[], int low, int high, int& comparaciones) {
    if (low >= high) return; // Caso Base: 0 o 1 elementos

    int pivotIdx = particionHoare(arr, low, high, comparaciones);
    quickSortHoare(arr, low, pivotIdx - 1, comparaciones);  // Subarreglo izquierdo (< pivote)
    quickSortHoare(arr, pivotIdx + 1, high, comparaciones); // Subarreglo derecho  (>= pivote)
}

// ── ESQUEMA DE LOMUTO con pivote ALEATORIO (Sec. 10.5 — mejora de rendimiento) ──
// Elegir un pivote aleatorio mitiga el peor caso O(N^2) en arreglos ya ordenados.
int particionLomutoAleatorio(int arr[], int low, int high) {
    int rIdx = low + rand() % (high - low + 1);
    swap(arr[rIdx], arr[high]); // Mover pivote aleatorio al final

    int pivot = arr[high];
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

void quickSortAleatorio(int arr[], int low, int high) {
    if (low < high) {
        int pi = particionLomutoAleatorio(arr, low, high);
        quickSortAleatorio(arr, low, pi - 1);
        quickSortAleatorio(arr, pi + 1, high);
    }
}

int main() {
    cout << "=== L37: QuickSort O(N log N) — Eric Roberts Sec. 10.5 ===" << endl;

    // ── Demo 1: QuickSort con esquema de Hoare ────────────────────────────
    cout << "\n--- 1. QuickSort (Esquema de Hoare, Pivote = primer elemento) ---" << endl;
    int datos1[] = {56, 25, 37, 58, 19, 30, 40, 70};
    int n1 = sizeof(datos1) / sizeof(datos1[0]);
    cout << "Original: "; imprimirArreglo(datos1, n1);
    int comp1 = 0;
    quickSortHoare(datos1, 0, n1 - 1, comp1);
    cout << "Ordenado: "; imprimirArreglo(datos1, n1);
    cout << "  (Comparaciones en partición: " << comp1 << ")" << endl;

    // ── Demo 2: Peor caso de QuickSort — arreglo ya ordenado ─────────────
    cout << "\n--- 2. Peor Caso: arreglo ya ordenado (sin pivote aleatorio) ---" << endl;
    int datos2[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int n2 = sizeof(datos2) / sizeof(datos2[0]);
    cout << "Original (ya ordenado): "; imprimirArreglo(datos2, n2);
    int comp2 = 0;
    quickSortHoare(datos2, 0, n2 - 1, comp2);
    cout << "Ordenado: "; imprimirArreglo(datos2, n2);
    cout << "  (Comparaciones: " << comp2 << " — notar degradacion hacia O(N^2))" << endl;

    // ── Demo 3: QuickSort con pivote aleatorio (mitiga peor caso) ─────────
    cout << "\n--- 3. QuickSort con Pivote Aleatorio (mitiga O(N^2)) ---" << endl;
    int datos3[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int n3 = sizeof(datos3) / sizeof(datos3[0]);
    cout << "Original (ya ordenado): "; imprimirArreglo(datos3, n3);
    quickSortAleatorio(datos3, 0, n3 - 1);
    cout << "Ordenado: "; imprimirArreglo(datos3, n3);

    // ── Demo 4: Comparativa MergeSort vs QuickSort ────────────────────────
    cout << "\n--- 4. MergeSort vs QuickSort (Figura 10-10, p. 457) ---" << endl;
    cout << "QuickSort es varias veces mas rapido que MergeSort en la practica." << endl;
    cout << "  Razon: QuickSort opera IN-PLACE (O(log N) pila de llamadas)." << endl;
    cout << "  MergeSort requiere O(N) memoria auxiliar para los sub-vectores." << endl;
    cout << "  Sin embargo, QuickSort tiene peor caso O(N^2) (arreglo ya ordenado)" << endl;
    cout << "  mientras MergeSort garantiza O(N log N) en TODOS los casos." << endl;

    return 0;
}
