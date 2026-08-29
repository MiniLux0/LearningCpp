// ============================================================================
// Reto E01: SistemaDeClima
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

int main() {
    int humedadSuelo{85}; 
    
    std::cout << "Lectura del sensor: " << humedadSuelo << "%\n";
    
    // TODO 1: Elimina el bug que rompe esta condicion.
    if (humedadSuelo < 40);
    {
        std::cout << "Alerta: Suelo seco. Encendiendo aspersores...\n";
    }
    
    // TODO 2: Refactoriza esto para usar un 'else' en lugar de otro 'if'.
    if (humedadSuelo >= 40)
    {
        std::cout << "Suelo hidratado. Aspersores apagados.\n";
    }
    
    return 0;
}
