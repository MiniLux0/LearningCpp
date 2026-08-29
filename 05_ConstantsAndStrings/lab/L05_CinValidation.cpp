// ============================================================================
// Laboratorio L05: Validacion de Entrada
// ============================================================================
// Objetivo: Aprender a manejar fallas de extraccion (Extraction Failures) y limpiar el buffer.
// ============================================================================

#include <iostream>

int main() {
    int edad{0};
    
    std::cout << "Ingresa tu edad: ";
    std::cin >> edad;
    
    // Si el usuario escribio "Hola", ocurre un error de extraccion de tipos.
    // Los caracteres quedan en el buffer y std::cin levanta la bandera fail().
    if (std::cin.fail()) {
        std::cout << "[SISTEMA] Troll detectado. No ingresaste un numero.\n";
        
        // 1. Restablecemos las banderas de error para reactivar std::cin
        std::cin.clear(); 
        
        // 2. Vaciamos la basura residual del buffer (ignorando hasta 10000 
        // caracteres o hasta encontrar la pulsacion de 'Enter' (\n))
        std::cin.ignore(10000, '\n'); 
        
        std::cout << "[SISTEMA] Tuberia destapada. Reinicia el programa para intentar de nuevo.\n";
    } else {
        std::cout << "Edad guardada exitosamente: " << edad << '\n';
    }

    return 0;
}
