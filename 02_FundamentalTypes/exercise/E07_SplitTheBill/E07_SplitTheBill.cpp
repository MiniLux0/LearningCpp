// ============================================================================
// Reto E07: Split the Bill (Final Boss)
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- Gestor de Gastos de Alquiler ---\n\n";

    // TODO 1: Inicializa el alquiler_base con 1250, los servicios con 150, 
    // y la cantidad de roommates con 3. (Usa llaves {})
    int alquiler_base;
    int servicios;
    int roommates;

    // TODO 2: Calcula el costo total sumando alquiler_base y servicios.
    int costo_total; // = ???

    // TODO 3: Calcula el pago exacto (con decimales) usando static_cast<double>
    double cuota_por_roommate; // = ???

    // TODO 4: Crea la logica booleana de validacion.
    // Solo debe ser true si: roommates > 0 Y alquiler_base > 0 Y servicios >= 0.
    bool sistema_ok; // = ???

    std::cout << "Validacion del sistema (1=Activo, 0=Fallo): " << sistema_ok << "\n";
    std::cout << "Costo total del departamento: $" << costo_total << "\n";
    std::cout << "Cada roommate debe pagar: $" << cuota_por_roommate << "\n";

    return 0;
}
