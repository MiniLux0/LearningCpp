#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
using namespace std;

// ============================================================================
// EJERCICIO 6 — EXPONENCIACIÓN RÁPIDA (POTENCIA RECURSIVA)
// Complejidad objetivo: Tiempo O(log exp), Espacio O(log exp) en pila.
// ============================================================================

double potenciaRapida(double base, int exp) {
    if (exp == 0) return 1.0;
    if (exp < 0) return 1.0 / potenciaRapida(base, -exp);

    double half = potenciaRapida(base, exp / 2);
    if (exp % 2 == 0) return half * half;
    else              return base * half * half;
}

// ── SISTEMA DE VERIFICACIÓN ROBUSTO ─────────────────────────────────────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [❌ FALLÓ] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automáticas de Exponenciación Rápida..." << endl;

    verificar(abs(potenciaRapida(2.0, 10) - 1024.0) < 1e-6, "2^10 = 1024");
    verificar(abs(potenciaRapida(2.0, -2) - 0.25) < 1e-6, "2^-2 = 0.25");
    cout << "  [PASO] Test 1: Potencias positivas y negativas OK" << endl;

    verificar(abs(potenciaRapida(5.0, 0) - 1.0) < 1e-6, "5^0 = 1.0");
    cout << "  [PASO] Test 2: Exponente 0 OK" << endl;

    cout << "\n¡TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E06: Exponenciación Rápida O(log exp) ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
