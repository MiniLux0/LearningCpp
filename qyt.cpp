#include <iostream>
#include <cmath>

using namespace std;

int main() {
    float y, x, z;
    for (y = 1.5f; y > -1.5f; y -= 0.1f) {
        for (x = -1.5f; x < 1.5f; x += 0.05f) {
            z = x * x + y * y - 1;
            if (z * z * z - x * x * y * y * y <= 0.0f) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}