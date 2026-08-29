// ============================================================================
// Reto E02: Optimizador de Calculos
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>

int main() {
    // TODO 1: Optimiza estas variables para que sean evaluadas en Tiempo de Compilacion usando 'constexpr' e inicializacion uniforme {}.
    int velocidadLuz = 299792; 
    int segundosPorMinuto = 60;
    int minutosPorHora = 60;
    
    // TODO 2: Fuerza al compilador a resolver esta expresion durante el Compile-time usando 'constexpr'.
    int distanciaLuzPorHora = velocidadLuz * segundosPorMinuto * minutosPorHora;

    int temperaturaSensor{0};
    std::cout << "Leyendo sensor termico... Ingresa valor: ";
    std::cin >> temperaturaSensor;

    // TODO 3: Protege la variable de temperatura.
    // Precaucion: ¿Puedes usar constexpr para un dato que acabas de leer con cin?
    int temperaturaProtegida = temperaturaSensor; 
    
    std::cout << "\n[REPORTE DEL SATELITE]\n";
    std::cout << "Distancia que la luz viaja en 1 hora: " << distanciaLuzPorHora << " km\n";
    std::cout << "Temperatura registrada: " << temperaturaProtegida << " grados\n";

    return 0;
}
