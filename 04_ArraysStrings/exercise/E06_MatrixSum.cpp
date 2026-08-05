#include <iostream>
#include <cassert>

using namespace std;

const int COLS = 10;

// E06 — 2D Matrix Sum (Row-Major Order)
int sumaMatriz(const int mat[][COLS], int rows, int actualCols) {
    int sum = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < actualCols; j++) {
            sum += mat[i][j];
        }
    }
    return sum;
}

int main() {
    int matrix[2][COLS]{
        {1, 2, 3}, // Row 0 (only 3 actual columns populated)
        {4, 5, 6}  // Row 1
    };

    int totalSum = sumaMatriz(matrix, 2, 3);
    cout << "Total matrix sum: " << totalSum << endl;
    assert(totalSum == 21);

    return 0;
}
