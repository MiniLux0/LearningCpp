// ============================================================================
// Laboratorio L08: Mini-Proyecto - Cajero Automático
// ============================================================================
// Objetivo: Integrar control de flujo (while, switch, if/else) y gestion de
//           ambitos (scope) en un programa interactivo de consola.
// ============================================================================

#include <iostream>

int main() {
    // 1. Estado persistente del usuario (vive durante toda la sesion)
    int balanceOperativo{1000};
    bool sesionActiva{true};

    std::cout << "========================================\n";
    std::cout << "      SISTEMA DE CAJERO AUTOMATICO     \n";
    std::cout << "========================================\n";

    // 2. Bucle principal de eventos
    while (sesionActiva) {
        std::cout << "\n--- MENU DE OPERACIONES ---\n";
        std::cout << "1. Consultar saldo disponible\n";
        std::cout << "2. Depositar fondos\n";
        std::cout << "3. Retirar efectivo\n";
        std::cout << "4. Finalizar sesion\n";
        std::cout << "Seleccione una opcion (1-4): ";

        // Variable local al bucle: se reinicia en cada iteracion
        int opcionSeleccionada{0};
        std::cin >> opcionSeleccionada;

        // 3. Evaluacion de la opcion con switch
        switch (opcionSeleccionada) {
            case 1:
                std::cout << "\n[CONSULTA] Saldo actual: $" << balanceOperativo << "\n";
                break;

            case 2: {
                // Ambito aislado con {} para declarar variables dentro del case
                std::cout << "\n[DEPOSITO] Ingrese el monto a depositar: $";
                int montoDeposito{0};
                std::cin >> montoDeposito;

                if (montoDeposito > 0) {
                    balanceOperativo = balanceOperativo + montoDeposito;
                    std::cout << "Deposito exitoso. Nuevo saldo: $" << balanceOperativo << "\n";
                } else {
                    std::cout << "Error: El monto a depositar debe ser mayor a $0.\n";
                }
                break;
            }

            case 3: {
                // Ambito aislado para evitar colision de nombres y fallos de salto
                std::cout << "\n[RETIRO] Ingrese el monto a retirar: $";
                int montoRetiro{0};
                std::cin >> montoRetiro;

                if (montoRetiro <= 0) {
                    std::cout << "Error: El monto de retiro debe ser positivo.\n";
                } else if (montoRetiro <= balanceOperativo) {
                    balanceOperativo = balanceOperativo - montoRetiro;
                    std::cout << "Retiro aprobado. Entregando billetes...\n";
                    std::cout << "Saldo restante: $" << balanceOperativo << "\n";
                } else {
                    std::cout << "Error: Fondos insuficientes para realizar la operacion.\n";
                }
                break;
            }

            case 4:
                std::cout << "\nCerrando sesion segura. Gracias por su visita.\n";
                sesionActiva = false;
                break;

            default:
                std::cout << "\nOpcion no reconocida. Por favor intente nuevamente.\n";
                break;
        }
    }

    std::cout << "\nPrograma finalizado con exito.\n";
    return 0;
}
