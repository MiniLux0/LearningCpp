// ============================================================================
// Laboratorio D04: BUG DEMO - Acceso Silencioso Fuera de Limites con []
// ============================================================================
// Objetivo: Demostrar que operator[] no valida limites, permitiendo lecturas
//           y escrituras corruptas en memoria sin detonar errores inmediatos.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D04_SilentOutofBoundsBug.cpp -o bug
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- DEMO DE BUG: ACCESO SILENCIOSO FUERA DE LIMITES ---\n";

    std::vector<int> datos{10, 20, 30}; // size = 3 (indices validos: 0, 1, 2)

    std::cout << "Tamano del vector: " << datos.size() << '\n';
    std::cout << "Elemento [0]: " << datos[0] << '\n';
    std::cout << "Elemento [2]: " << datos[2] << '\n';

    std::cout << "\n[PELIGRO] Accediendo a datos[100] usando operator[]...\n";

    // [FALLO] UNDEFINED BEHAVIOR: operator[] no valida limites y lee memoria no asignada
    int valorBasura = datos[100];
    std::cout << "Valor leido fuera de rango: " << valorBasura << " (Basura en Heap)\n";

    std::cout << "\nConclusion: operator[] no lanza excepciones y oculta errores de corrupcion.\n";
    std::cout << "Usa siempre .at() para garantizar Bounds Checking en etapas formativas.\n";

    return 0;
}
