#include <iostream>
using namespace std;

// ============================================================================
// L32 — PROBLEMAS CLÁSICOS RECURSIVOS
// ============================================================================

// 1. Factorial n! = n * (n-1)!
long long factorial(int n) {
    if (n <= 1) return 1; // Caso Base
    return n * factorial(n - 1); // Paso Recursivo
}

// 2. Fibonacci F(n) = F(n-1) + F(n-2)
long long fibonacci(int n) {
    if (n == 0) return 0; // Caso Base 1
    if (n == 1) return 1; // Caso Base 2
    return fibonacci(n - 1) + fibonacci(n - 2); // Paso Recursivo Múltiple
}

// 3. Potencia base^exp
double potencia(double base, int exp) {
    if (exp == 0) return 1.0; // Caso Base
    if (exp < 0) return 1.0 / potencia(base, -exp); // Exponente negativo
    return base * potencia(base, exp - 1); // Paso Recursivo
}

// 4. Impresión de C-string en reverso usando la pila de llamadas
void imprimirReverso(const char s[]) {
    if (s[0] == '\0') return; // Caso Base
    imprimirReverso(s + 1);   // Paso Recursivo (avanza puntero)
    cout << s[0];             // Se imprime al desapilar
}

int main() {
    cout << "=== L32: Problemas Clásicos Recursivos ===" << endl;

    // 1. Factorial
    cout << "\n--- 1. Factorial ---" << endl;
    cout << "factorial(5) (esperado 120): " << factorial(5) << endl;

    // 2. Fibonacci
    cout << "\n--- 2. Fibonacci ---" << endl;
    cout << "fibonacci(7) (esperado 13): " << fibonacci(7) << endl;

    // 3. Potencia
    cout << "\n--- 3. Potencia ---" << endl;
    cout << "potencia(2.0, 8) (esperado 256): " << potencia(2.0, 8) << endl;
    cout << "potencia(2.0, -3) (esperado 0.125): " << potencia(2.0, -3) << endl;

    // 4. Impresión Reversa de C-String
    cout << "\n--- 4. C-String Reverso ---" << endl;
    char palabra[] = "Estructura";
    cout << "Original: " << palabra << endl;
    cout << "Reverso: ";
    imprimirReverso(palabra);
    cout << endl;

    return 0;
}
