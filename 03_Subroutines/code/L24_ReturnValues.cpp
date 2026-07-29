#include <iostream>
using namespace std;

int foo_int() {
    return 42;
}

const char* foo_cstr() {
    return "hello";
}

void printNumber(int num) {
    cout << "number is " << num << endl;
}

void printNumberIfEven(int num) {
    if (num % 2 == 1) {
        cout << "odd number" << endl;
        return;
    }
    cout << "even number; number is " << num << endl;
}

void printOnNewLine(int x) {
    cout << "Integer: " << x << endl;
}

void printOnNewLine(const char* x) {
    cout << "String: " << x << endl;
}

void printOnNewLine(int x, int y) {
    cout << "Two integers: " << x << " and " << y << endl;
}

void mostrar(int x) {
    cout << "int: " << x << endl;
}

void mostrar(double x) {
    cout << "double: " << x << endl;
}

int main() {
    cout << "=== L24: Return Values ===" << endl;

    cout << "\n1. Tipo retorno coincide:" << endl;
    cout << "foo_int() = " << foo_int() << endl;
    cout << "foo_cstr() = " << foo_cstr() << endl;

    cout << "\n2. void (sin retorno):" << endl;
    printNumber(4);

    cout << "\n3. Early return:" << endl;
    printNumberIfEven(3);
    printNumberIfEven(4);

    cout << "\n4. Overloading por tipo:" << endl;
    printOnNewLine(42);
    printOnNewLine("Hola C++");

    cout << "\n5. Overloading por cantidad:" << endl;
    printOnNewLine(10);
    printOnNewLine(10, 20);

    cout << "\n6. Char promotion:" << endl;
    mostrar(5);
    mostrar(5.0);
    mostrar('A');

    return 0;
}