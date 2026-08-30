// ============================================================================
// Reto E05: Atrapando la Bomba (SOLUCION)
// ============================================================================

#include <iostream>
#include <vector>
#include <stdexcept>

void consultarCuenta(const std::vector<double>& cuentas, std::size_t idCuenta) {
    try {
        double saldo = cuentas.at(idCuenta);
        std::cout << "[EXITO] Saldo de la cuenta [" << idCuenta << "]: $" << saldo << '\n';
    }
    catch (const std::out_of_range& error) {
        std::cout << "[ALERTA] La cuenta [" << idCuenta << "] no existe en el sistema bancario.\n";
        std::cout << "Diagnostico tecnico: " << error.what() << '\n';
    }
}

int main() {
    std::cout << "--- TERMINAL BANCARIA INTERGALACTICA ---\n";

    const std::vector<double> cuentas{1500.50, 240.00, 8900.25}; // 3 cuentas (indices 0, 1, 2)

    // Consulta valida:
    consultarCuenta(cuentas, 1);

    // Consulta invalida (detona std::out_of_range capturada por el try/catch):
    consultarCuenta(cuentas, 50);

    std::cout << "\nEl servidor bancario permanece en linea.\n";
    return 0;
}
