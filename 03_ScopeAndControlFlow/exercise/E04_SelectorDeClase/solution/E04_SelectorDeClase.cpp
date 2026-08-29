// ============================================================================
// Reto E04: SelectorDeClase (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Selecciona tu clase (1=Guerrero, 2=Mago, 3=Arquero): ";
    int eleccion{1};
    
    switch (eleccion) {
        case 1: {
            std::cout << "¡Has elegido Guerrero!\n";
            // SOLUCION: El case ahora vive en su propio scope { }
            int bonusFuerza{15};
            std::cout << "Fuerza incrementada en " << bonusFuerza << ".\n";
            break; // SOLUCION: Añadido el freno.
        }
            
        case 2: {
            std::cout << "¡Has elegido Mago!\n";
            int bonusMagia{20};
            std::cout << "Poder magico incrementado en " << bonusMagia << ".\n";
            break; 
        }
            
        case 3: {
            std::cout << "¡Has elegido Arquero!\n";
            int bonusAgilidad{18};
            std::cout << "Agilidad incrementada en " << bonusAgilidad << ".\n";
            break;
        }
            
        default:
            std::cout << "Clase no valida.\n";
            break;
    }
    
    std::cout << "Creacion de personaje finalizada.\n";
    return 0;
}
