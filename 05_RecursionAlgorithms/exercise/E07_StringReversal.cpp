#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

// ============================================================================
// EJERCICIO 7 — INVERSIÓN RECURSIVA DE CADENAS
// Complejidad objetivo: Tiempo O(n), Espacio O(n) en pila.
// ============================================================================

string invertirCadena(const string& s) {
    if (s.length() <= 1) return s; // Caso base
    return invertirCadena(s.substr(1)) + s[0]; // Paso recursivo
}

// ── SISTEMA DE VERIFICACIÓN ROBUSTO ─────────────────────────────────────────
void verificar(bool condicion, const string& mensaje) {
    if (!condicion) {
        cerr << "  [❌ FALLÓ] " << mensaje << endl;
        exit(1);
    }
}

void ejecutarPruebas() {
    cout << "Ejecutando pruebas automáticas de Inversión de Cadenas..." << endl;

    verificar(invertirCadena("hola") == "aloh", "'hola' -> 'aloh'");
    verificar(invertirCadena("recursividad") == "dadivisrucer", "'recursividad' no coincide");
    cout << "  [PASO] Test 1: Inversión de palabras estándar OK" << endl;

    verificar(invertirCadena("") == "", "Cadena vacía");
    verificar(invertirCadena("A") == "A", "Cadena de 1 char");
    cout << "  [PASO] Test 2: Casos base de 0 y 1 carácter OK" << endl;

    cout << "\n¡TODOS LOS TESTS PASARON EXITOSAMENTE! (100% Correcto)" << endl;
}

int main() {
    cout << "=== E07: Inversión Recursiva de Cadenas ===" << endl << endl;
    ejecutarPruebas();
    return 0;
}
