// ============================================================================
// Reto E01: SistemaDeClima (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    int humedadSuelo{85}; 
    
    std::cout << "Lectura del sensor: " << humedadSuelo << "%\n";
    
    // SOLUCION: Se elimino el punto y coma asesino y se unifico el bloque usando if-else.
    if (humedadSuelo < 40) {
        std::cout << "Alerta: Suelo seco. Encendiendo aspersores...\n";
    } else {
        std::cout << "Suelo hidratado. Aspersores apagados.\n";
    }
    
    return 0;
}
