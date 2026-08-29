// ============================================================================
// Laboratorio L04: Parametros y Pass-by-value
// ============================================================================
// Objetivo: Observar como los argumentos inyectados a una funcion son 
//           clonados en memoria (Pass-by-value), aislando el valor original.
// ============================================================================

#include <iostream>

// Esta rutina recibe un CLON AISLADO de 'cantidad' en una nueva direccion de RAM.
void intentarDuplicar(int cantidad_local) {
    std::cout << "[Scope Interno] Recibi el clon con valor: " << cantidad_local << '\n';
    
    // Mutamos la memoria local
    cantidad_local = cantidad_local * 2;
    
    std::cout << "[Scope Interno] Reasigne el clon local a: " << cantidad_local << '\n';
}

// Esta funcion resuelve el fallo de arquitectura DEVOLVIENDO la transformacion matematica.
int duplicarRealmente(int cantidad_local) {
    int nuevo_valor{cantidad_local * 2};
    return nuevo_valor;
}

int main() {
    int oro_del_jugador{100};
    
    std::cout << "--- INTENTO FALLIDO (Mutacion Aislada) ---\n";
    std::cout << "Oro original: " << oro_del_jugador << '\n';
    
    // Le enviamos una copia exacta del 100 a la funcion
    intentarDuplicar(oro_del_jugador);
    
    std::cout << "Oro tras la ejecucion fallida: " << oro_del_jugador << " (Memoria original intacta)\n\n";
    
    std::cout << "--- INTENTO EXITOSO (Reasignacion por Retorno) ---\n";
    // Para mutar la variable original, atrapamos el retorno y sobreescribimos la memoria
    oro_del_jugador = duplicarRealmente(oro_del_jugador);
    
    std::cout << "Oro tras reasignar el retorno correcto: " << oro_del_jugador << '\n';
    
    return 0;
}
