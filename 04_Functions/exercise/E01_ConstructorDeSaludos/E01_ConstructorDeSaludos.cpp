// ============================================================================
// Reto E01: Constructor de Saludos
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <string>

// TODO: Definir funcion saludarInvitado(std::string, int)

int main() {
    std::string invitado1{"Bruce Wayne"};
    int prioridad1{1};
    
    std::string invitado2{"Clark Kent"};
    int prioridad2{2};
    
    std::string invitado3{"Joker"};
    int prioridad3{3};
    
    // TODO: Refactorizar logica monolitica usando la funcion saludarInvitado
    
    // Saludo al primer invitado
    if (prioridad1 == 1) {
        std::cout << "Bienvenido de nuevo, VIP " << invitado1 << ". Su mesa esta lista.\n";
    } else if (prioridad1 == 2) {
        std::cout << "Hola " << invitado1 << ", pasa adelante.\n";
    } else {
        std::cout << "Alerta: Intruso detectado (" << invitado1 << "). Llamando a seguridad.\n";
    }
    
    // Saludo al segundo invitado
    if (prioridad2 == 1) {
        std::cout << "Bienvenido de nuevo, VIP " << invitado2 << ". Su mesa esta lista.\n";
    } else if (prioridad2 == 2) {
        std::cout << "Hola " << invitado2 << ", pasa adelante.\n";
    } else {
        std::cout << "Alerta: Intruso detectado (" << invitado2 << "). Llamando a seguridad.\n";
    }
    
    // Saludo al tercer invitado
    if (prioridad3 == 1) {
        std::cout << "Bienvenido de nuevo, VIP " << invitado3 << ". Su mesa esta lista.\n";
    } else if (prioridad3 == 2) {
        std::cout << "Hola " << invitado3 << ", pasa adelante.\n";
    } else {
        std::cout << "Alerta: Intruso detectado (" << invitado3 << "). Llamando a seguridad.\n";
    }
    
    return 0;
}
