#include <iostream>
using namespace std;

// ============================================================================
// L34 — NOTACIÓN BIG-O Y ANÁLISIS ASINTÓTICO
// ============================================================================

// 1. O(1) - Complejidad Constante (Sección 10.4)
int obtenerPrimerElemento(const int arr[], int size) {
    if (size == 0) return -1;
    return arr[0]; // 1 sola operación en RAM independientemente del tamaño N
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
int calcularSuma(const int arr[], int size) {
    int suma = 0;
    for (int i = 0; i < size; i++) { // N iteraciones
        suma += arr[i];
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
int contarParesIguales(const int arr[], int size) {
    int contador = 0;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (i != j && arr[i] == arr[j]) {
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
    cout << "=== L34: Notación Big-O e Inspección de Complejidad ===" << endl;

    const int size = 6;
    int datos[size] = {10, 20, 30, 20, 50, 10};

    cout << "\n--- 1. O(1) Constante ---" << endl;
    cout << "Primer elemento: " << obtenerPrimerElemento(datos, size) << endl;

    cout << "\n--- 2. O(log N) Logarítmico (N = 1,000,000) ---" << endl;
    cout << "Pasos logarítmicos para N=1,000,000: " << contarPasosLogaritmicos(1000000) << " pasos" << endl;

    cout << "\n--- 3. O(N) Lineal ---" << endl;
    cout << "Suma acumulada: " << calcularSuma(datos, size) << endl;

    cout << "\n--- 4. O(N log N) Linealítmico (N = 1,000) ---" << endl;
    cout << "Operaciones estimadas: " << simularTrabajoLinearithmic(1000) << endl;

    cout << "\n--- 5. O(N^2) Cuadrático ---" << endl;
    cout << "Número de pares duplicados: " << contarParesIguales(datos, size) << endl;

    cout << "\n--- 6. O(2^N) Exponencial (N = 10) ---" << endl;
    cout << "Nodos en árbol de llamadas (2^10): " << ramificacionesExponenciales(10) << endl;

    return 0;
}
