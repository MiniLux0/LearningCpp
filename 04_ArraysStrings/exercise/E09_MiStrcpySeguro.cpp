#include <iostream>
using namespace std;

// Exercise 9 — Safe miStrcpy
// Copies src to dest only if it fits (using destSize to verify it before writing).
bool miStrcpy(char dest[], int destSize, const char src[])
{
    int cont = 0;
    for (int i = 0; src[i] != '\0'; i++){
        cont++;
    }
    if (cont < destSize){
        for (int i = 0; i <= cont; i++){
            dest[i] = src[i];
        }
        return true;
    }
    return false;
}

int main()
{
    char buf[10];

    bool exito1 = miStrcpy(buf, 10, "Hello");
    cout << "Copies \"Hello\" to buf[10] (expected true): "
         << (exito1 ? "true" : "false") << " -> dest: \"" << buf << "\"" << endl;

    bool exito2 = miStrcpy(buf, 5, "Hello World!");
    cout << "Copies \"Hello World!\" to buf[5] (expected false): "
         << (exito2 ? "true" : "false") << endl;

    return 0;
}
