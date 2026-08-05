#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

// ============================================================================
// EJERCICIO 3 — BÚSQUEDA BINARIA RECURSIVA
// Objetivo: Búsqueda binaria recursiva en arreglos ordenados.
// Complejidad objetivo: Tiempo O(log n), Espacio O(log n) en pila.
// ============================================================================

int busquedaBinaria(const int arr[], int low, int high, int target) {
    if (low > high) return -1; // Caso base: no encontrado

    int mid = low + (high - low) / 2; // Midpoint seguro

    if (arr[mid] == target) return mid;
    if (arr[mid] > target)
        return busquedaBinaria(arr, low, mid - 1, target);
    else
        return busquedaBinaria(arr, mid + 1, high, target);
}

// ── SISTEMA DE VERIFICACIÓN ROBUSTO ─────────────────────────────────────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [❌ FALLÓ] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automáticas de Búsqueda Binaria..." << endl;
    int datos[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(datos) / sizeof(datos[0]);

    // Test 1: Búsqueda de elementos existentes
    verificar(busquedaBinaria(datos, 0, n - 1, 23) == 5, "23 debe estar en índice 5");
    verificar(busquedaBinaria(datos, 0, n - 1, 2) == 0, "2 debe estar en índice 0");
    verificar(busquedaBinaria(datos, 0, n - 1, 91) == n - 1, "91 debe estar al final");
    cout << "  [PASO] Test 1: Búsqueda de elementos presentes OK" << endl;

    // Test 2: Búsqueda de elemento no existente
    verificar(busquedaBinaria(datos, 0, n - 1, 50) == -1, "50 no debe existir (-1)");
    cout << "  [PASO] Test 2: Elementos ausentes retornan -1 OK" << endl;

    cout << "\n¡TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E03: Búsqueda Binaria Recursiva ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
