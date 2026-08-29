// ============================================================================
// Reto E03: RescateDeVariables
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <string>

int main() {
    int oroBase{500};
    std::string contrasenaCorrecta{"abrete_sesamo"};
    
    std::cout << "Ingresa la clave del tesoro: ";
    std::string intento{""};
    std::cin >> intento;
    
    if (intento == contrasenaCorrecta) {
        std::cout << "Clave correcta. Aplicando bonus del tesoro.\n";
        
        // TODO 1: Arregla el Variable Shadowing aqui.
        int oroBase{oroBase + 200}; 
        
        // TODO 2: Arregla el Scope aislando la declaracion fuera del if.
        int recompensaTotal{oroBase * 2}; 
    } else {
        std::cout << "Clave incorrecta. No hay bonus.\n";
        int recompensaTotal{oroBase}; 
    }
    
    // ERROR COMPILACION: 'recompensaTotal' fue destruida, no existe aqui.
    std::cout << "\nEl jugador se lleva un total de: " << recompensaTotal << " de oro.\n";
    
    return 0;
}
