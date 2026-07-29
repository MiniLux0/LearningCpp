#include <iostream>
using namespace std;

int main() {
    cout << "=== L29: Multidimensional Arrays ===" << endl;

    // 1. Declaracion e inicializacion 2D
    int matriz[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    cout << "Matriz 3x4:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << "matriz[" << i << "][" << j << "] = " << matriz[i][j] << "  ";
        }
        cout << endl;
    }

    // 2. Inicializacion parcial
    int parcial[2][3] = {{1, 2}, {3}};  // resto ceros
    cout << "\nInicializacion parcial int parcial[2][3] = {{1, 2}, {3}}:" << endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << parcial[i][j] << " ";
        }
        cout << endl;
    }

    // 3. Inicializacion a cero
    int ceros[3][4] = {0};
    cout << "\nInicializacion a cero int ceros[3][4] = {0}:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) cout << ceros[i][j] << " ";
        cout << endl;
    }

    // 4. Tamano con sizeof
    int filas = sizeof(matriz) / sizeof(matriz[0]);
    int cols = sizeof(matriz[0]) / sizeof(int);
    cout << "\nFilas: " << filas << ", Columnas: " << cols << endl;

    // 5. Array 3D
    int cubo[2][3][4] = {0};
    cubo[1][2][3] = 99;
    cout << "\nArray 3D cubo[2][3][4], cubo[1][2][3] = " << cubo[1][2][3] << endl;

    // 6. Paso a funcion (decae a puntero a array[4])
    void imprimir2D(int m[][4], int filas);
    cout << "\nPaso a funcion imprimir2D(int m[][4], int filas):" << endl;
    imprimir2D(matriz, 3);

    // 7. Array de strings (array 2D de chars)
    char nombres[3][20] = {"Ana", "Carlos", "Beatriz"};
    cout << "\nArray de strings (char[3][20]):" << endl;
    for (int i = 0; i < 3; i++) {
        cout << "nombres[" << i << "] = " << nombres[i] << endl;
    }

    return 0;
}

void imprimir2D(int m[][4], int filas) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < 4; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}