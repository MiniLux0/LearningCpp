// ============================================================================
// Reto E06: Refactorizacion del Menu
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

// TODO: 1. Crea la funcion void dibujarMenu() aqui
// TODO: 2. Crea la funcion int pedirOpcion() aqui
// TODO: 3. Crea la funcion void ejecutarSalida() aqui

int main() {
    
    // --- BLOQUE 1: Renderizado (Mueve esto a dibujarMenu) ---
    std::cout << "------------------------\n";
    std::cout << "    LA TABERNA RPG      \n";
    std::cout << "------------------------\n";
    std::cout << "1. Comprar pocion\n";
    std::cout << "2. Vender chatarra\n";
    std::cout << "3. Salir\n";
    std::cout << "------------------------\n";
    
    // --- BLOQUE 2: Flujo de I/O (Mueve esto a pedirOpcion) ---
    int seleccion_usuario{0};
    std::cout << "Elige una opcion (1-3): ";
    std::cin >> seleccion_usuario;
    
    // El switch se queda en el main por ahora como controlador del flujo
    switch (seleccion_usuario) {
        case 1:
            std::cout << "Has comprado una pocion.\n";
            break;
        case 2:
            std::cout << "Has vendido tu chatarra.\n";
            break;
        case 3:
            // --- BLOQUE 3: Salida (Mueve esto a ejecutarSalida) ---
            std::cout << "Guardando partida...\n";
            std::cout << "¡Gracias por jugar!\n";
            break;
        default:
            std::cout << "Opcion invalida.\n";
            break;
    }
    
    return 0;
}
