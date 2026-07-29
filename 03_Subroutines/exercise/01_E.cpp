#include <iostream>
using namespace std;


void intercambiar(int &a , int &b){

    int t = a;
    a = b;
    b = t;
    
}

void intercambiar(double &a, double &b){

    double t = a;
    a = b;
    b = t;
}



int main() {
    
    int p = 4, q = 2;
    double x = 5.5, y = 7.5;

    intercambiar(p, q);   // resuelve a la versión int
    intercambiar(x, y);   // resuelve a la versión double

    cout << "p=" << p << " q=" << q;
    cout << "x=" << x << " y=" << y;

    return 0;
}

