#include <iostream>
using namespace std;

int main() {

    for (int i = 1; i <= 3; i++) {          // 🔵 Loop externo (filas)
        for (int j = 1; j <= 4; j++) {      // 🟢 Loop interno (columnas)
            cout << "(" << i << "," << j << ") ";
        }
        cout << endl; // salto de línea después de cada fila
    }

    for(int x = 0; x < 4; x = x + 1) {
        for(int y = 0; y <=x; y = y + 1)
            cout << y;
        cout << "\n";
}

    return 0;
}