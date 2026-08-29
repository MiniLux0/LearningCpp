// ============================================================================
// Reto E02: Calculadora de Area
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

int calcularArea(int base, int altura) {
    if (base > 0 && altura > 0) {
        return base * altura;
    }
    
    // TODO: Sellar este camino logico con un return explicito para evitar un Undefined Behavior.
}

int main() {
    int area_valida{calcularArea(10, 5)};
    int area_invalida{calcularArea(-2, 5)};
    
    std::cout << "--- SISTEMA DE ARQUITECTURA ---\n";
    std::cout << "Area 1 (10x5): " << area_valida << " metros cuadrados.\n";
    std::cout << "Area 2 (-2x5): " << area_invalida << " metros cuadrados.\n";
    
    return 0;
}
