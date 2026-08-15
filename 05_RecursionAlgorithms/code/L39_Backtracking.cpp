#include <iostream>
#include <string>
using namespace std;

// ============================================================================
// L38 — BACKTRACKING RECURSIVO: CHOOSE, EXPLORE, UNCHOOSE
// Capítulo 8 (p. 349) & Capítulo 9 (p. 389) — Eric Roberts
// ============================================================================

// ── SECCIÓN 1: SUBCONJUNTOS (Power Set) ────────────────────────────────────
// El patrón clásico: ELEGIR → EXPLORAR → DESHACER (Choose-Explore-Unchoose)
void generarSubconjuntos(const char elementos[], int totalElementos, int index, char actual[], int actualSize) {
    // CASO BASE: se tomó decisión sobre todos los elementos
    if (index == totalElementos) {
        cout << "{ ";
        for (int i = 0; i < actualSize; i++) cout << actual[i] << " ";
        cout << "}" << endl;
        return;
    }

    // OPCIÓN A: NO incluir elementos[index] → explorar sin modificar
    generarSubconjuntos(elementos, totalElementos, index + 1, actual, actualSize);

    // OPCIÓN B: INCLUIR elementos[index]
    actual[actualSize] = elementos[index];          // 1. ELEGIR (Choose)
    generarSubconjuntos(elementos, totalElementos, index + 1, actual, actualSize + 1); // 2. EXPLORAR (Explore)
    // 3. DESHACER (Unchoose / Backtrack) ocurre implícitamente al no incrementar actualSize en esta rama
}

// ── SECCIÓN 2: LABERINTO (Sección 9.1) ─────────────────────────────────────
// El laberinto se representa como una cuadrícula de chars:
//   '#' = pared, ' ' = pasillo abierto, 'S' = inicio, 'E' = salida
// La función solveMaze retorna true si encontró un camino hasta 'E'.

const int FILAS = 5;
const int COLS  = 9;

char laberinto[FILAS][COLS] = {
    {'#','#','#','#','#','#','#','#','#'},
    {'#',' ',' ',' ','#',' ',' ','E','#'},
    {'#','S','#',' ','#',' ','#','#','#'},
    {'#',' ','#',' ',' ',' ',' ',' ','#'},
    {'#','#','#','#','#','#','#','#','#'}
};

void imprimirLaberinto() {
    for (int r = 0; r < FILAS; r++) {
        for (int c = 0; c < COLS; c++) cout << laberinto[r][c];
        cout << endl;
    }
}

// Caso Base 1: ¿Llegamos a la salida 'E'?
// Caso Base 2: ¿La celda está bloqueada o ya visitada ('.')? → false
// Paso Recursivo: marcar, intentar las 4 direcciones, desmarcar (backtrack)
bool solveMaze(int r, int c) {
    // Caso Base 1: celda es la salida
    if (laberinto[r][c] == 'E') return true;

    // Caso Base 2: pared, fuera de bounds, o ya visitada
    if (r < 0 || r >= FILAS || c < 0 || c >= COLS) return false;
    if (laberinto[r][c] == '#' || laberinto[r][c] == '.') return false;

    laberinto[r][c] = '.';  // 1. ELEGIR — marcar como visitado

    // 2. EXPLORAR las 4 direcciones (Norte, Sur, Este, Oeste)
    if (solveMaze(r - 1, c)) return true; // Norte
    if (solveMaze(r + 1, c)) return true; // Sur
    if (solveMaze(r, c + 1)) return true; // Este
    if (solveMaze(r, c - 1)) return true; // Oeste

    laberinto[r][c] = ' ';  // 3. DESHACER — backtrack (desmarcar)
    return false;
}

// ── SECCIÓN 3: JUEGO NIM (Sección 9.2) ─────────────────────────────────────
// Nim: montón de monedas. Cada turno se pueden tomar 1, 2 o 3 monedas.
// El jugador que toma la ÚLTIMA moneda PIERDE.
// isBadPosition y findGoodMove son mutuamente recursivas (Sec. 9.2).

const int MIN_MOVE = 1;
const int MAX_MOVE = 3;

// Declaración adelantada para mutua recursión
bool isBadPosition(int nCoins);

// findGoodMove: busca un movimiento que deje al oponente en posición mala
// Retorna el número de monedas a tomar, o -1 si no existe buen movimiento.
int findGoodMove(int nCoins) {
    for (int take = MIN_MOVE; take <= MAX_MOVE && take < nCoins; take++) {
        if (isBadPosition(nCoins - take)) return take;
    }
    return -1; // Sin buen movimiento → posición mala
}

// isBadPosition: una posición es mala si no existe ningún buen movimiento
bool isBadPosition(int nCoins) {
    if (nCoins == 1) return true;          // Caso Base: solo 1 moneda = mala
    return findGoodMove(nCoins) == -1;     // Sin buen movimiento = mala
}

void demostrarNim(int nCoins) {
    cout << "Monedas iniciales: " << nCoins << endl;
    int turno = 1;
    while (nCoins > 1) {
        int movimiento = findGoodMove(nCoins);
        if (movimiento == -1) movimiento = 1; // Sin buen movimiento: tomar 1

        cout << "  Turno " << turno << ": Computadora toma " << movimiento
             << " moneda(s). Quedan " << nCoins - movimiento << "." << endl;
        nCoins -= movimiento;
        turno++;
    }
    cout << "  => Solo queda 1 moneda. El HUMANO debe tomarla. Computadora GANA." << endl;
}

// ── MAIN ────────────────────────────────────────────────────────────────────
int main() {
    cout << "=== L38: Backtracking Recursivo — Roberts Cap. 8 & 9 ===" << endl;

    // ── Demo 1: Power Set con Choose-Explore-Unchoose ────────────────────
    cout << "\n--- 1. Todos los subconjuntos de {A, B, C} (Power Set) ---" << endl;
    const int total = 3;
    char letras[total] = {'A', 'B', 'C'};
    char actual[total];
    generarSubconjuntos(letras, total, 0, actual, 0);
    cout << "Total: 2^3 = 8 subconjuntos" << endl;

    // ── Demo 2: Laberinto recursivo (Sección 9.1) ────────────────────────
    cout << "\n--- 2. Resolver Laberinto (Seccion 9.1 - Theseus) ---" << endl;
    cout << "Laberinto inicial:" << endl;
    imprimirLaberinto();

    if (solveMaze(2, 1)) { // Coordenadas de 'S'
        cout << "\nSolucion encontrada (camino marcado con '.'):" << endl;
        imprimirLaberinto();
    } else {
        cout << "\nNo existe solucion." << endl;
    }

    // ── Demo 3: Juego Nim — Backtracking sobre juegos (Sección 9.2) ─────
    cout << "\n--- 3. Juego Nim con " << 13 << " monedas (Seccion 9.2) ---" << endl;
    cout << "Reglas: tomar 1, 2 o 3 monedas por turno. Quien tome la ultima, PIERDE." << endl;
    demostrarNim(13);

    // ── Análisis: posiciones buenas y malas en Nim ───────────────────────
    cout << "\n--- 4. Analisis de posiciones en Nim (1 a 10 monedas) ---" << endl;
    for (int n = 1; n <= 10; n++) {
        cout << "  " << n << " monedas: "
             << (isBadPosition(n) ? "MALA (quien mueve pierde)" : "BUENA (quien mueve gana)")
             << endl;
    }

    return 0;
}
