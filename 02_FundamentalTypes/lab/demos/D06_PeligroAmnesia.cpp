// ============================================================================
// Laboratorio D06: BUG DEMO - La amnesia de auto
// ============================================================================
// Objetivo: Mostrar por qué confiar ciegamente en 'auto' con divisiones
//           puede ocultar bugs y causar pérdidas de datos silenciosas.
//
// INSTRUCCIONES:
// Intenta compilar y ejecutar este archivo:
// g++ D06_PeligroAmnesia.cpp -o bug
//
// Observa cómo el tesorero se queda con oro perdido por no usar casting.
// ============================================================================

#include <iostream>

int main() {
    int oro_total{500};
    int cantidad_jugadores{3};

    // BUG INTENCIONAL: El programador confia ciegamente en auto.
    // Cree que como la division no es exacta (500/3 = 166.66), 
    // "auto" sera inteligente y creara un double.
    
    auto oro_por_jugador{oro_total / cantidad_jugadores}; 

    std::cout << "El botín es de " << oro_total << " de oro.\n";
    std::cout << "Somos " << cantidad_jugadores << " jugadores.\n\n";

    std::cout << "Según la computadora, cada jugador recibe: " << oro_por_jugador << "\n";

    // Como ambos eran int, la división fue entera (166).
    // auto miro el resultado (166) y dijo "Ah, esto es un int".
    // Los decimales se esfumaron antes de que 'auto' los viera.
    std::cout << "Oro contabilizado: " << (oro_por_jugador * cantidad_jugadores) << "\n";
    std::cout << "¡El tesorero del gremio se robo el resto!\n";

    return 0;
}
