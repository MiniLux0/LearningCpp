// ============================================================================
// Laboratorio L03: Operadores Aritméticos
// ============================================================================
// Objetivo: Comprender la precedencia de operadores matemáticos, el peligro de la división entera y el uso del operador módulo (%).
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- Operadores Aritmeticos ---\n";
    
    int manzanas{5};
    int peras{3};
    int total{manzanas + peras};
    std::cout << "Total de frutas: " << total << '\n';

    std::cout << "\n--- Precedencia ---\n";
    int resultado_sin_parentesis{2 + 3 * 4}; 
    std::cout << "2 + 3 * 4 = " << resultado_sin_parentesis << " (la multiplicacion se hizo primero)\n";
    
    int resultado_con_parentesis{(2 + 3) * 4};
    std::cout << "(2 + 3) * 4 = " << resultado_con_parentesis << " (los parentesis obligan a sumar primero)\n";

    std::cout << "\n--- Division Entera vs Decimal ---\n";
    int rebanadas{7};
    int personas{2};
    std::cout << "7 rebanadas entre 2 personas (usando int) = " << rebanadas / personas << " rebanadas cada uno.\n";

    double rebanadas_exactas{7.0};
    std::cout << "7.0 rebanadas entre 2 personas (usando double) = " << rebanadas_exactas / personas << " rebanadas cada uno.\n";

    std::cout << "\n--- El operador Modulo (%) ---\n";
    int cartas{10};
    int jugadores{3};
    int sobran{cartas % jugadores};
    std::cout << "Si reparto 10 cartas entre 3 jugadores de forma entera, me sobran: " << sobran << " cartas en la mano.\n";

    return 0;
}
