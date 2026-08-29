// ============================================================================
// Reto E05: Recibo Formateado (SOLUCIÓN)
// ============================================================================

#include <iostream>
#include <string>

int main() {
    // 1. Inicialización vacía segura
    std::string nombreCompleto{""};
    std::string producto{""};

    // 2. Usando std::getline() en vez de std::cin para soportar nombres con espacios
    std::cout << "Nombre completo del cliente: ";
    std::getline(std::cin, nombreCompleto);

    std::cout << "Producto a comprar: ";
    std::getline(std::cin, producto);

    // 3. Imprimiendo el recibo
    std::cout << "\n--- TICKET DE COMPRA ---\n";
    std::cout << "Cliente\t: " << nombreCompleto << "\n";
    std::cout << "Item\t: " << producto << "\n";
    std::cout << "------------------------\n";

    return 0;
}
