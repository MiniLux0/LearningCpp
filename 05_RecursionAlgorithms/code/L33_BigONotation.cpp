#include <iostream>
#include <vector>
using namespace std;

// ============================================================================
// L33 — NOTACIÓN BIG-O Y ANÁLISIS ASINTÓTICO
// ============================================================================

// 1. O(1) - Complejidad Constante (Sección 10.4)
int obtenerPrimerElemento(const vector<int>& v) {
    if (v.empty()) return -1;
    return v[0]; // 1 sola operación en RAM independientemente del tamaño N
}

// 2. O(log N) - Complejidad Logarítmica (Sección 10.4)
int contarPasosLogaritmicos(int n) {
    int pasos = 0;
    while (n > 1) { // Reduce n a la mitad en cada paso (Divide y Vencerás)
        n /= 2;
        pasos++;
    }
    return pasos;
}

// 3. O(N) - Complejidad Lineal (Sección 10.4)
int calcularSuma(const vector<int>& v) {
    int suma = 0;
    for (int num : v) { // N iteraciones
        suma += num;
    }
    return suma;
}

// 4. O(N log N) - Complejidad Linealítmica (Sección 10.4)
long long simularTrabajoLinearithmic(int n) {
    long long operaciones = 0;
    for (int i = 0; i < n; i++) { // N iteraciones externas
        int temp = n;
        while (temp > 1) { // log N iteraciones internas
            temp /= 2;
            operaciones++;
        }
    }
    return operaciones;
}

// 5. O(N^2) - Complejidad Cuadrática (Sección 10.4)
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

// 6. O(2^N) - Complejidad Exponencial (Sección 10.4)
int ramificacionesExponenciales(int n) {
    if (n <= 1) return 1;
    return ramificacionesExponenciales(n - 1) + ramificacionesExponenciales(n - 1);
}

int main() {
    cout << "=== L33: Notación Big-O e Inspección de Complejidad ===" << endl;

    vector<int> datos = {10, 20, 30, 20, 50, 10};

    cout << "\n--- 1. O(1) Constante ---" << endl;
    cout << "Primer elemento: " << obtenerPrimerElemento(datos) << endl;

    cout << "\n--- 2. O(log N) Logarítmico (N = 1,000,000) ---" << endl;
    cout << "Pasos logarítmicos para N=1,000,000: " << contarPasosLogaritmicos(1000000) << " pasos" << endl;

    cout << "\n--- 3. O(N) Lineal ---" << endl;
    cout << "Suma acumulada: " << calcularSuma(datos) << endl;

    cout << "\n--- 4. O(N log N) Linealítmico (N = 1,000) ---" << endl;
    cout << "Operaciones estimadas: " << simularTrabajoLinearithmic(1000) << endl;

    cout << "\n--- 5. O(N^2) Cuadrático ---" << endl;
    cout << "Número de pares duplicados: " << contarParesIguales(datos) << endl;

    cout << "\n--- 6. O(2^N) Exponencial (N = 10) ---" << endl;
    cout << "Nodos en árbol de llamadas (2^10): " << ramificacionesExponenciales(10) << endl;

    return 0;
}
