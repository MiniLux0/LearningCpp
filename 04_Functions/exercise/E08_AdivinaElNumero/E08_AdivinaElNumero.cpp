// ============================================================================
// Reto E08: Adivina el Numero
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <random>

// TODO: 1. Rutina 'generarNumeroSecreto()': Usa <random> con 'static' para generar y retornar int del 1 al 100.

// TODO: 2. Rutina 'pedirIntento()': Maneja I/O de consola y retorna el input del usuario.

// TODO: 3. Controlador 'jugarPartida(int objetivo)':
// - Declara un contador de iteraciones.
// - Implementa un ciclo iterativo while(true).
// - Invoca 'pedirIntento()' e intercepta el resultado.
// - Aplica flujo condicional (if/else if) para validar el input contra el objetivo.
// - Si hay coincidencia, emite el reporte de iteraciones y aplica Retorno Temprano ('return;') para abortar el Scope.

int main() {
    std::cout << "--- SISTEMA DE CALIBRACION ---\n";
    std::cout << "Inicializando semilla del 1 al 100...\n";
    
    // TODO: 4. Flujo de Orquestacion Principal.
    // Inicializa una variable local delegando la tarea a generarNumeroSecreto().
    // Pasa ese valor como argumento inyectado hacia jugarPartida() para desatar el Game Loop.
    
    return 0;
}
