// ============================================================================
// Laboratorio D03: BUG DEMO - VariableShadowingBug
// ============================================================================
// Objetivo: Mostrar como redeclarar una variable anula silenciosamente nuestra logica.
//
// INSTRUCCIONES:
// Compila con `g++ D03_VariableShadowingBug.cpp -o bug`
// ============================================================================

#include <iostream>

int main() {
    int escudosNave{100}; // Escudo original
    
    std::cout << "[SISTEMA] Escudos al " << escudosNave << "%\n";
    std::cout << "[ALERTA] Impacto de asteroide inminente.\n";
    
    bool impacto{true};
    
    if (impacto) {
        // BUG INTENCIONAL: Variable Shadowing
        // En lugar de restar al escudo, el programador puso "int" por accidente,
        // sombreando silenciosamente a la variable original del Scope superior.
        int escudosNave{escudosNave - 40}; 
        std::cout << "[DANO] Escudos reducidos a " << escudosNave << "% (Dentro del if)\n";
    } // La variable local 'escudosNave' es destruida de la memoria aqui con el 60.
    
    // El escudo original jamas sufrio dano.
    std::cout << "[REPORTE FINAL] Escudos actuales: " << escudosNave << "%\n";
    std::cout << "¿Por que no recibimos dano?\n";
    
    return 0;
}
