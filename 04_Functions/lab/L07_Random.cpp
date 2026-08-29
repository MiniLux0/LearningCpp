// ============================================================================
// Laboratorio L07: PRNG en C++ Moderno (Pseudo-Random Number Generator)
// ============================================================================
// Objetivo: Observar la arquitectura correcta de un PRNG encapsulado usando 
//           <random> y la persistencia de estado con el modificador static.
// ============================================================================

#include <iostream>
#include <random>

int generarDanio() {
    // 1. ENTROPIA Y MOTOR MATEMATICO
    // 'static' evita que el motor se destruya al finalizar el Scope,
    // preservando el estado de la secuencia estocastica en llamadas rapidas.
    static std::mt19937 motor_aleatorio{std::random_device{}()};
    
    // 2. DISTRIBUCION ESTADISTICA
    // Restringimos la generacion a un rango inclusivo.
    std::uniform_int_distribution<int> distribucion_danio{10, 25};
    
    // 3. INYECCION Y RETORNO
    return distribucion_danio(motor_aleatorio);
}

int main() {
    std::cout << "--- SISTEMA DE COMBATE ---\n";
    std::cout << "Ejecutando rafaga de llamadas consecutivas (Microsegundos):\n\n";
    
    int golpe1{generarDanio()};
    int golpe2{generarDanio()};
    int golpe3{generarDanio()};
    
    std::cout << "Impacto 1: " << golpe1 << " puntos.\n";
    std::cout << "Impacto 2: " << golpe2 << " puntos.\n";
    std::cout << "Impacto 3: " << golpe3 << " puntos.\n";
    
    std::cout << "\n(El modificador static conservo el estado; la distribucion es correcta).\n";
    
    return 0;
}
