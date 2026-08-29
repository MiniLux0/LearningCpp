// ============================================================================
// Reto E03: Panel de Bienvenida (SOLUCION)
// ============================================================================

#include <iostream>
#include <string>

void imprimirBanner() {
    std::cout << "***************************************\n";
    std::cout << "*                                     *\n";
    std::cout << "*    H O T E L   P A R A I S O        *\n";
    std::cout << "*      5 Estrellas de Lujo            *\n";
    std::cout << "*                                     *\n";
    std::cout << "***************************************\n";
}

int main() {
    std::string cliente{"Sr. Anderson"};
    
    imprimirBanner(); 
    
    std::cout << "\nHabitacion lista para: " << cliente << '\n';
    
    return 0;
}
