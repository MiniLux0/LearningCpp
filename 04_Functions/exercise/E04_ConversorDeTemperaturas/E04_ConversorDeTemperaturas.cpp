// ============================================================================
// Reto E04: Conversor de Temperaturas
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

// TODO: Esta funcion deberia devolver un int, pero actualmente es void.
void convertirAFahrenheit(int grados_celsius) {
    // Formula correcta, pero aplica mutacion aislada sobre memoria temporal (Pass-by-value).
    grados_celsius = (grados_celsius * 9 / 5) + 32;
    
    // TODO: Falta retornar el dato resultante al main para su reasignacion.
}

int main() {
    int temperatura_actual{20};
    
    std::cout << "--- LABORATORIO --- \n";
    std::cout << "Temperatura original leida: " << temperatura_actual << " C\n";
    
    // TODO: La funcion actualmente desecha la data al finalizar. 
    // Cambia la firma para que devuelva un int, y usa su invocacion para 
    // reasignar la direccion de memoria de 'temperatura_actual'.
    convertirAFahrenheit(temperatura_actual);
    
    std::cout << "Temperatura procesada: " << temperatura_actual << " F\n";
    
    return 0;
}
