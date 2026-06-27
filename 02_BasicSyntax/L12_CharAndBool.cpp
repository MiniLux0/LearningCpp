#include <iostream>
using namespace std;

int main(){

//char 
char letter = 'A';
char number = '7'; // character 7, no number 7
char space = ' ';
char letter2;

cout << "ASCII (A) value : " << (int)letter << "\n";
cout << "Number (65) to ASCII : " << (char)65 << "\n";

cout << "Sizeof(char): " << sizeof(char) << " bytes\n";

//Bool

bool isStudent = true;
bool isTeacher = false;

cout << "Is student: " << isStudent << "\n";
cout << "Is teacher: " << isTeacher << "\n";

//ASCII(aritmetic)

char nextLetter = letter + 1;

cout << "Next letter is: " << nextLetter << "\n";

cout << "Enter a character: ";

cin >> letter2;

cout << "ASCII (letter) value : " << (int)letter2 << "\n";

return 0;

}