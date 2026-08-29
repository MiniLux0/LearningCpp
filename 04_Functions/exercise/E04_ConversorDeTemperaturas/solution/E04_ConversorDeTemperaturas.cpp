// ============================================================================
// Reto E04: Conversor de Temperaturas (SOLUCION)
// ============================================================================

#include <iostream>

// Cambiamos el tipo de retorno a int
int convertirAFahrenheit(int grados_celsius) {
    int grados_fahrenheit{(grados_celsius * 9 / 5) + 32};
    
    // Devolvemos la data calculada (Evitando la perdida por aislamiento Pass-by-value)
    return grados_fahrenheit;
}

int main() {
    int temperatura_actual{20};
    
    std::cout << "--- LABORATORIO --- \n";
    std::cout << "Temperatura original leida: " << temperatura_actual << " C\n";
    
    // Capturamos el flujo de retorno y reasignamos la variable original
    temperatura_actual = convertirAFahrenheit(temperatura_actual);
    
    // Ahora si imprimira 68 en lugar de 20.
    std::cout << "Temperatura procesada: " << temperatura_actual << " F\n";
    
    return 0;
}
