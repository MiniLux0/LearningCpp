// ============================================================================
// Reto E03: Secuencias de Escape (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    // Uso de \t para alinear columnas y \n para saltos de línea sin vaciar el buffer
    std::cout << "Item\tCantidad\tPrecio\n";
    std::cout << "Pocion\t5\t\t10.5\n";
    std::cout << "Espada\t1\t\t150.0\n";
    
    // Uso de \" para lograr que las comillas literales aparezcan en pantalla
    std::cout << "El jefe dijo, \"Buen trabajo\".\n";

    return 0;
}
