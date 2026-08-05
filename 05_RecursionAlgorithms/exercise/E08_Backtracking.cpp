#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
using namespace std;

// ============================================================================
// EJERCICIO 8 — BACKTRACKING: GENERACIÓN DE SUBCONJUNTOS (POWER SET)
// Complejidad objetivo: Tiempo O(2^n), Espacio O(n) en pila.
// ============================================================================

void generarSubconjuntosHelper(const vector<int>& nums, size_t idx,
                               vector<int>& actual, vector<vector<int>>& resultado) {
    if (idx == nums.size()) {
        resultado.push_back(actual);
        return;
    }

    // Opción 1: Excluir nums[idx]
    generarSubconjuntosHelper(nums, idx + 1, actual, resultado);

    // Opción 2: Incluir nums[idx] (Choose -> Explore -> Unchoose)
    actual.push_back(nums[idx]);
    generarSubconjuntosHelper(nums, idx + 1, actual, resultado);
    actual.pop_back();
}

vector<vector<int>> generarSubconjuntos(const vector<int>& nums) {
    vector<vector<int>> resultado;
    vector<int> actual;
    generarSubconjuntosHelper(nums, 0, actual, resultado);
    return resultado;
}

// ── SISTEMA DE VERIFICACIÓN ROBUSTO ─────────────────────────────────────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [❌ FALLÓ] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automáticas de Backtracking (Subconjuntos)..." << endl;

    vector<int> nums = {1, 2, 3};
    vector<vector<int>> subconjuntos = generarSubconjuntos(nums);

    verificar(subconjuntos.size() == 8, "Para N=3 deben haber 2^3 = 8 subconjuntos");
    cout << "  [PASO] Test 1: Conteo de subconjuntos 2^N (2^3 = 8) OK" << endl;

    cout << "\n¡TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E08: Generación de Subconjuntos con Backtracking ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
