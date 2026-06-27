#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    float fValue1 = 1 / 3;
    float fValue2 = 1.0 / 3;
    float fValue3 = 1 / 3.0;
    float fValue4 = 1.0 / 3.0;
    double dValue1 = 1.0 / 3.0;

    cout << fixed;
    cout << "fValue1 (1/3):     " << fValue1 << "\n";
    cout << "fValue2 (1.0/3):   " << fValue2 << "\n";
    cout << "fValue3 (1/3.0):   " << fValue3 << "\n";
    cout << "fValue4 (1.0/3.0): " << fValue4 << "\n";
    cout << "dValue1 (1.0/3.0): " << dValue1 << "\n";

    cout << "\n--- Precision ---\n";
    cout << "float (6 decimales):  " << setprecision(6) << fValue4 << "\n";
    cout << "double (6 decimales): " << setprecision(6) << dValue1 << "\n";
    cout << "float (20 decimales): " << setprecision(20) << fValue4 << "\n";
    cout << "double (20 decimales):" << setprecision(20) << dValue1 << "\n";


    cout << "\n--- Scientific Notation ---\n";
    cout << scientific << setprecision(2);
    cout << "float:  " << fValue4 << "\n";
    cout << "double: " << dValue1 << "\n";

    cout << "\n--- Size ---\n";
    cout << "sizeof(float):  " << sizeof(float) << " bytes\n";
    cout << "sizeof(double): " << sizeof(double) << " bytes\n";

    return 0;
}
