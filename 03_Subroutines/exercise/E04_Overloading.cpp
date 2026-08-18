#include <iostream>
using namespace std;

bool isGreater(int a, int b);
bool isGreater(double a, double b, double tolerance);

int main() {
    
    return 0;
}

bool isGreater(int a, int b){

    if(a > b){
        return true;
    }
    return false;
}

bool isGreater(double a, double b, double tolerance){

    if(a - b > tolerance){
        return true;
    }
    return false;
}

