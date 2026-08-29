// ============================================================================
// Laboratorio L03: BlocksAndScope
// ============================================================================
// Objetivo: Entender la visibilidad (scope) desde bloques externos hacia internos.
// ============================================================================

#include <iostream>

int main() {
    int multiplicadorBase{5};
    std::cout << "Estamos en main. Multiplicador es: " << multiplicadorBase << "\n";

    if (multiplicadorBase == 5) {
        // Bloque interno: Puede ver multiplicadorBase sin problemas.
        int bonoTemporal{10};
        
        std::cout << "Entramos al bloque interno.\n";
        std::cout << "Bono: " << bonoTemporal << "\n";
        
        // Modificando la variable del scope exterior (valido)
        multiplicadorBase = multiplicadorBase + bonoTemporal; 
        std::cout << "Nuevo multiplicador (desde adentro): " << multiplicadorBase << "\n";
    } // Aqui muere 'bonoTemporal'

    // std::cout << bonoTemporal; // ¡DESCOMENTAR ESTO CAUSARA UN ERROR DE COMPILACION!
    std::cout << "De vuelta a main. Multiplicador sobrevive con: " << multiplicadorBase << "\n";
    
    return 0;
}
