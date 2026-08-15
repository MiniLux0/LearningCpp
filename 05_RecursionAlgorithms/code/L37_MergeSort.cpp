#include <iostream>
using namespace std;

// ============================================================================
// L36 — MERGESORT: ORDENAMIENTO POR MEZCLA O(N log N)
// Sección 10.3 (p. 443) — Eric Roberts, Programming Abstractions in C++
// ============================================================================

void imprimirArreglo(const int arr[], int size) {
    for (int i = 0; i < size; i++) cout << arr[i] << " ";
    cout << endl;
}

// ── PASO 1: MEZCLA (MERGE) ────────────────────────────────────────────────
// Combina dos mitades ya ordenadas dentro del mismo arreglo.
void merge(int arr[], int left, int mid, int right) {
    int temp[100]; // Arreglo estático temporal, suficiente para las demos
    int p1 = left;
    int p2 = mid + 1;
    int idx = 0;

    // Mientras ambas mitades tengan elementos, elegir el menor
    while (p1 <= mid && p2 <= right) {
        if (arr[p1] <= arr[p2]) {
            temp[idx++] = arr[p1++];
        } else {
            temp[idx++] = arr[p2++];
        }
    }

    // Copiar el resto de la mitad no agotada
    while (p1 <= mid) temp[idx++] = arr[p1++];
    while (p2 <= right) temp[idx++] = arr[p2++];

    // Volcar los elementos ordenados de nuevo al arreglo original
    for (int i = 0; i < idx; i++) {
        arr[left + i] = temp[i];
    }
}

// ── PASO 2: MERGESORT RECURSIVO ───────────────────────────────────────────
void mergeSort(int arr[], int left, int right) {
    if (left >= right) return; // Caso Base

    int mid = left + (right - left) / 2;

    // Salto de Fe Recursivo
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);

    // Mezclar
    merge(arr, left, mid, right);
}

// ── PASO 3: VERSIÓN CON CONTEO DE OPERACIONES ────────────────────────────
int mergeCount = 0;

void mergeConConteo(int arr[], int left, int mid, int right) {
    int temp[100];
    int p1 = left, p2 = mid + 1, idx = 0;
    while (p1 <= mid && p2 <= right) {
        mergeCount++;
        if (arr[p1] <= arr[p2]) temp[idx++] = arr[p1++];
        else                    temp[idx++] = arr[p2++];
    }
    while (p1 <= mid) temp[idx++] = arr[p1++];
    while (p2 <= right) temp[idx++] = arr[p2++];
    for (int i = 0; i < idx; i++) arr[left + i] = temp[i];
}

void mergeSortConConteo(int arr[], int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSortConConteo(arr, left, mid);
    mergeSortConConteo(arr, mid + 1, right);
    mergeConConteo(arr, left, mid, right);
}

int main() {
    cout << "=== L36: MergeSort O(N log N) — Eric Roberts Sec. 10.3 ===" << endl;

    // ── Demo 1: MergeSort básico ──────────────────────────────────────────
    cout << "\n--- 1. MergeSort (Arreglo Estático) ---" << endl;
    const int size1 = 7;
    int datos[size1] = {38, 27, 43, 3, 9, 82, 10};
    cout << "Original: "; imprimirArreglo(datos, size1);
    mergeSort(datos, 0, size1 - 1);
    cout << "Ordenado: "; imprimirArreglo(datos, size1);

    // ── Demo 2: Paso a paso del merge ────────────────────────────────────
    cout << "\n--- 2. Demostración del paso MERGE ---" << endl;
    const int size2 = 8;
    int v[size2] = {25, 30, 40, 70, 19, 35, 55, 80}; // Dos mitades ya ordenadas
    cout << "Arreglo con 2 mitades ordenadas: "; imprimirArreglo(v, size2);
    merge(v, 0, 3, 7);
    cout << "Mezcla final: "; imprimirArreglo(v, size2);

    // ── Demo 3: Conteo de comparaciones para N=8 ─────────────────────────
    cout << "\n--- 3. Conteo de comparaciones de mezcla (N=8) ---" << endl;
    mergeCount = 0;
    const int size3 = 8;
    int prueba[size3] = {56, 25, 37, 58, 19, 30, 40, 70};
    cout << "Original: "; imprimirArreglo(prueba, size3);
    mergeSortConConteo(prueba, 0, size3 - 1);
    cout << "Ordenado: "; imprimirArreglo(prueba, size3);
    cout << "Comparaciones en mezclas: " << mergeCount << endl;
    cout << "Cota teorica N*log2(N) = 8*3 = 24" << endl;

    // ── Demo 4: Comparativa de escalamiento N^2 vs N log N ───────────────
    cout << "\n--- 4. Escalamiento N^2 vs N*log(N) ---" << endl;
    cout << "N=10:      N^2=100        N*logN~33" << endl;
    cout << "N=100:     N^2=10,000     N*logN~664" << endl;
    cout << "N=1,000:   N^2=1,000,000  N*logN~9,965" << endl;

    return 0;
}
