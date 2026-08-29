// ============================================================================
// Reto E06: Detective Auto (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- Lector de Sensores ---\n";

    // SOLUCION: Tipos explicitos porque no son productos de casteos evidentes
    int lecturas_totales{15}; 
    double temperatura_base{22.5}; 
    bool sensor_activo{true}; 

    // BUG solucionado usando tipos explicitos o casteos
    double margen_error_inexacto{lecturas_totales / 2}; // Si solo arreglas el tipo, sigue siendo inexacto
    
    // Aquí es el UNICO lugar donde 'auto' esta justificado (Regla de Oro)
    // porque el tipo se ve inmediatamente en el static_cast.
    auto margen_error_real{static_cast<double>(lecturas_totales) / 2};
    
    std::cout << "Margen de error actual (INEXACTO): " << margen_error_inexacto << "\n";
    std::cout << "Margen de error real: " << margen_error_real << "\n";

    return 0;
}
