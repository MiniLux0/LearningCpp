#include <iostream>
using namespace std;

// ============================================================================
// L32 — PROBLEMAS CLÁSICOS RECURSIVOS
// ============================================================================

// 1. Factorial n! = n * (n-1)! (Sección 7.2)
long long factorial(int n) {
    if (n <= 1) return 1; // Caso Base
    return n * factorial(n - 1); // Paso Recursivo
}

// 2a. Fibonacci Naive F(n) = F(n-1) + F(n-2) — O(2^N) (Sección 7.3)
long long fibonacciNaive(int n) {
    if (n == 0) return 0; // Caso Base 1
    if (n == 1) return 1; // Caso Base 2
    return fibonacciNaive(n - 1) + fibonacciNaive(n - 2); // Árbol Binario
}

// 2b. Fibonacci Optimizado mediante Secuencia Aditiva (Tail Recursion) — O(N) (Sección 7.3)
long long secuenciaAditiva(int n, long long a, long long b) {
    if (n == 0) return a;
    if (n == 1) return b;
    return secuenciaAditiva(n - 1, b, a + b);
}

long long fibonacciLineal(int n) {
    return secuenciaAditiva(n, 0, 1);
}

// 3. Verificación de Palíndromos eficiente con índices — O(N) (Sección 7.4)
bool esPalindromoHelper(const string& str, int low, int high) {
    if (low >= high) return true; // Caso Base: 0 o 1 caracteres restantes
    if (str[low] != str[high]) return false; // Descarte rápido
    return esPalindromoHelper(str, low + 1, high - 1); // Paso Recursivo reduciendo límites
}

bool esPalindromo(const string& str) {
    return esPalindromoHelper(str, 0, str.length() - 1);
}

// 4. Las Torres de Hanói — Divide y Vencerás — O(2^N) (Sección 8.1)
void torresDeHanoi(int n, char origen, char destino, char auxiliar, int& totalMovimientos) {
    if (n == 1) { // Caso Base: Mover 1 disco directamente
        totalMovimientos++;
        cout << "  [Mov " << totalMovimientos << "] Mover disco 1 de " << origen << " a " << destino << endl;
        return;
    }

    // Paso 1: Mover n-1 discos de origen a auxiliar usando destino
    torresDeHanoi(n - 1, origen, auxiliar, destino, totalMovimientos);

    // Paso 2: Mover el disco n directamente de origen a destino
    totalMovimientos++;
    cout << "  [Mov " << totalMovimientos << "] Mover disco " << n << " de " << origen << " a " << destino << endl;

    // Paso 3: Mover n-1 discos de auxiliar a destino usando origen
    torresDeHanoi(n - 1, auxiliar, destino, origen, totalMovimientos);
}

int main() {
    cout << "=== L32: Problemas Clásicos Recursivos ===" << endl;

    // 1. Factorial
    cout << "\n--- 1. Factorial ---" << endl;
    cout << "factorial(5) (esperado 120): " << factorial(5) << endl;

    // 2. Fibonacci (Naive vs Lineal)
    cout << "\n--- 2. Fibonacci (Naive O(2^N) vs Lineal O(N)) ---" << endl;
    cout << "fibonacciNaive(10): " << fibonacciNaive(10) << endl;
    cout << "fibonacciLineal(40) (eficiente): " << fibonacciLineal(40) << endl;

    // 3. Verificación de Palíndromos
    cout << "\n--- 3. Verificación de Palíndromos ---" << endl;
    string p1 = "reconocer";
    string p2 = "algoritmo";
    cout << "¿'" << p1 << "' es palíndromo?: " << (esPalindromo(p1) ? "Sí" : "No") << endl;
    cout << "¿'" << p2 << "' es palíndromo?: " << (esPalindromo(p2) ? "Sí" : "No") << endl;

    // 4. Las Torres de Hanói
    cout << "\n--- 4. Las Torres de Hanói (n = 3 discos) ---" << endl;
    int movimientos = 0;
    torresDeHanoi(3, 'A', 'C', 'B', movimientos);
    cout << "Total movimientos para 3 discos (esperado 2^3 - 1 = 7): " << movimientos << endl;

    return 0;
}
