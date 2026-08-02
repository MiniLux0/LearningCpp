#include <iostream>
#include <vector>
using namespace std;

// ============================================================================
// L33 — NOTACIÓN BIG-O Y ANÁLISIS ASINTÓTICO
// ============================================================================

// 1. O(1) - Complejidad Constante
int obtenerPrimerElemento(const vector<int>& v) {
    if (v.empty()) return -1;
    return v[0]; // 1 sola operación independientemente de N
}

// 2. O(N) - Complejidad Lineal
int calcularSuma(const vector<int>& v) {
    int suma = 0;
    for (int num : v) { // N iteraciones
        suma += num;
    }
    return suma;
}

// 3. O(N^2) - Complejidad Cuadrática
int contarParesIguales(const vector<int>& v) {
    int contador = 0;
    int n = v.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && v[i] == v[j]) {
                contador++;
            }
        }
    }
    return contador;
}

int main() {
    cout << "=== L33: Notación Big-O e Inspección de Complejidad ===" << endl;

    vector<int> datos = {10, 20, 30, 20, 50, 10};

    cout << "\n--- 1. O(1) Constante ---" << endl;
    cout << "Primer elemento: " << obtenerPrimerElemento(datos) << endl;

    cout << "\n--- 2. O(N) Lineal ---" << endl;
    cout << "Suma acumulada: " << calcularSuma(datos) << endl;

    cout << "\n--- 3. O(N^2) Cuadrático ---" << endl;
    cout << "Número de pares duplicados: " << contarParesIguales(datos) << endl;

    return 0;
}
