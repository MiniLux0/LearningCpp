#include <iostream>
using namespace std;

// ============================================================================
// L31 — PENSAR RECURSIVAMENTE: CASO BASE, PASO RECURSIVO Y PILA DE LLAMADAS
// ============================================================================

// Ejemplo 1: Conteo regresivo recursivo mostrando la traza de la pila
void cuentaRegresiva(int n) {
    // 1. Caso Base: interrumpe las llamadas cuando n llega a 0
    if (n == 0) {
        cout << "¡Despegue! (Caso base alcanzado n = 0)" << endl;
        return;
    }

    // 2. Paso Recursivo: se imprime el valor actual y se llama con n - 1
    cout << "Entrando a cuentaRegresiva(" << n << ")" << endl;
    cuentaRegresiva(n - 1);
    cout << "Saliendo de cuentaRegresiva(" << n << ") - Desapilando" << endl;
}

// Ejemplo 2: Suma de los primeros N enteros (Suma acumulativa recursiva)
int sumaRecursiva(int n) {
    if (n <= 1) { // Caso Base
        return n;
    }
    return n + sumaRecursiva(n - 1); // Paso Recursivo
}

// Prototipos necesarios para la Recursión Mutua (Sección 7.6 del libro)
bool esImpar(int n);

// Ejemplo 3: Recursión Mutua (isEven / isOdd)
bool esPar(int n) {
    if (n == 0) return true; // Caso Base
    return esImpar(n - 1);   // Paso Recursivo llamando a esImpar
}

bool esImpar(int n) {
    if (n == 0) return false; // Caso Base
    return esPar(n - 1);      // Paso Recursivo llamando a esPar
}

int main() {
    cout << "=== L31: Pensar Recursivamente ===" << endl;

    // 1. Demostración de la Pila de Llamadas (Call Stack)
    cout << "\n--- 1. Traza de la Pila de Llamadas (n = 3) ---" << endl;
    cuentaRegresiva(3);

    // 2. Demostración de Suma Acumulativa
    cout << "\n--- 2. Suma Acumulativa Recursiva ---" << endl;
    int n = 5;
    cout << "Suma de 1 a " << n << " (esperado 15): " << sumaRecursiva(n) << endl;

    // 3. Demostración de Recursión Mutua
    cout << "\n--- 3. Recursión Mutua (esPar / esImpar) ---" << endl;
    cout << "¿Es par 4?: " << (esPar(4) ? "Sí" : "No") << endl;
    cout << "¿Es impar 7?: " << (esImpar(7) ? "Sí" : "No") << endl;

    return 0;
}
