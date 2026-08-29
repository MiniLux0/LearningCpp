// ============================================================================
// Laboratorio L01: Anatomia de una funcion
// ============================================================================
// Objetivo: Observar como se declaran, definen e invocan las funciones basicas 
//           por encima del main, garantizando una compilacion exitosa.
// ============================================================================

#include <iostream>
#include <string>

// --- DEFINICION DE FUNCIONES DELEGADAS ---

// 1. Una funcion que no recibe parametros ni devuelve datos (Accion pura)
void imprimirSeparador() {
    std::cout << "-----------------------------------\n";
}

// 2. Una funcion que requiere parametros (Inputs) y retorna un dato (Output)
int calcularEdadEn2050(int edad_actual) {
    int edad_futura{edad_actual + 24}; // (Asumiendo que estamos en 2026)
    return edad_futura;
}

// --- PUNTO DE ENTRADA PRINCIPAL ---

int main() {
    std::cout << "Inicializando simulacion temporal...\n";
    
    // Invocacion directa a una funcion void
    imprimirSeparador();
    
    std::string usuario_actual{"Admin"};
    int edad_actual{42};
    
    std::cout << "Analizando perfil de " << usuario_actual << " (Edad: " << edad_actual << ")\n";
    
    // Invocacion inyectando argumentos y atrapando el valor de retorno
    int edad_proyectada{calcularEdadEn2050(edad_actual)};
    
    std::cout << "Su edad en el anio 2050 sera: " << edad_proyectada << " anios.\n";
    
    imprimirSeparador();
    
    return 0;
}
