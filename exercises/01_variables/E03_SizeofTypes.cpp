/*
 * E03 — Sizeof Types
 * ------------------
 * Usa sizeof para mostrar el tamano en bytes de:
 * int, short, long, long long, float, double, char, bool.
 *
 * Salida esperada (puede variar segun plataforma):
 *   sizeof(int):        4 bytes
 *   sizeof(short):      2 bytes
 *   sizeof(long):       4 bytes
 *   sizeof(long long):  8 bytes
 *   sizeof(float):      4 bytes
 *   sizeof(double):     8 bytes
 *   sizeof(char):       1 bytes
 *   sizeof(bool):       1 bytes
 */

#include <iostream>
using namespace std;

int main() {

    cout << "sizeof(int): " << sizeof(int) << " bytes\n";
    cout << "sizeof(short): " << sizeof(short) << " bytes\n";
    cout << "sizeof(long): " << sizeof(long) << " bytes\n";
    cout << "sizeof(long long): " << sizeof(long long) << " bytes\n";
    cout << "sizeof(float): " << sizeof(float) << " bytes\n";
    cout << "sizeof(double): " << sizeof(double) << " bytes\n";
    cout << "sizeof(char): " << sizeof(char) << " bytes\n";
    cout << "sizeof(bool): " << sizeof(bool) << " bytes\n";

    return 0;
}
