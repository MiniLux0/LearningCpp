#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    cout << "=== L27: Array Basics ===" << endl;

    // 1. Declaracion y definicion
    int numeros[5];
    int valores[5] = {10, 20, 30, 40, 50};
    int otros[] = {1, 2, 3, 4, 5}; // tamano inferido

    cout << "Declaracion: int numeros[5];" << endl;
    cout << "Inicializacion: int valores[5] = {10, 20, 30, 40, 50};" << endl;
    cout << "Tamano inferido: int otros[] = {1, 2, 3, 4, 5};" << endl;

    // 2. Acceso por indice (0-based)
    cout << "\nAcceso por indice (0-based):" << endl;
    cout << "valores[0] = " << valores[0] << endl;
    cout << "valores[4] = " << valores[4] << endl;
    cout << "valores[2] = " << valores[2] << endl;

    // Modificar elementos
    valores[2] = 99;
    cout << "Despues de valores[2] = 99: valores[2] = " << valores[2] << endl;

    // 3. Tamano del array
    int tam = sizeof(valores) / sizeof(valores[0]);
    cout << "\nTamano: sizeof(valores)/sizeof(valores[0]) = " << tam << endl;

    // 3b. Inicializacion parcial -> resto ceros
    int parcial[5] = {1, 2}; // resto se inicializa a 0
    cout << "\nInicializacion parcial int parcial[5] = {1, 2}:" << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << "parcial[" << i << "] = " << parcial[i] << endl;
    }

    // 4. Recorrido con for
    cout << "\nRecorrido con for:" << endl;
    for (int i = 0; i < tam; i++)
    {
        cout << "valores[" << i << "] = " << valores[i] << endl;
    }

    // 5. Range-based for (C++11)
    cout << "\nRange-based for (C++11):" << endl;
    for (int v : valores)
    {
        cout << v << " ";
    }
    cout << endl;

    // 6. Array de chars (C-string)
    char nombre[20] = "Hola";
    cout << "\nC-string: char nombre[20] = \"Hola\": " << nombre << endl;
    cout << "strlen(nombre) = " << strlen(nombre) << endl;

    // 7. Inicializacion a cero
    int ceros[10] = {0};
    cout << "\nInicializacion a cero: int ceros[10] = {0}:" << endl;
    for (int i = 0; i < 10; i++)
        cout << ceros[i] << " ";
    cout << endl;

    // 8. EJERCICIO: Leer N valores desde teclado y mostrarlos
    // Enunciado:
    // Escribe un programa que:
    // Declare un arreglo de enteros de tamaño 6 (usa una constante o variable para el tamaño,
    // no lo repitas como número mágico en el loop — aquí es donde vigilo tu patrón de "números fijos")
    // Le pida al usuario los 6 valores uno por uno con cin
    // Los imprima todos de nuevo, separados por espacio
    // cout << "\n=== EJERCICIO: Leer N valores y mostrarlos ===" << endl;
    // const int TAM = 6;
    // int datos[TAM];

    // cout << "Introduce " << TAM << " enteros:" << endl;
    // for (int i = 0; i < TAM; i++) {
    //     cout << "datos[" << i << "] = ";
    //     cin >> datos[i];
    // }

    // cout << "\nValores leidos: ";
    // for (int i = 0; i < TAM; i++) {
    //     cout << datos[i];
    //     if (i < TAM - 1) cout << " ";
    // }
    // cout << endl;

    cout << "Ejercicio" << endl;

    const int TAM = 6;
    int datos[TAM];

    cout << "Introduce " << TAM << " enteros:" << endl;

    for (int i = 0; i < TAM; i++){
        cout << "Entero N" << i + 1 << ": ";
        cin >> datos[i];
    }

    cout << "\nValores leidos: "<< endl;
    for (int i = 0; i < TAM; i++){
        cout << "Entero N" << i + 1 << ": " << datos[i] << endl;
    }

    return 0;
}