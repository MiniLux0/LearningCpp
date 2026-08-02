#include <iostream>
using namespace std;

// Exercise 6 — Matrix sum
// Sums all elements of a matrix mat[][10] using only filas x columnasReales.
int sumaMatriz(const int mat[][10], int filas, int columnasReales) {
    int sum = 0;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnasReales; j++) {
            sum += mat[i][j];
        }
    }
    return sum;
}

int main() {
    int mat[3][10] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    cout << "Sum (3 rows, 3 real columns, expected 45): " 
         << sumaMatriz(mat, 3, 3) << endl;

    return 0;
}

// Theoretical explanation: Why does `mat[][10]` allow leaving the 1st dimension empty but NOT the 2nd?
// 1. Contiguous Memory Layout (Row-Major Order):
//    In C++, a two-dimensional array is stored in RAM as a single continuous 1D strip.
//    Complete Row 0 -> Complete Row 1 -> Complete Row 2.
//
// 2. Offset Calculation (Addressing):
//    To access `mat[i][j]`, the compiler calculates the physical address using the formula:
//    Address = Base_Address + (i * NUMBER_OF_COLUMNS + j) * sizeof(int)
//
// 3. Why is the number of columns (2nd dimension) MANDATORY?
//    The compiler must necessarily know the number of columns (in this case 10)
//    to figure out how many elements it must "skip" in RAM to advance to row `i`.
//    Without that value (`mat[][]`), it cannot calculate where row `i` begins.
//
// 4. Why can the number of rows (1st dimension) be omitted?
//    The 1st dimension only indicates how many rows there are in total, but does not change the distance between elements.
//    That is why `mat[][10]` decays into a pointer to an array of 10 integers: `int (*mat)[10]`.
