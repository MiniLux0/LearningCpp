// ============================================================================
// Reto E03: Panel de Bienvenida
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <string>

// TODO: Crear funcion void imprimirBanner()

int main() {
    std::string cliente{"Sr. Anderson"};
    
    // TODO: Mover a imprimirBanner()
    std::cout << "***************************************\n";
    std::cout << "*                                     *\n";
    std::cout << "*    H O T E L   P A R A I S O        *\n";
    std::cout << "*      5 Estrellas de Lujo            *\n";
    std::cout << "*                                     *\n";
    std::cout << "***************************************\n";
    
    // TODO: Llamar a imprimirBanner() correctamente
    int status{imprimirBanner()}; 
    
    std::cout << "\nHabitacion lista para: " << cliente << '\n';
    
    return 0;
}
