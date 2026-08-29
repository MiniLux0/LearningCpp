// ============================================================================
// Reto E03: Formateador de Nombres (SOLUCIÓN)
// ============================================================================

#include <iostream>
#include <string> // Solucion 1: Libreria obligatoria

int main() {
    std::string nombreJugador{"Kael"};
    
    // Solucion 2: Al encapsular los literales estáticos en objetos dinámicos 
    // usando inicializacion uniforme, la suma fluira de maravilla.
    std::string prefijo{"Etiqueta: "};
    std::string clan{"[Novato] "};
    
    // Todo funciona porque empezamos operando con un objeto std::string
    std::string etiquetaChat = prefijo + clan + nombreJugador + " (Lv.1)";
    
    // NOTA AVANZADA: Otra opcion valida en C++ moderno era instanciar al vuelo:
    // std::string etiquetaChat = std::string{"Etiqueta: "} + "[Novato] " + nombreJugador + " (Lv.1)";
    
    std::cout << etiquetaChat << '\n';

    return 0;
}
