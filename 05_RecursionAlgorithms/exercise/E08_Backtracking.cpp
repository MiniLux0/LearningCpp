#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

// ============================================================================
// EJERCICIO 8 — BACKTRACKING: GENERACIÓN DE SUBCONJUNTOS (POWER SET)
// Complejidad objetivo: Tiempo O(2^n), Espacio O(n) en pila.
// Usa arreglos en lugar de vector para ser congruente con L39.
// ============================================================================

const int MAX_ELEMS = 20;
int actual[MAX_ELEMS]; // Arreglo que representa el subconjunto en construccion
int actualSize = 0;    // Cuantos elementos hay en 'actual'
int countSubconjuntos = 0; // Para la verificacion automatica

void generarSubconjuntos(const int nums[], int n, int idx) {
    if (idx == n) {
        countSubconjuntos++;
        return;
    }

    // Opcion 1: NO incluir nums[idx]
    generarSubconjuntos(nums, n, idx + 1);

    // Opcion 2: SI incluir nums[idx] (Choose -> Explore -> Unchoose)
    actual[actualSize] = nums[idx]; // 1. ELEGIR
    actualSize++;
    generarSubconjuntos(nums, n, idx + 1); // 2. EXPLORAR
    actualSize--;                          // 3. DESHACER
}

// ── SISTEMA DE VERIFICACION ROBUSTO ──────────────────────────────────────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [FALLO] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automaticas de Backtracking (Subconjuntos)..." << endl;

    int nums[] = {1, 2, 3};
    int n = 3;
    
    countSubconjuntos = 0;
    actualSize = 0;
    generarSubconjuntos(nums, n, 0);

    verificar(countSubconjuntos == 8, "Para N=3 deben haber 2^3 = 8 subconjuntos");
    cout << "  [PASO] Test 1: Conteo de subconjuntos 2^N (2^3 = 8) OK" << endl;
    
    int nums2[] = {1, 2, 3, 4, 5};
    countSubconjuntos = 0;
    actualSize = 0;
    generarSubconjuntos(nums2, 5, 0);

    verificar(countSubconjuntos == 32, "Para N=5 deben haber 2^5 = 32 subconjuntos");
    cout << "  [PASO] Test 2: Conteo de subconjuntos 2^N (2^5 = 32) OK" << endl;

    cout << "\n TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E08: Generacion de Subconjuntos con Backtracking ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
