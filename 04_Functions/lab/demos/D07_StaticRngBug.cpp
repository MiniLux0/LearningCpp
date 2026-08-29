// ============================================================================
// Laboratorio D07: BUG DEMO - Colapso Estocastico (Falta de Persistencia)
// ============================================================================
// Objetivo: Observar el fallo de aleatoriedad cuando el motor PRNG se 
//           destruye y reconstruye instantaneamente por falta del `static`.
//
// INSTRUCCIONES: Compila con `g++ D07_StaticRngBug.cpp -o bug` y ejecuta.
// ============================================================================

#include <iostream>
#include <random>

int generarDanioRoto() {
    // BUG ARQUITECTONICO: Falta el modificador 'static' al inicio de la declaracion.
    // El motor se inicializa pidiendo una semilla de entropia al hardware local, 
    // pero al terminar la funcion, su Scope es destruido junto a su memoria.
    std::mt19937 motor_roto{std::random_device{}()};
    
    std::uniform_int_distribution<int> distribucion_danio{10, 25};
    
    return distribucion_danio(motor_roto);
}

int main() {
    std::cout << "--- SISTEMA DE COMBATE (ESTADO CORRUPTO) ---\n";
    std::cout << "Ejecutando rafaga de llamadas consecutivas (Microsegundos):\n\n";
    
    // Como las invocaciones a la rutina ocurren dentro de la misma ventana 
    // de reloj del procesador, el hardware de entropia extraera semillas gemelas, 
    // inicializando motores clonados que arrojaran el mismo resultado.
    
    std::cout << "Impacto 1: " << generarDanioRoto() << " puntos.\n";
    std::cout << "Impacto 2: " << generarDanioRoto() << " puntos.\n";
    std::cout << "Impacto 3: " << generarDanioRoto() << " puntos.\n";
    std::cout << "Impacto 4: " << generarDanioRoto() << " puntos.\n";
    std::cout << "Impacto 5: " << generarDanioRoto() << " puntos.\n";
    
    std::cout << "\n[ERROR FATAL] Los outputs son clonados. La generacion pseudo-aleatoria (PRNG) colapso.\n";
    
    return 0;
}
