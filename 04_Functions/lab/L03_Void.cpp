// ============================================================================
// Laboratorio L03: Funciones Void
// ============================================================================
// Objetivo: Observar el comportamiento de las funciones que ejecutan acciones sin devolver datos.
// ============================================================================

#include <iostream>

// Funcion de accion pura: no recibe parametros ni devuelve nada.
void imprimirSeparador() {
    std::cout << "--------------------------------------------------\n";
}

// Funcion void con aborto temprano usando 'return;'
void procesarAcceso(int nivel_seguridad) {
    if (nivel_seguridad < 5) {
        std::cout << "Acceso denegado. Nivel insuficiente.\n";
        return; // Aborta la funcion inmediatamente sin devolver nada.
    }
    
    // Si sobrevive al if, hace su trabajo.
    std::cout << "Acceso concedido. Abriendo boveda principal...\n";
}

int main() {
    std::cout << "Iniciando sistema de seguridad...\n";
    
    // Llamada correcta a una funcion void: Se llama como una instruccion independiente.
    imprimirSeparador();
    
    std::cout << "Intento de intruso (Nivel 2):\n";
    procesarAcceso(2);
    
    imprimirSeparador();
    
    std::cout << "Intento de administrador (Nivel 10):\n";
    procesarAcceso(10);
    
    imprimirSeparador();
    
    return 0;
}
