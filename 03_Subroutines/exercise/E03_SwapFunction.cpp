#include <iostream>
using namespace std;


void arrayStatistics(int arr[], int size, int &max, int &min, double &average);

int main() {
    
    int matrix[]= {1,2,3,4,5,6,2,4,5,6};
    int size = 10;
    int maxVal;
    int minVal;
    double avgVal;

    arrayStatistics(matrix, size, maxVal, minVal, avgVal);

    cout << "Highest Number: " << maxVal  <<  endl;
    cout << "Lowest Number: " << minVal  <<  endl;
    cout << "Average Number: " << avgVal  <<  endl;
    return 0;
}

void arrayStatistics(int arr[], int size, int &max, int &min, double &average){

    max = arr[0];
    min = arr[0];
    average = 0;

    for (int i = 0; i < size ; i++) {
        if(arr[i] > max){
            max = arr[i];
        }

        if(arr[i] < min){
            min = arr[i];
        }

        average = (average + arr[i]);
        
    }

    average = average/size;
}