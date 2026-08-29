// ============================================================================
// Reto E06: Detective Auto
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- Lector de Sensores ---\n";

    // TODO: Reemplaza todos los 'auto' que no cumplan la Regla de Oro
    // por su tipo explicito correcto (int, double, bool).
    
    auto lecturas_totales{15}; 
    auto temperatura_base{22.5}; 
    auto sensor_activo{true}; 

    // OUCH: Aqui hay un bug de division entera escondido.
    auto margen_error{lecturas_totales / 2}; 
    std::cout << "Margen de error actual (INEXACTO): " << margen_error << "\n";

    // TODO: Arregla este bug combinando static_cast y dejando a 'auto' 
    // solo donde es obvio (Regla de Oro).
    auto margen_error_real{lecturas_totales / 2};
    std::cout << "Margen de error real: " << margen_error_real << "\n";

    return 0;
}
