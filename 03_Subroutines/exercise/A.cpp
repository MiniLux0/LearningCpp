#include <iostream>
using namespace std;


void estadisticasArreglo(int arr[], int tam, int &mayor, int &menor, double &promedio);

int main() {
    
    int matrix[]= {1,2,3,4,5,6,2,4,5,6};
    int tam = 10;
    int nmayor;
    int nmenor;
    double npromedio;

    estadisticasArreglo(matrix, tam, nmayor, nmenor, npromedio);

    cout << "Numero Mayor: " << nmayor  <<  endl;
    cout << "Numero Menor: " << nmenor  <<  endl;
    cout << "Numero Promedio: " << npromedio  <<  endl;
    return 0;
}

void estadisticasArreglo(int arr[], int tam, int &mayor, int &menor, double &promedio){

    mayor = arr[0];
    menor = arr[0];
    promedio = 0;

    for (int i = 0; i < tam ; i++) {
        if(arr[i] > mayor){
            mayor = arr[i];
        }

        if(arr[i] < menor){
            menor = arr[i];
        }

        promedio = (promedio + arr[i]);
        
    }

    promedio = promedio/tam;
}