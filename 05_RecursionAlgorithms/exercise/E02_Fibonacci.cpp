#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

// ============================================================================
// EJERCICIO 2 — SERIE DE FIBONACCI (NAIVE Y MEMOIZADO)
// Objetivo: Implementar Fibonacci recursivo simple y memoizado.
// Naive:    Tiempo O(2^n), Espacio O(n) en pila de llamadas.
// Memoizado: Tiempo O(n), Espacio O(n) — arreglo memo[] como cuaderno.
// ============================================================================

// ── 1. Fibonacci Naive (Ingenuo) ─────────────────────────────────────────────
long long fibNaive(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibNaive(n - 1) + fibNaive(n - 2);
}

// ── 2. Fibonacci Memoizado (con arreglo estático como cuaderno) ──────────────
const int MAX_N = 100;
long long memo[MAX_N];

void inicializarMemo() {
    for (int i = 0; i < MAX_N; i++) memo[i] = -1;
}

long long fibMemoHelper(int n) {
    if (memo[n] != -1) return memo[n]; // Paso 1: consultar cuaderno
    if (n == 0) return (memo[0] = 0);  // Paso 2: caso base
    if (n == 1) return (memo[1] = 1);  // Paso 2: caso base

    // Pasos 3 y 4: calcular y anotar
    memo[n] = fibMemoHelper(n - 1) + fibMemoHelper(n - 2);
    return memo[n];
}

long long fibMemo(int n) {
    if (n < 0) return -1;
    inicializarMemo();
    return fibMemoHelper(n);
}

// ── SISTEMA DE VERIFICACIÓN ROBUSTO ──────────────────────────────────────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [FALLO] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automaticas de Fibonacci..." << endl;

    // Test 1: Casos Base
    verificar(fibNaive(0) == 0 && fibMemo(0) == 0, "fib(0) debe ser 0");
    verificar(fibNaive(1) == 1 && fibMemo(1) == 1, "fib(1) debe ser 1");
    cout << "  [PASO] Test 1: Casos Base (fib(0)=0, fib(1)=1) OK" << endl;

    // Test 2: Valores Estándar
    verificar(fibNaive(10) == 55 && fibMemo(10) == 55, "fib(10) debe ser 55");
    cout << "  [PASO] Test 2: fib(10) = 55 OK" << endl;

    // Test 3: Rendimiento con Memoización (fib(50) — imposible sin memo)
    long long f50 = fibMemo(50);
    verificar(f50 == 12586269025LL, "fib(50) no coincide");
    cout << "  [PASO] Test 3: Memoizacion eficiente fib(50) = 12586269025 OK" << endl;

    cout << "\n TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E02: Fibonacci Naive vs Memoizado ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
