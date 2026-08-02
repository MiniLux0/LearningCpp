#include <iostream>
using namespace std;

// ============================================================================
// L29 — MULTIDIMENSIONAL ARRAYS: MATRICES, MEMORY, AND FUNCTIONS
// ============================================================================

// Prototype declaration in namespace scope (Best practice)
void imprimir2D(const int m[][4], int filas);
void transpuesto(int m[3][3]);

int main() {
    cout << "=== L29: Multidimensional Arrays ===" << endl;

    // 1. 2D Declaration and initialization with nested braces
    cout << "\n--- 1. 2D Matrix (3x4) ---" << endl;
    int matriz[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    cout << "Printing by passing to function imprimir2D(const int m[][4], int filas):" << endl;
    imprimir2D(matriz, 3);

    // 2. Warning: Uninitialized local matrix vs. Zero initialization (= {})
    cout << "\n--- 2. Uninitialized Local Variables vs. Zeros (= {}) ---" << endl;
    
    // int sinInicializar[2][2]; // Contains GARBAGE VALUES from RAM
    // cout << "Garbage example: " << sinInicializar[0][0] << endl;

    int ceros[3][4] = {}; // ✅ Explicit zero initialization
    cout << "int ceros[3][4] = {}:" << endl;
    imprimir2D(ceros, 3);

    // 3. Partial initialization
    cout << "\n--- 3. Partial initialization int parcial[2][3] = {{1, 2}, {3}} ---" << endl;
    int parcial[2][3] = {{1, 2}, {3}}; // Missing elements are filled with 0
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << parcial[i][j] << " ";
        }
        cout << endl;
    }

    // 4. Calculating rows and columns with sizeof
    cout << "\n--- 4. Calculating Rows and Columns with sizeof ---" << endl;
    int totalBytes = sizeof(matriz);        // 3 * 4 * 4 = 48 bytes
    int bytesFila  = sizeof(matriz[0]);     // 4 * 4 = 16 bytes
    int bytesElem  = sizeof(matriz[0][0]);  // 4 bytes

    int filas = sizeof(matriz) / sizeof(matriz[0]);       // 48 / 16 = 3
    int cols  = sizeof(matriz[0]) / sizeof(matriz[0][0]); // 16 / 4  = 4

    cout << "sizeof(matriz) = " << totalBytes << " bytes" << endl;
    cout << "sizeof(matriz[0]) = " << bytesFila << " bytes" << endl;
    cout << "sizeof(matriz[0][0]) = " << bytesElem << " bytes" << endl;
    cout << "Calculated rows: " << filas << ", Calculated columns: " << cols << endl;

    // 5. Three-Dimensional (3D) Arrays
    cout << "\n--- 5. 3D Array cubo[2][3][4] ---" << endl;
    int cubo[2][3][4] = {}; // 2 layers, 3 rows, 4 columns
    cubo[1][2][3] = 99;      // Modify element in Layer 1, Row 2, Column 3
    cout << "cubo[1][2][3] = " << cubo[1][2][3] << endl;

    // 6. C-String Matrix (2D char)
    cout << "\n--- 6. C-String Matrix (char[3][20]) ---" << endl;
    char nombres[3][20] = {"Ana", "Carlos", "Beatriz"};
    for (int i = 0; i < 3; i++) {
        cout << "Person " << i + 1 << ": " << nombres[i] << endl;
    }

    // 7. Proposed Exercise: In-Place 3x3 Transpose
    cout << "\n--- 7. Proposed Exercise: In-Place Transpose (3x3) ---" << endl;
    int matri[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    cout << "Original Matrix:" << endl;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matri[i][j] << " ";
        }
        cout << endl;
    }

    transpuesto(matri);

    cout << "Transposed Matrix:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) 
        cout << matri[i][j] << " ";
        cout << endl;
    }

    return 0;
}

// Function implementations
void imprimir2D(const int m[][4], int filas) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < 4; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}

// void transpuesto(int m[3][3]) {
//     for (int i = 0; i < 3; i++) {
//         for (int j = i + 1; j < 3; j++) {
//             int temp = m[i][j];
//             m[i][j] = m[j][i];
//             m[j][i] = temp;
//         }
//     }
// }

void transpuesto(int matriz[3][3]){
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3 ; j++) {
            int temp = matriz[i][j];
            matriz[i][j] = matriz[j][i];
            matriz[j][i] = temp; 
        }
    }
}