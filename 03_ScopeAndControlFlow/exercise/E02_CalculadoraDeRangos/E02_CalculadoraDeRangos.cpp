// ============================================================================
// Reto E02: CalculadoraDeRangos
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

int main() {
    int pesoVehiculo{6000}; 
    
    std::cout << "Vehiculo en bascula: " << pesoVehiculo << " kg.\n";
    
    // TODO: El orden de estas comprobaciones es logicamente incorrecto.
    // Reordenalas para que el cobro en cascada sea justo.
    if (pesoVehiculo >= 0) {
        std::cout << "Vehiculo ligero. Cobrando $10.\n";
    } else if (pesoVehiculo >= 2500) {
        std::cout << "Vehiculo mediano. Cobrando $25.\n";
    } else if (pesoVehiculo > 5000) {
        std::cout << "Vehiculo pesado. Cobrando $50.\n";
    } else {
        std::cout << "Error de lectura en la bascula.\n";
    }
    
    return 0;
}
