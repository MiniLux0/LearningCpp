#include <iostream>
#include <limits>

using namespace std;

int main()
{

    cout << "INT_MAX: " << INT_MAX << "\n";
    cout << INT_MIN << "\n";
    cout << SHRT_MAX << "\n";
    cout << SHRT_MIN << "\n";
    cout << LONG_MAX << "\n";
    cout << LONG_MIN << "\n";
    cout << LLONG_MAX << "\n";
    cout << LLONG_MIN << "\n";

    cout << "Size of int: " << sizeof(int) << " bytes\n";
    cout << "Size of short: " << sizeof(short) << " bytes\n";
    cout << "Size of long: " << sizeof(long) << " bytes\n";
    cout << "Size of long long: " << sizeof(long long) << " bytes\n";

    return 0;
}