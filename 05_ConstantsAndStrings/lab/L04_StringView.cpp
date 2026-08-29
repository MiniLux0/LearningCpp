// ============================================================================
// Laboratorio L04: std::string_view
// ============================================================================
// Objetivo: Aprender a usar std::string_view para leer texto sin copiar memoria pesada.
// ============================================================================

#include <iostream>
#include <string>
#include <string_view> // Requerido para las vistas ligeras

// Usamos string_view en los parametros para NO clonar el pesado objeto original.
// La funcion recibe una referencia ligera de solo lectura.
void imprimirEtiqueta(std::string_view etiqueta) {
    std::cout << ">>> " << etiqueta << " <<<\n";
}

int main() {
    std::string granTexto{"Este es un texto larguisimo que costaria mucha memoria RAM copiar."};
    
    // 1. Al invocar la funcion, el compilador solo transfiere la vista ligera a 'imprimirEtiqueta'.
    imprimirEtiqueta(granTexto);
    
    // 2. string_view funciona nativamente con literales de texto (C-strings).
    // En lugar de instanciar memoria dinamica, solo establece la vista de lectura.
    imprimirEtiqueta("Texto estatico directo");

    // 3. Podemos declarar variables locales del tipo string_view
    std::string_view vistaLocal{granTexto};
    std::cout << "Viendo desde el main: " << vistaLocal << '\n';

    return 0;
}
