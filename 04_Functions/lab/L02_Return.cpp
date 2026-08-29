// ============================================================================
// Laboratorio L02: Retornando valores
// ============================================================================
// Objetivo: Observar como la ejecucion de la funcion finaliza inmediatamente despues del return.
// ============================================================================

#include <iostream>

// Funcion segura: Todos los caminos devuelven un valor.
int calcularNivel(int puntos) {
    if (puntos >= 100) {
        return 2; // Si tiene 100 o mas, devuelve Nivel 2 y termina.
    }
    
    // Si la computadora llega a esta linea, es porque NO entro al if anterior.
    // Garantizamos que siempre devolvemos algo:
    return 1;
}

// Funcion demostrativa: El codigo muerto despues del return.
int obtenerBonoSecreto() {
    return 999;
    
    // La computadora nunca, jamas leera las lineas debajo del primer return que ejecute.
    std::cout << "Esto es 'Codigo Muerto' (Dead Code). Nunca me imprimire.\n";
}

int main() {
    int puntos_jugador{120};
    int puntos_novato{40};
    
    // Capturamos las devoluciones de las funciones en variables
    int nivel_jugador{calcularNivel(puntos_jugador)};
    int nivel_novato{calcularNivel(puntos_novato)};
    
    std::cout << "Jugador avanzado es Nivel: " << nivel_jugador << '\n';
    std::cout << "Jugador novato es Nivel: " << nivel_novato << '\n';
    
    std::cout << "\nReclamando el bono secreto...\n";
    std::cout << "Bono recibido: " << obtenerBonoSecreto() << '\n';
    
    return 0;
}
