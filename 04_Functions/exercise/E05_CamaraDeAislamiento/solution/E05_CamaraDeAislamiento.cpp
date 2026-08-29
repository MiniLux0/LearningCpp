// ============================================================================
// Reto E05: Camara de Aislamiento (SOLUCION)
// ============================================================================

#include <iostream>

int escanearTarjeta() {
    int id_empleado{105};
    int nivel_de_acceso{(id_empleado % 3) + 1}; 
    
    return nivel_de_acceso;
}

int main() {
    std::cout << "--- SISTEMA DE SEGURIDAD ---\n";
    std::cout << "Escaneando tarjeta en el lector principal...\n";
    
    // El Scope principal intercepta el valor transferido inicializando una nueva variable
    int nivel_de_acceso{escanearTarjeta()};
    
    // Ahora el identificador existe en el Scope del main() y la auditoria compila
    if (nivel_de_acceso == 1) {
        std::cout << "Puerta abierta. Bienvenido, Director.\n";
    } else {
        std::cout << "Acceso denegado. Se requiere Nivel 1.\n";
    }
    
    return 0;
}
