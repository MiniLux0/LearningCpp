// ============================================================================
// Reto E05: Atrapando la Bomba
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <vector>
#include <stdexcept>

void consultarCuenta(const std::vector<double>& cuentas, std::size_t idCuenta) {
    // TODO: Envuelve la siguiente operacion en un bloque try/catch
    // para capturar 'const std::out_of_range& error' y evitar que el programa colapse.
    
    double saldo = cuentas.at(idCuenta);
    std::cout << "[EXITO] Saldo de la cuenta [" << idCuenta << "]: $" << saldo << '\n';
}

int main() {
    std::cout << "--- TERMINAL BANCARIA INTERGALACTICA ---\n";

    std::vector<double> cuentas{1500.50, 240.00, 8900.25}; // 3 cuentas (indices 0, 1, 2)

    // Consulta valida:
    consultarCuenta(cuentas, 1);

    // Consulta invalida (detona std::out_of_range):
    consultarCuenta(cuentas, 50);

    std::cout << "\nEl servidor bancario permanece en linea.\n";
    return 0;
}
