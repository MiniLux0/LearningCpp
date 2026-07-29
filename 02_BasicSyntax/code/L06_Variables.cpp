#include <iostream>
using namespace std;

int main()
{

    double weightCatLuna = 5.02;
    double weightCatSun = 4.12;

    double averageWeightCats = (weightCatLuna + weightCatSun) / 2;

    char initialLuna = 'L';
    char initialSun = 'S';

    bool hasDog = true;

    int numberCats = 5;
    int numberDogs = 7;
    int numberAnimals = numberCats + numberDogs;

    cout << "Initials of cats: " << initialLuna << " and " << initialSun << "\n";

    cout << "Number of cats: " << numberCats << "\n";
    cout << "Number of dogs: " << numberDogs << "\n";
    cout << "Total number of animals: " << numberAnimals << "\n";


    if (hasDog) {
        cout << "You already have dogs in your home.\n";
    }

    cout << "New dog acquired!\n";

   
    numberDogs += 1;
    numberAnimals = numberCats + numberDogs;

    cout << "Updated number of dogs: " << numberDogs << "\n";
    cout << "Updated total animals: " << numberAnimals << "\n";

  
    cout << "Weight of Luna: " << weightCatLuna << "\n";
    cout << "Weight of Sun: " << weightCatSun << "\n";
    cout << "Average weight of cats: " << averageWeightCats << "\n";

    return 0;
}