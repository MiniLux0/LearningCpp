// ============================================================================
// Reto E05: Camara de Aislamiento
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

// TODO: Cambia esta funcion para que en lugar de void, devuelva un int
void escanearTarjeta() {
    int id_empleado{105};
    
    // Calcula el acceso (ficticio) basado en el ID
    int nivel_de_acceso{(id_empleado % 3) + 1}; 
    
    // TODO: Retorna el nivel de acceso en lugar de permitir la liberacion de su memoria.
}

int main() {
    std::cout << "--- SISTEMA DE SEGURIDAD ---\n";
    std::cout << "Escaneando tarjeta en el lector principal...\n";
    
    // TODO: Necesitas interceptar el output de la funcion inicializando una variable local.
    escanearTarjeta();
    
    // BUG: El Scope principal carece de visibilidad sobre 'nivel_de_acceso'. 
    // Arregla la arquitectura del flujo para que esta invocacion compile exitosamente.
    if (nivel_de_acceso == 1) {
        std::cout << "Puerta abierta. Bienvenido, Director.\n";
    } else {
        std::cout << "Acceso denegado. Se requiere Nivel 1.\n";
    }
    
    return 0;
}
