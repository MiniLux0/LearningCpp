// ============================================================================
// Reto E08: Adivina el Numero (SOLUCION)
// ============================================================================

#include <iostream>
#include <random>

int generarNumeroSecreto() {
    static std::mt19937 motor{std::random_device{}()};
    std::uniform_int_distribution<int> rango{1, 100};
    
    return rango(motor);
}

int pedirIntento() {
    int input{0};
    std::cout << "Ingresa tu intento: ";
    std::cin >> input;
    
    return input;
}

void jugarPartida(int objetivo) {
    int intentos{0};
    
    while (true) {
        int intento_jugador{pedirIntento()};
        intentos = intentos + 1;
        
        if (intento_jugador > objetivo) {
            std::cout << "[INFO] Objetivo menor. Calibra hacia abajo.\n\n";
        } else if (intento_jugador < objetivo) {
            std::cout << "[INFO] Objetivo mayor. Calibra hacia arriba.\n\n";
        } else {
            std::cout << "\n[EXITO] Calibracion exacta. El objetivo era " << objetivo << ".\n";
            std::cout << "El sistema tardo " << intentos << " iteraciones en sincronizar.\n";
            
            // Retorno temprano: Aborta el bucle y destruye la funcion instantaneamente
            return; 
        }
    }
}

int main() {
    std::cout << "--- SISTEMA DE CALIBRACION ---\n";
    std::cout << "Inicializando semilla del 1 al 100...\n\n";
    
    // Orquestador Modular (El main no posee logica de bucles)
    int meta_secreta{generarNumeroSecreto()};
    jugarPartida(meta_secreta);
    
    return 0;
}
