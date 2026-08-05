#include <iostream>
#include <utility>
#include <cassert>

using namespace std;

const int COLS = 10;

// E07 — Transpose Square Matrix In-Place
void transponer(int mat[][COLS], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) { // Upper triangle traversal (j > i)
            swap(mat[i][j], mat[j][i]);
        }
    }
}

int main() {
    int matrix[COLS][COLS]{
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    transponer(matrix, 3);

    cout << "Transposed Matrix (3x3):" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }

    assert(matrix[0][1] == 4 && matrix[1][0] == 2);

    return 0;
}
