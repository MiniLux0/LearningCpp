#include <iostream>
using namespace std;


void swapValues(int &a , int &b){

    int t = a;
    a = b;
    b = t;
    
}

void swapValues(double &a, double &b){

    double t = a;
    a = b;
    b = t;
}



int main() {
    
    int p = 4, q = 2;
    double x = 5.5, y = 7.5;

    swapValues(p, q);   // resolves to the int version
    swapValues(x, y);   // resolves to the double version

    cout << "p=" << p << " q=" << q;
    cout << "x=" << x << " y=" << y;

    return 0;
}

