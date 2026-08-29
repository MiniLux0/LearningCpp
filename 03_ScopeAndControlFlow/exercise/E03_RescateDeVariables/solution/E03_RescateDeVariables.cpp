// ============================================================================
// Reto E03: RescateDeVariables (SOLUCIÓN)
// ============================================================================

#include <iostream>
#include <string>

int main() {
    int oroBase{500};
    int recompensaTotal{0}; // SOLUCION 2: Nace en 'main', sobrevive todo el programa.
    
    std::string contrasenaCorrecta{"abrete_sesamo"};
    
    std::cout << "Ingresa la clave del tesoro: ";
    std::string intento{""};
    std::cin >> intento;
    
    if (intento == contrasenaCorrecta) {
        std::cout << "Clave correcta. Aplicando bonus del tesoro.\n";
        
        // SOLUCION 1: Se quito 'int' para evitar Shadowing. Modificamos el real.
        oroBase = oroBase + 200; 
        
        // Modificamos la variable que nacio arriba, no creamos una nueva.
        recompensaTotal = oroBase * 2; 
    } else {
        std::cout << "Clave incorrecta. No hay bonus.\n";
        recompensaTotal = oroBase; 
    }
    
    // Ahora funciona perfectamente, porque recompensaTotal sigue viva.
    std::cout << "\nEl jugador se lleva un total de: " << recompensaTotal << " de oro.\n";
    
    return 0;
}
