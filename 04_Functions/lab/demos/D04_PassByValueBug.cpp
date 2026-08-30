// ============================================================================
// Laboratorio D04: BUG DEMO - Pass-By-Value 
// ============================================================================
// Objetivo: Mostrar el fallo logico al intentar mutar una variable de estado 
//           creyendo que el Scope interno afecta la memoria original.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D04_PassByValueBug.cpp -o bug
// Ejecuta y observa el fallo en la actualizacion de los datos.
// ============================================================================

#include <iostream>

void atacarMonstruo(int vida_monstruo) {
    // BUG ARQUITECTONICO: Creemos que estamos aplicando la resta sobre
    // la memoria original, pero solo estamos mutando un clon temporal local.
    vida_monstruo = vida_monstruo - 50;
    std::cout << "[Servidor] Calculo exitoso. Memoria temporal reducida a " << vida_monstruo << '\n';
}

int main() {
    int vida_boss{100};
    
    std::cout << "Vida original asignada en memoria: " << vida_boss << '\n';
    
    std::cout << "Ejecutando algoritmo de reduccion...\n";
    atacarMonstruo(vida_boss);
    
    // ERROR LOGICO: La direccion de memoria original del boss sigue en 100.
    std::cout << "Vida final auditada en el main: " << vida_boss << " (El algoritmo perdio la transformacion)\n";
    
    return 0;
}
