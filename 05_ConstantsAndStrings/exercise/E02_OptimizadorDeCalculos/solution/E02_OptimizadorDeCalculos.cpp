// ============================================================================
// Reto E02: Optimizador de Calculos (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    // Usamos constexpr e inicializacion uniforme. El compilador asume la carga.
    constexpr int velocidadLuz{299792}; 
    constexpr int segundosPorMinuto{60};
    constexpr int minutosPorHora{60};
    
    // El compilador resuelve esta gran multiplicacion ANTES de que el programa corra.
    constexpr int distanciaLuzPorHora{velocidadLuz * segundosPorMinuto * minutosPorHora};

    // --- (Simulacion de los sensores espaciales) ---
    int temperaturaSensor{0};
    std::cout << "Leyendo sensor termico espacial... Ingresa valor: ";
    std::cin >> temperaturaSensor;

    // Solo podemos usar 'const' aqui, porque depende de una lectura en vivo (std::cin).
    // El compilador no puede predecir el futuro ni saber que ingresara el usuario.
    const int temperaturaProtegida{temperaturaSensor}; 
    
    std::cout << "\n[REPORTE DEL SATELITE]\n";
    std::cout << "Distancia que la luz viaja en 1 hora: " << distanciaLuzPorHora << " km\n";
    std::cout << "Temperatura registrada: " << temperaturaProtegida << " grados\n";

    return 0;
}
