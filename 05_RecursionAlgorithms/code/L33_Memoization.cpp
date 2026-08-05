#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <chrono>

using namespace std;

// ============================================================================
// L33 — DEMOSTRACIÓN DE MEMOIZACIÓN & PROGRAMACIÓN DINÁMICA TOP-DOWN
// Stanford CS106B Capítulo 8 (Sección 8.4)
// ============================================================================

static long long llamadasNaive = 0;
static long long llamadasMemo = 0;

// 1. Fibonacci Naive — O(2^N) Exponencial
long long fibonacciNaive(int n) {
    llamadasNaive++;
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacciNaive(n - 1) + fibonacciNaive(n - 2);
}

// 2. Fibonacci Memoizado con vector — O(N) Lineal
long long fibVectorHelper(int n, vector<long long>& memo) {
    llamadasMemo++;
    if (memo[n] != -1) return memo[n]; // Consulta caché en O(1)
    if (n == 0) return (memo[0] = 0);
    if (n == 1) return (memo[1] = 1);

    memo[n] = fibVectorHelper(n - 1, memo) + fibVectorHelper(n - 2, memo);
    return memo[n];
}

long long fibonacciMemo(int n) {
    if (n < 0) return -1;
    vector<long long> memo(n + 1, -1);
    return fibVectorHelper(n, memo);
}

// 3. Grid Traveler — Conteo de caminos en grilla R x C con unordered_map
long long gridTravelerMemo(int r, int c, unordered_map<string, long long>& memo) {
    string key = to_string(r) + "," + to_string(c);
    if (memo.count(key)) return memo[key];

    if (r == 0 || c == 0) return 0;
    if (r == 1 && c == 1) return 1;

    memo[key] = gridTravelerMemo(r - 1, c, memo) + gridTravelerMemo(r, c - 1, memo);
    return memo[key];
}

long long contarCaminosGrilla(int r, int c) {
    unordered_map<string, long long> memo;
    return gridTravelerMemo(r, c, memo);
}

int main() {
    cout << "=== L33: DEMOSTRACION DE MEMOIZACION (TOP-DOWN DP) ===" << endl << endl;

    // --- 1. COMPARATIVA DE LLAMADAS: FIBONACCI NAIVE VS MEMOIZADO ---
    cout << "--- 1. Comparativa de Llamadas: fib(35) ---" << endl;

    llamadasNaive = 0;
    auto t1 = chrono::high_resolution_clock::now();
    long long resNaive = fibonacciNaive(35);
    auto t2 = chrono::high_resolution_clock::now();
    chrono::duration<double, milli> durNaive = t2 - t1;

    llamadasMemo = 0;
    auto t3 = chrono::high_resolution_clock::now();
    long long resMemo = fibonacciMemo(35);
    auto t4 = chrono::high_resolution_clock::now();
    chrono::duration<double, milli> durMemo = t4 - t3;

    cout << "Fibonacci Naive(35):    " << resNaive << endl;
    cout << "  - Llamadas recursivas: " << llamadasNaive << " (Exponencial O(2^N))" << endl;
    cout << "  - Tiempo transcurrido: " << durNaive.count() << " ms" << endl << endl;

    cout << "Fibonacci Memoizado(35): " << resMemo << endl;
    cout << "  - Llamadas recursivas: " << llamadasMemo << " (Lineal O(N))" << endl;
    cout << "  - Tiempo transcurrido: " << durMemo.count() << " ms" << endl;
    cout << "  -> Factor de reducción de llamadas: " << (llamadasNaive / llamadasMemo) << "x menos llamadas!" << endl;

    // --- 2. DEMOSTRACIÓN DE FIBONACCI GRANDE (fib(80)) ---
    cout << "\n--- 2. Fibonacci Grande: fib(80) (Imposible con Naive) ---" << endl;
    long long fib80 = fibonacciMemo(80);
    cout << "fib(80) = " << fib80 << " (Calculado instantáneamente gracias a memoización)" << endl;

    // --- 3. SEGUNDO CASO: GRID TRAVELER EN GRILLA 18x18 ---
    cout << "\n--- 3. Grid Traveler (Caminos en Grilla 18x18) ---" << endl;
    int filas = 18, columnas = 18;
    long long caminos = contarCaminosGrilla(filas, columnas);
    cout << "Número de caminos únicos en grilla de " << filas << "x" << columnas << ": " << caminos << endl;

    return 0;
}
