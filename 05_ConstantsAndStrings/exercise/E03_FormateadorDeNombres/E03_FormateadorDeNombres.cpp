// ============================================================================
// Reto E03: Formateador de Nombres
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>
// TODO 1: ¿Falta incluir alguna libreria maestra aqui?

int main() {
    std::string nombreJugador{"Kael"};

    // TODO 2: Esta linea genera un error de compilacion porque intenta
    // concatenar dos literales estaticos primitivos ("Etiqueta: " y "[Novato] ").
    // Arreglalo forzando a que la operacion inicie con un objeto std::string dinamico.
    
    std::string etiquetaChat = "Etiqueta: " + "[Novato] " + nombreJugador + " (Lv.1)";
    
    std::cout << etiquetaChat << '\n';

    return 0;
}
