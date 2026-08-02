#include <iostream>
#include <vector>
using namespace std;

// ============================================================================
// L38 — BACKTRACKING RECURSIVO: CHOOSE, EXPLORE, UNCHOOSE
// ============================================================================

// Ejercicio: Generar todos los subconjuntos posibles de un vector (Power Set)
void generarSubconjuntos(const vector<char>& elementos, int index, vector<char>& actual) {
    // 1. Caso Base: Se ha tomado una decisión para todos los elementos
    if (index == (int)elementos.size()) {
        cout << "{ ";
        for (char c : actual) cout << c << " ";
        cout << "}\n";
        return;
    }

    // Opcion 1: NO incluir elementos[index]
    generarSubconjuntos(elementos, index + 1, actual);

    // Opcion 2: INCLUIR elementos[index]
    actual.push_back(elementos[index]);                // 1. CHOOSE
    generarSubconjuntos(elementos, index + 1, actual);  // 2. EXPLORE
    actual.pop_back();                                 // 3. UNCHOOSE (Backtrack)
}

int main() {
    cout << "=== L38: Backtracking Recursivo (Subconjuntos) ===" << endl;

    vector<char> letras = {'A', 'B', 'C'};
    vector<char> conjuntoActual;

    cout << "Todos los subconjuntos posibles de {'A', 'B', 'C'}:" << endl;
    generarSubconjuntos(letras, 0, conjuntoActual);

    return 0;
}
