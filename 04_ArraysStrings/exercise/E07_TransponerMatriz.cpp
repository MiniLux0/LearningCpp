#include <iostream>
using namespace std;

// Exercise 7 — Transpose square matrix
// Transposes a square matrix mat[][10] of size n x n in place.
void transponer(int mat[][10], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n ;j++) {
            int temp = mat[i][j];
            mat[i][j] = mat[j][i];
            mat[j][i] = temp;

        }
    }
}

void imprimirMatriz(const int mat[][10], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int mat[3][10] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    cout << "Original:" << endl;
    imprimirMatriz(mat, 3);

    transponer(mat, 3);

    cout << "\nTransposed (expected 1 4 7 / 2 5 8 / 3 6 9):" << endl;
    imprimirMatriz(mat, 3);

    return 0;
}
