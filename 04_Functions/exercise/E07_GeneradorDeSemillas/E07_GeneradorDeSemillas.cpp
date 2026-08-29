// ============================================================================
// Reto E07: Generador de Semillas
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <random>

int generarNivelEnemigo() {
    // TODO: A esta instanciacion le falta el modificador de memoria para 
    // persistir su estado y prevenir el colapso estocastico de la semilla.
    std::mt19937 motor_rpg{std::random_device{}()};
    
    // Rango del nivel 1 al 10
    std::uniform_int_distribution<int> rango_nivel{1, 10};
    
    return rango_nivel(motor_rpg);
}

int main() {
    std::cout << "--- GENERADOR DE HORDAS RPG ---\n";
    std::cout << "¡Una horda de 3 enemigos se acerca!\n\n";
    
    // Llamamos a la funcion 3 veces seguidas instantaneamente
    int enemigo1{generarNivelEnemigo()};
    int enemigo2{generarNivelEnemigo()};
    int enemigo3{generarNivelEnemigo()};
    
    std::cout << "Enemigo 1: Nivel " << enemigo1 << '\n';
    std::cout << "Enemigo 2: Nivel " << enemigo2 << " (¿Clon?)\n";
    std::cout << "Enemigo 3: Nivel " << enemigo3 << " (¿Clon?)\n";
    
    return 0;
}
