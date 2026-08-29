// ============================================================================
// Reto E04: SelectorDeClase
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Selecciona tu clase (1=Guerrero, 2=Mago, 3=Arquero): ";
    int eleccion{1}; 
    
    switch (eleccion) {
        case 1:
            std::cout << "¡Has elegido Guerrero!\n";
            // TODO 1: Aisla el scope de este case con { } para evitar el error.
            int bonusFuerza{15};
            std::cout << "Fuerza incrementada en " << bonusFuerza << ".\n";
            // TODO 2: Falta el freno.
            
        case 2:
            std::cout << "¡Has elegido Mago!\n";
            int bonusMagia{20};
            std::cout << "Poder magico incrementado en " << bonusMagia << ".\n";
            // TODO: Falta el freno y aislar.
            
        case 3:
            std::cout << "¡Has elegido Arquero!\n";
            int bonusAgilidad{18};
            std::cout << "Agilidad incrementada en " << bonusAgilidad << ".\n";
            break;
            
        default:
            std::cout << "Clase no valida.\n";
            break;
    }
    
    std::cout << "Creacion de personaje finalizada.\n";
    return 0;
}
