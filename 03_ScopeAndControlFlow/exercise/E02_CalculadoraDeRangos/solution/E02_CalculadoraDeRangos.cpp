// ============================================================================
// Reto E02: CalculadoraDeRangos (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    int pesoVehiculo{6000}; 
    
    std::cout << "Vehiculo en bascula: " << pesoVehiculo << " kg.\n";
    
    // SOLUCION: Se ordenaron las condiciones de mayor a menor restriccion.
    if (pesoVehiculo > 5000) {
        std::cout << "Vehiculo pesado. Cobrando $50.\n";
    } else if (pesoVehiculo >= 2500) {
        std::cout << "Vehiculo mediano. Cobrando $25.\n";
    } else if (pesoVehiculo >= 0) {
        std::cout << "Vehiculo ligero. Cobrando $10.\n";
    } else {
        std::cout << "Error de lectura en la bascula.\n";
    }
    
    return 0;
}
