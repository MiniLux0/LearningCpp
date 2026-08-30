// ============================================================================
// Laboratorio D03: BUG DEMO - Confusion de Inicializacion (Llaves vs Parentesis)
// ============================================================================
// Objetivo: Demostrar el error logico derivado de confundir la lista de
//           inicializacion {N} con el constructor de conteo (N).
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D03_BraceInitBug.cpp -o bug
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- DEMO DE BUG: CONFUSION DE INICIALIZACION ---\n";

    // Intencion del desarrollador: Crear un vector de 5 posiciones vacias (en cero)
    // Error cometido: Usar llaves {} en lugar de parentesis ()
    std::vector<int> inventarioBug{5};

    // Inicializacion correcta para 5 casillas:
    std::vector<int> inventarioCorrecto(5);

    std::cout << "Vector con LLAVES {5}:\n";
    std::cout << "  Tamano (.size()): " << inventarioBug.size() << " (Se esperaba 5)\n";
    std::cout << "  Elemento unico [0]: " << inventarioBug.at(0) << '\n';

    std::cout << "\nVector con PARENTESIS (5):\n";
    std::cout << "  Tamano (.size()): " << inventarioCorrecto.size() << " (Correcto)\n";
    for (std::size_t i{0}; i < inventarioCorrecto.size(); ++i) {
        std::cout << "  Posicion [" << i << "]: " << inventarioCorrecto.at(i) << '\n';
    }

    std::cout << "\nConclusion: {5} crea 1 elemento de valor 5; (5) crea 5 elementos en cero.\n";
    return 0;
}
