#include <iostream>
#include <vector>
using namespace std;

// ============================================================================
// L36 — MERGESORT: ORDENAMIENTO POR MEZCLA O(N log N)
// Sección 10.3 (p. 443) — Eric Roberts, Programming Abstractions in C++
// ============================================================================

void imprimirVector(const vector<int>& v) {
    for (int x : v) cout << x << " ";
    cout << endl;
}

// ── PASO 1: MEZCLA (MERGE) ────────────────────────────────────────────────
// Combina dos sub-vectores v1 y v2 (ambos ya ordenados) de vuelta en dest.
// El primer elemento de la mezcla SIEMPRE es el menor de los primeros de v1/v2.
void merge(vector<int>& dest, const vector<int>& v1, const vector<int>& v2) {
    int p1 = 0, p2 = 0;
    dest.clear();

    // Mientras ambos vectores tengan elementos, elegir el menor
    while (p1 < (int)v1.size() && p2 < (int)v2.size()) {
        if (v1[p1] <= v2[p2]) {
            dest.push_back(v1[p1++]);
        } else {
            dest.push_back(v2[p2++]);
        }
    }

    // Copiar el resto del vector no agotado (el otro ya quedó vacío)
    while (p1 < (int)v1.size()) dest.push_back(v1[p1++]);
    while (p2 < (int)v2.size()) dest.push_back(v2[p2++]);
}

// ── PASO 2: MERGESORT RECURSIVO ───────────────────────────────────────────
// Estrategia Divide y Vencerás (Sección 10.3):
//   1. Caso Base: vector de 0 o 1 elementos → ya está ordenado
//   2. Dividir: partir el vector en dos mitades v1 y v2
//   3. Conquistar: ordenar v1 y v2 recursivamente
//   4. Combinar: mezclar v1 y v2 de vuelta en vec
void mergeSort(vector<int>& vec) {
    int n = vec.size();
    if (n <= 1) return; // Caso Base

    // Dividir en dos mitades
    int mid = n / 2;
    vector<int> v1(vec.begin(), vec.begin() + mid);
    vector<int> v2(vec.begin() + mid, vec.end());

    // Salto de Fe Recursivo: asumir que sortean correctamente
    mergeSort(v1);
    mergeSort(v2);

    // Mezclar las dos mitades ya ordenadas
    merge(vec, v1, v2);
}

// ── PASO 3: VERSIÓN CON CONTEO DE OPERACIONES ────────────────────────────
int mergeCount = 0;

void mergeConConteo(vector<int>& dest, const vector<int>& v1, const vector<int>& v2) {
    int p1 = 0, p2 = 0;
    dest.clear();
    while (p1 < (int)v1.size() && p2 < (int)v2.size()) {
        mergeCount++;
        if (v1[p1] <= v2[p2]) dest.push_back(v1[p1++]);
        else                   dest.push_back(v2[p2++]);
    }
    while (p1 < (int)v1.size()) dest.push_back(v1[p1++]);
    while (p2 < (int)v2.size()) dest.push_back(v2[p2++]);
}

void mergeSortConConteo(vector<int>& vec) {
    int n = vec.size();
    if (n <= 1) return;
    int mid = n / 2;
    vector<int> v1(vec.begin(), vec.begin() + mid);
    vector<int> v2(vec.begin() + mid, vec.end());
    mergeSortConConteo(v1);
    mergeSortConConteo(v2);
    mergeConConteo(vec, v1, v2);
}

int main() {
    cout << "=== L36: MergeSort O(N log N) — Eric Roberts Sec. 10.3 ===" << endl;

    // ── Demo 1: MergeSort básico ──────────────────────────────────────────
    cout << "\n--- 1. MergeSort (vector<int>) ---" << endl;
    vector<int> datos = {38, 27, 43, 3, 9, 82, 10};
    cout << "Original: "; imprimirVector(datos);
    mergeSort(datos);
    cout << "Ordenado: "; imprimirVector(datos);

    // ── Demo 2: Paso a paso del merge (Sección 10.3) ─────────────────────
    cout << "\n--- 2. Demostración del paso MERGE ---" << endl;
    vector<int> v1 = {25, 30, 40, 70};   // Mitad izquierda ya ordenada
    vector<int> v2 = {19, 35, 55, 80};   // Mitad derecha ya ordenada
    vector<int> resultado;
    cout << "v1 (ordenado): "; imprimirVector(v1);
    cout << "v2 (ordenado): "; imprimirVector(v2);
    merge(resultado, v1, v2);
    cout << "Mezcla final: "; imprimirVector(resultado);

    // ── Demo 3: Conteo de comparaciones para N=8 ─────────────────────────
    cout << "\n--- 3. Conteo de comparaciones de mezcla (N=8) ---" << endl;
    mergeCount = 0;
    vector<int> prueba = {56, 25, 37, 58, 19, 30, 40, 70};
    cout << "Original: "; imprimirVector(prueba);
    mergeSortConConteo(prueba);
    cout << "Ordenado: "; imprimirVector(prueba);
    cout << "Comparaciones en mezclas: " << mergeCount << endl;
    cout << "Cota teorica N*log2(N) = 8*3 = 24" << endl;

    // ── Demo 4: Comparativa de escalamiento N^2 vs N log N ───────────────
    cout << "\n--- 4. Escalamiento N^2 vs N*log(N) (de la Figura 10-5) ---" << endl;
    cout << "N=10:      N^2=100        N*logN~33" << endl;
    cout << "N=100:     N^2=10,000     N*logN~664" << endl;
    cout << "N=1,000:   N^2=1,000,000  N*logN~9,965" << endl;
    cout << "N=10,000:  N^2=100M       N*logN~132,877" << endl;
    cout << "N=100,000: N^2=10^10      N*logN~1,660,964" << endl;

    return 0;
}
