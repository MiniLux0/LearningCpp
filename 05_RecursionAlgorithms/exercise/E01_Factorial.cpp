#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

// ============================================================================
// EJERCICIO 1 — FACTORIAL RECURSIVO
// Objetivo: Calcular n! recursivamente manejando casos base y valores inválidos.
// Complejidad objetivo: Tiempo O(n), Espacio O(n) en pila de llamadas.
// ============================================================================

// TODO: Implementa la función factorial recursiva.
// - Caso base: 0! = 1, 1! = 1
// - Paso recursivo: n * factorial(n - 1)
// - Validación: Si n < 0, retornar -1
long long factorial(int n) {
    if (n < 0) return -1;
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// ── SISTEMA DE VERIFICACIÓN ROBUSTO (Funciona aun con NDEBUG / -O2) ─────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [❌ FALLÓ] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automáticas de Factorial..." << endl;

    // Test 1: Casos Base
    verificar(factorial(0) == 1, "0! debe ser 1");
    verificar(factorial(1) == 1, "1! debe ser 1");
    cout << "  [PASO] Test 1: Casos Base (0! = 1, 1! = 1) OK" << endl;

    // Test 2: Entradas Válidas
    verificar(factorial(5) == 120, "5! debe ser 120");
    verificar(factorial(10) == 3628800LL, "10! debe ser 3628800");
    cout << "  [PASO] Test 2: Valores Estándar (5! y 10!) OK" << endl;

    // Test 3: Validación de Entradas Negativas
    verificar(factorial(-5) == -1, "n < 0 debe retornar -1");
    cout << "  [PASO] Test 3: Guard para números negativos (-5 -> -1) OK" << endl;

    cout << "\n¡TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E01: Factorial Recursivo ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
