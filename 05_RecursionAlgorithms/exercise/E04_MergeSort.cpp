#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
using namespace std;

// ============================================================================
// EJERCICIO 4 — MERGESORT (ORDENAMIENTO POR MEZCLA)
// Complejidad objetivo: Tiempo O(n log n), Espacio O(n) auxiliar.
// ============================================================================

void merge(vector<int>& dest, const vector<int>& v1, const vector<int>& v2) {
    size_t p1 = 0, p2 = 0;
    dest.clear();
    while (p1 < v1.size() && p2 < v2.size()) {
        if (v1[p1] <= v2[p2]) dest.push_back(v1[p1++]);
        else                  dest.push_back(v2[p2++]);
    }
    while (p1 < v1.size()) dest.push_back(v1[p1++]);
    while (p2 < v2.size()) dest.push_back(v2[p2++]);
}

void mergeSort(vector<int>& vec) {
    if (vec.size() <= 1) return;

    size_t mid = vec.size() / 2;
    vector<int> v1(vec.begin(), vec.begin() + mid);
    vector<int> v2(vec.begin() + mid, vec.end());

    mergeSort(v1);
    mergeSort(v2);
    merge(vec, v1, v2);
}

// ── SISTEMA DE VERIFICACIÓN ROBUSTO ─────────────────────────────────────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [❌ FALLÓ] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automáticas de MergeSort..." << endl;

    vector<int> datos = {38, 27, 43, 3, 9, 82, 10};
    vector<int> esperado = {3, 9, 10, 27, 38, 43, 82};

    mergeSort(datos);
    verificar(datos == esperado, "Arreglo desordenado no coincide");
    cout << "  [PASO] Test 1: Ordenamiento de vector estándar OK" << endl;

    vector<int> vacio = {};
    mergeSort(vacio);
    verificar(vacio.empty(), "Vector vacío debió permanecer vacío");
    cout << "  [PASO] Test 2: Caso borde vector vacío OK" << endl;

    cout << "\n¡TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E04: MergeSort O(N log N) ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
