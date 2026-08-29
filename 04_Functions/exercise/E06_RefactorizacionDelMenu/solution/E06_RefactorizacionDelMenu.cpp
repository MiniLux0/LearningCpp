// ============================================================================
// Reto E06: Refactorizacion del Menu (SOLUCION)
// ============================================================================

#include <iostream>

void dibujarMenu() {
    std::cout << "------------------------\n";
    std::cout << "    LA TABERNA RPG      \n";
    std::cout << "------------------------\n";
    std::cout << "1. Comprar pocion\n";
    std::cout << "2. Vender chatarra\n";
    std::cout << "3. Salir\n";
    std::cout << "------------------------\n";
}

int pedirOpcion() {
    int seleccion{0};
    std::cout << "Elige una opcion (1-3): ";
    std::cin >> seleccion;
    return seleccion;
}

void ejecutarSalida() {
    std::cout << "Guardando partida...\n";
    std::cout << "¡Gracias por jugar!\n";
}

int main() {
    // 1. Invocamos la sub-rutina de efecto secundario para renderizar la interfaz
    dibujarMenu();
    
    // 2. Invocamos el flujo de I/O e interceptamos su retorno
    int seleccion_usuario{pedirOpcion()};
    
    // 3. El condicional queda limpio como coordinador arquitectonico
    switch (seleccion_usuario) {
        case 1:
            std::cout << "Has comprado una pocion.\n";
            break;
        case 2:
            std::cout << "Has vendido tu chatarra.\n";
            break;
        case 3:
            ejecutarSalida();
            break;
        default:
            std::cout << "Opcion invalida.\n";
            break;
    }
    
    return 0;
}
