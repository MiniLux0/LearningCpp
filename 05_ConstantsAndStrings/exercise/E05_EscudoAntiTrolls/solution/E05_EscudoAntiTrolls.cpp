// ============================================================================
// Reto E05: Escudo Anti-Trolls (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    int pinCajero{0};
    bool accesoConcedido{false};

    while (accesoConcedido == false) {
        std::cout << "Ingrese su PIN numerico secreto: ";
        std::cin >> pinCajero;

        // Solucion 1: Detectamos el fallo leyendo la alarma de std::cin
        if (std::cin.fail()) {
            std::cout << "[ALERTA] Entrada invalida detectada. Activando protocolo de limpieza...\n";
            
            // Solucion 2: Apagamos el estado de fallo
            std::cin.clear();
            
            // Solucion 3: Tiramos la basura atascada (hasta 10000 chars o el salto de linea)
            std::cin.ignore(10000, '\n');
            
        } else if (pinCajero == 1234) {
            std::cout << "Acceso Concedido.\n";
            accesoConcedido = true;
        } else {
            std::cout << "PIN incorrecto. Intente nuevamente.\n";
        }
    }

    return 0;
}
