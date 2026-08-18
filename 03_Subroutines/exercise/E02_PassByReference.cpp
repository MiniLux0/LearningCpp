#include <iostream>
using namespace std;


// prototype (declaration)
void division(int numerator, int denominator, int &quotient, int &remainder);

int main() {
    
    int num = 11, div = 3, quot, rem;

    division(num, div, quot, rem);

    cout << quot << rem;
    return 0;
}

void division(int numerator, int denominator, int &quotient, int &remainder){

    quotient = numerator / denominator;
    remainder = numerator - (denominator * quotient);
}