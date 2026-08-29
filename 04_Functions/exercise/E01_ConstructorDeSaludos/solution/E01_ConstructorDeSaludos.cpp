// ============================================================================
// Reto E01: Constructor de Saludos (SOLUCION)
// ============================================================================

#include <iostream>
#include <string>

void saludarInvitado(std::string nombre, int prioridad) {
    if (prioridad == 1) {
        std::cout << "Bienvenido de nuevo, VIP " << nombre << ". Su mesa esta lista.\n";
    } else if (prioridad == 2) {
        std::cout << "Hola " << nombre << ", pasa adelante.\n";
    } else {
        std::cout << "Alerta: Intruso detectado (" << nombre << "). Llamando a seguridad.\n";
    }
}

int main() {
    std::string invitado1{"Bruce Wayne"};
    int prioridad1{1};
    
    std::string invitado2{"Clark Kent"};
    int prioridad2{2};
    
    std::string invitado3{"Joker"};
    int prioridad3{3};
    
    saludarInvitado(invitado1, prioridad1);
    saludarInvitado(invitado2, prioridad2);
    saludarInvitado(invitado3, prioridad3);
    
    return 0;
}
