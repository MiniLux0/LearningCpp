// ============================================================================
// Reto E07: Split the Bill (Final Boss) (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- Gestor de Gastos de Alquiler ---\n\n";

    // 1: Inicializacion uniforme estricta
    int alquiler_base{1250};
    int servicios{150};
    int roommates{3};

    // 2: Calculo de costos
    int costo_total{alquiler_base + servicios};

    // 3: Pago exacto con casteo seguro
    double cuota_por_roommate{static_cast<double>(costo_total) / roommates};

    // 4: Logica booleana combinada (&&)
    bool roommates_validos{roommates > 0};
    bool alquiler_valido{alquiler_base > 0};
    bool servicios_validos{servicios >= 0};
    
    bool sistema_ok{roommates_validos && alquiler_valido && servicios_validos};

    std::cout << "Validacion del sistema (1=Activo, 0=Fallo): " << sistema_ok << "\n";
    std::cout << "Costo total del departamento: $" << costo_total << "\n";
    std::cout << "Cada roommate debe pagar: $" << cuota_por_roommate << "\n";

    return 0;
}
