// ============================================================================
// Reto E08: CajeroAutomatico (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    int saldo{1000};
    
    while (true) {
        std::cout << "\n=== BANCO CENTRAL ===\n";
        std::cout << "1. Consultar Saldo\n";
        std::cout << "2. Retirar Dinero\n";
        std::cout << "3. Salir\n";
        std::cout << "Elija una opcion: ";
        
        int opcion{0};
        std::cin >> opcion;
        
        switch (opcion) {
            case 1:
                std::cout << "Su saldo actual es: $" << saldo << "\n";
                break;
                
            case 2: {
                std::cout << "¿Cuanto desea retirar?: $";
                int retiro{0};
                std::cin >> retiro;
                
                if (retiro <= saldo) {
                    saldo = saldo - retiro;
                    std::cout << "Retiro exitoso. Por favor, tome su dinero.\n";
                } else {
                    std::cout << "Error: Fondos insuficientes.\n";
                }
                break;
            }
                
            case 3:
                std::cout << "Gracias por usar el Banco Central. Hasta luego.\n";
                return 0; // Tambien se podria usar break pero habria que manejar el fin
                
            default:
                std::cout << "Opcion invalida. Intente de nuevo.\n";
                break;
        }
    }
    
    return 0;
}
