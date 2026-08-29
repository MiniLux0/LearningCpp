// ============================================================================
// Reto E05: Escudo Anti-Trolls
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>

int main() {
    int pinCajero{0};
    bool accesoConcedido{false};

    while (accesoConcedido == false) {
        std::cout << "Ingrese su PIN numerico secreto: ";
        std::cin >> pinCajero;

        // TODO 1: Reemplaza la condicion "false" por la comprobacion del estado de error de cin
        if (false) {
            std::cout << "[ALERTA] Entrada invalida detectada. Activando protocolo de limpieza...\n";
            
            // TODO 2: Restablece las banderas de error para devolver a cin a un estado operativo
            
            // TODO 3: Limpia la basura residual atascada en el buffer (ignora hasta 10000 letras o un Enter)
            
        } else if (pinCajero == 1234) {
            std::cout << "Acceso Concedido.\n";
            accesoConcedido = true;
        } else {
            std::cout << "PIN incorrecto. Intente nuevamente.\n";
        }
    }

    return 0;
}
