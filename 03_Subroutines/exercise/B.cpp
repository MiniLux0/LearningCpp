#include <iostream>
using namespace std;

bool esMayor(int a, int b);
bool esMayor(double a, double b, double tolerancia);

int main() {
    
    return 0;
}

bool esMayor(int a, int b){

    if(a > b){
        return true;
    }
    return false;
}

bool esMayor(double a, double b, double toleracion){

    if(a - b > toleracion){
        return true;
    }
    return false;
}

