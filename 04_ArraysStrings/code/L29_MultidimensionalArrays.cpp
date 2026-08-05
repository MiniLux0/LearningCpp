#include <iostream>

using namespace std;

// ============================================================================
// L29 — MULTIDIMENSIONAL ARRAYS: 2D MATRICES & ROW-MAJOR ORDER
// Stanford CS106B Chapter 11 / MIT 6.096 Lecture 04
// ============================================================================

const int COLS = 4; // Column dimension MUST be constant for parameters

// Function receiving 2D Matrix (Column dimension strictly required)
void printMatrix(const int mat[][COLS], int rows) {
    for (int i = 0; i < rows; i++) {
        cout << "Row " << i << ": [ ";
        for (int j = 0; j < COLS; j++) {
            cout << mat[i][j] << "\t";
        }
        cout << "]" << endl;
    }
}

// Function demonstrating contiguous 1D RAM memory addresses in Row-Major order
void printRAMLayout(const int mat[][COLS], int rows) {
    cout << "\n--- Physical RAM Layout (Row-Major Order) ---" << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < COLS; j++) {
            cout << "mat[" << i << "][" << j << "] @ " << &mat[i][j] 
                 << " = " << mat[i][j] << endl;
        }
    }
}

int main() {
    cout << "=== MULTIDIMENSIONAL ARRAYS & ROW-MAJOR ORDER ===" << endl << endl;

    int matrix[3][COLS]{
        { 1,  2,  3,  4},  // Row 0
        { 5,  6,  7,  8},  // Row 1
        { 9, 10, 11, 12}   // Row 2
    };

    cout << "--- Matrix Traversal ---" << endl;
    printMatrix(matrix, 3);

    printRAMLayout(matrix, 3);

    return 0;
}