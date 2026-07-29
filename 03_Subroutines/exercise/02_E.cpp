#include <iostream>
using namespace std;


// prototipo (declaración)
void division(int numerador, int divisor, int &cociente, int &residuo);

int main() {
    
    int num =11, div = 3, coc, re;

    division(num,div,coc,re);

    cout << coc << re;
    return 0;
}

void division(int numerador, int divisor, int &cociente, int &residuo){

    cociente = numerador / divisor;
    residuo = numerador - (divisor * cociente);
}