// ============================================================================
// Reto E07: Generador de Semillas (SOLUCION)
// ============================================================================

#include <iostream>
#include <random>

int generarNivelEnemigo() {
    // Al usar 'static', el motor persiste en memoria entre invocaciones,
    // garantizando la iteracion correcta de la secuencia pseudo-aleatoria (PRNG).
    static std::mt19937 motor_rpg{std::random_device{}()};
    
    std::uniform_int_distribution<int> rango_nivel{1, 10};
    
    return rango_nivel(motor_rpg);
}

int main() {
    std::cout << "--- GENERADOR DE HORDAS RPG ---\n";
    std::cout << "¡Una horda de 3 enemigos se acerca!\n\n";
    
    // Ahora si veremos enemigos de distintos niveles
    int enemigo1{generarNivelEnemigo()};
    int enemigo2{generarNivelEnemigo()};
    int enemigo3{generarNivelEnemigo()};
    
    std::cout << "Enemigo 1: Nivel " << enemigo1 << '\n';
    std::cout << "Enemigo 2: Nivel " << enemigo2 << '\n';
    std::cout << "Enemigo 3: Nivel " << enemigo3 << '\n';
    
    return 0;
}
